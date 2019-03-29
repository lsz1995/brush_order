<template>
  <div class="account">
    <!--顶部-->
    <my-header></my-header>
    <!--<el-container>-->
    <!--中间-->
    <el-main class="account-content">
      <router-view name='accontent'></router-view>
    </el-main>
    <!--</div>-->
    <!--</el-container>-->
    <!--底部-->
    <my-footer></my-footer>
  </div>
</template>

<script>
// import Login from '@/components/accounts/Login'
import MyHeader from '@/components/layout/MyHeader'
import MyFooter from '@/components/layout/MyFooter'
export default {
  name: 'Account',
  components: {
    // Login,
    MyFooter,
    MyHeader
  },
  data () {
    return {
      myFooter: 'Copyright © 我的公司 All right reserved'
    }
  }
}
</script>

<style scoped>
  .account {
    width: 100%;
    height: 100%;
    background-color: rgb(250, 250, 250);
  }

  .account-content {
    width: 1000px;
    /*height: 470px;*/
    height: 100%;
    border:0px solid #C0C0C0;
    background-color: rgb(255, 255, 255);
    margin: 0 auto
  }

</style>
