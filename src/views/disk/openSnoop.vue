<template>
    <div>
        <h1>进程打开的文件信息：</h1>
        <el-table :data="tableData" style="width: 100%" stripe>
            <el-table-column prop="curTime" label="时间" sortable>
            </el-table-column>
            <el-table-column prop="pid" label="PID" sortable>
            </el-table-column>
            <el-table-column prop="comm" label="COMM" sortable>
            </el-table-column>
            <el-table-column prop="fd" label="FD" sortable>
            </el-table-column>
            <el-table-column prop="err" label="ERR" sortable>
            </el-table-column>
            <el-table-column prop="path" label="文件路径" sortable>
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            tableData: [], // 虚拟内存大小数据表格初始化
        }
    },
    created() {
        const _this = this
        const getInfo = () => {
            axios.get('http://localhost:3000/openSnoop')
                .then(response => {
                    _this.tableData.length = 0
                    const retList = response.data
                    for (let i = retList.length - 1; i >= 0; i--) {
                        const curTime = retList[i][0]
                        const pid = retList[i][1]
                        const comm = retList[i][2]
                        const fd = retList[i][3]
                        const err = retList[i][4]
                        const path = retList[i][5]
                        const newRow = {
                            curTime: curTime,
                            pid: pid,
                            comm: comm,
                            fd: fd,
                            err: err,
                            path: path
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
