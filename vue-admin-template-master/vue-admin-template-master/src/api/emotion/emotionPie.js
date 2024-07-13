import request from '@/utils/request'

export function queryCommentEmotion(searchObj) {
  return request({
    url: '/emotion/queryCommentEmotion',
    method: 'get',
    params: searchObj
  })
}