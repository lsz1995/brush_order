<template>
  <div class="my-header">
    <div class="backImage">
      <el-row class="top" type="flex" justify="end">
        <el-col :span="6">
          <div class="">
            <template v-if="username">
              欢迎您，<span>{{username}}</span> <a @click="onLoginOut">退出</a>
            </template>
            <template v-else>
              你好，请 <router-link :to="'/account/login'">登录</router-link> | <router-link :to="'/account/selectrole'">注册</router-link>
            </template>
          </div>
        </el-col>
      </el-row>

      <el-row class="top-title">
        <el-col :span="3" ><div class="title-name">野狼</div></el-col>
      </el-row>
    </div>
    <div class="list">
      <div class="list-width">
        <a class="list-name" href="/">首页</a>
      </div>
    </div>
  </div>
</template>

<script>
import cookie from '../../assets/js/cookie'
export default {
  name: 'MyHeader',
  data () {
    return {
      username: ''
    }
  },
  methods: {
    onLoginOut () {
      cookie.delCookie('token')
      cookie.delCookie('name')
      // 重新触发store
      // 更新store数据
      this.$store.dispatch('setInfo')
      // 跳转到登录
      this.$router.push({path: '/account/login'})
    }
  },
  mounted: function () {
    this.$http.get('/users/1/') // 将信息发送给后端
      .then((res) => { // axios返回的数据都在res.data里
        // console.log(res)
        if (res.status === 200) { // 如果成功
          this.username = res.data.username
        }
      })
  }
}
</script>

<style scoped>
  .my-header {
    width: 100%;
    height: 100%;
    margin: 0 auto;
    background: rgba(75,154,165,0.7);
  }
  .backImage {
    width: 100%;
    background:url('../../assets/image/背景图.jpg') no-repeat center top 65%;
    opacity: 0.9;
  }
  .top {
    background: rgba(80, 80, 80, 0.2);
    height: 33px;
  }
  .top-title {
    width: 1000px;
    height:120px;
    margin: 0 auto;
  }
  .title-name {
    color: white;
    font-size: 56px;
    font-weight: bolder;
    line-height:1.7;
    margin-top: 10px;
  }
  .list {
    width: 100%;
    height: 38px;
    background: antiquewhite;
  }
  .list-width {
    width: 1000px;
    height: 100%;
    margin: 0 auto;
  }
  .list-name {
    font-size: 18px;
    font-weight: bolder;
    padding:0 10px 0 10px;
    line-height: 40px;
    height: 100%;
    color: black;
  }
</style>
