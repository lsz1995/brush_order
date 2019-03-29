<template>
  <div class="admin">
    <!--顶部-->
    <my-header></my-header>
    <!--中间-->
    <div class="main-background">
      <el-main class="my-main">
        <!--菜单栏-->
        <el-row type="flex" justify="center">
          <el-col :span="6">
            <el-aside style="width: 220px">
              <admin-nav-menu></admin-nav-menu>
            </el-aside>
          </el-col >
          <!--内容-->
          <el-col :span="18">
            <router-view name='content'></router-view>
          </el-col>
        </el-row>
      </el-main>
      <!--底部-->
      <my-footer></my-footer>
    </div>
  </div>
</template>

<script>
import MyHeader from '@/components/layout/MyHeader'
import AdminNavMenu from '@/components/layout/AdminNavMenu'
import MyFooter from '@/components/layout/MyFooter'
export default {
  name: 'Admin',
  components: {
    MyHeader,
    AdminNavMenu,
    MyFooter
  }
}
</script>

<style scoped>
  .pages {
    margin: 0 auto;
  }
  .main-background{
    background: rgb(246, 246, 246);
  }
  .my-main {
    border:1px solid white;
    background-color: white;
    border-radius: 3px;
    width: 1000px;
    height: 100%;
    margin: 0 auto;
  }

</style>
