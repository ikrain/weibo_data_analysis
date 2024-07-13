import request from '@/utils/request'


export function queryTopicNum() {
  return request({
    url: '/home/queryTopicNum',
    method: 'get'
  })
}

export function queryArticleNum() {
  return request({
    url: '/home/queryArticleNum',
    method: 'get'
  })
}

export function queryTopicAddNum() {
  return request({
    url: '/home/queryTopicAddNum',
    method: 'get'
  })
}

export function queryArticleAddNum() {
  return request({
    url: '/home/queryArticleAddNum',
    method: 'get'
  })
}