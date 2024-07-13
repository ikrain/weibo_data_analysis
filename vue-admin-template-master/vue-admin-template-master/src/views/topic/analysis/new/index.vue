<template>
  <div class="headerTag">
    <div slot="header" class="clearfix">
      <span class="analysis-title">最新舆情</span>
    </div>
    <div v-for="item in this.newItem" :key="item.id" class="topic-item" v-loading="loading">
      <li></li>
      <el-link v-bind:href="item.topic_link" type="primary">
        {{ item.topic_name }}
      </el-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NewTopic',
  data() {
    return {
      loading: false,
      newItem: []
    }
  },
  mounted(){
    this.getNewTopic()
  },
  methods:{
    async getNewTopic(){
      this.loading = true
      const result = await this.$API.newTopic.queryNewTopic()
      this.newItem = result["data"]["weekRankList"]
      this.loading = false
    }
  }
}
</script>

<style scoped>
  /* .headerTag{
    height: 368px;
  } */

  .clearfix {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #eee;
  }

  .topic-item {
    display: flex;
    line-height: 30px;
  }

  .raido-button {
    /* padding-bottom: 10px; */
  }

  .analysis-title{
    font-family: "Microsoft YaHei";
    font-size: 22px;
  }
</style>
