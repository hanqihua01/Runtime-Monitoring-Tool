<template>
    <div>
        <div class="echart" id="mychart" :style="{ height: '300px' }"></div>
        <div>
            <h1>当前常驻内存大小：</h1>
            <p>常驻内存大小低于<label><input v-model="warningThreshold" style="width: 80px; text-align: center;"></label>时，为<span
                    style="color: #057b29">OK</span>状态；
                常驻内存大小不低于<label><input v-model="warningThreshold" style="width: 80px; text-align: center;"></label>时，为<span
                    style="color: #f8b303">WARNING</span>状态；
                常驻内存大小不低于<label><input v-model="criticalThreshold" style="width: 80px; text-align: center;"></label>时，为<span
                    style="color: #f04949">CRITICAL</span>状态。</p>
            <el-table :data="tableData" style="width: 100%" :row-class-name="tableRowClassName">
                <el-table-column prop="time" label="时间" sortable>
                </el-table-column>
                <el-table-column prop="num" label="常驻内存大小" sortable>
                </el-table-column>
                <el-table-column prop="state" label="状态"
                    :filters="[{ text: 'OK', value: 'OK' }, { text: 'WARNING', value: 'WARNING' }, { text: 'CRITICAL', value: 'CRITICAL' }]"
                    :filter-method="filterHandler">
                </el-table-column>
            </el-table>
        </div>
    </div>
</template>

<style>
.el-table .ok-row {
    background: #d7fce2;
}

.el-table .warning-row {
    background: #faf0c6;
}

.el-table .critical-row {
    background: #f6cccc;
}
</style>

<script>
import axios from 'axios'
import * as echarts from "echarts";
export default {
    data() {
        return {
            warningThreshold: 3500000, // 常驻内存大小警告阈值
            criticalThreshold: 4000000, // 常驻内存大小风险阈值
            tableData: [], // 常驻内存大小数据表格初始化
            option: '',
            myChart: '',
            data: [
                {
                    value: 0,
                    name: "OK"
                },
                {
                    value: 0,
                    name: "WARNING"
                },
                {
                    value: 0,
                    name: "CRITICAL"
                }
            ]
        }
    },
    methods: {
        // 设置常驻内存大小数据表格行颜色
        tableRowClassName({ row, rowIndex }) {
            if (parseInt(row.num) >= this.warningThreshold && parseInt(row.num) < this.criticalThreshold) {
                return 'warning-row'
            } else if (parseInt(row.num) >= this.criticalThreshold) {
                return 'critical-row'
            }
            return 'ok-row'
        },
        // 常驻内存大小状态过滤器
        filterHandler(value, row, column) {
            const property = column['property']
            return row[property] === value
        },
        initEcharts() {
            this.option = {
                legend: {
                    // 图例
                    data: ["OK", "WARNING", "CRITICAL"],
                    right: "10%",
                    top: "30%",
                    orient: "vertical"
                },
                title: {
                    // 设置饼图标题，位置设为顶部居中
                    text: "常驻内存状态占比",
                    top: "0%",
                    left: "center"
                },
                color: ['#26d65b', '#f4eb43', '#f15037'],
                series: [
                    {
                        type: "pie",
                        label: {
                            show: true,
                            formatter: "{b} : {c} ({d}%)" // b代表名称，c代表对应值，d代表百分比
                        },
                        radius: "60%", //饼图半径
                        data: this.data
                    }
                ]
            };
            this.myChart = echarts.init(document.getElementById("mychart"));// 图标初始化
            this.myChart.setOption(this.option);// 渲染页面
            //随着屏幕大小调节图表
            window.addEventListener("resize", () => {
                myChart.resize();
            });
        },
    },
    created() {
        const _this = this
        const getInfo = () => {
            axios.get('http://localhost:3000/ResidentMemorySize')
                .then(response => {
                    _this.tableData.length = 0
                    _this.data[0].value = 0
                    _this.data[1].value = 0
                    _this.data[2].value = 0
                    const retList = response.data
                    for (let i = retList.length - 1; i >= 0; i--) {
                        const sizeNum = retList[i][0]
                        const curTime = retList[i][1]
                        const newRow = {
                            time: curTime,
                            num: sizeNum,
                            state: 'OK'
                        }
                        const intNum = parseInt(sizeNum)
                        if (intNum >= _this.warningThreshold && intNum < _this.criticalThreshold) {
                            newRow.state = 'WARNING'
                            _this.data[1].value += 1
                        } else if (intNum >= _this.criticalThreshold) {
                            newRow.state = 'CRITICAL'
                            _this.data[2].value += 1
                        } else {
                            _this.data[0].value += 1
                        }
                        _this.tableData.unshift(newRow)
                    }
                    if (_this.myChart != '' && _this.option != '') {
                        _this.myChart.setOption(_this.option)
                    }
                })
        }
        this.$nextTick(function () {
            this.initEcharts()
        })
        getInfo()
        setInterval(getInfo, 1000 * 10)
    }
}
</script>
