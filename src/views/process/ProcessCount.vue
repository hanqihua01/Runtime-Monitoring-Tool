<template>
    <div>
        <h1>运行时验证程序监控中：{{ mtlSentence }}</h1>
        <input type="text" v-model="inputText">
        <button @click="handleButtonClick">提交</button>
        <div>
            <div>
                <h1>当前CPU占用：</h1>
                <el-progress :text-inside="true" :stroke-width="30" :percentage="cpuPercentage"
                    v-bind:status="cpuStatus"></el-progress>
                <p>CPU占用低于<label><input v-model="cpuPercentageWarningThreshold"
                            style="width: 30px; text-align: center;"></label>时，为<span style="color: #057b29">OK</span>状态；
                    CPU占用不低于<label><input v-model="cpuPercentageWarningThreshold"
                            style="width: 30px; text-align: center;"></label>时，为<span
                        style="color: #f8b303">WARNING</span>状态；
                    CPU占用不低于<label><input v-model="cpuPercentageExceptionThreshold"
                            style="width: 30px; text-align: center;"></label>时，为<span
                        style="color: #f04949">CRITICAL</span>状态。
                </p>
            </div>
            <div class="echart" id="mychart" :style="{ height: '300px' }"></div>
        </div>

        <div>
            <h1>当前进程数量：</h1>
            <p>进程数量低于<label><input v-model="warningThreshold" style="width: 30px; text-align: center;"></label>时，为<span
                    style="color: #057b29">OK</span>状态；
                进程数量不低于<label><input v-model="warningThreshold" style="width: 30px; text-align: center;"></label>时，为<span
                    style="color: #f8b303">WARNING</span>状态；
                进程数量不低于<label><input v-model="criticalThreshold" style="width: 30px; text-align: center;"></label>时，为<span
                    style="color: #f04949">CRITICAL</span>状态。</p>
            <el-table :data="tableData" style="width: 100%" :row-class-name="tableRowClassName">
                <el-table-column prop="time" label="时间" sortable>
                </el-table-column>
                <el-table-column prop="num" label="进程数量" sortable>
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
            cpuPercentage: '0', // cpu占用数据初始化
            cpuStatus: 'success', // cpu占用颜色初始化
            cpuPercentageWarningThreshold: 10, // cpu占用警告阈值
            cpuPercentageExceptionThreshold: 50, // cpu占用风险阈值
            warningThreshold: 355, // 进程数量警告阈值
            criticalThreshold: 360, // 进程数量风险阈值
            tableData: [], // 进程数量数据表格初始化,
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
            ],

            mtlSentence: '请输入MTL规约',
            mtlSpecific: '',
            inputText: 'G(procNum -> (F[1, 9] ~procNum))'
        };
    },
    methods: {
        // 设置进程数量数据表格行颜色
        tableRowClassName({ row, rowIndex }) {
            if (parseInt(row.num) >= this.warningThreshold && parseInt(row.num) < this.criticalThreshold) {
                return 'warning-row'
            } else if (parseInt(row.num) >= this.criticalThreshold) {
                return 'critical-row'
            }
            return 'ok-row'
        },
        // 进程数量状态过滤器
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
                    text: "进程状态占比",
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
        handleButtonClick() {
            this.mtlSpecific = this.inputText
            this.mtlSentence = "请等待MTL验证"
            axios.post('http://localhost:3000/mtlProcessCount', { mtl: this.mtlSpecific })
                .then(response => {
                    const resStr = response.data
                    if (resStr === 'True') {
                        this.mtlSentence = "根据MTL验证，当前系统运行状态未违反规约"
                    }
                    else if (resStr === 'False') {
                        this.mtlSentence = "根据MTL验证：当前系统运行状态违反规约"
                    } else {
                        this.mtlSentence = "MTL规约错误"
                    }
                })
        }
    },
    created() {
        const _this = this
        const getInfo = () => {
            axios.get('http://localhost:3000/ProcessCount')
                .then(response => {
                    _this.tableData.length = 0
                    _this.data[0].value = 0
                    _this.data[1].value = 0
                    _this.data[2].value = 0
                    const retList = response.data
                    for (let i = retList.length - 1; i >= 0; i--) {
                        const processNum = retList[i][0]
                        const curTime = retList[i][1]
                        const newRow = {
                            time: curTime,
                            num: processNum,
                            state: 'OK'
                        }
                        const intNum = parseInt(processNum)
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
            axios.get('http://localhost:3000/cpuPercentage')
                .then(response => {
                    const cpuPercentageString = response.data[0][0]
                    const cpuPercentageFinal = parseFloat(cpuPercentageString)
                    _this.cpuPercentage = String(cpuPercentageFinal.toFixed(2))
                    if (cpuPercentageFinal >= _this.cpuPercentageWarningThreshold && cpuPercentageFinal < _this.cpuPercentageExceptionThreshold) {
                        _this.cpuStatus = 'warning'
                    } else if (cpuPercentageFinal >= _this.cpuPercentageExceptionThreshold) {
                        _this.cpuStatus = 'exception'
                    } else {
                        _this.cpuStatus = 'success'
                    }
                })
        }
        this.$nextTick(function () {
            this.initEcharts()
        })
        getInfo()
        setInterval(getInfo, 1000 * 60)
    }
}
</script>
