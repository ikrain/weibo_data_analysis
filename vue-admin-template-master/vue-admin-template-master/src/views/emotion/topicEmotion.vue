<template>
  <div>
    <EmotionTop></EmotionTop>
    <EmotionBottom></EmotionBottom>
  </div>
</template>

<script>
import EmotionTop from './chart/index.vue'
import EmotionBottom from './list/index.vue'
export default {
  name: 'TopicEmotion',
  components:{
    EmotionTop,
    EmotionBottom
  }
}
</script>

<style>

</style>
