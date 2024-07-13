<template>
  <div id="commentPieChart"></div>
</template>

<script>
import * as echarts from 'echarts'
export default {
  name: 'PieChart',
  data(){
    return{
      pieData: [
        {'name': '积极', 'value': 0},
        {'name': '消极', 'value': 0},
        {'name': '中立', 'value': 0}
      ],
      searchObj: { // 包含请求搜索条件数据的对象
        topic_name: '结婚黄牛'
      },
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
      this.$API.emotionPie.queryCommentEmotion(this.searchObj).then((result) => {
        const articleCommentList = result.data["articleCommentList"]
        for(var j=0; j<this.pieData.length; j++){
          this.pieData[j].value = 0
        }
        for(var i=0; i<articleCommentList.length; i++){
          for(var j=0; j<this.pieData.length; j++){
            if( this.pieData[j].name === articleCommentList[i].emotion_state ){
              this.pieData[j].value += 1
            }
          }
        }
        console.log("this.pieData: ", this.pieData);
        // 基于准备好的dom，初始化echarts实例
        let myChart = echarts.init(document.getElementById('commentPieChart'))
        let option = {
          title: {
            text: '情感倾向分布',
            left: 'center'
          },
          tooltip: {
            trigger: 'item'
          },
          series: [
            {
              name: 'Access From',
              type: 'pie',
              radius: '60%',
              data: this.pieData,
              emphasis: {
                itemStyle: {
                  shadowBlur: 10,
                  shadowOffsetX: 0,
                  shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
              }
            }
          ]
        }
        // 绘制图表
        myChart.setOption(option)
      })
    }
  }
}
</script>

<style scoped>
  #commentPieChart{
    width: 100%;
    height: 300px;
  }
</style>