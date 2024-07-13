<template>
  <div>
    <el-row :gutter="10">
      <el-col :span="6">
        <el-card class="card-color1">
          <Detail title="热门话题数" :count="this.topicNum"></Detail>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="card-color2">
          <Detail title="博文总数" :count="this.articleNum"></Detail>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="card-color3">
          <Detail title="新增话题数"  :count="this.topicAddNum"></Detail>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="card-color4">
          <Detail title="新增博文数"  :count="this.articleAddNum"></Detail>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Detail from './Detail/index'
export default {
  name: 'Card',
  data(){
    return{
      topicNum: 0,
      articleNum: 0,
      topicAddNum: 0,
      articleAddNum: 0
    }
  },
  components: {
    Detail
  },
  mounted(){
    this.getTopicNum()
    this.getArticleNum()
    this.getTopicAddNum()
    this.getArticleAddNum()
  },
  methods:{
    async getTopicNum(){
      const result = await this.$API.card.queryTopicNum()
      this.topicNum = result.data["topicNum"]
    },
    async getArticleNum(){
      const result = await this.$API.card.queryArticleNum()
      this.articleNum = result.data["articleNum"]
    },
    async getTopicAddNum(){
      const result = await this.$API.card.queryTopicAddNum()
      this.topicAddNum = result.data["topicAddNum"]
    },
    async getArticleAddNum(){
      const result = await this.$API.card.queryArticleAddNum()
      this.articleAddNum = result.data["articleAddNum"]
    },
  }
}
</script>

<style scoped>
.card-color1{
  background-color:cornflowerblue;
}

.card-color2{
  background-color:orange;
}

.card-color3{
  background-color:rgb(242, 90, 82);
}

.card-color4{
  background-color:rgb(96, 228, 96);
}
</style>
