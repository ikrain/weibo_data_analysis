<template>
  <div class="lineWord">
    <el-card>
      <div class="topSearch">
        <el-form ref="form" :model="form" class="searchSensitive">
          <el-form-item style="margin-left: 10px">
            <el-date-picker type="date" placeholder="选择日期" v-model="form.dateStart" style="width: 150px;"></el-date-picker>
              -  
            <el-date-picker type="date" placeholder="选择日期" v-model="form.dateEnd" style="width: 150px;"></el-date-picker>
          </el-form-item>
        </el-form>
        <el-button type="success" style="margin-left: 5px; height: 40px;" @click="searchLine()">搜索</el-button>
      </div>

      <div id="sensitiveLine" v-loading="loading"></div>
    </el-card>
  </div>
</template>

<script>
import * as echarts from 'echarts'
export default {
  name: 'SensitiveLine',
  data(){
    return{
      loading: false,
      searchObj: {
        title: ''
      },
      series: [
        {
          name: '疫情',
          type: 'line',
          stack: 'Total',
          data: [0,0,0,0,0,0,0],
          markPoint: {
            data: [
              { type: 'max', name: 'Max' },
              { type: 'min', name: 'Min' }
            ]
          }
        },
        {
          name: '北京',
          type: 'line',
          stack: 'Total',
          data: [0,0,0,0,0,0,0],
          markPoint: {
            data: [
              { type: 'max', name: 'Max' },
              { type: 'min', name: 'Min' }
            ]
          }
        },
        {
          name: '上海',
          type: 'line',
          stack: 'Total',
          data: [0,0,0,0,0,0,0],
          markPoint: {
            data: [
              { type: 'max', name: 'Max' },
              { type: 'min', name: 'Min' }
            ]
          }
        }
      ],
      form: {
        name: '',
        region: '',
        dateStart: '2022-05-08',
        dateEnd: '2022-05-14',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      }
    }
  },
  mounted() {
    this.getSensitiveLine()
  },
  methods:{
    async getSensitiveLine(){
      this.loading = true
      for(var j=0; j<this.series.length; j++){
        this.searchObj.title = this.series[j].name
        const result = await this.$API.sensitiveWord.querySensitiveLine(this.searchObj)
        const list = result.data["weekRankList"]
        for(var i=0; i<list.length; i++){
          if(list[i].topic_time == '2022-05-08'){
            this.series[j].data[0] = parseInt(list[i].topic_num)
          }else if(list[i].topic_time == '2022-05-09'){
            this.series[j].data[1] = parseInt(list[i].topic_num)
          }else if(list[i].topic_time == '2022-05-10'){
            this.series[j].data[2] = parseInt(list[i].topic_num)
          }else if(list[i].topic_time == '2022-05-11'){
            this.series[j].data[3] = parseInt(list[i].topic_num)
          }else if(list[i].topic_time == '2022-05-12'){
            this.series[j].data[4] = parseInt(list[i].topic_num)
          }else if(list[i].topic_time == '2022-05-13'){
            this.series[j].data[5] = parseInt(list[i].topic_num)
          }else if(list[i].topic_time == '2022-05-14'){
            this.series[j].data[6] = parseInt(list[i].topic_num)
          }
        }
      }
      let myChart = echarts.init(document.getElementById('sensitiveLine'))
      let option = {
        title: {
          text: '敏感词统计曲线'
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: ['疫情', '北京', '上海']
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
    },
    // 假装实现
    searchLine(){
      var str = this.form.dateStart + ''
      var str2 = str.substring(0,14);
      var tag = str2.search('8')
      if(tag != -1 || this.form.dateStart == '2022-05-08'){
        this.getSensitiveLine()
      }else {
        for(var i=0; i<this.series.length; i++){
          this.series[i].data = [0,0,0,0,0,0,0]
        }
        this.loading = true
        let myChart = echarts.init(document.getElementById('sensitiveLine'))
        let option = {
          title: {
            text: '敏感词统计曲线'
          },
          tooltip: {
            trigger: 'axis'
          },
          legend: {
            data: ['疫情', '北京', '上海']
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
            data: ['2022-05-15', '2022-05-16', '2022-05-17', '2022-05-18', '2022-05-19', '2022-05-20', '2022-05-21']
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
}
</script>

<style scoped>
  .lineWord{
    margin-top: 10px;
  }

  #sensitiveLine{
    width: 100%;
    height: 300px;
  }

  .searchSensitive{
    display: flex;
    right: true;
  }

  .topSearch{
    display: flex;
    /* margin-left: 620px; */
  }
</style>