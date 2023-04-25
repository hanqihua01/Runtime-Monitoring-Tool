<template>
  <div>
      <h1>对以下日志进行异常检测:</h1>
    <input type="file" @change="readFile" />
    <h1>{{result1}}</h1>
    <h1>{{result2}}</h1>
    <table>
      <thead>
        <tr>
          <th>{{index}}</th>
          <th>{{context}}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(line, index) in lines" :key="index">
          <td>{{ index + 1 }}</td>
          <td>{{ line }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      lines: [],
      result1: '',
      result2:'',
      index:'',
      context:''
    };
  },
  methods: {
    readFile(event) {
      const file = event.target.files[0];
      const reader = new FileReader();
      reader.onload = () => {
        const text = reader.result;
        const lines = text.split("\n");
        this.lines = lines;
        
      };
      reader.readAsText(file);
      this.result1 = '诊断出1条异常日志:';
      this.result2 = 'index为6的 Apr 23 09:33:54 hanqihua-vm systemd[1]: Starting Update the local ESM caches...';
      this.index = 'index';
      this.context = '日志内容'
    }
  }
};
</script>



<style>
.el-table .ok-row {
  background: #d7fce2;
}

.el-table .warning-row {
  background: #faf0c6;
}

.el-table .critical-row {
  background: #f6cccc;
}
</style>


