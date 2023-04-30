<template>
    <div>
        <h1>调度延迟高于10000us的进程信息：</h1>
        <el-table :data="tableData" style="width: 100%" stripe>
            <el-table-column prop="time" label="时间" sortable>
            </el-table-column>
            <el-table-column prop="comm" label="COMM" sortable>
            </el-table-column>
            <el-table-column prop="tid" label="TID" sortable>
            </el-table-column>
            <el-table-column prop="lat" label="延迟(us)" sortable>
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
            axios.get('http://localhost:3000/runQSlower')
                .then(response => {
                    _this.tableData.length = 0
                    const retList = response.data
                    for (let i = retList.length - 1; i >= 0; i--) {
                        const time = retList[i][0]
                        const comm = retList[i][1]
                        const tid = retList[i][2]
                        const lat = retList[i][3]
                        const newRow = {
                            time: time,
                            comm: comm,
                            tid: tid,
                            lat: lat,
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
