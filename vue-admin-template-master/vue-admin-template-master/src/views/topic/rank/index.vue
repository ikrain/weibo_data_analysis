<template>
  <div class="rank-topic">
    <el-card>
      <div slot="header" class="clearfix">
        <span class="analysis-title">每周热点话题</span>
        <div class="search-input">
          <el-input placeholder="请输入内容" prefix-icon="el-icon-search" v-model="tempSearchObj.content"></el-input>
          <el-button type="success" style="margin-left: 5px" @click="search">搜索</el-button>
        </div>
      </div>

      <div>
        <el-table v-loading="loading" class="topic-table" :data="tableData" stripe style="width: 100%;">
          <el-table-column type="index" prop="id" label="话题ID" width="80" align="center"></el-table-column>
          <el-table-column prop="content" label="话题内容" width="400" align="center">
            <!-- 在 <template> 上使用特殊的 slot-scope 特性，可以接收传递给插槽的 prop 属性。 -->
            <template slot-scope="scope">
              <el-link type="primary" @click="goToDetail(scope.row)" target="_blank">{{ scope.row.topic_name }}</el-link>
            </template>
          </el-table-column>
          <el-table-column prop="topic_time" label="话题创建时间" align="center"></el-table-column>
          <el-table-column prop="topic_num" label="话题热度" align="center"></el-table-column>
        </el-table>
      </div>

      <!-- 分页器 -->
      <div class="bottom-page">
        <el-pagination
          :current-page="this.searchObj.page"
          :total="total"
          :page-size="limit"
          :page-sizes="[10, 15, 20]"
          style="padding: 20px 0;"
          layout="prev, pager, next, jumper, ->, sizes, total"
          @current-change="getRankTopic"
          @size-change="handleSizeChange"
        />
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "WeekTopic",
  data() {
    return {
      searchObj: { // 包含请求搜索条件数据的对象
        content: '',
        // 实现分页的字段
        page: 1,
        limit: 8
      },
      tempSearchObj: { // 包含请求搜索条件数据的对象
        content: '',
        // 实现分页的字段
        page: 1,
        limit: 8
      },
      total: 20,
      tableData: [],
      loading: false
    }
  },
  
  created(){
    this.getRankTopic()
  },

  methods:{
    // 搜索话题
    search() {
      this.searchObj = { ...this.tempSearchObj }
      this.getRankTopic()
    },
    /* 获取分页列表 */
    async getRankTopic(page = 1) {
      this.searchObj.page = page
      const { searchObj } = this
      this.loading = true
      const result = await this.$API.weekRank.getWeekList(searchObj)
      this.loading = false
      this.tableData = result.data["weekRankVoList"]
      this.total = result.data["total"]
    },
    /* 处理pageSize发生改变的监听回调 */
    handleSizeChange(pageSize) {
      this.searchObj.page = 1
      this.searchObj.limit = pageSize
      this.getRankTopic()
    },
    // 跳转到 每周热门话题 详情页
    // 同时将参数 tdData 传递过去
    goToDetail(tdData){
      this.$router.push({
        path: '/analysisTopic',
        query: tdData
      });
      console.log("tdData: ", tdData);
    }
  }
}
</script>

<style scoped>
.rank-topic {
  padding-top: 10px;
}

.search-input {
  width: 270px;
  cursor: pointer;
  float: right;
}

.clearfix .search-input {
  display: flex;
  justify-content: space-between;
}

.topic-item {
  display: flex;
  line-height: 32px;
}

.analysis-title {
  font-family: "Microsoft YaHei";
  font-size: 22px;
  line-height: 50px;
}

.bottom-page{
  padding-top: 10px;
}
</style>
