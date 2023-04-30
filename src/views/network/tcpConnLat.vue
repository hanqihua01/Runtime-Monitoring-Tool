<template>
    <div>
        <h1>TCP连接延迟：</h1>
        <el-table :data="tableData" style="width: 100%" stripe>
            <el-table-column prop="curTime" label="时间" sortable>
            </el-table-column>
            <el-table-column prop="pid" label="PID" sortable>
            </el-table-column>
            <el-table-column prop="comm" label="COMM" sortable>
            </el-table-column>
            <el-table-column prop="ip" label="IP版本" sortable>
            </el-table-column>
            <el-table-column prop="saddr" label="源地址" sortable>
            </el-table-column>
            <el-table-column prop="daddr" label="目的地址" sortable>
            </el-table-column>
            <el-table-column prop="dport" label="目的端口" sortable>
            </el-table-column>
            <el-table-column prop="lat" label="延迟" sortable>
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
            axios.get('http://localhost:3000/tcpConnLat')
                .then(response => {
                    _this.tableData.length = 0
                    const retList = response.data
                    for (let i = retList.length - 1; i >= 0; i--) {
                        const curTime = retList[i][0]
                        const pid = retList[i][1]
                        const comm = retList[i][2]
                        const ip = retList[i][3]
                        const saddr = retList[i][4]
                        const daddr = retList[i][5]
                        const dport = retList[i][6]
                        const lat = retList[i][7]
                        const newRow = {
                            curTime: curTime,
                            pid: pid,
                            comm: comm,
                            ip: ip,
                            saddr: saddr,
                            daddr: daddr,
                            dport: dport,
                            lat: lat
                        }
                        _this.tableData.unshift(newRow)                        
                    }
                })
        }
        getInfo()
        setInterval(getInfo, 1000 * 10)
    }
}
</script>
