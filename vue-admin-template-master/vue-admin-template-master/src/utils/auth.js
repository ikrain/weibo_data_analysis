import Cookies from 'js-cookie'

const TokenKey = 'vue_admin_template_token'

// 登录后，需要获取信息时，获取Token
export function getToken() {
  return Cookies.get(TokenKey)
}

// 登录成功后保存Token
export function setToken(token) {
  return Cookies.set(TokenKey, token)
}

// 用户退出后，移除Token
export function removeToken() {
  return Cookies.remove(TokenKey)
}
