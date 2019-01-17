<template>
  <fieldset>
      <AccountKit v-show="false" ref="accountKit">
        <el-button type="primary" @click="login">認證</el-button>
      </AccountKit>
    <el-form label-position="top" :model="applicant" label-width="80px" :rules="rules" ref="form">
      <el-form-item label="姓名" prop="username">
        <el-input placeholder="e.g. 邱威傑" v-model="applicant.username"></el-input>
      </el-form-item>
      <el-form-item label="手機">
        <el-input placeholder="e.g. 0912345678" v-model="applicant.mobile"></el-input>
      </el-form-item>
      <el-form-item label="身份別" prop="region">
        <el-select v-model="applicant.region" placeholder="請選擇">
          <el-option
            v-for="(item, index) in $store.state.regions"
            :key="index"
            :value="item.id"
            :label="item.name"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="住址">
        <el-input placeholder="e.g. 信義路三段" v-model="road"></el-input>
      </el-form-item>
      <el-form-item label="Email" prop="email">
        <el-input placeholder="e.g. froggy@froggy.com" v-model="applicant.email"></el-input>
      </el-form-item>
      <el-form-item prop="agreement">
          <el-checkbox :label="agreementText" name="type" v-model="applicant.agreement"></el-checkbox>
      </el-form-item>
      <el-form-item>
        <el-button @click="$emit('previous')">上一頁</el-button>
        <el-button type="primary" @click="nextPage">下一頁</el-button>
      </el-form-item>
    </el-form>

  </fieldset>
</template>

<script>
import AccountKit from '@/components/AccountKit.vue'
export default {
  name: 'InputUserInfo',
  components: {
    AccountKit
  },
  props: {
    isClose: {
      type: Boolean,
      default: () => {
        return false
      }
    }
  },
  data: () => ({
    showAgreementPopup: false,
    agreementText: '我已閱讀並同意台北市議員邱威傑選民服務系統隱私權及個人資料使用說明',
    regions: [],
    road: '',
    district: '',
    applicant: {
      username: '',
      mobile: '',
      email: '',
      address: '',
      region: 1,
      agreement: false
    },
    rules: {
      username: [{
        required: true,
        message: '請輸入姓名',
        trigger: 'blur'
      }],
      region: [{
        required: true,
        message: '請選擇身份別',
        trigger: 'change'
      }],
      email: [{
        required: true,
        message: '請輸入電子郵件信箱',
        trigger: 'blur'
      },
      {
        type: 'email',
        message: '電子郵件格式錯誤',
        trigger: 'change'
      }],
      agreement: [{
        required: true,
        message: '請同意個資使用',
        trigger: 'change'
      }]
    }
  }),
  mounted () {
    this.regions = this.$store.state.region
  },
  watch: {
    isClose: function (value) {
      if (value) {
        this.$validator.errors.clear()
        this.applicant = {
          username: '',
          mobile: '',
          email: '',
          address: '',
          region: 0
        }
      }
    },
    road: function (value) {
      this.applicant.address = this.district.name + this.road
    }
  },
  methods: {
    login () {
      this.$refs.accountKit.login(
        {
          countryCode: '+886',
          phoneNumber: '0938926812'
        },
        this.loginCallback
      )
    },
    loginCallback (response) {
      console.log(response)
      let accountKitResp = {
        code: response.code,
        status: response.status,
        state: response.state
      }
      this.getAccountKitToken(accountKitResp)
    },
    getAccountKitToken (accountKitResp) {
      console.log(accountKitResp)

      this.axios.post('/api/users/accountkit_get_token/', accountKitResp)
        .then(response => {
          console.log('jwt ', response)
        })
        .catch(e => { console.log(e) })
    },
    selectDistrict () {
      this.applicant.region = this.district.id
      this.applicant.address = this.district.name
    },
    nextPage () {
      this.$refs.form.validate((valid) => {
        if (valid) {
          console.log('form pass')
          this.$store.commit('setCase', this.applicant)
          this.$emit('next')
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    validate () {
      return new Promise((resolve, reject) => {
        this.$refs.form.validate((valid) => {
          this.$emit('on-validate', valid, this.model)
          resolve(valid)
        })
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    }
  }
}
</script>

<style lang="css" scoped>
</style>
