import request from '@/utils/request'

// 将mock接口 换为 真实的接口

// 对外暴露登录接口函数
export function login(data) {
  return request({
    // url: '/vue-admin-template/user/login',
    url: '/user/login',
    method: 'post',
    data
  })
}

// 对外暴露获取用户信息接口函数
export function getInfo(token) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/user/info',
    method: 'get',
    params: { token }
  })
}

// 对外暴露登出接口函数
export function logout() {
  return request({
    // url: '/vue-admin-template/user/logout',
    url: '/user/logout',
    method: 'post'
  })
}
