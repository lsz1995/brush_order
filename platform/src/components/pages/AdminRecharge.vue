<template>
  <div class="admin-recharge">
    <!--标题头-->
    <el-row>
      <el-col :span="24">
        管理员-充值订单确认
        <hr style="height:1px;border:none;border-top:3px solid #555555;width: 100%;margin:10px auto">
      </el-col>
    </el-row>
    <!--充值记录列表-->
    <el-table :data="tableData" stripe style="width: 100%" height="650" size="mini">
      <el-table-column label="充值订单">
        <el-table-column prop="add_time" label="提交时间" width="90"></el-table-column>
        <el-table-column prop="method" label="支付方式" width="70"></el-table-column>
        <el-table-column prop="order_number" label="交易号" width="200"></el-table-column>
        <el-table-column prop="money" label="充值金额" width="100"></el-table-column>
        <el-table-column prop="arrival_money" label="到账金额" width="100"></el-table-column>
        <el-table-column prop="state" label="状态" width="70"></el-table-column>
        <el-table-column prop="state" label="操作">
          <template slot-scope="scope">
            <el-button @click="handleConfirm(scope.$index, scope.row)" type="danger" :disabled="scope.row.state==='充值成功'" size="mini">确认</el-button>
          </template>
        </el-table-column>
      </el-table-column>
    </el-table>
    <el-pagination
      layout="prev, pager, next"
      @current-change="handleCurrentChange"
      :current-page="currentPage"
      :total="pageCount">
    </el-pagination>
  </div>
</template>

<script>
export default {
  name: 'AdminRecharge',
  data () {
    return {
      tableData: [{}],
      pageCount: 50,
      currentPage: 1
    }
  },
  mounted: function () {
    // 获取充值列表
    this.getRechargeList()
  },
  methods: {
    handleConfirm (index, row) {
      if (row.method === '支付宝') {
        row.method = 1
      } else if (row.method === '微信') {
        row.method = 2
      } else {
        row.method = 3
      }
      let obj = {
        money: row.money,
        method: row.method,
        order_number: row.order_number,
        arrival_money: row.arrival_money,
        state: true
      }
      this.$http.patch('/RechargeSure/' + row.id + '/', obj) // 将信息发送给后端
        .then((res) => { // axios返回的数据都在res.data里
          if (res.status === 200) { // 如果成功
            this.tableData[index].state = '充值成功'
            this.getRechargeList()
          }
        })
    },
    getRechargeList () {
      // 获取充值列表
      this.$http.get('/RechargeSure/?page=' + this.currentPage) // 将信息发送给后端
        .then((res) => { // axios返回的数据都在res.data里
          // console.log(res)
          if (res.status === 200) { // 如果成功
            this.tableData = res.data.results
            this.pageCount = res.data.count
            for (var i = 0; i < this.tableData.length; i++) {
              if (this.tableData[i].method === 1) {
                this.tableData[i].method = '支付宝'
              } else if (this.tableData[i].method === 2) {
                this.tableData[i].method = '微信'
              } else {
                this.tableData[i].method = '其他'
              }
            }
            for (var j = 0; j < this.tableData.length; j++) {
              if (this.tableData[j].state) {
                this.tableData[j].state = '充值成功'
              } else {
                this.tableData[j].state = '待审核'
              }
            }
          } else {
            this.tableData = 'null'
          }
        })
    },
    handleCurrentChange (val) {
      this.currentPage = val
      this.getRechargeList()
    }
  }
}
</script>

<style scoped>

</style>
