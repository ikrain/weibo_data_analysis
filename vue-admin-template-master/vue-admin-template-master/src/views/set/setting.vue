<template>
  <div class="scrapySet">
    <el-card style="height: 640px;">
      <h2>系统爬虫配置信息</h2>
      <div>
        <el-row :gutter="10">
          <el-col span="8">
            <ScrapyLog></ScrapyLog>
          </el-col>
          <el-col span="8">
            <AnalysisLog></AnalysisLog>
          </el-col>
          <el-col span="8">
            <ClearLog></ClearLog>
          </el-col>
        </el-row>
      </div>
    </el-card>
  </div>
</template>

<script>
import ScrapyLog from './scrapyLog/index.vue'
import AnalysisLog from './analysisLog/index.vue'
import ClearLog from './clearData/index.vue'
export default {
  name: 'Set',
  components:{
    ScrapyLog,
    AnalysisLog,
    ClearLog
  }
}
</script>

<style scoped>
  .scrapySet{
    margin-top: 10px;
  }
</style>
