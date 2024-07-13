<template>
  <div class="rank-topic">
    <el-card>
      <div slot="header" class="clearfix">
        <span class="analysis-title">舆情信息检索</span>
        <div class="search-input">
          <el-input placeholder="请输入内容" prefix-icon="el-icon-search" v-model="tempSearchObj.content"></el-input>
          <el-button type="success" @click="search" style="margin-left: 5px">搜索</el-button>
        </div>
      </div>

      <div>
        <el-table v-loading="loading" class="topic-table" :data="tableData" stripe style="width: 100%;">
          <el-table-column prop="author_name" label="作者" width="150" align="center"></el-table-column>
          <el-table-column prop="article_time" label="时间" width="150" align="center"></el-table-column>
          <el-table-column prop="article_content" label="内容" width="700px" align="center">
            <!-- 在 <template> 上使用特殊的 slot-scope 特性，可以接收传递给插槽的 prop 属性。 -->
            <template slot-scope="scope">
              <!-- <el-link v-html="brightenKeyword(scope.row.article_content,'哈尔滨')" type="primary" @click="goToArticleDetail(scope.row.article_link)" target="_blank">{{ scope.row.article_content }}</el-link> -->
              <div href="#" class="topicUrl" v-html="brightenKeyword(scope.row.article_content,tempSearchObj.content)" @click="goToArticleDetail(scope.row.article_link)">
                {{ scope.row.article_content }}
              </div>
            </template>
          </el-table-column>
          <el-table-column prop="article_emotion" label="情感值" align="center"></el-table-column>
          <!-- <el-table-column prop="emotion_state" label="情感极性" align="center">
            <template slot-scope="scope">
              <span :key="scope.row.emotion_state">
                <el-tag size="small" v-if="scope.row.emotion_state == '积极'" style="color:white;background-color:#24b524;">{{ scope.row.emotion_state }}</el-tag>
                <el-tag size="small" v-if="scope.row.emotion_state == '消极'" style="color:white;background-color:red;">{{ scope.row.emotion_state }}</el-tag>
                <el-tag size="small" v-if="scope.row.emotion_state == '中立'" style="color:white;background-color:#269cff;">{{ scope.row.emotion_state }}</el-tag>
              </span>
            </template>
          </el-table-column> -->
          <el-table-column prop="article_hot_value" label="热度值" align="center"></el-table-column>
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
          @current-change="getTopicSearch"
          @size-change="handleSizeChange"
        />
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'AllTopic',
  data() {
    return {
      searchObj: { // 包含请求搜索条件数据的对象
        content: '',
        // 实现分页的字段
        page: 1,
        limit: 10
      },
      tempSearchObj: { // 包含请求搜索条件数据的对象
        content: '',
        // 实现分页的字段
        page: 1,
        limit: 10
      },
      total: 20,
      tableData: [],
      loading: false,
    }
  },
  mounted(){
    this.getTopicSearch()
  },
  methods:{
    highlight(text) {
      const highlightStr = `<span class="active">${this.searchObj.content}</span>`
      const reg = new RegExp(this.searchObj.content, 'gi')
      return text.replace(reg, highlightStr)
    },
    // 搜索话题
    search() {
      this.searchObj = { ...this.tempSearchObj }
       this.getTopicSearch()
    },
    /* 获取分页列表 */
    async getTopicSearch(page = 1) {
      this.searchObj.page = page
      const { searchObj } = this
      this.loading = true
      const result = await this.$API.searchTopic.getSearchTopic(searchObj)
      this.loading = false
      this.tableData = result.data["searchTopicVoList"]
      console.log("getData: ", this.tableData);
      this.total = result.data["total"]
    },
    /* 处理pageSize发生改变的监听回调 */
    handleSizeChange(pageSize) {
      this.searchObj.page = 1
      this.searchObj.limit = pageSize
      this.getTopicSearch()
    },
    goToArticleDetail(url){
      window.open(url,"_blank"); 
      console.log('http://'+url);
    },
    //搜索高亮
    brightenKeyword(val, keyword) {
      // if (keyword.length > 0) {
      let keywordArr = keyword.split("");
      val = val + "";
      keywordArr.forEach(item => {
        if (val.indexOf(item) !== -1 && item !== "") {
          val = val.replace(
            new RegExp(item,'g'),
            '<font style="color: red">' + item + "</font>"
          );
        }
      });
      return val;
      // }
      //  else {
      //   alert(keyword+"sadf")
      //   return val;
      // }
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

.topicUrl{
  color: #2196f3;
}
</style>
