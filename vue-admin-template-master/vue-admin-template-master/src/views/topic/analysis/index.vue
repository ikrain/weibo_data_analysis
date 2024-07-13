<template>
  <div class="top-card">
    <el-row :gutter="10">
      <el-col :span="16">
        <el-card>
          <Worldcloud></Worldcloud>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card>
          <NewTopic></NewTopic>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Worldcloud from './worldcloud/index.vue'
import NewTopic from './new/index.vue'
export default {
  name: 'Top',
  components: {
    Worldcloud,
    NewTopic
  }
}
</script>
<style scoped>
  .top-card{
    padding-top: 10px;
  }
</style>
