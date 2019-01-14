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
        v-model.trim="applicant.name">
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
        for="phone"
        class="col-sm-2 col-form-label">
        市話
      </label>
      <input
        type="text"
        name="phone"
        id="phone"
        class="form-control col-sm-10"
        placeholder="e.g. 021234567(選填)"
        v-validate="'numeric'"
        v-model.trim="applicant.phone">
    </div>
    <div class="form-row">
      <label
        for="address"
        class="col-sm-2 col-form-label">
        市話
      </label>
      <input
        type="text"
        name="address"
        id="address"
        class="form-control col-sm-10"
        placeholder="e.g. 臺北市中正區黎明里北平西路3號"
        v-model.trim="applicant.address">
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
      @click="previous">
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
    next: {
      type: Function,
      default: () => {
        console.log('havent init')
      }
    },
    previous: {
      type: Function,
      default: () => {
        console.log('havent init')
      }
    }
  },
  data: () => ({
    showAgreementPopup: false,
    caseCompletePopup: false,
    agreement: false,
    isResidentCheck: '',
    applicant: {
      location: '',
      district: '',
      name: '',
      mobile: '',
      phone: '',
      email: '',
      address: ''
    }
  }),
  methods: {
    submit () {
      this.$validator.validateAll().then((result) => {
        if (result) {
          console.log('Form Submitted!')
          if (!this.agreement) {
            console.log('please check agreement')
            this.showAgreementPopup = true
          } else {
            console.log('form pass')
            this.caseCompletePopup = true
          }
          return
        }
        console.log('Correct them errors!')
      })
    }
  }
}
</script>

<style lang="css" scoped>
</style>
