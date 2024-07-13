<template>
  <div class="emotion-bottom">
    <el-card>
      
      <div slot="header" class="clearfix">
        <div class="search-input">
          <el-input placeholder="请输入内容" prefix-icon="el-icon-search" v-model="tempSearchObj.topic_name"></el-input>
          <el-button type="success" @click="search" style="margin-left: 5px">搜索</el-button>
        </div>
      </div>

      <div>
        <el-table :loading="loading" class="topic-table" :data="tableData" stripe style="width: 100%;">
          <el-table-column type="index" label="序号" width="100" align="center"></el-table-column>
          <el-table-column prop="comment_author_name" label="作者" width="180" align="center"></el-table-column>
          <el-table-column prop="comment_time" label="时间" width="180" align="center"></el-table-column>
          <el-table-column prop="comment_content" label="内容" width="500px" align="center">
            <!-- 用插槽的方法来改变颜色! -->
            <template slot-scope="scope">
              <div :style="{ color: scope.row.comment_content ? '#2196f3' : '#2196f3' }">
                {{ scope.row.comment_content }}
              </div>
            </template>
          </el-table-column>
          <el-table-column prop="comment_emotion" label="情感值" align="center"></el-table-column>
          <el-table-column prop="emotion_state" label="情感极性" align="center">
            <template slot-scope="scope">
              <span :key="scope.row.emotion_state">
                <el-tag size="small" v-if="scope.row.emotion_state == '积极'" style="color:white;background-color:#24b524;">{{ scope.row.emotion_state }}</el-tag>
                <el-tag size="small" v-if="scope.row.emotion_state == '消极'" style="color:white;background-color:red;">{{ scope.row.emotion_state }}</el-tag>
                <el-tag size="small" v-if="scope.row.emotion_state == '中立'" style="color:white;background-color:#269cff;">{{ scope.row.emotion_state }}</el-tag>
              </span>
            </template>
          </el-table-column>
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
          @current-change="getCommList"
          @size-change="handleSizeChange"
        />
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'EmotionBottom',
  data(){
    return{
      searchObj: { // 包含请求搜索条件数据的对象
        topic_name: '结婚黄牛',
        // 实现分页的字段
        page: 1,
        limit: 10
      },
      tempSearchObj: { // 包含请求搜索条件数据的对象
        topic_name: '结婚黄牛',
        // 实现分页的字段
        page: 1,
        limit: 10
      },
      total: 10,
      tableData: [],
      loading: false,
    }
  },
  mounted(){
    this.getCommList()
  },
  methods:{
    // 搜索话题
    search() {
      this.searchObj = { ...this.tempSearchObj }
      this.getCommList()
    },
    /* 获取分页列表 */
    async getCommList(page = 1) {
      this.searchObj.page = page
      const { searchObj } = this
      this.loading = true
      const result = await this.$API.emotionList.queryCommEmoByPage(searchObj)
      this.loading = false
      this.tableData = result.data["articleCommentList"]
      this.total = result.data["total"]
    },
    /* 处理pageSize发生改变的监听回调 */
    handleSizeChange(pageSize) {
      this.searchObj.page = 1
      this.searchObj.limit = pageSize
      this.getCommList()
    },
  }
}
</script>

<style scoped>
  .emotion-bottom{
    margin-top: 10px;
  }

  .search-input {
    width: 270px;
    cursor: pointer;
    float: left;
  }

  .clearfix .search-input {
    display: flex;
    justify-content: space-between;
  }
</style>