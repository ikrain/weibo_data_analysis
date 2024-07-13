<template>
  <div>
    <Top></Top>
    <WeekTopic></WeekTopic>
  </div>
</template>

<script>
import Top from './analysis/index.vue'
import WeekTopic from './rank/index.vue'
export default {
  name: 'TopicDetection',
  components:{
    Top,
    WeekTopic
  }
}
</script>

<style>

</style>
