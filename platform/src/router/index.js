import Vue from 'vue'
import Router from 'vue-router'
// import cookie from '../assets/js/cookie'
// 全局状态控制引入
import store from '../store/'
// import axios from 'axios'

import Account from '@/components/accounts/Account'
import Login from '@/components/accounts/Login'
import Register from '@/components/accounts/Register'
import SelectRole from '@/components/accounts/SelectRole'
import UserInfo from '@/components/accounts/UserInfo'

import User from '@/components/layout/User'
import Home from '@/components/pages/Home'
import Recharge from '@/components/pages/Recharge'
import ToCash from '@/components/pages/ToCash'
import Shop from '@/components/pages/Shop'

import Admin from '@/components/layout/Admin'
import AdminRecharge from '@/components/pages/AdminRecharge'
import AdminToCash from '@/components/pages/AdminToCash'

import Test from '@/components/Test'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      redirect: '/account/login'
    }, {
      path: '/account',
      component: Account,
      redirect: '/account/login',
      children: [
        {
          // 当 /login 匹配成功，
          // Login 会被渲染在 Account 的 <router-view> 中
          path: 'login',
          name: 'Login',
          components: {
            accontent: Login
          },
          meta: {
            title: '登陆',
            need_token: false
          }
        }, {
          path: 'selectrole',
          name: 'SelectRole',
          components: {
            accontent: SelectRole
          },
          meta: {
            title: '选择角色',
            need_token: false
          }
        }, {
          path: 'register',
          name: 'Register',
          components: {
            accontent: Register
          },
          meta: {
            title: '卖家注册',
            need_token: false
          }
        }
      ]
    }, {
      path: '/user',
      component: User,
      redirect: '/user/home',
      children: [
        {
          path: 'home',
          name: 'Home',
          components: {
            content: Home
          },
          meta: {
            title: '用户信息首页',
            need_token: true
          }
        }, {
          path: 'userinfo',
          name: 'UserInfo',
          components: {
            content: UserInfo
          },
          meta: {
            title: '修改密码',
            need_token: true
          }
        }, {
          path: 'recharge',
          name: 'Recharge',
          components: {
            content: Recharge
          },
          meta: {
            title: '充值',
            need_token: true,
            user_type: 1
          }
        }, {
          path: 'tocash',
          name: 'ToCash',
          components: {
            content: ToCash
          },
          meta: {
            title: '提现',
            need_token: true,
            user_type: 1
          }
        }, {
          path: 'shop',
          name: 'Shop',
          components: {
            content: Shop
          },
          meta: {
            title: '店铺',
            need_token: true,
            user_type: 1
          }
        }
      ]
    }, {
      path: '/admin',
      component: Admin,
      redirect: '/admin/home',
      children: [
        {
          path: 'admin-recharge',
          name: 'AdminRecharge',
          components: {
            content: AdminRecharge
          },
          meta: {
            title: '管理员-充值',
            need_token: true,
            user_type: 0
          }
        }, {
          path: 'admin-tocash',
          name: 'AdminToCash',
          components: {
            content: AdminToCash
          },
          meta: {
            title: '管理员-提现',
            need_token: true,
            user_type: 0
          }
        }
      ]
    }, {
      path: '/test',
      name: 'Test',
      component: Test,
      meta: {
        title: '测试',
        need_token: false
      }
    }, {
      path: '*',
      redirect: '/' // 输入其他不存在的地址自动跳回首页
    }]
})

// 路由跳转拦截
router.beforeEach((to, from, next) => {
  const token = store.state.userInfo.token
  if (!token) {
    if (!to.meta.need_token) {
      next()
    } else {
      next({
        path: '/account/login'
      })
    }
  } else {
    if (!to.meta.need_token) {
      if (to.path === '/account/login') {
        next({
          path: '/user/home'
        })
      } else {
        next()
      }
    } else {
      next()
    }
  }
})

export default router
