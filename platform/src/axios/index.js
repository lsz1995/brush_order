// 引入vue
// import Vue from 'vue'
import axios from 'axios'

// 全局状态控制引入
import store from '../store/'

import cookie from '../assets/js/cookie'
// import * as types from '../store/mutation-types'
// import router from '../router'

// axios 配置
axios.defaults.timeout = 5000
// axios.defaults.baseURL = 'http://10.206.148.125:8001/'
axios.defaults.baseURL = 'http://47.112.116.80:8005/'
console.log(store.state.userInfo.token)
// http request 拦截器
axios.interceptors.request.use(
  config => {
    if (store.state.userInfo.token) { // 判断是否存在token，如果存在的话，则每个http header都加上token
      config.headers.Authorization = `JWT ${store.state.userInfo.token}`
    }
    return config
  },
  err => {
    return Promise.reject(err)
  })

// http response 拦截器
axios.interceptors.response.use(
  undefined,
  error => {
    let res = error.response
    switch (res.status) {
      case 401:
        // 返回 401 清除token信息并跳转到登录页面
        cookie.delCookie('token')
        cookie.delCookie('name')
        store.state.userInfo.token = ''
        store.state.userInfo.name = ''
        // store.commit(types.LOGOUT)
        // router.replace({
        //   path: '/app/login',
        //   query: {redirect: router.currentRoute.fullPath}
        // })
        console.log('未登录 或者token过期')
        break
      case 403:
        console.log('您没有该操作权限')
        break
      // alert('您没有该操作权限')
      case 500:
        console.log('服务器错误')
        break
      // alert('服务器错误');
    }
    return Promise.reject(error.response.data) // 返回接口返回的错误信息
  })
