<template>
  <div>
    <div slot="header" class="clearfix">
      <h3>敏感话题</h3>
    </div>
    <div v-for="item in this.newItem" :key="item.id" class="topic-item">
      <li></li>
      <el-link v-bind:href="item.topic_link" type="primary">
        {{ item.topic_name }}
      </el-link>
    </div>
    <div>
      <el-radio-group  v-model="radio" size="small">
        <el-radio-button  
          v-for="item in this.radioList" 
          :label="item.sensitive_word" 
          :key="item.id" 
          @click.native="searchTopicByWord(item.sensitive_word)"></el-radio-button>
        <!-- <el-radio-button label="疫情"></el-radio-button> -->
      </el-radio-group>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SensitiveTopic',
  data(){
    return {
      newItem: [],
      radio: '北京',
      radioList: [
        {
          sensitive_word: ''
        }
      ],
      searchObj: {
        senWord: ''
      }
    }
  },
  mounted(){
    this.getSenWord()
  },
  methods:{

    // 为实现兄弟组件间互调方法而设置
    async getSenWord2(){
      this.loading = true
      const result = await this.$API.sensitiveWord.querySenWord();
      this.radioList = result.data["sensitiveWordList"]
      this.loading = false
    },

    // 获取敏感词
    async getSenWord(){
      this.loading = true
      const result = await this.$API.sensitiveWord.querySenWord();
      this.radioList = result.data["sensitiveWordList"]
      this.radio = this.radioList[0].sensitive_word
      this.getTopicByWord(this.radio)
      this.loading = false
    },
    // 获取敏感词下的话题
    async getTopicByWord(word){
      this.loading = true
      this.searchObj.senWord = word
      const result = await this.$API.sensitiveWord.queryTopicByWord(this.searchObj);
      this.newItem = result.data["weekRankList"]
      this.loading = false
    },
    searchTopicByWord(word){
      this.getTopicByWord(word)
    }
  }
}
</script>

<style scoped>
  h3{
    margin-top: 0px;
  }

  .topic-item {
    display: flex;
    line-height: 30px;
  }
</style>