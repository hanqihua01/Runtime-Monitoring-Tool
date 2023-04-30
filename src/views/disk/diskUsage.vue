<template>
    <div>
        <h1>当前磁盘空间占用：</h1>
        <el-table :data="tableData" style="width: 100%" :row-class-name="tableRowClassName" stripe>
            <el-table-column prop="fileSystem" label="文件系统">
            </el-table-column>
            <el-table-column prop="capacity" label="容量" sortable>
            </el-table-column>
            <el-table-column prop="used" label="已用" sortable>
            </el-table-column>
            <el-table-column prop="available" label="可用" sortable>
            </el-table-column>
            <el-table-column prop="usedPercentage" label="已用%" sortable>
            </el-table-column>
            <el-table-column prop="mount" label="挂载点">
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
            axios.get('http://localhost:3000/diskUsage')
                .then(response => {
                    _this.tableData.length = 0
                    const retString = response.data
                    const retList = retString.split('|')
                    for (let i = 0; i < retList.length; i++) {
                        const tempString = retList[i]
                        
                        const tempList = tempString.split(/\s+/)
                        console.log(tempList)

                        const newRow = {
                            fileSystem: tempList[0],
                            capacity: tempList[1],
                            used: tempList[2],
                            available: tempList[3],
                            usedPercentage: tempList[4],
                            mount: tempList[5]
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
