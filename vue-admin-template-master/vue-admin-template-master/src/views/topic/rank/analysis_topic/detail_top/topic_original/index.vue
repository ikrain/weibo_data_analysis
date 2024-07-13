<template>
  <div id="originalChart"></div>
</template>

<script>
import { mapState } from 'vuex'
import * as echarts from 'echarts'
export default {
  name: 'OriginalTrend',
  data(){
    return{
      topicDetailData: {},
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
    this.getOriginal()
  },
  methods:{
    getOriginal(){
      // 获取趋势字符串
      var str = this.dataObj["topic_original_trend"]
      // 将趋势字符串转化为数组
      var arr = eval('(' + str + ')')
      var j = 0
      for(var i=0; i<arr.length; i+=1){
        this.numData[j] = arr[i].value
        this.dateData[j] = arr[i].time
        j++
      }
      let myChart = echarts.init(document.getElementById('originalChart'))
      let option = {
        title: {
          text: '原创趋势',
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
            name: '原创人数',
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
  #originalChart{
    width: 100%;
    height: 275px;
  }
</style>