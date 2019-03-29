<template>
  <div class="login">
    <el-form class="login-form" :label-position="labelPosition" :model="formName" :rules="rules" size="mini">
      <!--<p class="login_title">账号登陆</p>-->

      <el-form-item label="手机号" prop="username">
        <el-input type="text" v-model="formName.username"></el-input>
      </el-form-item>

      <el-form-item label="密码" prop="password">
        <el-input type="password" v-model="formName.password"></el-input>
      </el-form-item>

      <!--<el-checkbox v-model="checked" class="remember">下次自动登陆</el-checkbox>-->
      <a href="#" style="float: right">忘记密码</a><br/>
      <el-button class="on-login" type="primary" @click="onLogin" size="medium">登陆</el-button>

    </el-form>

  </div>
</template>

<script>
import cookie from '../../assets/js/cookie'
export default {
  name: 'Login',
  data () {
    return {
      formName: {
        username: '',
        password: '',
        error: '',
        userNameError: '',
        parseWordError: ''
      },
      rules: {
        username: [{
          required: true, type: 'string', message: '请输入用户名', trigger: 'blur'
        }],
        password: [{
          required: true, message: '请输入密码', trigger: 'blur'
        }]
      },
      labelPosition: 'top',
      checked: false
    }
  },
  // mounted: function () {
  //   this.$http.get('/users/1/') // 将信息发送给后端
  //     .then((res) => { // axios返回的数据都在res.data里
  //       // console.log(res)
  //       if (res.status === 200) { // 如果成功
  //         // this.username = res.data.username
  //         if (res.data.user_type === 1) {
  //           this.$router.push({path: '/user/home'})
  //         } else if (res.data.user_type === 0) {
  //           this.$router.push({path: '/admin/home'})
  //         }
  //       }
  //     })
  // },
  methods: {
    onLogin () {
      let obj = {
        username: this.formName.username,
        password: this.formName.password
      }
      var that = this
      this.$http.post('/login/', obj) // 将信息发送给后端
        .then((res) => { // axios返回的数据都在res.data里
          console.log(res)
          if (res.status === 200) { // 如果成功
            // 本地存储用户信息
            cookie.setCookie('name', this.username, 7)
            cookie.setCookie('token', res.data.token, 7)
            // 存储在store
            // 更新store数据
            that.$store.dispatch('setInfo')
            // 登录成功，显示提示语
            this.$message({
              type: 'success',
              message: '登陆成功！'
            })
            // 跳转到首页页面
            this.routerTo()
          }
        })
        .catch(function (error) {
          console.log(error)
          if ('non_field_errors' in error) {
            that.error = error.non_field_errors[0]
            that.$message({
              type: 'error',
              message: '登陆失败！' + that.error
            })
          }
          if ('username' in error) {
            that.userNameError = error.username[0]
          }
          if ('password' in error) {
            that.parseWordError = error.password[0]
          }
        })
    },
    routerTo () {
      this.$http.get('/users/1/') // 将信息发送给后端
        .then((res) => { // axios返回的数据都在res.data里
          // console.log(res)
          if (res.status === 200) { // 如果成功
            // this.username = res.data.username
            if (res.data.user_type === 1) {
              this.$router.push({path: '/user/home'})
            } else if (res.data.user_type === 0) {
              this.$router.push({path: '/admin/home'})
            }
          }
        })
    }
  }
}
</script>

<style>
  .login {
    background: azure;
    border-radius: 4px;
    width: 270px;
    height:330px;
    color:black;
    /*margin-left: auto;*/
    float: right;
    /*margin-right: 150px;*/
    /*margin-top: 30px;*/
  }

  .login .el-form-item__label {
    color :black;
  }

  .login .el-checkbox {
    color :black;
  }
  .on-login {
    margin-top: 20px;
    /*float: left;*/
    width: 270px
  }
  .login-form {
    margin-top: 20px
  }

</style>
