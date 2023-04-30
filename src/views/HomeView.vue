<template>
  <div>
    <div style="margin-left: 1%;">
      <el-descriptions title="系统信息" direction="vertical" :column="2" border>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-menu"></i>
            操作系统
          </template>
          {{ OS }}
        </el-descriptions-item>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-s-platform"></i>
            主机
          </template>
          {{ Host }}
        </el-descriptions-item>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-info"></i>
            内核版本
          </template>
          {{ Kernel }}
        </el-descriptions-item>
        <el-descriptions-item label="运行时间">
          <template slot="label">
            <i class="el-icon-s-promotion"></i>
            运行时间
          </template>
          {{ Uptime }}
        </el-descriptions-item>
        <el-descriptions-item label="CPU">
          <template slot="label">
            <i class="el-icon-s-tools"></i>
            CPU
          </template>
          {{ CPU }}
        </el-descriptions-item>
        <el-descriptions-item label="GPU">
          <template slot="label">
            <i class="el-icon-picture"></i>
            GPU
          </template>
          {{ GPU }}
        </el-descriptions-item>
        <el-descriptions-item label="内存">
          <template slot="label">
            <i class="el-icon-s-management"></i>
            内存
          </template>
          {{ Memory }}
        </el-descriptions-item>
      </el-descriptions>
    </div>
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
import axios from 'axios'
export default {
  data() {
    return {
      value: new Date(),
      OS: '',
      Host: '',
      Kernel: '',
      Uptime: '',
      CPU: '',
      GPU: '',
      Memory: ''
    }
  },
  created() {
    const _this = this
    const getInfo = () => {
      axios.get('http://localhost:3000/systemInfo')
        .then(response => {
          // Ubuntu 20.04.6 LTS x86_64|VMware Virtual Platform None|5.15.0-69-generic|2 hours, 3 mins|Intel i7-1065G7 (4) @ 1.497GHz|00:0f.0 VMware SVGA II Adapter|2848MiB / 3889MiB|
          const retString = response.data
          const retList = retString.split('|')
          _this.OS = retList[0]

          _this.Host = retList[1]
          _this.Kernel = retList[2]
          _this.Uptime = retList[3]
          _this.CPU = retList[4]
          _this.GPU = retList[5]
          _this.Memory = retList[6]
        })
    }
    getInfo()
    setInterval(getInfo, 1000 * 60)
  }
}
</script>