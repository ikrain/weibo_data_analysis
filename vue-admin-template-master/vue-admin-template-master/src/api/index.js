// 将四个模块请求的接口函数统一暴露
// import * as trademark from './product/tradeMark'
// import * as attr from './product/attr'
// import * as spu from './product/spu'
// import * as sku from './product/sku'

// 引入权限相关的接口文件
import * as user from './manage/user'
import * as role from './manage/role'
import * as map from './dashboard/map'
import * as pie from './dashboard/pie'
import * as line from './dashboard/line'
import * as weekRank from './topic/weekRank'
import * as newTopic from './topic/newTopic'
import * as searchTopic from './search/searchTopic'
import * as emotionPie from './emotion/emotionPie'
import * as emotionList from './emotion/emotionList'
import * as sensitiveWord from './sensitive/sensitiveWord'
import * as card from './dashboard/card'


// 对外暴露
export default {
  user,
  role,
  map,
  pie,
  line,
  weekRank,
  newTopic,
  searchTopic,
  emotionPie,
  emotionList,
  sensitiveWord,
  card
}
