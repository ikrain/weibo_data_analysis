import request from '@/utils/request'


export function queryCommMap() {
  return request({
    url: '/home/queryMap',
    method: 'get'
  })
}