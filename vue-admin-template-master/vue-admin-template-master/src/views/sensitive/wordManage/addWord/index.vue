<template>
  <div>
    <div slot="header" class="clearfix">
        <div class="search-input">
          <h3>
            敏感词管理
            <!-- <el-button type="success" @click="search" style="margin-left: 5px;float: right">搜索</el-button> -->
            <el-tag
              :key="tag"
              v-for="tag in dynamicTags"
              closable
              :disable-transitions="false"
              @close="handleClose(tag)">
              {{tag}}
            </el-tag>
            <el-input
              class="input-new-tag"
              v-if="inputVisible"
              v-model="inputValue"
              ref="saveTagInput"
              size="small"
              @keyup.enter.native="handleInputConfirm"
              @blur="handleInputConfirm"
            >
            </el-input>
            <el-button v-else class="button-new-tag" size="small" @click="showInput"> + 添加敏感词</el-button>
          </h3>
        </div>
      </div>

      <div>
        <el-table :loading="loading" class="topic-table" :data="tableData" stripe style="width: 100%;">
          <el-table-column type="index" label="序号" align="center"></el-table-column>
          <el-table-column prop="sensitive_word" label="敏感词" align="center">
            <template slot-scope="scope">
              <span :key="scope.row.sensitive_word">
                <el-tag size="small" style="color:white;background-color:#2196f3;">{{ scope.row.sensitive_word }}</el-tag>
              </span>
            </template>
          </el-table-column>
          <el-table-column prop="create_time" label="创建时间" width="150px" align="center"></el-table-column>
          <el-table-column prop="creater" label="创建人" align="center"></el-table-column>       
          <el-table-column label="操作" align="center">
            <template slot-scope="scope">
              <el-button size="mini" type="danger" @click="deleteSenWord(scope.row.id)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
  </div>
</template>

<script>
export default {
  name: 'AddWord',
  data(){
    return{
      tableData: [],
      loading: false,

      addWord: {
        sensitive_word: '',
        creater: 'admin'
      },
      // 删除所用字段
      delObj: {
        id: ''
      },

      // 使用tag添加敏感词
      dynamicTags: [],
      inputVisible: false,
      inputValue: ''
    }
  },
  mounted(){
    this.getSenWord()
  },
  methods:{
    async getSenWord(){
      this.loading = true
      const result = await this.$API.sensitiveWord.querySenWord();
      this.tableData = result.data["sensitiveWordList"]
      this.loading = false
    },

    deleteSenWord(id){
      this.$confirm(' 是否要删除此敏感词?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(async () => {
        this.delObj.id = id
        await this.$API.sensitiveWord.delSenWordById(this.delObj)
        this.$message({
          type: 'success',
          message: '删除成功!'
        });
        this.getSenWord()
        // 触发父组件方法，让父组件使兄弟组件也刷新
        this.$emit('updateData')
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        });          
      });
    },

    // 使用tag添加敏感词
    handleClose(tag) {
      this.dynamicTags.splice(this.dynamicTags.indexOf(tag), 1);
    },
    showInput() {
      this.inputVisible = true;
      this.$nextTick(_ => {
        this.$refs.saveTagInput.$refs.input.focus();
      });
    },
    handleInputConfirm() {
      let inputValue = this.inputValue;
      if (inputValue) {
        // this.dynamicTags.push(inputValue);
        this.addWord.sensitive_word = inputValue
        this.$API.sensitiveWord.insertSenWord(this.addWord);
        // 触发父组件方法，让父组件使兄弟组件也刷新
        this.$emit('updateData','wuwuwuw')
      }
      this.inputVisible = false;
      this.inputValue = '';
      this.getSenWord()
    }

  }
}
</script>

<style scoped>
  h3{
    margin-top: 0px;
  }

  .button-new-tag{
    background-color: #4caf50;
    color: white;
  }
</style>