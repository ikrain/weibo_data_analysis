<template>
  <div>
    <h3>
      数据采集日志
      <span>
        （每4h爬取一次）
      </span> 
    </h3>
    <div class="block">
      <el-timeline>
        <el-timeline-item
          v-for="(activity, index) in activities"
          :key="index"
          :icon="activity.icon"
          :type="activity.type"
          :color="activity.color"
          :size="activity.size"
          :timestamp="activity.timestamp">
          {{activity.content}}
        </el-timeline-item>
      </el-timeline>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ScrapyLog',
  data(){
    return{
      activities: [
        {
          content: '数据采集完成......',
          timestamp: '2022-05-15 23:29',
          size: 'large',
          type: 'primary',
          icon: 'el-icon-more'
        }, {
          content: '数据采集完成......',
          timestamp: '2022-05-15 19:29',
          color: '#0bbd87'
        }, {
          content: '数据采集完成......',
          timestamp: '2022-05-15 15:29',
          size: 'large'
        }, {
          content: '数据采集完成......',
          timestamp: '2022-05-15 11:29'
        }, {
          content: '数据采集完成......',
          timestamp: '2022-05-15 7:29'
        }, {
          content: '数据采集完成......',
          timestamp: '2022-05-15 03:29'
        }
      ]
    }
  }
}
</script>

<style scoped>
  h3{
    margin-left: 50px;
  }

  .block{
    margin-left: 50px;
  }

  span{
    font-size: 15px;
    color: #939393;
  }

</style>