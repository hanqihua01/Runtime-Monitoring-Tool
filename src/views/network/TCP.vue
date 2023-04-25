<template>
    <div>
        <h1>当前James Server状态为：<span v-bind:style="colorSetting">{{ jamesStatus }}</span>；
        运行端口为<span v-bind:style="colorSetting">{{ jamesPort }}</span>。</h1>
        <el-table :data="tableData" style="width: 100%" :row-class-name="tableRowClassName">
            <el-table-column prop="time" label="时间" sortable>
            </el-table-column>
            <el-table-column prop="status" label="SMTP状态" sortable>
            </el-table-column>
            <el-table-column prop="resTime" label="SMTP响应时间">
            </el-table-column>
        </el-table>
    </div>
</template>

<style>
.el-table .ok-row {
    background: #d7fce2;
}

.el-table .critical-row {
    background: #f6cccc;
}
</style>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            colorSetting: 'color: #f04949',
            jamesStatus: 'Something wrong...',
            jamesPort: '0',
            tableData: []
        }
    },
    methods: {
        tableRowClassName({ row, rowIndex }) {
            if (row.status === 'OK') {
                return 'ok-row'
            } else {
                return 'critical-row'
            }
        }
    },
    created() {
        const _this = this
        const getInfo = () => {
            axios.get('http://localhost:3000/smtpStatus')
                .then(response => {
                    _this.tableData.length = 0
                    const retList = response.data
                    for (let i = retList.length - 1; i >= 0; i--) {
                        const status = retList[i][0]
                        const resTime = retList[i][1]
                        const curTime = retList[i][2]
                        const newRow = {
                            time: curTime,
                            status: status,
                            resTime: resTime
                        }
                        if (status === 'CRITICAL') {
                            newRow.resTime = '无响应'
                        }
                        _this.tableData.unshift(newRow)                        
                    }
                })
            axios.get('http://localhost:3000/jamesStatus')
                .then(response => {
                    const status = response.data[0][0]
                    const port = response.data[0][1]
                    if (status === 'not') {
                        _this.jamesStatus = 'Not running'
                        _this.jamesPort = '0'
                        _this.colorSetting = 'color: #f04949'
                    } else {
                        _this.jamesStatus = 'Running'
                        _this.jamesPort = port
                        _this.colorSetting = 'color: #057b29'
                    }
                })
        }
        getInfo()
        setInterval(getInfo, 1000 * 5)
    }
}
</script>
