<template>
  <div class="topicInfo">
    <div class="infoTop">
      <h3>
        <i class="el-icon-s-order" style="color:#75A7E2;"/>
         # {{ dataObj["topic_name"] }} # 
        <el-tag size="">
          {{ dataObj["topic_category"] }}
        </el-tag>
      </h3>
    </div>
    <div>
      <h3>
        <i class="el-icon-s-promotion" style="color:#75A7E2;"/>
         导语 
      </h3>
      <div style="text-indent: 32px;">
        {{ dataObj["topic_introduction"] }}
      </div>
    </div>
    <div class="infoBottom">
      <h3>
        <i class="el-icon-data-analysis" style="color:#75A7E2;"/>
        话题总览
      </h3>
      <div class="topicView">
        <div class="read" style="float: left; margin-left: 80px;">
          <div class="numFont">
            {{ dataObj["topic_read_num"] }}
          </div>
          <span>阅读次数</span>
        </div>
        
        <div class="talk" style="float: left; margin-left: 80px;">
          <div class="numFont">
            {{ dataObj["topic_talk_num"] }}
          </div>
          <span>讨论次数</span>
        </div>
        
        <div class="original" style="float: left; margin-left: 80px;">
          <div class="numFont">
            {{ dataObj["topic_original_num"] }}
          </div>
          <span>原创人数</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: 'TopicInfo',
  data(){
    return{
      size: ''
    }
  },
  computed: {
    // 从 Vuex 中获取公用数据，
    // 其中 topicDetail 为Vuex模块名
    // dataObj 为接收数据的参数名，可以直接使用dataIbj，无需再赋值
    ...mapState("topicDetail",[
      "dataObj"
    ])
  },
  methods(){
  }
}
</script>

<style scoped>
  .topicInfo{  
    width: 100%;
    height: 255px;
  }
  .topicView{
    text-align: center;
  }
  .numFont{
    font-size: 23px;
  }
  span{
    font-size: 12px;
    color: #939393;
  }
</style>