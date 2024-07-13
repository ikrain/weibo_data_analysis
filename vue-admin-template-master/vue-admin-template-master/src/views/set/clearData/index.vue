<template>
  <div>
    <h3>
      数据清理日志
      <span>
        （每24h清理一次过期数据）
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
  name: 'ClearLog',
  data(){
    return{
      activities: [
        {
          content: '数据清理完成......',
          timestamp: '2022-05-15 01:59',
          size: 'large',
          type: 'primary',
          icon: 'el-icon-more'
        }, {
          content: '数据清理完成......',
          timestamp: '2022-05-14 01:59',
          color: '#0bbd87'
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