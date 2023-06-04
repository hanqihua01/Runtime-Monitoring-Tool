<template>
    <div>
        <h1>被动建立的TCP连接：</h1>
        <el-table :data="tableData" style="width: 100%" stripe>
            <el-table-column prop="curTime" label="时间" sortable>
            </el-table-column>
            <el-table-column prop="pid" label="PID" sortable>
            </el-table-column>
            <el-table-column prop="comm" label="COMM" sortable>
            </el-table-column>
            <el-table-column prop="ip" label="IP版本" sortable>
            </el-table-column>
            <el-table-column prop="raddr" label="远程地址" sortable>
            </el-table-column>
            <el-table-column prop="rport" label="远程端口" sortable>
            </el-table-column>
            <el-table-column prop="laddr" label="本地地址" sortable>
            </el-table-column>
            <el-table-column prop="lport" label="本地端口" sortable>
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
            axios.get('http://localhost:3000/passiveTCP')
                .then(response => {
                    _this.tableData.length = 0
                    const retList = response.data
                    for (let i = retList.length - 1; i >= 0; i--) {
                        const curTime = retList[i][0]
                        const pid = retList[i][1]
                        const comm = retList[i][2]
                        const ip = retList[i][3]
                        const raddr = retList[i][4]
                        const rport = retList[i][5]
                        const laddr = retList[i][6]
                        const lport = retList[i][7]
                        const newRow = {
                            curTime: curTime,
                            pid: pid,
                            comm: comm,
                            ip: ip,
                            raddr: raddr,
                            rport: rport,
                            laddr: laddr,
                            lport: lport
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
