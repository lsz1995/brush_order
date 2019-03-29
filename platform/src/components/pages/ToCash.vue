<template>
  <div class="to-cash">
    <el-row>
      <el-col :span="24">
        提现
        <hr style="height:1px;border:none;border-top:3px solid #555555;width: 100%;margin:10px auto">
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="24" class="rest-money">
        <p>现金余额：{{money}}元</p>
        <p>温馨提示：每天只能申请提现1次。</p>
        <p>有时会出现延迟到账的情况。具体到账时间以收款银行入账时间为准。</p>
      </el-col>
    </el-row>
      <!--提现表单-->
    <el-row class="recharge-form-back">
      <el-form class="recharge-form" label-width="150px" :model="formMessage" :rules="rules" size="mini">
        <el-form-item label="提现金额(元):" prop="toMoney">
          <el-input placeholder="" v-model="formMessage.toMoney"></el-input>
        </el-form-item>

        <!--<el-form-item label="选择提现银行：">-->
          <!--<el-select v-model="formMessage.bankName" placeholder="请选择银行:">-->
            <!--<el-option label="中国光大银行" value="中国光大银行"></el-option>-->
            <!--<el-option label="建设银行" value="建设银行"></el-option>-->
            <!--<el-option label="中国银行" value="中国银行"></el-option>-->
          <!--</el-select>-->
        <!--</el-form-item>-->
        <el-form-item label="银行卡姓名:" prop="userCardName">
          <el-input type="text" placeholder="" v-model="formMessage.userCardName"></el-input>
        </el-form-item>
        <el-form-item label="请填提现银行卡号:" prop="bankNumber">
          <el-input type="text" placeholder="" v-model="formMessage.bankNumber"></el-input>
        </el-form-item>

        <el-form-item label="手续费:" prop="cMoney">
          <p>￥-{{formMessage.toMoney * 0.006}}</p>
        </el-form-item>

        <!--<el-form-item label="设置安全密码" prop="saveNumber">-->
          <!--<el-input type="text" placeholder="" v-model="formMessage.saveNumber"></el-input>-->
        <!--</el-form-item>-->
        <el-button @click="onToCash" class="on-to-cash" type="primary" size="medium">申请提现</el-button>
      </el-form>
    </el-row>
    <!--提现记录列表-->
    <el-table :data="tableData" stripe style="width: 100%;margin-top: 10px" height="250" size="mini">
      <el-table-column label="提现记录">
        <el-table-column prop="add_time" label="提交时间" width="120"></el-table-column>
        <el-table-column prop="money" label="提现金额" width="100"></el-table-column>
        <!--<el-table-column prop="reduceMoney" label="手续费" width="100"></el-table-column>-->
        <el-table-column prop="arrival_money" label="实际金额" width="100"></el-table-column>
        <el-table-column prop="state" label="状态"></el-table-column>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'ToCash',
  data () {
    return {
      money: '',
      formMessage: {
        toMoney: '',
        // bankName: '',
        userCardName: '',
        bankNumber: '',
        saveNumber: ''
      },
      rules: {
        bankName: [{
          required: true
        }],
        toMoney: [{
          required: true, message: '请输入提现金额', trigger: 'blur'
        }],
        userCardName: [{
          required: true, message: '请输入银行卡姓名', trigger: 'blur'
        }],
        bankNumber: [{
          required: true, message: '请输入银行卡号', trigger: 'blur'
        }]
      },
      tableData: [{}]
    }
  },
  computed: {
    arrivalMoney: function () {
      return this.formMessage.toMoney * 0.994
    }
  },
  mounted: function () {
    this.$http.get('/users/1/') // 将信息发送给后端
      .then((res) => { // axios返回的数据都在res.data里
        // console.log(res)
        if (res.status === 200) { // 如果成功
          this.money = res.data.balance
        } else {
          this.money = 'null'
        }
      })
    // 提现列表
    this.$http.get('/Withdraw/') // 将信息发送给后端
      .then((res) => { // axios返回的数据都在res.data里
        // console.log(res)
        if (res.status === 200) { // 如果成功
          this.tableData = res.data.results
          for (var j = 0; j < this.tableData.length; j++) {
            if (this.tableData[j].state) {
              this.tableData[j].state = '提现成功'
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
    onToCash () {
      let obj = {
        money: this.formMessage.toMoney,
        Bank_number: this.formMessage.bankNumber,
        name: this.formMessage.userCardName,
        arrival_money: this.arrivalMoney,
        state: false
      }
      var that = this
      this.$http.post('/Withdraw/', obj) // 将信息发送给后端
        .then((res) => { // axios返回的数据都在res.data里
          // console.log(res)
          if (res.status === 201) { // 如果成功
            // 成功，显示提示语
            this.$message({
              type: 'success',
              message: '提现信息提交成功，核实成功便会到账！'
            })
          }
        })
        .catch(function (error) {
          console.log(error)
          if ('non_field_errors' in error) {
            that.error = error.non_field_errors[0]
            that.$message({
              type: 'error',
              message: '提现失败！' + that.error
            })
          }
        })
    }
  }
}
</script>

<style scoped>
  .to-cash {
    font-size: 14px;
  }
  .rest-money {
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
    margin-top: 10px;
  }
  .recharge-form {
    width: 400px;
    margin: 30px auto;
  }
  .on-to-cash {
    margin: auto 170px
  }
</style>
