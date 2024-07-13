import request from '@/utils/request'


export function queryTopicArea() {
  return request({
    url: '/home/queryTopicArea',
    method: 'get'
  })
}