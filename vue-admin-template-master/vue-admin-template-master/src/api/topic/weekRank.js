import request from '@/utils/request'

/* 获取后台用户分页列表(带搜索) */
export function getWeekList(searchObj) {
  return request({
    url: '/topic/queryWeekRank',
    method: 'get',
    params: searchObj
  })
}
