<template>
  <fieldset>
    <el-form label-position="top" :model="applicant" label-width="80px" :rules="rules" ref="form">
      <el-form-item id="type-select">
        您選擇的類別是
        <el-select v-model="type" placeholder="請選擇">
          <el-option
            v-for="(item, index) in $store.state.types"
            :key="index"
            :value="item.id"
            :label="item.name"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="姓名" prop="username">
        <el-input placeholder="e.g. 邱威傑" v-model.trim="applicant.username"></el-input>
      </el-form-item>
      <el-form-item :label="mobileText">
        <el-row class="phone-auth" type="flex">
          <el-button v-if="!$store.state.authentication" type="primary" @click="phoneAuth" :loading="authenticating">手機認證</el-button>
          <div class="mobile-number" v-show="$store.state.authentication">{{ applicant.mobile }}</div>
          <i class="el-icon-success" v-show="$store.state.authentication"></i>
        </el-row>
        <div class="el-form-item__error" style="color: #fff !important;">
          如果您的裝置未接收到驗證簡訊，請逕聯絡團隊為您服務！
        </div>
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
      <el-form-item prop="agreement" style="margin-bottom:1vh;">
          <label style="color:#fff;">
            <span aria-checked="mixed" class="el-checkbox__input" :class="{'is-checked' : applicant.agreement}">
              <span class="el-checkbox__inner"></span>
              <input type="checkbox" aria-hidden="true" class="el-checkbox__original" v-model="applicant.agreement" @change="showAgreementModal=true"/>
              {{agreementText}}
            </span>
          </label>
      </el-form-item>
    </el-form>
    <div class="form-footer-btn">
      <el-button @click="$emit('previous')">上一頁</el-button>
      <el-button @click="nextPage">下一頁</el-button>
    </div>
    <AgreementModal v-if="showAgreementModal" @close="disagree(true)" @disagree="disagree(false)">
    </AgreementModal>
    <AuthModal v-if="showAuthModal"  @cancel="dismissAuthModal"></AuthModal>
  </fieldset>
</template>

<script>
import AgreementModal from '@/components/AgreementModal.vue'
import AuthModal from '@/components/AuthModal.vue'
export default {
  name: 'InputUserInfo',
  components: {
    AgreementModal,
    AuthModal
  },
  data: () => ({
    mobileText: '',
    showAgreementModal: false,
    showAuthModal: false,
    authenticating: false,
    agreementText: '我同意《台北市議員邱威傑市民服務系統使用說明及隱私權政策》',
    type: '',
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
  props: ['selectedType'],
  watch: {
    selectedType: function (value) {
      this.type = value
    },
    type: function (value) {
      this.$store.commit('setCase', { type: value })
    }
  },
  created () {
  },
  mounted() {
  },
  methods: {
    disagree (value) {
      this.applicant.agreement = value
      this.showAgreementModal = false
    },
    phoneAuth () {
      this.showAuthModal = true
      this.authenticating = true
    },
    dismissAuthModal (status) {
      this.showAuthModal = false
      if(status !== 'DISMISS'){
        firebase.auth().currentUser.getIdToken(false).then(t => {
          let auth = status.split(',')
          this.sendToken(t, auth[1].replace('+886', '0'))
        }).catch(e => {
          this.$alert('請重新認證', '呱吉提示', {
            type: 'warning',
            confirmButtonText: '好！'
          })
        })
      }
      this.authenticating = false
    },
    sendToken (t, mobile) {
      this.axios.post('/api/users/token_auth/', {
        token: t
      }).then(response => {
        this.mobileText = '手機號碼'
        this.applicant.mobile = mobile
        let jwt = { Authorization: 'JWT ' + response.data.jwt }
        this.$store.commit('setJWT', jwt)
        this.$store.commit('setAuthenticated', true)
      }).catch(e => {
        let title = e.response.status + ' ' + e.response.statusText
        let content = e.response.data[0] ? e.response.data[0] : '請聯絡工作人員 02-27297708 分機 7152、7252'
        this.$alert(content, title, {
          type: 'error'
        })
      })
    },
    nextPage () {
      this.$refs.form.validate((valid) => {
        if (valid) {
          if (this.$store.state.authentication) {
            if (this.applicant.agreement) {
              this.$store.commit('setCase',
                {
                  username: this.applicant.username,
                  email: this.applicant.email,
                  address: this.applicant.address,
                  region: this.applicant.region
                })
              this.$emit('next')
            } else {
              this.$alert('請同意本系統個資使用', '呱吉提示', {
                type: 'warning',
                confirmButtonText: '好！'
              })
            }
          } else {
            this.$alert('請通過手機認證', '呱吉提示', {
              type: 'warning',
              confirmButtonText: '好！'
            })
          }
        } else {
          this.$emit('validateFail')
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

<style lang="css">
.phone-auth{
  flex-direction: row;
}

.phone-auth > i{
  font-size: x-large;
  line-height: 40px;
  margin-left: 20px;
  color: darkgreen;
}

.mobile-number {
  color: #fff;
  font-size: large;
  font-weight: 600;
}
</style>
