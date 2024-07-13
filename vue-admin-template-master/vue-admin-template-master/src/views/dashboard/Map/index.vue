<template>
  <div class="map-body">
    <el-card>
      <div id="mapchart"></div>
    </el-card>
  </div>
</template>

<script>
import * as echarts from 'echarts'
export default {
  name: 'Map',
  data(){
    return{
      // 地图数据
      dataList: []
    }
  },
  mounted() {
    this.getCommentMap()
  },
  methods:{
    // 中国地图展示每个省份的用户活跃数
    getCommentMap(){
      let myChart = echarts.init(document.getElementById('mapchart'))
      this.$API.map.queryCommMap().then((result) => {
        const mapListVo = result.data["mapListVo"]
        mapListVo[31].name = '台湾'   
        mapListVo[32].name = '香港'   
        mapListVo[33].name = '澳门'
        this.dataList = mapListVo
        // 数据获取完毕后，再渲染地图
        let option = {
          title: {
            text: '微博活跃用户分布图',
            subtext: '',
            left: 'left',
            textStyle: {
              color: '#fff',
              fontSize: 30
            },
            subtextStyle: {
              fontSize: 20
            }
          },
          tooltip: {
            triggerOn: 'click',
            formatter: function (e, t, n) {
              return e.seriesName + '<br />' + e.name + '：' + e.value
            }
          },
          // 热力地图
          visualMap: {
            min: 0,
            max: 1000,
            left: 240,
            textStyle: {
              color: '#fff'
            },
            pieces: [
              {
                gt: 400,
                label: '> 400 人',
                color: '#7f1100'
              },
              {
                gte: 301,
                lte: 400,
                label: '301 - 400 人',
                color: '#ff5428'
              },
              {
                gte: 201,
                lt: 300,
                label: '201 - 300 人',
                color: '#ff8c71'
              },
              {
                gte: 101,
                lt: 200,
                label: '101 - 200 人',
                color: '#ffd768'
              },
              {
                gte: 1,
                lt: 100,
                label: '0 - 100 人',
                color: '#f5e4d7'
              },
              {
                value: 0,
                label: '0 人',
                color: '#ffffff'
              }
            ]
          },
          series: [
            {
              name: '活跃人数',
              data: this.dataList,
              type: 'map',
              map: 'china',
              zoom: 1.2,
              aspectScale: 0.75,
              label: {
                // 默认文本标签样式
                normal: {
                  color: 'white',
                  show: true
                },
                // 高亮文本标签样式
                emphasis: {
                  color: 'yellow',
                  fontSize: 22,
                  fontWeight: 'bold'
                }
              },
              itemStyle: {
                // 默认区域样式
                normal: {
                  // 区域背景透明
                  areaColor: 'transparent',
                  borderColor: 'rgba(39,211,233, 1)',
                  borderWidth: 1
                },
                // 高亮区域样式
                emphasis: {
                  // 高亮区域背景色
                  areaColor: '#01ADF2'
                }
              }
            }
          ]
        }
        myChart.setOption(option)
      });
    }
  }
}
</script>

<style scoped>
.map-body {
  margin-top: 20px;
}

#mapchart {
  width: 100%;
  height: 500px;
  background: #304156;
  padding: 30px;
  box-sizing: border-boxs;
}
</style>
