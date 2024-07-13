import request from '@/utils/request'

export function querySenWord() {
  return request({
    url: '/sensitive/queryWord',
    method: 'get'
  })
}

export function insertSenWord(senWordInfo){
  return request({
    url: '/sensitive/add',
    method: 'post',
    data: senWordInfo
  })
}

export function delSenWordById(delObj){
  return request({
    url: '/sensitive/delete',
    method: 'get',
    params: delObj
  })
}


export function queryTopicByWord(searchObj) {
  return request({
    url: '/sensitive/queryTopicByWord',
    method: 'get',
    params: searchObj
  })
}

export function querySensitiveLine(searchObj) {
  return request({
    url: '/sensitive/queryNumByWord',
    method: 'get',
    params: searchObj
  })
}
