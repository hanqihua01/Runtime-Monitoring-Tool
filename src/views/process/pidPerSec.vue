<template>
    <div>
        <h1>运行时验证程序监控中：{{ mtlSentence }}</h1>
        <input type="text" v-model="inputText">
        <button @click="handleButtonClick">提交</button>
        <div id="pidPerSec" style="width: 100%; height: 520px;"></div>
    </div>
</template>

<script>
import * as echarts from "echarts"
import axios from 'axios'
export default {
    data() {
        return {
            option: '',
            myChart: '',
            data: [],
            xLabels: [],
            mtlSentence: '请输入MTL规约',
            mtlSpecific: '',
            inputText: 'G(newProcs -> ~(G[1, 2] newProcs))'
        }
    },
    methods: {
        initEcharts() {
            this.option = {
                notMerge: true,
                tooltip: {
                    trigger: 'axis'
                },
                grid: {
                    top: '15%',
                    left: '1%',
                    right: '1%',
                    bottom: '5%',
                    containLabel: true
                },
                toolbox: {
                    feature: {
                        magicType: {
                            title: {
                                line: '折线图',
                                bar: '柱状图'
                            },
                            type: ['line', 'bar']
                        },
                        saveAsImage: {}
                    }
                },
                xAxis: {
                    type: 'category',
                    boundaryGap: true,
                    axisTick: {
                        alignWithLabel: true
                    },
                    data: this.xLabels
                },
                yAxis: {
                    type: 'value',
                    boundaryGap: true,
                },
                series: [{
                    name: '新创建的进程数量',
                    type: 'line',
                    smooth: true,
                    areaStyle: {
                        color: {
                            type: 'linear',
                            x: 0, y: 0, x2: 0, y2: 1,
                            colorStops: [{
                                offset: 0, color: 'rgb(255,200,213)'
                            }, {
                                offset: 1, color: '#ffffff'
                            }],
                            global: false
                        }
                    },
                    itemStyle: {
                        color: 'rgb(255,96,64)',
                        lineStyle: {
                            color: 'rgb(255,96,64)',
                        }
                    },
                    data: this.data
                }]
            }
            this.myChart = echarts.init(document.getElementById('pidPerSec'))
            this.myChart.setOption(this.option)
        },
        handleButtonClick() {
            this.mtlSpecific = this.inputText
            this.mtlSentence = "请等待MTL验证"
            axios.post('http://localhost:3000/mtlPidPerSec', { mtl: this.mtlSpecific })
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
            axios.get('http://localhost:3000/pidPerSec')
                .then(response => {
                    _this.data.length = 0
                    _this.xLabels.length = 0
                    const retList = response.data
                    for (let i = 0; i < retList.length; i++) {
                        const time = retList[i][0]
                        const num = retList[i][1]
                        _this.xLabels.unshift(time)
                        _this.data.unshift(num)
                    }
                    if (_this.myChart != '' && _this.option != '') {
                        _this.myChart.setOption(_this.option)
                    }
                })

            // if (_this.mtlSpecific === '') {
            //     _this.mtlSentence = "请输入MTL规约"
            // } else {
            //     // axios.get('http://localhost:3000/mtlPidPerSec')
            //     //     .then(response => {
            //     //         const resStr = response.data
            //     //         if (resStr === 'True') {
            //     //             _this.mtlSentence = "根据MTL验证，当前系统运行状态未违反规约"
            //     //         }
            //     //         else if (resStr === 'False') {
            //     //             _this.mtlSentence = "根据MTL验证：当前系统运行状态违反规约"
            //     //         } else {
            //     //             _this.mtlSentence = "MTL规约错误"
            //     //         }
            //     //     })
            //     axios.post('http://localhost:3000/mtlPidPerSec', { mtl: _this.mtlSpecific })
            //     .then(response => {
            //         const resStr = response.data
            //         if (resStr === 'True') {
            //             _this.mtlSentence = "根据MTL验证，当前系统运行状态未违反规约"
            //         }
            //         else if (resStr === 'False') {
            //             _this.mtlSentence = "根据MTL验证：当前系统运行状态违反规约"
            //         } else {
            //             _this.mtlSentence = "MTL规约错误"
            //         }
            //     })
            // }
        }
        this.$nextTick(function () {
            this.initEcharts()
        })
        getInfo()
        setInterval(getInfo, 1000)
    }
}
</script>
