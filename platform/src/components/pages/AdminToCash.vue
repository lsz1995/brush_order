<template>
  <div class="admin-to-cash">
    <!--标题头-->
    <el-row>
      <el-col :span="24">
        管理员-提现订单确认
        <hr style="height:1px;border:none;border-top:3px solid #555555;width: 100%;margin:10px auto">
      </el-col>
    </el-row>
    <!--提现记录列表-->
    <el-table :data="tableData" stripe style="width: 100%" height="670" size="mini">
      <el-table-column label="提现订单">
        <el-table-column prop="add_time" label="提交时间" width="90"></el-table-column>
        <!--<el-table-column prop="method" label="支付方式" width="70"></el-table-column>-->
        <el-table-column prop="Bank_number" label="银行卡号" width="190"></el-table-column>
        <el-table-column prop="name" label="银行卡姓名" width="60"></el-table-column>
        <el-table-column prop="money" label="提现金额" width="80"></el-table-column>
        <el-table-column prop="arrival_money" label="到账金额" width="80"></el-table-column>
        <el-table-column prop="state" label="状态" width="80"></el-table-column>
        <el-table-column prop="state" label="操作">
          <template slot-scope="scope">
            <el-button @click="handleConfirm(scope.$index, scope.row)" type="danger" :disabled="scope.row.state==='提现成功'" size="mini">确认</el-button>
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
// import qs from 'qs'
export default {
  name: 'AdminToCash',
  data () {
    return {
      tableData: [{}],
      pageCount: 50,
      currentPage: 1
    }
  },
  mounted: function () {
    // 获取提现列表
    this.getToCashList()
  },
  methods: {
    handleConfirm (index, row) {
      // console.log(row)
      let obj = {
        money: row.money,
        Bank_number: row.Bank_number,
        name: row.name,
        state: true,
        arrival_money: row.arrival_money
      }
      // console.log(obj)
      this.$http.patch('/WithdrawSure/' + row.id + '/', obj) // 将信息发送给后端
        .then((res) => { // axios返回的数据都在res.data里
          if (res.status === 200) { // 如果成功
            // console.log(res)
            this.tableData[index].state = '提现成功'
            this.getToCashList()
          }
        })
    },
    getToCashList () {
      // 获取提现列表
      this.$http.get('/WithdrawSure/?page=' + this.currentPage) // 将信息发送给后端
        .then((res) => { // axios返回的数据都在res.data里
          // console.log(res)
          if (res.status === 200) { // 如果成功
            this.tableData = res.data.results
            this.pageCount = res.data.count
            for (var j = 0; j < this.tableData.length; j++) {
              if (this.tableData[j].state) {
                this.tableData[j].state = '提现成功'
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
      this.getToCashList()
    }
  }
}
</script>

<style scoped>

</style>
