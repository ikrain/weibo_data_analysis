<template>
  <div>
    <DetailTop></DetailTop>
    <DetailBottom></DetailBottom>
  </div>
</template>

<script>
import DetailTop from './detail_top/index.vue'
import DetailBottom from './detail_bottom/index.vue'
export default {
  name: 'AnalysisTopic',
  components:{
    DetailTop,
    DetailBottom
  },
  data(){
    return{
      topicDetailData: {},
      n: 1
    }
  },
  mounted(){
    // 接收 rank 页面通过路由跳转传递过来的数据
    this.topicDetailData = this.$route.query
    console.log("vuex: ", this.topicDetailData);
    // 给 vuex 传递公用数据
    this.$store.dispatch('topicDetail/initdata', this.topicDetailData)
  },
  methods:{

  }
}
</script>

<style>

</style>