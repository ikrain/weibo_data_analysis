import request from '@/utils/request'


export function queryTopicTime() {
  return request({
    url: '/home/queryTopicTime',
    method: 'get'
  })
}

export function queryCommentTime() {
  return request({
    url: '/home/queryCommentTime',
    method: 'get'
  })
}

export function queryArticleTime() {
  return request({
    url: '/home/queryArticleTime',
    method: 'get'
  })
}