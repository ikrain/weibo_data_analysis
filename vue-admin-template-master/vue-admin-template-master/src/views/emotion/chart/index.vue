<template>
  <div style="margin-top: 10px;">
    <el-card>

      <div slot="header" class="clearfix">
        <div class="search-input">
          <el-input placeholder="请输入内容" prefix-icon="el-icon-search" v-model="searchObj.topic_name"></el-input>
          <el-button type="success" @click="search" style="margin-left: 5px">搜索</el-button>
        </div>
      </div>

      <div>
        <el-row :gutter="10">
          <el-col span="8">
              <BarChart ref="BarChart"></BarChart>
          </el-col>
          <el-col span="8">
              <EmotionInfo ref="EmotionInfo"></EmotionInfo>
          </el-col>
          <el-col span="8">
              <PieChart ref="PieChart"></PieChart>
          </el-col>
        </el-row>
      </div>
    </el-card>
  </div>
</template>

<script>
import BarChart from './barChart/index.vue';
import EmotionInfo from './emotionInfo/index.vue';
import PieChart from './pieChart/index.vue';
export default {
  name: 'EmotionTop',
  data(){
    return{
      searchObj: { // 包含请求搜索条件数据的对象
        topic_name: '结婚黄牛'
      },
    }
  },
  components:{
    BarChart,
    EmotionInfo,
    PieChart
  },
  methods:{
    search(){
      this.$refs.BarChart.searchCommentEmotion(this.searchObj)
      this.$refs.EmotionInfo.searchCommentEmotion(this.searchObj)
      this.$refs.PieChart.searchCommentEmotion(this.searchObj)
    }
  }
}
</script>

<style scoped>
  .search-input {
    width: 270px;
    cursor: pointer;
    float: left;
  }

  .clearfix .search-input {
    display: flex;
    justify-content: space-between;
  }
</style>