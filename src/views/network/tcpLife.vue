<template>
    <div>
        <h1>TCP数据大小与时长：</h1>
        <el-table :data="tableData" style="width: 100%" stripe>
            <el-table-column prop="curTime" label="时间" sortable>
            </el-table-column>
            <el-table-column prop="pid" label="PID" sortable>
            </el-table-column>
            <el-table-column prop="comm" label="COMM" sortable>
            </el-table-column>
            <el-table-column prop="laddr" label="本地地址" sortable>
            </el-table-column>
            <el-table-column prop="lport" label="本地端口" sortable>
            </el-table-column>
            <el-table-column prop="raddr" label="远程地址" sortable>
            </el-table-column>
            <el-table-column prop="rport" label="远程端口" sortable>
            </el-table-column>
            <el-table-column prop="tx" label="传输数据大小(KB)" sortable>
            </el-table-column>
            <el-table-column prop="rx" label="接收数据大小(KB)" sortable>
            </el-table-column>
            <el-table-column prop="ms" label="TCP连接建立时长(ms)" sortable>
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
            axios.get('http://localhost:3000/tcpLife')
                .then(response => {
                    _this.tableData.length = 0
                    const retList = response.data
                    for (let i = retList.length - 1; i >= 0; i--) {
                        const curTime = retList[i][0]
                        const pid = retList[i][1]
                        const comm = retList[i][2]
                        const laddr = retList[i][3]
                        const lport = retList[i][4]
                        const raddr = retList[i][5]
                        const rport = retList[i][6]
                        const tx = retList[i][7]
                        const rx = retList[i][8]
                        const ms = retList[i][9]
                        const newRow = {
                            curTime: curTime,
                            pid: pid,
                            comm: comm,
                            laddr: laddr,
                            lport: lport,
                            raddr: raddr,
                            rport: rport,
                            tx: tx,
                            rx: rx,
                            ms: ms
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
