<template>
  <div class="detail-top">
    <el-row :gutter="10">
      <el-col span="12">
        <el-card>
          <TopicInfo></TopicInfo>
        </el-card>
      </el-col>
      <el-col span="12">
        <el-card>
          <OriginalTrend></OriginalTrend>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import TopicInfo from './topic_info/index'
import OriginalTrend from './topic_original/index'
export default {
  name: 'DetailTop',
  components:{
    TopicInfo,
    OriginalTrend
  }
}
</script>

<style scoped>
  .detail-top{
    margin-top: 10px;
  }
</style>