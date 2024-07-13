<template>
  <div class="senTopic">
    <el-row :gutter="10">
      <el-col span="16">
        <el-card>
          <AddWord @updateData='updateData'></AddWord>
        </el-card>
      </el-col>
      <el-col span="8">
        <el-card>
          <SensitiveTopic ref="SensitiveTopic"></SensitiveTopic>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import AddWord from './addWord/index.vue'
import SensitiveTopic from './sensitiveTopic/index.vue'
export default {
  name: 'Sensitive',
  components:{
    AddWord,
    SensitiveTopic
  },
  methods:{
    // 实现 兄弟组件间 同时进行数据刷新 的中介方法
    updateData(){
      this.$refs.SensitiveTopic.getSenWord2()
    }
  }
}
</script>

<style scoped>
  .senTopic{
    margin-top: 10px;
  }
</style>