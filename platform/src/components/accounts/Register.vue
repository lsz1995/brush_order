<template>
  <div class="register">
    <h2>用户注册</h2>
    <hr style="height:15px;border:none;border-top:3px solid #555555;width: 700px;margin: 15px auto">
    <el-form class="register-form" label-width="100px" :model="formMessage" :rules="rules" size="mini">
      <!--<p class="register_title">账号注册</p>-->

      <el-form-item label="用户名:" prop="username">
        <el-input type="text" placeholder="用户名不得小于 3 个字符" v-model="formMessage.username"></el-input>
      </el-form-item>

      <el-form-item label="密码:" prop="password">
        <el-input type="password" placeholder="密码不得小于8个字符" v-model="formMessage.password"></el-input>
      </el-form-item>

      <el-form-item label="确认密码:" prop="cpassword">
        <el-input type="password" placeholder="请再次输入密码" v-model="formMessage.cpassword"></el-input>
      </el-form-item>

      <el-form-item label="E-mail:" prop="email">
        <el-input type="email" placeholder="用于接收通知，找回密码等" v-model="formMessage.email"></el-input>
      </el-form-item>

      <el-form-item label="联系QQ:" prop="qqnumber">
        <el-input type="text" placeholder="请输入QQ号" v-model="formMessage.qqnumber"></el-input>
      </el-form-item>

      <el-form-item label="手机号:" prop="mobile">
        <el-input type="text" placeholder="用于接收通知，找回密码等" v-model="formMessage.mobile"></el-input>
      </el-form-item>

      <el-form-item label="被邀请码:" prop="invite">
        <el-input type="text" placeholder="请输入邀请吗" v-model="formMessage.invite"></el-input>
      </el-form-item>

      <!--<p v-show="formMessage.error.mobile">{{formMessage.error.mobile}}</p>-->
      <el-checkbox v-model="formMessage.checked">我已仔细阅读并同意接受 《服务协议》</el-checkbox>
      <el-button @click="onRegister" class="on-apply" type="primary" size="medium">提交注册</el-button>
    </el-form>
  </div>
</template>

<script>
import cookie from '../../assets/js/cookie'
export default {
  name: 'Register',
  data () {
    return {
      formMessage: {
        username: '',
        password: '',
        cpassword: '',
        email: '',
        qqnumber: '',
        mobile: '',
        invite: '',
        // error: {
        //   mobile: '',
        //   password: '',
        //   username: '',
        //   code: ''
        // },
        checked: ''
      },
      rules: {
        username: [{
          required: true, type: 'string', message: '请输入用户名', trigger: 'blur'
        }],
        password: [{
          required: true, message: '请输入密码', trigger: 'blur'
        }],
        cpassword: [{
          required: true, message: '确认密码', trigger: 'blur'
        }, {
          validator: (rule, value, callback) => {
            if (value === '') {
              callback(new Error('请再次输入密码'))
            } else if (value !== this.formMessage.password) {
              callback(new Error('两次输入的密码不一致'))
            } else {
              callback()
            }
          },
          trigger: 'blur'
        }],
        email: [{
          required: true, type: 'email', message: '请输入邮箱', trigger: 'blur'
        }],
        qqnumber: [{
          required: true, message: '请输入QQ号码', trigger: 'blur'
        }],
        mobile: [{
          required: true, message: '请输入手机号', trigger: 'blur'
        }]
      }
    }
  },
  methods: {
    onRegister () {
      let obj = {
        username: this.formMessage.username,
        password: this.formMessage.password,
        mobile: this.formMessage.mobile,
        email: this.formMessage.email,
        qq_number: this.formMessage.qqnumber,
        Be_Invite_code: this.formMessage.invite
      }
      var that = this
      this.$http.post('/users/', obj) // 将信息发送给后端
        .then((res) => { // axios返回的数据都在res.data里
          console.log(res)
          if (res.status === 201) { // 如果成功
            // 本地存储用户信息
            cookie.setCookie('name', this.formMessage.username, 7)
            cookie.setCookie('token', res.data.token, 7)
            // 存储在store
            // 更新store数据
            that.$store.dispatch('setInfo')
            // console.log(res)
            this.$message({ // 成功，显示提示语
              type: 'success',
              message: '注册成功！'
            })
            this.$router.push('/user') // 进入首页面，成功
          }
        })
        .catch(function (error) {
          console.log(error)
          that.$message({
            type: 'error',
            message: '注册失败！' + that.error
          })
        })
    }
  }
}
</script>

<style>
  .register {
    width: 800px;
    height: 100%;
    color:black;
    margin: 20px auto;
    background-color: rgb(255, 255, 255);
    border:0px solid #C0C0C0;
  }
  .register-form {
    width: 330px;
    color:black;
    margin: 0 auto
  }

  .on-apply {
    margin-top: 20px;
    width: 150px;
    margin-left: 100px
  }

  .register .el-form-item__label {
    color: black;
  }

</style>
