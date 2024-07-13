<template>
  <div style="margin-left: 20px">
    <h3 align="center" style="padding-bottom: 5px;">情感倾向图表</h3>
    <el-table :data="tableData" border="true" stripe style="width: 100%;font-size: 18px;">
      <el-table-column prop="emotion" align="center" label="情绪" > </el-table-column>
      <el-table-column prop="comment" align="center" label="评论数"> </el-table-column>
      <el-table-column prop="percentage" align="center" label="占比"></el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "EmotionInfo",
  data(){
    return{
      tableData: [
        {
          emotion: '积极',
          comment: 0,
          percentage: ''
        },{
          emotion: '中立',
          comment: 0,
          percentage: ''
        },{
          emotion: '消极',
          comment: 0,
          percentage: ''
        }
      ],
      searchObj: {
        topic_name: '结婚黄牛'
      }
    }
  },
  mounted(){
    this.getCommentEmotion()
  },
  methods:{
    searchCommentEmotion(obj){
      this.searchObj.topic_name = obj.topic_name
      this.getCommentEmotion()
    },
    getCommentEmotion(){
      this.$API.emotionPie.queryCommentEmotion(this.searchObj).then((result) => {
        const articleCommentList = result.data["articleCommentList"]
        // 每次查询前，要将comment赋值为0
        for(var j=0; j<this.tableData.length; j++){
          this.tableData[j].comment = 0
          this.tableData[j].percentage = ''
        }
        for(var i=0; i<articleCommentList.length; i++){
          if(articleCommentList[i].emotion_state === '积极'){
            this.tableData[0].comment += 1
          }else if(articleCommentList[i].emotion_state === '中立'){
            this.tableData[1].comment += 1
          }else if(articleCommentList[i].emotion_state === '消极'){
            this.tableData[2].comment += 1
          }
        }
        var per0 = this.tableData[0].comment / articleCommentList.length
        console.log(per0);
        this.tableData[0].percentage = String(per0.toFixed(2) * 100) + '%'
        var per1 = this.tableData[1].comment / articleCommentList.length
        this.tableData[1].percentage = String(per1.toFixed(2) * 100) + '%'
        var per2 = this.tableData[2].comment / articleCommentList.length
        this.tableData[2].percentage = String(per2.toFixed(2) *100) + '%'
      });
    }
  }
};
</script>

<style></style>
