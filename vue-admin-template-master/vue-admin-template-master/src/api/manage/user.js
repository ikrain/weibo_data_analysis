import request from '@/utils/request'

const api_name = '/user/queryPage'

/* 获取后台用户分页列表(带搜索) */
export function getPageList(searchObj) {
  return request({
    url: '/user/queryPage',
    method: 'get',
    params: searchObj
  })
}

// 根据用户名（也可以没有该参数）查询查询所有用户
export function selectUser(searchObj) {
  return request({
    url: '/user/query',
    method: 'get',
    params: searchObj
  })
}

// 根据ID删除指定用户
export function delUserById(delObj){
  return request({
    url: '/user/delete',
    method: 'get',
    params: delObj
  })
}

export function insertUser(userInfo){
  return request({
    url: '/user/add',
    method: 'post',
    data: userInfo
  })
}


export function updateUser(userInfo){
  return request({
    url: '/user/modify',
    method: 'post',
    data: userInfo
  })
}
