<template>
  <div class="selectRole">
    <h2>用户注册</h2>
    <hr style="height:15px;border:none;border-top:3px solid #555555;width: 700px;margin: 15px auto">
    <div class="select-button">
      <h2 style="text-align: center">请选择用户角色</h2>
      <el-button @click="onSeller" class="on-apply" type="primary" size="medium">我是商家</el-button>
      <el-button @click="onBuyer" class="on-apply" type="primary" size="medium">我是买家</el-button>
      <p style="text-align: center">注意：禁止注册多个买家账号</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'selectRole',
  methods: {
    onSeller () {
      this.$router.push({path: '/account/register'})
    },
    onBuyer () {
    }
  }
}
</script>

<style scoped>
  .selectRole {
    width: 700px;
    height: 100%;
    color:black;
    margin: 0 auto
  }
  .select-button {
    width: 500px;
    color: black;
    margin: 0 auto
  }
</style>
