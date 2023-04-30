<template>
    <div>
        <el-container>
            <div class="echart" id="loadchart" :style="LoadChartStyle"></div>
        </el-container>
        <el-container>
            <div id="cpuLoad" style="width: 100%; height: 520px;"></div>
        </el-container>
    </div>
</template>

<script>
import * as echarts from "echarts"
import axios from 'axios'
export default {
    data() {
        return {
            warningThreshold: 0.7,
            criticalThreshold: 0.8,
            xData: ["最近1分钟CPU平均负载", "最近5分钟CPU平均负载", "最近15分钟CPU平均负载"],
            test: [],
            loaddata: [0.1, 0.1, 0.1],
            LoadChartStyle: { float: "left", width: "100%", height: "400px" },

            charts: '', // 图
            option: '', // 图的设置
            opinionData: [],//数据
            xLabels: []
        }
    },
    mounted() {
        this.$nextTick(() => { this.initEcharts() })
    },
    methods: {
        initEcharts() {
            // 基本柱状图
            const option = {
                title: {
                    left: '1%',
                    text: 'CPU实时负载'
                },
                toolbox: {
                    feature: {
                        saveAsImage: {} 
                    }
                },
                xAxis: {
                    data: this.xData
                },
                yAxis: {},
                grid: {
                    top: '15%',
                    left: '1%',
                    right: '1%',
                    bottom: '5%',
                    containLabel: true
                },
                series: [
                    {
                        type: "bar", //形状为柱状图
                        data: this.loaddata
                    }
                ]
            };
            const LoadChart = echarts.init(document.getElementById("loadchart"));
            LoadChart.setOption(option);
            //随着屏幕大小调节图表
            window.addEventListener("resize", () => {
                LoadChart.resize();
            });
        },
        drawLine(id) {
            this.charts = echarts.init(document.getElementById(id))
            this.option = {
                notMerge: true,
                title: {
                    left: '1%',
                    text: "CPU历史负载",//标题文本，支持使用 \n 换行。
                },
                tooltip: {
                    trigger: 'axis'
                },
                // legend: {
                //     align: 'right',//文字在前图标在后
                //     left: '1%',
                //     top: '10%',
                //     data: ['CPU负载']
                // },
                grid: {
                    top: '15%',
                    left: '1%',
                    right: '1%',
                    bottom: '5%',
                    containLabel: true
                },
                toolbox: {
                    feature: {
                        magicType: {  //设置动态类型切换
                            title: {
                                line: '折线图',
                                bar: '柱状图'
                            },
                            type: ['line', 'bar']
                        },
                        saveAsImage: {} //保存为图片
                    }
                },
                xAxis: {
                    type: 'category',
                    boundaryGap: true,
                    axisTick: {
                        alignWithLabel: true //保证刻度线和标签对齐
                    },
                    data: this.xLabels //x坐标的名称
                },
                yAxis: {
                    type: 'value',
                    boundaryGap: true,
                },
                series: [{
                    name: 'CPU负载',
                    type: 'line', //折线图line;柱形图bar;饼图pie
                    smooth: true, // 平滑曲线
                    areaStyle: {
                        //显示区域颜色---渐变效果
                        color: {
                            type: 'linear',
                            x: 0, y: 0, x2: 0, y2: 1,
                            colorStops: [{
                                offset: 0, color: 'rgb(255,200,213)' // 0% 处的颜色
                            }, {
                                offset: 1, color: '#ffffff' // 100% 处的颜色
                            }],
                            global: false // 缺省为 false
                        }
                    },
                    itemStyle: {
                        color: 'rgb(255,96,64)', //改变折线点的颜色
                        lineStyle: {
                            color: 'rgb(255,96,64)', //改变折线颜色
                        }
                    },
                    data: this.opinionData
                }]
            }
            this.charts.setOption(this.option)
        },
        async getInfo() {
            await axios.get('http://localhost:3000/cpuPercentage')
                .then(response => {
                    this.opinionData.length = 0
                    this.xLabels.length = 0
                    for (let i = response.data.length - 1; i >= 0; i--) {
                        const cpuPercentageString = response.data[i][0]
                        const curTimeString = response.data[i][1]
                        this.opinionData.push(cpuPercentageString)
                        this.xLabels.push(curTimeString)
                    }
                })
            if (this.charts != '' && this.option != '') {
                this.charts.setOption(this.option)
            }
        }
    },
    created() {
        const _this = this
        const getInfo = () => {
            axios.get('http://localhost:3000/CpuLoad')
                .then(response => {
                    const load = response.data
                    this.test.unshift(load)
                    const loaddataString = this.test[0]
                    const temp = loaddataString.split(',')
                    const num1 = parseFloat(temp[0])
                    const num2 = parseFloat(temp[1])
                    const num3 = parseFloat(temp[2])
                    _this.loaddata[0] = num1
                    _this.loaddata[1] = num2
                    _this.loaddata[2] = num3
                    _this.initEcharts()
                })
                .catch(error => {
                    console.log(error)
                })
        }
        getInfo()
        setInterval(getInfo, 1000 * 3)

        this.getInfo()
        this.$nextTick(function () {
            this.drawLine('cpuLoad')
        })
        setInterval(this.getInfo, 1000 * 10)
    }
}
</script>
