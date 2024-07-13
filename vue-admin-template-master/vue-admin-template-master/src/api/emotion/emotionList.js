import request from '@/utils/request'

export function queryCommEmoByPage(searchObj) {
  return request({
    url: '/emotion/queryCommEmoByPage',
    method: 'get',
    params: searchObj
  })
}