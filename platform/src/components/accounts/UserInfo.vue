<template>
    <div class="user-info">
      <el-row class="user-info-back" type="flex" justify="center">
        <el-form class="user-info" label-width="150px" :model="formMessage" :rules="rules" size="mini">
          <el-form-item label="用户名:" prop="userName">
            <!--<el-input type="password" placeholder="" v-model="formMessage.oldPassword"></el-input>-->
          </el-form-item>
          <el-form-item label="用户类型:" prop="userName">
            <!--<el-input type="password" placeholder="" v-model="formMessage.oldPassword"></el-input>-->
          </el-form-item>
          <el-form-item label="原密码:" prop="oldPassword">
             <el-input type="password" placeholder="" v-model="formMessage.oldPassword"></el-input>
          </el-form-item>
          <el-form-item label="新密码:" prop="newPassword">
            <el-input type="password" placeholder="" v-model="formMessage.newPassword"></el-input>
          </el-form-item>
          <el-form-item label="确认密码:" prop="cnewPassword">
            <el-input type="password" placeholder="请再次输入密码" v-model="formMessage.cnewPassword"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button @click="onChange" class="on-change" type="primary" size="medium">确定修改</el-button>
          </el-form-item>
        </el-form>
      </el-row>
    </div>
</template>

<script>
export default {
  name: 'UserInfo',
  data () {
    return {
      formMessage: {
        oldPassword: '',
        // ArrivalMoney: '',
        newPassword: '',
        cnewPassword: ''
      }
    }
  },
  methods: {
    onChange () {

    }
  }
}
</script>

<style scoped>

</style>
