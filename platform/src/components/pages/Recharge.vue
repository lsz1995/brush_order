<template>
  <div class="recharge">
    <!--标题头-->
    <el-row>
      <el-col :span="24">
        充值
        <hr style="height:1px;border:none;border-top:3px solid #555555;width: 100%;margin:10px auto">
      </el-col>
    </el-row>
    <!--余额和说明框-->
    <el-row>
      <el-col :span="24" class="recharge-message">
        <p>现金余额：{{money}}元</p>
        <p>填写正确转账信息，核实成功便会到账。</p>
      </el-col>
    </el-row>
    <!--二维码图片-->
    <el-row>
      <el-col :span="12"><div class="grid-content">微信转账</div><img src="../../assets/image/WeChat-QR-code.jpg"  height="400px" /></el-col>
      <el-col :span="12"><div class="grid-content">支付宝转账</div><img src="../../assets/image/Alipay-QE-code.jpg"  height="400px" /></el-col>
    </el-row>
    <!--充值信息表单-->
    <el-row class="recharge-form-back" type="flex" justify="center">
      <el-form class="recharge-form" label-width="150px" :model="formMessage" :rules="rules" size="mini">
        <el-form-item label="充值方式:">
          <el-select v-model="formMessage.payMode" placeholder="请选择充值方式:">
            <el-option label="微信充值" value="微信充值"></el-option>
            <el-option label="支付宝充值" value="支付宝充值"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="充值金额(元):" prop="payMoney">
          <el-input placeholder="" v-model="formMessage.payMoney"></el-input>
          <p>您充值金额：￥{{formMessage.payMoney}} （手续费：￥-{{reduceMoney}}）</p>
          <p>到账金额：￥{{arrivalMoney}}</p>
        </el-form-item>
        <el-form-item label="请填充值转账单号:" prop="payNumber">
          <el-input type="text" placeholder="" v-model="formMessage.payNumber"></el-input>
        </el-form-item>
        <el-button @click="onRecharge" class="on-recharge" type="primary" size="medium">确定充值</el-button>
      </el-form>
    </el-row>
    <el-row class="explain-content">
      <p>充值说明：</p>
      <p>充值手续费：0.6%，充值10000元以上不收取手续费。</p>
      <p>转账后人工审核充值到平台账户中。</p>
    </el-row>
    <!--充值记录列表-->
    <el-table :data="tableData" stripe style="width: 100%" height="250" size="mini">
      <el-table-column label="充值记录">
        <el-table-column prop="add_time" label="提交时间" width="120"></el-table-column>
        <el-table-column prop="method" label="支付方式" width="100"></el-table-column>
        <el-table-column prop="order_number" label="交易号" width="200"></el-table-column>
        <el-table-column prop="money" label="充值金额" width="100"></el-table-column>
        <el-table-column prop="arrival_money" label="到账金额" width="100"></el-table-column>
        <el-table-column prop="state" label="状态"></el-table-column>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'Recharge',
  data () {
    return {
      money: '',
      formMessage: {
        payMoney: '',
        // ArrivalMoney: '',
        payNumber: '',
        payMode: ''
      },
      rules: {
        payMode: [{
          required: true
        }],
        payMoney: [{
          required: true, message: '请输入充值金额', trigger: 'blur'
        }],
        payNumber: [{
          required: true, message: '请输入充值转账单号', trigger: 'blur'
        }]
      },
      tableData: [{}]
    }
  },
  computed: {
    arrivalMoney: function () {
      if (this.formMessage.payMoney < 10000) {
        return this.formMessage.payMoney * 0.994
      } else {
        return this.formMessage.payMoney
      }
    },
    reduceMoney: function () {
      if (this.formMessage.payMoney < 10000) {
        return this.formMessage.payMoney * 0.006
      } else {
        return 0
      }
    },
    payModeNumber: function () {
      if (this.formMessage.payMode === '支付宝转账') {
        return 1
      } else if (this.formMessage.payMode === '微信转账') {
        return 2
      } else {
        return 3
      }
    }
  },
  mounted: function () {
    // 用户信息，余额
    this.$http.get('/users/1/') // 将信息发送给后端
      .then((res) => { // axios返回的数据都在res.data里
        // console.log(res)
        if (res.status === 200) { // 如果成功
          this.money = res.data.balance
        } else {
          this.money = 'null'
        }
      })
    // 充值列表
    this.$http.get('/Recharge/') // 将信息发送给后端
      .then((res) => { // axios返回的数据都在res.data里
        // console.log(res)
        if (res.status === 200) { // 如果成功
          this.tableData = res.data.results
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
          // console.log(this.tableData)
        } else {
          this.tableData = 'null'
        }
      })
  },
  methods: {
    onRecharge () {
      let obj = {
        money: this.formMessage.payMoney,
        method: this.payModeNumber,
        order_number: this.formMessage.payNumber,
        arrival_money: this.arrivalMoney,
        state: false
      }
      var that = this
      this.$http.post('/Recharge/', obj) // 将信息发送给后端
        .then((res) => { // axios返回的数据都在res.data里
          // console.log(res)
          if (res.status === 201) { // 如果成功
            // 成功，显示提示语
            this.$message({
              type: 'success',
              message: '充值信息提交成功！'
            })
          }
        })
        .catch(function (error) {
          console.log(error)
          if ('non_field_errors' in error) {
            that.error = error.non_field_errors[0]
            that.$message({
              type: 'error',
              message: '提交充值信息失败！' + that.error
            })
          }
        })
    }
  }
}
</script>

<style scoped>
  .recharge {
    font-size: 14px;
  }
  .recharge-message {
    height: 100px;
    border-radius: 5px;
    background: rgba(0, 0, 0, 0.1);
  }
  .grid-content {
    /*border-radius: 4px;*/
    min-height: 36px;
    margin-top: 20px;
  }
  .recharge-form-back {
    border-radius: 5px;
    background: rgba(0, 0, 0, 0.1);
  }
  .recharge-form {
    width: 400px;
    margin: 30px auto;
  }
  .on-recharge {
    margin: 10px 170px
  }
  .explain-content {
    margin: 20px auto;
  }
</style>
