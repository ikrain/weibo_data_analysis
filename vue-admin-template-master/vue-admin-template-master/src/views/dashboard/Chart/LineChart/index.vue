<template>
  <div id="linechart" v-loading="loading"></div>
</template>

<script>
import * as echarts from 'echarts'
import '@/utils/chart/china'
export default {
  name: 'LineChart',
  data(){
    return{
      loading: false,
      series: [
        {
          name: '话题数',
          type: 'line',
          stack: 'Total',
          data: [0, 0, 0, 0, 0, 0, 0],
          markPoint: {
            data: [
              { type: 'max', name: 'Max' },
              { type: 'min', name: 'Min' }
            ]
          }
        },
        {
          name: '博文数',
          type: 'line',
          stack: 'Total',
          data: [0, 0, 0, 0, 0, 0, 0],
          markPoint: {
            data: [
              { type: 'max', name: 'Max' },
              { type: 'min', name: 'Min' }
            ]
          }
        },
        {
          name: '评论数',
          type: 'line',
          stack: 'Total',
          data: [0, 0, 0, 0, 0, 1111, 1580],
          markPoint: {
            data: [
              { type: 'max', name: 'Max' },
              { type: 'min', name: 'Min' }
            ]
          }
        },
      ]
    }
  },
  mounted() {
    this.getTime()
  },
  methods:{
    async getTime(){
      this.loading = true
      const resultTopic = await this.$API.line.queryTopicTime()
      const resultComment = await this.$API.line.queryCommentTime()
      const resultArticle = await this.$API.line.queryArticleTime()
      const listTopic = resultTopic.data["topicTimeVoList"]
      const listComment = resultComment.data["commentTimeVoList"]
      const listArticle = resultArticle.data["articleTimeVoList"]
      for(var i=0; i<listTopic.length; i++){
        if(listTopic[i].topic_time == '2022-05-08'){
          this.series[0].data[0] = parseInt(listTopic[i].count)
        }else if(listTopic[i].topic_time == '2022-05-09'){
          this.series[0].data[1] = parseInt(listTopic[i].count)
        }else if(listTopic[i].topic_time == '2022-05-10'){
          this.series[0].data[2] = parseInt(listTopic[i].count)
        }else if(listTopic[i].topic_time == '2022-05-11'){
          this.series[0].data[3] = parseInt(listTopic[i].count)
        }else if(listTopic[i].topic_time == '2022-05-12'){
          this.series[0].data[4] = parseInt(listTopic[i].count)
        }else if(listTopic[i].topic_time == '2022-05-13'){
          this.series[0].data[5] = parseInt(listTopic[i].count)
        }else if(listTopic[i].topic_time == '2022-05-14'){
          this.series[0].data[6] = parseInt(listTopic[i].count)
        }
      }
      for(var i=0; i<listComment.length; i++){
        if(listComment[i].comment_time == '2022-05-08'){
          this.series[2].data[0] = parseInt(listComment[i].count)
        }else if(listComment[i].comment_time == '2022-05-09'){
          this.series[2].data[1] = parseInt(listComment[i].count)
        }else if(listComment[i].comment_time == '2022-05-10'){
          this.series[2].data[2] = parseInt(listComment[i].count)
        }else if(listComment[i].comment_time == '2022-05-11'){
          this.series[2].data[3] = parseInt(listComment[i].count)
        }else if(listComment[i].comment_time == '2022-05-12'){
          this.series[2].data[4] = parseInt(listComment[i].count)
        }else if(listComment[i].comment_time == '2022-05-13'){
          this.series[2].data[5] = parseInt(listComment[i].count)
        }else if(listComment[i].comment_time == '2022-05-14'){
          this.series[2].data[6] = parseInt(listComment[i].count)
        }
      }
      for(var i=0; i<listArticle.length; i++){
        if(listArticle[i].article_time == '2022-05-08'){
          this.series[1].data[0] = parseInt(listArticle[i].count)
        }else if(listArticle[i].article_time == '2022-05-09'){
          this.series[1].data[1] = parseInt(listArticle[i].count)
        }else if(listArticle[i].article_time == '2022-05-10'){
          this.series[1].data[2] = parseInt(listArticle[i].count)
        }else if(listArticle[i].article_time == '2022-05-11'){
          this.series[1].data[3] = parseInt(listArticle[i].count)
        }else if(listArticle[i].article_time == '2022-05-12'){
          this.series[1].data[4] = parseInt(listArticle[i].count)
        }else if(listArticle[i].article_time == '2022-05-13'){
          this.series[1].data[5] = parseInt(listArticle[i].count)
        }else if(listArticle[i].article_time == '2022-05-14'){
          this.series[1].data[6] = parseInt(listArticle[i].count)
        }
      }
      let myChart = echarts.init(document.getElementById('linechart'))
      let option = {
        title: {
          text: '舆情信息统计曲线'
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: ['话题数', '博文数', '评论数']
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
          data: ['2022-05-08', '2022-05-09', '2022-05-10', '2022-05-11', '2022-05-12', '2022-05-13', '2022-05-14']
        },
        yAxis: {
          type: 'value'
        },
        series: this.series
      }
      myChart.setOption(option)
      this.loading = false
    }
  }

}
</script>

<style scoped>
#linechart{
  width: 100%;
  height: 300px;
}
</style>
