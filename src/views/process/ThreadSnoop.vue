<template>
    <div>
        <h1>新建的线程信息：</h1>
        <el-table :data="tableData" style="width: 100%" stripe>
            <el-table-column prop="curTime" label="时间" sortable>
            </el-table-column>
            <el-table-column prop="pid" label="PID" sortable>
            </el-table-column>
            <el-table-column prop="comm" label="COMM" sortable>
            </el-table-column>
            <el-table-column prop="func" label="函数" sortable>
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            tableData: [],
        }
    },
    created() {
        const _this = this
        const getInfo = () => {
            axios.get('http://localhost:3000/threadSnoop')
                .then(response => {
                    _this.tableData.length = 0
                    const retList = response.data
                    for (let i = retList.length - 1; i >= 0; i--) {
                        const curTime = retList[i][0]
                        const pid = retList[i][1]
                        const comm = retList[i][2]
                        const func = retList[i][3]
                        const newRow = {
                            curTime: curTime,
                            pid: pid,
                            comm: comm,
                            func: func
                        }
                        _this.tableData.unshift(newRow)                        
                    }
                })
        }
        getInfo()
        setInterval(getInfo, 1000 * 5)
    }
}
</script>
