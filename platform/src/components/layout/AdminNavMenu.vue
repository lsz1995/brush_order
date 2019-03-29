<template>
  <el-menu
    :default-active="$route.path"
    class="el-menu-vertical-demo"
    router>
    <el-menu-item-group>
      <template slot="title"><i class="el-icon-caret-bottom"></i>活动管理</template>
      <el-menu-item index="1" style="padding-left: 40px;">首页公告</el-menu-item>
      <el-menu-item index="/user/home" style="padding-left: 40px;">个人中心</el-menu-item>
      <el-menu-item index="1" style="padding-left: 40px;">发布活动</el-menu-item>
      <el-menu-item index="1" style="padding-left: 40px;">我发布的活动</el-menu-item>
      <el-menu-item index="1" style="padding-left: 40px;">我的活动详情</el-menu-item>
    </el-menu-item-group>
    <el-menu-item-group>
      <template slot="title"><i class="el-icon-caret-bottom"></i>我的钱包</template>
      <el-menu-item index="/admin/admin-recharge" style="padding-left: 40px;">充值订单</el-menu-item>
      <el-menu-item index="/admin/admin-tocash" style="padding-left: 40px;">提现订单</el-menu-item>
    </el-menu-item-group>
    <el-menu-item-group>
      <template slot="title"><i class="el-icon-caret-bottom"></i>我的账号</template>
      <el-menu-item index="/1" style="padding-left: 40px;">店铺管理</el-menu-item>
      <el-menu-item index="1" style="padding-left: 40px;">选项2</el-menu-item>
    </el-menu-item-group>
    <el-menu-item-group>
      <template slot="title"><i class="el-icon-caret-bottom"></i>分组1</template>
      <el-menu-item index="1" style="padding-left: 40px;">选项1</el-menu-item>
      <el-menu-item index="1" style="padding-left: 40px;">选项2</el-menu-item>
    </el-menu-item-group>
  </el-menu>
</template>

<script>
// import Router from 'vue-router'
export default {
  name: 'AdminNavMenu'
}
</script>

<style>
  .el-menu-item-group__title {
    font-size:18px;
    color: black;
    font-weight: bolder;
  }
  .el-menu-item {
  }
</style>
