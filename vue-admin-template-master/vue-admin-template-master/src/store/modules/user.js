import { login, logout, getInfo } from '@/api/user'
import { getToken, setToken, removeToken } from '@/utils/auth'
import { resetRouter, asyncRoutes, anyRoutes, constantRoutes } from '@/router'
import router from '@/router'
import cloneDeep from 'lodash/cloneDeep'

const getDefaultState = () => {
  return {
    token: getToken(),
    name: '',
    avatar: '',
    // 服务器返回的菜单的信息（权限），数组内的元素是字符串
    routes: [],
    // 角色信息
    roles: [],
    // 按钮权限信息
    buttons: [],
    // 经计算用户所要显示在页面中的异步路由
    resultAsyncRoutes: [],
    // 最终要显示的路由
    resultAllRoutes: []
  }
}

const state = getDefaultState()

const mutations = {
  RESET_STATE: (state) => {
    Object.assign(state, getDefaultState())
  },
  SET_TOKEN: (state, token) => {
    state.token = token
  },
  SET_NAME: (state, name) => {
    state.name = name
  },
  SET_AVATAR: (state, avatar) => {
    state.avatar = avatar
  },
  SET_RESULTASYNCROUTES: (state, asyncRoutes) => {
    state.resultAsyncRoutes = asyncRoutes;
    // 计算出所要展示的异步路由以后，将其与常量路由和任意路由合并
    state.resultAllRoutes = constantRoutes.concat(state.resultAsyncRoutes, anyRoutes)
    router.addRoutes(state.resultAllRoutes)
  }
}

// 定义一个函数，根据从服务器获取的用户权限信息，计算出系统所要给用户展示的路由
const computedAsyncRoutes = (asyncRoutes,routes)=>{
  //过滤出当前用户【超级管理|普通员工】需要展示的异步路由
 return asyncRoutes.filter(item=>{
      //数组当中没有这个元素返回索引值-1，如果有这个元素返回的索引值一定不是-1 
     if(routes.indexOf(item.name)!=-1){
       //递归:别忘记还有2、3、4、5、6级路由
       if(item.children&&item.children.length){
           item.children = computedAsyncRoutes(item.children,routes);
       }
       return true;
     }
  })
}

const actions = {
  // user login 处理登录业务
  login({ commit }, userInfo) {
    // 解析出用户名和密码
    const { username, password } = userInfo
    return new Promise((resolve, reject) => {
      login({ username: username.trim(), password: password }).then(response => {
        const { data } = response
        commit('SET_TOKEN', data.token)
        setToken(data.token)
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // get user info 获取用户信息
  getInfo({ commit, state }) {
    return new Promise((resolve, reject) => {
      getInfo(state.token).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }

        const { name, avatar } = data

        commit('SET_NAME', name)
        commit('SET_AVATAR', avatar)
        commit('SET_USERINFO',data);
        // 将从服务器获取到用户权限存储到Vue仓库
        commit('SET_RESULTASYNCROUTES', computedAsyncRoutes(cloneDeep(asyncRoutes), data.routes))
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  // user logout 登出
  logout({ commit, state }) {
    return new Promise((resolve, reject) => {
      logout(state.token).then(() => {
        removeToken() // must remove  token  first
        resetRouter()
        commit('RESET_STATE')
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // remove token
  resetToken({ commit }) {
    return new Promise(resolve => {
      removeToken() // must remove  token  first
      commit('RESET_STATE')
      resolve()
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}

