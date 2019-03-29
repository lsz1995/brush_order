<template>
  <div class="shop">
    <!--标题头-->
    <el-row>
      <el-col :span="24">
        店铺管理
        <hr style="height:1px;border:none;border-top:3px solid #555555;width: 100%;margin:10px auto">
      </el-col>
    </el-row>
    <el-table :data="tableData" stripe style="width: 100%" height="250" size="mini">
      <el-table-column label="绑定店铺">
        <el-table-column prop="store_name" label="店铺名称" width="150"></el-table-column>
        <el-table-column prop="store_category" label="类目" width="150"></el-table-column>
        <el-table-column prop="fullAddress" label="发货地址" width="300"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button @click="handleDelete(scope.$index, scope.row)" type="danger" size="mini">删除</el-button>
          </template>
        </el-table-column>
      </el-table-column>
    </el-table>
    <el-row class="on-add-shop" type="flex" justify="center">
      <el-button @click="onAddShop"  type="primary" size="medium">添加店铺</el-button>
    </el-row>
    <template v-if="ifAdd">
      <hr style="height:1px;border:none;border-top:1px dashed rgb(150,150,150);width: 100%;margin:20px auto">
      <el-row>
        <p>添加店铺：</p>
        <p>提示：淘宝C店必须是加入消保的店铺</p>
      </el-row>
      <!--添加店铺信息表单-->
      <el-row>
        <el-form class="shop-form" label-width="120px" ref="shopForm" :model="formMessage" :rules="rules" size="mini">
          <el-form-item label="店铺旺旺:" prop="shopWW">
            <el-input type="text" placeholder="" v-model="formMessage.shopWW"></el-input>
          </el-form-item>
          <el-form-item label="店铺名称:" prop="shopName">
            <el-input type="text" placeholder="" v-model="formMessage.shopName"></el-input>
          </el-form-item>
          <el-form-item label="店铺类目:" prop="shopCategory">
            <el-input type="text" placeholder="" v-model="formMessage.shopCategory"></el-input>
          </el-form-item>
          <el-form-item label="店铺链接:" prop="shopURL">
            <el-input type="text" placeholder="" v-model="formMessage.shopURL"></el-input>
          </el-form-item>
          <el-form-item label="发件人姓名:" prop="senderName">
            <el-input type="text" placeholder="" v-model="formMessage.senderName"></el-input>
          </el-form-item>
          <el-form-item label="手机:" prop="senderMobile">
            <el-input type="text" placeholder="" v-model="formMessage.senderMobile"></el-input>
          </el-form-item>
          <el-form-item label="所在地区:">
            <template>
              <!--<div id="province">-->
              <el-cascader
                size="mini"
                :options="options"
                v-model="selectedOptions"
                @change="addressChange">
              </el-cascader>
              <!--</div>-->
            </template>
          </el-form-item>
          <el-form-item label="详细地址:" prop="address">
            <el-input type="text" placeholder="" v-model="formMessage.address"></el-input>
          </el-form-item>
          <el-form-item label="邮编:" prop="postalCode">
            <el-input type="text" placeholder="" v-model="formMessage.postalCode"></el-input>
          </el-form-item>
          <el-form-item label="卖家中心截图:" prop="image">
            <el-upload
              ref="upload"
              action=""
              :beforeUpload="beforeUploadPicture"
              :on-success="successUpload"
              :on-change="imageChange"
              :on-preview="handlePreview"
              :auto-upload="false"
              :on-exceed="handleExceed"
              :http-request="handleFile"
              :multiple="false"
              :limit="1"
              :file-list="image_path"
              list-type="picture">
              <el-button size="small" type="primary">点击上传</el-button>
              <!--<i class="el-icon-plus"></i>-->
              <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
            </el-upload>
            <!--<input class="file" name="file" type="file" accept="image/png,image/gif,image/jpeg" @change="update"/>-->
          </el-form-item>
          <el-button @click="onShop" class="on-shop" type="primary" size="medium">确定添加店铺</el-button>
        </el-form>
      </el-row>
    </template>
  </div>
</template>

