<template>
  <div>
    <LineWord/>
    <SensitiveTopic/>
  </div>
</template>

<script>
import LineWord from './lineWord/index.vue'
import SensitiveTopic from './wordManage/index.vue'
export default {
  name: 'Sensitive',
  components:{
    LineWord,
    SensitiveTopic
  }
}
</script>

<style>

</style>