import request from '@/utils/request'

/* 获取后台用户分页列表(带搜索) */
export function queryNewTopic() {
  return request({
    url: '/topic/queryNewTopic',
    method: 'get'
  })
}