<script>
import { regionData, CodeToText } from 'element-china-area-data'
export default {
  name: 'Shop',
  data () {
    return {
      formMessage: {
        shopWW: '',
        shopName: '',
        shopCategory: '',
        shopURL: '',
        senderName: '',
        senderMobile: '',
        province: '',
        city: '',
        district: '',
        address: '',
        postalCode: '',
        image: '',
        state: ''
      },
      image_path: [],
      options: regionData,
      selectedOptions: [],
      rules: {
        shopWW: [{
          required: true, type: 'string', message: '请输入店铺旺旺号', trigger: 'blur'
        }],
        shopName: [{
          required: true, type: 'string', message: '请输入店铺名', trigger: 'blur'
        }],
        shopCategory: [{
          required: true, type: 'string', message: '请输入店类目', trigger: 'blur'
        }],
        shopURL: [{
          required: true, type: 'string', message: '请输入店铺网址', trigger: 'blur'
        }],
        senderName: [{
          required: true, type: 'string', message: '请输入发件人姓名', trigger: 'blur'
        }],
        senderMobile: [{
          required: true, type: 'string', message: '请输入手机号', trigger: 'blur'
        }],
        address: [{
          required: true, type: 'string', message: '请输入详细地址', trigger: 'blur'
        }],
        postalCode: [{
          required: true, type: 'string', message: '请输入邮编', trigger: 'blur'
        }],
        image: [{
          required: true, type: 'string', message: '请上传图片', trigger: 'blur'
        }]
      },
      ifAdd: false,
      tableData: [{}]
      // getShopList: ''
    }
  },
  mounted: function () {
    // 获取店铺列表
    this.getShopList()
  },
  // computed: {
  //   param: function (file) {
  //     console.log(1)
  //     let paramData = new FormData()
  //     paramData.append('image', file, file.name)
  //     paramData.append('store_ww', this.formMessage.shopWW)
  //     paramData.append('store_name', this.formMessage.shopName)
  //     paramData.append('store_category', this.formMessage.shopCategory)
  //     paramData.append('store_url', this.formMessage.shopURL)
  //     paramData.append('sender_name', this.formMessage.senderName)
  //     paramData.append('mobile', this.formMessage.senderMobile)
  //     paramData.append('province', this.formMessage.province)
  //     paramData.append('city', this.formMessage.city)
  //     paramData.append('district', this.formMessage.district)
  //     paramData.append('address', this.formMessage.address)
  //     paramData.append('postal_code', this.formMessage.postalCode)
  //     return paramData
  //   }
  // },
  methods: {
    onAddShop () {
      this.ifAdd = !this.ifAdd
    },
    // 选择省市区
    addressChange (arr) {
      this.formMessage.province = CodeToText[arr[0]]
      this.formMessage.city = CodeToText[arr[1]]
      this.formMessage.district = CodeToText[arr[2]]
    },
    // 限制上传文件的个数和定义超出限制时的行为
    handleExceed (files, fileList) {
      this.$message.warning(`当前限制选择 1 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`)
    },
    // 用户上传时的图片格式和大小校验
    beforeUploadPicture (file) {
      const isIMAGE = file.type === 'image/jpeg' || 'image/png'
      const isLt2M = file.size / 1024 / 1024 < 2
      if (!isIMAGE) {
        this.$message.error('上传图片只能是 JPG/PNG 格式!')
        return false
      }
      if (!isLt2M) {
        this.$message.error('上传图片大小不能超过 2MB!')
        return false
      }
      return isIMAGE && isLt2M

      // return false
    },
    handleFile () { },
    imageChange (file, fileList, name) {
      console.log(file, fileList)
      this.image_path = fileList
    },
    handlePreview (file) {
      console.log(file)
    },
    // 添加店铺信息
    onShop (file) {
      // 获取表单
      // let form = this.$refs['shopForm'].$el
      // 创建 FormData 对象
      // let paramData = new FormData(form)
      let paramData = new FormData()
      paramData.append('image', this.image_path[0] ? this.image_path[0].raw : '')
      paramData.append('store_ww', this.formMessage.shopWW)
      paramData.append('store_name', this.formMessage.shopName)
      paramData.append('store_category', this.formMessage.shopCategory)
      paramData.append('store_url', this.formMessage.shopURL)
      paramData.append('sender_name', this.formMessage.senderName)
      paramData.append('mobile', this.formMessage.senderMobile)
      paramData.append('province', this.formMessage.province)
      paramData.append('city', this.formMessage.city)
      paramData.append('district', this.formMessage.district)
      paramData.append('address', this.formMessage.address)
      paramData.append('postal_code', this.formMessage.postalCode)
      // 记得配置请求头中 Content-Type 为'multipart/form-data'
      let config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      var that = this
      this.$http.post('/store/', paramData, config) // 将信息发送给后端
        .then((res) => { // axios返回的数据都在res.data里
          console.log(res)
          if (res.status === 201) { // 如果成功
            // 登录成功，显示提示语
            this.$message({
              type: 'success',
              message: '店铺添加成功！'
            })
            this.onAddShop()
            this.getShopList()
          }
        })
        .catch(function (error) {
          console.log(error)
          if ('non_field_errors' in error) {
            that.error = error.non_field_errors[0]
            that.$message({
              type: 'error',
              message: '失败！' + that.error
            })
          }
        })
    },
    successUpload (response, file, filelist) {
      console.log(response)
    },
    // 获取店铺列表
    getShopList () {
      this.$http.get('/store/') // 将信息发送给后端
        .then((res) => { // axios返回的数据都在res.data里
          // console.log(res)
          if (res.status === 200) { // 如果成功
            this.tableData = res.data.results
            for (var i = 0; i < this.tableData.length; i++) {
              this.tableData[i].fullAddress = this.tableData[i].province + this.tableData[i].city + this.tableData[i].district + this.tableData[i].address
            }
          } else {
            this.tableData = 'null'
          }
        })
    },
    // 删除店铺
    handleDelete (index, row) {
      // console.log(row.id)
      this.$http.delete('/store/' + row.id) // 将信息发送给后端
        .then((res) => { // axios返回的数据都在res.data里
          if (res.status === 204) { // 如果成功
            // 成功，显示提示语
            this.$message({
              type: 'success',
              message: '店铺删除成功！'
            })
            // 删除后再次获取店铺列表
            this.getShopList()
          }
        })
    }
  }
}
</script>

<style scoped>
  .on-add-shop {
    margin-top: 10px;
    margin-bottom: 10px;
  }
  .shop-form {
    width: 330px;
    margin-left: 30px;
    margin-top: 20px;
  }
  .on-shop {
    margin-left: 70px;
  }
  .back-line {
    border-bottom:#CCC 1px dashed;
  }
</style>
