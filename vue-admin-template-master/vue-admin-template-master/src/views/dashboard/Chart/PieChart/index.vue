<template>
  <!-- 准备一个容器 -->
  <div id="piechart"></div>
</template>

<script>
import * as echarts from 'echarts'
export default {
  name: 'PieChart',
  data(){
    return{
      pieData: []
    }
  },
  mounted() {
    this.getTopicArea()
  },
  methods:{
    getTopicArea(){
      this.$API.pie.queryTopicArea().then((result) => {
        const topicArea = result.data["topicAreaVo"]
        this.pieData = topicArea
        // 基于准备好的dom，初始化echarts实例
        let myChart = echarts.init(document.getElementById('piechart'))
        let option = {
          title: {
            text: '舆情分布领域',
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
  #piechart {
    width: 100%;
    height: 300px;
  }
</style>
