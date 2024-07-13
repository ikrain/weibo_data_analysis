// 准备Actions——用于响应组件中的动作
const actions = {
  // 此处context为迷你版store
  initdata(context, value){
    context.commit('INITDATA',value)
  }
}
// 准备mutations——用于操作数据（state）
const mutations = {
  INITDATA(state, value){
    state.dataObj = value
  }
}
// 准备state——用于存储数据
const state ={
  dataObj: {}
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
