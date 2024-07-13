import request from '@/utils/request'

/* 获取后台用户分页列表(带搜索) */
export function getSearchTopic(searchObj) {
  return request({
    url: '/search/querySearchTopic',
    method: 'get',
    params: searchObj
  })
}
