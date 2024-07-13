import request from '@/utils/request'

// 查询系统角色(参数username可以有，也可以没有)
export function selectRole(searchObj){
  return request({
    url: '/role/query',
    method: 'get',
    params: searchObj
  })
}

// 根据ID删除角色
export function delRoleById(delObj){
  return request({
    url: '/role/delete',
    method: 'get',
    params: delObj
  })
}

export function updateRoleAuth(roleInfo){
  return request({
    url: '/role/modifyAuth',
    method: 'post',
    data: roleInfo
  })
}

export function addRole(roleInfo){
  return request({
    url: '/role/addRole',
    method: 'post',
    data: roleInfo
  })
}