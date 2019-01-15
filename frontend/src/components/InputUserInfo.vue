<template>
  <!-- Page three -->
  <fieldset>
    <h2 class="fs-title">
      Create your account
    </h2>
    <h3 class="fs-subtitle">
      Fill in your credentials
    </h3>
    <div class="form-row">
      <label
        for="name"
        class="col-sm-2 col-form-label">
        姓名
      </label>
      <input
        type="text"
        name="name"
        id="name"
        class="form-control col-sm-10"
        placeholder="e.g. 邱威傑"
        v-validate="'required'"
        v-model.trim="applicant.username">
      <div class="col-sm-12 invalid-feedback">
        {{ errors.first('name') }}
      </div>
    </div>
    <div class="form-row">
      <label
        for="mobile"
        class="col-sm-2 col-form-label">
        手機
      </label>
      <input
        type="text"
        name="mobile"
        id="mobile"
        class="form-control col-sm-10"
        placeholder="e.g. 0912345678"
        v-validate="{ required: true, regex: /^09\d{8}$/ }"
        v-model.trim="applicant.mobile">
      <div class="col-sm-12 invalid-feedback">
        {{ errors.first('mobile') }}
      </div>
    </div>
    <div class="form-row">
      <label
        for="address"
        class="col-sm-2 col-form-label">
        住址
      </label>
      <select
        name="district"
        id="district"
        class="form-control col-sm-5 district-bottom"
        @change="selectDistrict"
        v-validate="'required'"
        v-model="district">
        <option
          disabled
          value="">
          選擇行政區
        </option>
        <option
          v-for="(item, index) in $store.state.regions"
          :key="index"
          :value="item">
          {{ item.name }}
        </option>
      </select>
      <div class="col-sm-12 invalid-feedback">
        {{ errors.first('district') }}
      </div>
    </div>

    <div class="form-row">
      <input
        type="text"
        name="road"
        id="road"
        class="form-control col-sm-10 offset-sm-2"
        placeholder="e.g. 信義路三段"
        v-validate="'required|max:20'"
        v-model.lazy.trim="road">
      <div class="col-sm-12 invalid-feedback">
        {{ errors.first('road') }}
      </div>
    </div>
    <div class="form-row">
      <label
        for="email"
        class="col-sm-2 col-form-label">
        Email
      </label>
      <input
        type="text"
        name="email"
        id="email"
        class="form-control col-sm-10"
        placeholder="e.g. froggy@froggy.com"
        v-validate="'required|email'"
        v-model.trim="applicant.email">
      <div class="col-sm-12 invalid-feedback">
        {{ errors.first('email') }}
      </div>
    </div>
    <div
      class="form-row">
      <div
        class="col-sm-2">
        Checkbox
      </div>
      <div class="col-sm-10">
        <div class="form-check">
          <input
            class="form-check-input"
            type="checkbox"
            id="agreementCheck"
            v-model="agreement">
          <label
            class="form-check-label"
            for="agreementCheck">
            我同意台北市議員邱威傑選民服務系統隱私權及個人資料使用說明
          </label>
        </div>
      </div>
    </div>

    <input
      type="button"
      name="previous"
      class="previous action-button-previous"
      value="Previous"
      @click="$emit('previous')">
    <input
      type="button"
      name="submit"
      class="next action-button"
      value="submit"
      @click="submit">
    <Modal
      v-if="showAgreementPopup"
      @close="showAgreementPopup = false">
      <h2 slot="body">
        請同意個人資料使用
      </h2>
    </Modal>
    <Modal
      v-if="caseCompletePopup"
      @close="caseCompletePopup = false">
      <h2 slot="body">
        案件已送出
      </h2>
    </Modal>
  </fieldset>
</template>

<script>
import Modal from './Modal.vue'
export default {
  name: 'InputUserInfo',
  components: {
    Modal
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
    caseCompletePopup: false,
    agreement: false,
    regions: [],
    road: '',
    district: '',
    applicant: {
      username: '',
      mobile: '',
      email: '',
      address: '',
      region: 1
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
    selectDistrict () {
      this.applicant.region = this.district.id
      this.applicant.address = this.district.name
    },
    submit () {
      this.$validator.validateAll().then((result) => {
        if (result) {
          console.log('Form Submitted!')
          if (!this.agreement) {
            console.log('please check agreement')
            this.showAgreementPopup = true
          } else {
            console.log('form pass')
            this.$store.commit('setCase', this.applicant)
            this.submitCase()
          }
          return
        }
        console.log('Correct them errors!')
      })
    },
    submitCase () {
      let caseData = Object.assign({}, this.$store.state.case)
      console.log(caseData)
      this.axios.post('/api/cases', caseData, { headers: this.$store.state.header })
        .then(response => {
          console.log('submit success')
          this.caseCompletePopup = true
        })
        .catch(e => { console.log(e) })
    }
  }
}
</script>

<style lang="css" scoped>
  .district-bottom {
    margin-bottom: 10px;
  }
</style>
