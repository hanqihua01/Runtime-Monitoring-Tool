<template>
    <div>
      <!-- CPU负载历史数据图 -->
      <div id="cpuLoad" style="width: 100%; height: 520px;"></div>
      <div>
        <el-calendar v-model="value" first-day-of-week="7">
          <template slot="dateCell" slot-scope="{date, data}">
            <p :class="data.isSelected ? 'is-selected' : ''">
              {{ data.day.split('-').slice(1)[1] }}
            </p>
          </template>
        </el-calendar>
      </div>
    </div>
  </template>
  
  <script>
  import * as echarts from 'echarts'
  import axios from 'axios'
  export default {
    data() {
      return {
        value: new Date(),
        charts: '', // 图
        option: '', // 图的设置
        opinionData: [],//数据
        xLabels: []
      }
    },
    methods: {
      drawLine(id) {
        this.charts = echarts.init(document.getElementById(id))
        this.option = {
          notMerge: true,
          title: {
            left: '1%',
            text: "CPU负载变化曲线",//标题文本，支持使用 \n 换行。
          },
          tooltip: {
            trigger: 'axis'
          },
          legend: {
            align: 'right',//文字在前图标在后
            left: '1%',
            top: '10%',
            data: ['CPU负载']
          },
          grid: {
            top: '20%',
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
      this.getInfo()
      this.$nextTick(function () {
        this.drawLine('cpuLoad')
      })
      setInterval(this.getInfo, 1000 * 5)
    }
  }
  </script>
  