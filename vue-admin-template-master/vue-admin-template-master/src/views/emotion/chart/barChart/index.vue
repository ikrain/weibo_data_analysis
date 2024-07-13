<template>
  <div v-loading="this.loading" id="commentBarChart">
  </div>
</template>

<script>
import * as echarts from 'echarts'
export default {
  name: 'BarChart',
  data(){
    return{
      searchObj: { // 包含请求搜索条件数据的对象
        topic_name: '结婚黄牛'
      },
      barData: [0,0,0],
      loading: false
    }
  },
  mounted(){
    this.getCommentEmotion()
  },
  methods:{
    searchCommentEmotion(obj){
      this.searchObj.topic_name = obj.topic_name
      this.getCommentEmotion()
    },
    getCommentEmotion(){
      this.loading = true
      this.$API.emotionPie.queryCommentEmotion(this.searchObj).then((result) => {
        const articleCommentList = result.data["articleCommentList"]
        for(var j=0; j<this.barData.length; j++){
          this.barData[j] = 0
        }
        for(var i=0; i<articleCommentList.length; i++){
          if(articleCommentList[i].emotion_state === '消极'){
            this.barData[0] += 1
          }else if(articleCommentList[i].emotion_state === '中立'){
            this.barData[1] += 1
          }else if(articleCommentList[i].emotion_state === '积极'){
            this.barData[2] += 1
          }
        }
        // 基于准备好的dom，初始化echarts实例
        let myChart = echarts.init(document.getElementById('commentBarChart'))
        let option = {
          title: {
            text: '情感倾向统计'
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'shadow'
            }
          },
          grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
          },
          xAxis: {
            type: 'value',
            boundaryGap: [0, 0.01]
          },
          yAxis: {
            type: 'category',
            data: ['消极', '中立', '积极']
          },
          series: [
            {
              name: '评论数',
              type: 'bar',
              data: this.barData,
              barWidth: 30,
              itemStyle: {
                normal: {
                  color: function(params) {
                    // 给出颜色组
                    var colorList = ['#4587E7','#F5AD1D','#ff7f50','#da70d6','#32cd32','#6495ed'];
                    return colorList[params.dataIndex%colorList.length]
                  },
                },
              }
            }
          ]
        }
        // 绘制图表
        myChart.setOption(option)
        this.loading = false
      })
    }
  }
}
</script>

<style scoped>
  #commentBarChart{
    width: 100%;
    height: 300px;
  }
</style>