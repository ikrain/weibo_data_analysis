<template>
  <div id="readTrend"></div>
</template>

<script>
import * as echarts from 'echarts'
import { mapState } from 'vuex'
export default {
  name: 'ReadTrend',
  data(){
    return{
      numData: [],
      dateData: []
    }
  },
  computed: {
    // 从 Vuex 中获取公用数据，
    // 其中 topicDetail 为Vuex模块名
    // dataObj 为接收数据的参数名，可以直接使用dataIbj，无需再赋值
    ...mapState("topicDetail",[
      "dataObj"
    ])
  },
  mounted(){
    this.getReadChart()
  },
  methods:{
    getReadChart(){
      // 获取趋势字符串
      var str = this.dataObj["topic_read_trend"]
      // 将趋势字符串转化为数组
      var arr = eval('(' + str + ')')
      var j = 0
      for(var i=0; i<arr.length; i++){
        this.numData[j] = arr[i].value
        this.dateData[j] = arr[i].time
        j++
      }
      let myChart = echarts.init(document.getElementById('readTrend'))
      let option = {
        title: {
          text: '阅读趋势',
        },
        tooltip: {
          trigger: 'axis'
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: this.dateData
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            name: '阅读人数',
            type: 'line',
            stack: 'Total',
            smooth: true,
            data: this.numData
          }
        ]
      }
      myChart.setOption(option)
    }
  }
}
</script>

<style scoped>
  #readTrend{
    width: 100%;
    height: 275px;
  }
</style>