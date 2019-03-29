<template>
  <div class="my-footer">
  <!--底部-->
    <hr style="height:1px;border:none;border-top:1px solid #555555;">
    <el-footer style="text-align: center">{{ myFooter }}</el-footer>
  </div>
</template>

<script>
export default {
  name: 'MyFooter',
  data () {
    return {
      myFooter: 'Copyright © 我的公司 All right reserved'
    }
  }
}
</script>

<style scoped>
.my-footer {
  width: 1100px;
  margin-top: 50px;
  margin-left: auto;
  margin-right: auto;
}
</style>
