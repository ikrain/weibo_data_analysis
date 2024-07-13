<template>
  <div class="chart-body">
    <el-row :gutter="10">
      <el-col :span="16">
        <el-card>
          <LineChart></LineChart>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card>
          <PieChart></PieChart>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import LineChart from './LineChart/index.vue'
import PieChart from './PieChart/index.vue'
export default {
  name: 'Chart',
  components:{
    LineChart,
    PieChart
  }
}
</script>

<style scoped>
  .chart-body{
    margin-top: 20px;
  }
</style>
