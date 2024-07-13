import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 *  常量路由：
 *  - 就是无论用户是什么角色，都可以看见
 *  异步路由：
 *  - 通过用户的角色进行过滤从而显示响应的路由
 */
export const asyncRoutes = [
  {
    name: 'Topic',
    path: '/',
    component: Layout,
    redirect: '/topic',
    children: [
      {
        path: 'topic',
        name: 'Topic',
        component: () => import('@/views/topic/topicDetection'),
        meta: { title: '热点话题', icon: 'el-icon-aim' }
      }
    ]
  },
  


  {
    name: 'Emotion',
    path: '/',
    component: Layout,
    redirect: '/emotion',
    children: [{
      path: 'emotion',
      name: 'Emotion',
      component: () => import('@/views/emotion/topicEmotion'),
      meta: { title: '情感分析', icon: 'el-icon-view' }
    }]
  },

  {
    name: 'Search',
    path: '/',
    component: Layout,
    redirect: '/search',
    children: [{
      path: 'search',
      name: 'Search',
      component: () => import('@/views/search/topicSearch'),
      meta: { title: '舆情检索', icon: 'el-icon-search' }
    }]
  },

  {
    name: 'Manage',
    path: '/manage',
    component: Layout,
    redirect: '/manage',
    children: [
      {
        path: 'user',
        name: 'User',
        component: () => import('@/views/manage/user/index'),
        meta: { title: '用户管理', icon: '' }
      },
      {
        path: 'role',
        name: 'Role',
        component: () => import('@/views/manage/role/index'),
        meta: { title: '角色管理', icon: '' }
      },
      {
        path: 'menu',
        name: 'Menu',
        component: () => import('@/views/manage/menu/index'),
        meta: { title: '权限管理', icon: '' },
        hidden: true
      }
    ],
    meta: { title: '系统管理', icon: 'el-icon-user' }
  },

  {
    name: 'Set',
    path: '/',
    component: Layout,
    redirect: '/set',
    children: [{
      path: 'set',
      name: 'Set',
      component: () => import('@/views/set/setting'),
      meta: { title: '数据处理日志', icon: 'el-icon-setting' }
    }]
  }
];


/**
 * 路由的配置（固定路由）：
 *  - 下面路由的配置都是写死的，要想为不同的用户提供不同的路由，则需要动态拆分路由
 */
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },

  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: '首页', icon: 'el-icon-s-home' }
    }]
  },

  {
    path: '/',
    component: Layout,
    redirect: '/sensitive',
    children: [{
      path: 'sensitive',
      name: 'Sensitive',
      component: () => import('@/views/sensitive/index'),
      meta: { title: '敏感词分析', icon: 'el-icon-s-management' }
    }]
  },

  {
    path: '/',
    component: Layout,
    redirect: '/analysisTopic',
    children: [{
      path: 'analysisTopic',
      name: 'AnalysisTopic',
      component: () => import('@/views/topic/rank/analysis_topic/index'),
      // hidden: true
    }]
  },
]

export const addRoutes = [
  {
    
  }
]

/**
 * 任意路由：
 *  - 当路径出现错误时，重定向404
 * 404 page must be placed at the end !!!
 */
 export const anyRoutes = { path: '*', redirect: '/404', hidden: true }


// export const constantRoutes = [
//   {
//     path: '/login',
//     component: () => import('@/views/login/index'),
//     hidden: true
//   },

//   {
//     path: '/404',
//     component: () => import('@/views/404'),
//     hidden: true
//   },

//   {
//     path: '/',
//     component: Layout,
//     redirect: '/dashboard',
//     children: [{
//       path: 'dashboard',
//       name: 'Dashboard',
//       component: () => import('@/views/dashboard/index'),
//       meta: { title: '首页', icon: 'el-icon-s-home' }
//     }]
//   },

//   {
//     path: '/',
//     component: Layout,
//     redirect: '/topic',
//     children: [{
//       path: 'topic',
//       name: 'Topic',
//       component: () => import('@/views/topic/topicDetection'),
//       meta: { title: '热点话题', icon: 'el-icon-aim' }
//     }]
//   },

//   {
//     path: '/',
//     component: Layout,
//     redirect: '/emotion',
//     children: [{
//       path: 'emotion',
//       name: 'Emotion',
//       component: () => import('@/views/emotion/topicEmotion'),
//       meta: { title: '情感分析', icon: 'el-icon-view' }
//     }]
//   },

//   {
//     path: '/',
//     component: Layout,
//     redirect: '/search',
//     children: [{
//       path: 'search',
//       name: 'Search',
//       component: () => import('@/views/search/topicSearch'),
//       meta: { title: '舆情检索', icon: 'el-icon-search' }
//     }]
//   },

//   {
//     path: '/manage',
//     component: Layout,
//     redirect: '/manage',
//     children: [
//       {
//         path: 'user',
//         name: 'User',
//         component: () => import('@/views/manage/user/index'),
//         meta: { title: '用户管理', icon: '' }
//       },
//       {
//         path: 'role',
//         name: 'Role',
//         component: () => import('@/views/manage/role/index'),
//         meta: { title: '角色管理', icon: '' }
//       },
//       {
//         path: 'menu',
//         name: 'Menu',
//         component: () => import('@/views/manage/menu/index'),
//         meta: { title: '权限管理', icon: '' }
//       }
//     ],
//     meta: { title: '系统管理', icon: 'el-icon-user' }
//   },

//   {
//     path: '/',
//     component: Layout,
//     redirect: '/set',
//     children: [{
//       path: 'set',
//       name: 'Set',
//       component: () => import('@/views/set/setting'),
//       meta: { title: '系统配置', icon: 'el-icon-setting' }
//     }]
//   },

//   // 404 page must be placed at the end !!!
//   { path: '*', redirect: '/404', hidden: true }
// ]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
