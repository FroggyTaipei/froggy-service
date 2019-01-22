<template>
  <fieldset>
    <el-form label-position="top" :model="applicant" label-width="80px" :rules="rules" ref="form">
      <el-form-item :label="$store.state.typeText">
      </el-form-item>
      <el-form-item label="姓名" prop="username">
        <el-input placeholder="e.g. 邱威傑" v-model.trim="applicant.username"></el-input>
      </el-form-item>
      <el-form-item>
        <el-row class="accountkit" type="flex">
          <AccountKit ref="accountKit">
            <el-button type="primary" @click="login" :disabled="authenticating">手機認證</el-button>
          </AccountKit>
          <i class="el-icon-success" v-show="authentication"></i>
          <i class="el-icon-loading" v-show="authenticating"></i>
        </el-row>
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
        <el-input placeholder="e.g. 信義路三段" v-model.trim="applicant.address"></el-input>
      </el-form-item>
      <el-form-item label="Email" prop="email">
        <el-input placeholder="e.g. froggy@froggy.com" v-model.trim="applicant.email"></el-input>
      </el-form-item>
      <el-form-item prop="agreement">
          <el-checkbox :label="agreementText" name="type" v-model="applicant.agreement" @change="clickAgreement"></el-checkbox>
      </el-form-item>
    </el-form>
    <div class="form-footer-btn">
      <el-button @click="$emit('previous')">上一頁</el-button>
      <el-button @click="nextPage">下一頁</el-button>
    </div>
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
    dialogAgreement: {
      type: Boolean,
      default: () => {
        return false
      }
    }
  },
  data: () => ({
    authentication: false,
    authenticating: false,
    agreementText: '我同意選民服務個資使用',
    applicant: {
      username: '',
      mobile: '',
      email: '',
      address: '',
      region: '',
      agreement: ''
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
  watch: {
    dialogAgreement: function (value) {
      console.log(value)
      this.applicant.agreement = value
    }
  },
  methods: {
    clickAgreement () {
      if (this.applicant.agreement) {
        this.dialogAgreement = true
        this.$emit('showAgreement')
      }
    },
    login () {
      this.$refs.accountKit.login(
        {
          countryCode: '+886'
        },
        this.loginCallback
      )
      this.authenticating = true
    },
    loginCallback (response) {
      if (response && response.status === 'PARTIALLY_AUTHENTICATED') {
        this.getAccountKitToken({
          code: response.code,
          status: response.status,
          state: response.state
        })
      } else {
        this.$alert('發生錯誤，請稍後再試', '提示', {
          type: 'warning'
        })
      }
    },
    getAccountKitToken (accountKitResp) {
      console.log(accountKitResp)
      this.authenticating = false
      this.axios.post('/api/users/accountkit_get_token/', accountKitResp)
        .then(response => {
          let jwt = { Authorization: 'JWT ' + response.data.jwt }
          this.authentication = true
          this.$store.commit('setJWT', jwt)
        })
        .catch(e => {
          console.log(e)
        })
    },
    nextPage () {
      this.$emit('next')
      // this.$refs.form.validate((valid) => {
      //   if (valid) {
      //     if (this.authentication) {
      //       if (this.applicant.agreement) {
      //         console.log('form pass')
      //         this.$store.commit('setCase',
      //           {
      //             username: this.applicant.username,
      //             email: this.applicant.email,
      //             address: this.applicant.address,
      //             region: this.applicant.region
      //           })
      //         this.$emit('next')
      //       } else {
      //         this.$alert('請同意本系統個資使用', '提示', {
      //           type: 'warning'
      //         })
      //       }
      //     } else {
      //       this.$alert('請通過手機認證', '提示', {
      //         type: 'warning'
      //       })
      //     }
      //   } else {
      //     console.log('error submit!!')
      //     return false
      //   }
      // })
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

<style lang="css">
.accountkit{
  flex-direction: row;
}

.accountkit > i{
  font-size: x-large;
  line-height: 40px;
  margin-left: 20px;
  color: darkgreen;
}
</style>
