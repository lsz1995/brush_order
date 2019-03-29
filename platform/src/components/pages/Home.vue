<template>
  <div class="user">
    <el-row type="flex">
      <el-col :span="24">
        <div class="username-content">用户名：{{username}}
        <router-link :to="'/user/userinfo'" style="font-size: 12px">修改密码</router-link>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="12"><div class="grid-content back-line">现金余额：{{money}}</div></el-col>
    </el-row>
    <el-row>
      <el-col :span="12"><div class="grid-content back-line">注册时间：{{usertime}}</div></el-col>
    </el-row>
    <el-row >
      <el-col :span="12"><div class="grid-content back-line">用户类型：{{usertype}}</div></el-col>
    </el-row>
  </div>

</template>

<script>
export default {
  name: 'User',
  data () {
    return {
      username: '',
      usertime: '',
      money: '',
      usertype: ''
    }
  },
  mounted: function () {
    this.$http.get('/users/1/') // 将信息发送给后端
      .then((res) => { // axios返回的数据都在res.data里
        // console.log(res)
        if (res.status === 200) { // 如果成功
          this.username = res.data.username
          this.money = res.data.balance
        }
      })
  }
}
</script>

<style scoped>
  .user {
    font-size: 14px;
  }
  .username-content {
    min-height: 50px;
    font-size: 20px;
    font-weight: bold;
  }
  .usertime-content {
    font-size: 12px;
  }
  .grid-content {
    /*border-radius: 4px;*/
    min-height: 36px;
    margin-top: 20px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
  .back-line {
    border-bottom:#CCC 1px dashed;
  }
</style>
