<template>
  <div class="detail-bottom">
    <el-row :gutter="10">
      <el-col span="12">
        <el-card>
          <ReadTrend></ReadTrend>
        </el-card>
      </el-col>
      <el-col span="12">
        <el-card>
          <TalkTrend></TalkTrend>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import ReadTrend from './topic_read/index.vue'
import TalkTrend from './topic_talk/index.vue'
export default {
  name: 'DetailBottom',
  components:{
    ReadTrend,
    TalkTrend
  },
  data(){
    return{

    }
  },
  methods:{

  }
}
</script>

<style scoped>
  .detail-bottom{
    margin-top: 10px;
  }
</style>