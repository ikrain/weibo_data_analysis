<template>
  <div class="world-cloud-img">
    <span class="analysis-title">{{ fit }}</span>
    <el-image
      :src="require('../../../../assets/topic_week.png')"
      :fit="fit">
    </el-image>
  </div>
</template>

<script>
export default {
  name: 'WorldCloud',
  data() {
    return {
      fit: '每周热词',
      // url: 'https://s2.loli.net/2022/04/28/OJ2p75yWixhAo9R.png'
      url: 'D:\Program\Pycharm\weibo_data\weibo_data\analysis\topic_week.png'
    }
  }
}
</script>

<style scoped>
  .world-cloud-img {
    width: 100%;
    /*height: 325px;*/
    height: 100%;
  }
  .analysis-title{
    font-family: "Microsoft YaHei";
    font-size: 22px;
    border-bottom: 1px solid #eee;
  }
</style>
