<template>
  <!-- Page three -->
  <fieldset>
    <h2 class="fs-title">
      Create your account
    </h2>
    <h3 class="fs-subtitle">
      Fill in your credentials
    </h3>
    <div
      class="form-group row"
      :class="{ 'form-group--error': $v.applicant.name.$error }">
      <label
        for="name"
        class="col-sm-2 col-form-label">
        姓名
      </label>
      <div class="col-sm-10">
        <input
          type="text"
          name="name"
          id="name"
          placeholder="請輸入真實姓名"
          v-model.trim="$v.applicant.name.$model">
      </div>
      <div v-if="$v.applicant.name.$error">
        <div
          class="error col-sm-12"
          v-if="!$v.applicant.name.required">
          Field is required
        </div>
      </div>
    </div>
    <div class="form-group row resident-checkbox">
      <label
        for="name"
        class="col-sm-2 col-form-label">
        身份別
      </label>
      <div class="form-inline col-sm-10">
        <div class="form-inline col-sm-6">
          <div class="form-check col-sm-4">
            <input
              class="form-check-input"
              type="checkbox"
              id="residentCheck"
              v-model="applicant.isResident">
            <label
              class="form-check-label"
              for="residentCheck">
              台北市民
            </label>
          </div>
          <div class="col-sm-8">
            <select
              class="form-control"
              v-model="applicant.district">
              <option
                disabled
                value="">
                Please select one
              </option>
              <option
                v-for="(item, index) in districts"
                :key="index">
                {{ item }}
              </option>
            </select>
          </div>
        </div>
        <div class="col-sm-6">
          <div class="form-check">
            <input
              class="form-check-input"
              type="checkbox"
              id="nonResidentCheck"
              v-model="applicant.isResident">
            <label
              class="form-check-label"
              for="nonResidentCheck">
              非台北市民
            </label>
          </div>
        </div>
      </div>
    </div>
    <div
      class="form-group row"
      :class="{ 'form-group--error': $v.applicant.mobile.$error }">
      <label
        for="mobile"
        class="col-sm-2 col-form-label">
        手機
      </label>
      <div class="col-sm-10">
        <input
          type="text"
          name="mobile"
          id="mobile"
          placeholder="請輸入手機號碼"
          v-model.trim="$v.applicant.mobile.$model">
      </div>
      <div v-if="$v.applicant.mobile.$error">
        <div
          class="error col-sm-12"
          v-if="!$v.applicant.mobile.required">
          Field is required
        </div>
        <div
          class="error col-sm-12"
          v-if="!$v.applicant.mobile.numeric">
          Please input numbers
        </div>
      </div>
    </div>
    <div
      class="form-group row"
      :class="{ 'form-group--error': $v.applicant.phone.$error }">
      <label
        for="phone"
        class="col-sm-2 col-form-label">
        市話
      </label>
      <div class="col-sm-10">
        <input
          type="text"
          name="phone"
          id="phone"
          placeholder="請輸入市話號碼"
          v-model.trim="$v.applicant.phone.$model">
      </div>
      <div v-if="$v.applicant.phone.$error">
        <div
          class="error col-sm-12"
          v-if="!$v.applicant.phone.required">
          Field is required
        </div>
        <div
          class="error col-sm-12"
          v-if="!$v.applicant.phone.numeric">
          Please input numbers
        </div>
      </div>
    </div>
    <div
      class="form-group row"
      :class="{ 'form-group--error': $v.applicant.email.$error }">
      <label
        for="mail"
        class="col-sm-2 col-form-label">
        Email
      </label>
      <div class="col-sm-10">
        <input
          type="text"
          name="mail"
          id="mail"
          placeholder="請輸入電子郵件帳號"
          v-model="$v.applicant.email.$model">
      </div>
      <div v-if="$v.applicant.email.$error">
        <div
          class="error col-sm-12"
          v-if="!$v.applicant.email.required">
          Field is required
        </div>
        <div
          class="error col-sm-12"
          v-if="!$v.applicant.email.email">
          Please input valid email address
        </div>
      </div>
    </div>
    <div
      class="form-group row">
      <div
        class="col-sm-2">
        Checkbox
      </div>
      <div class="col-sm-10">
        <div class="form-check">
          <input
            class="form-check-input"
            type="checkbox"
            id="agreementCheck">
          <label
            class="form-check-label"
            for="agreementCheck">
            我同意台北市議員邱威傑選民服務系統隱私權及個人資料使用說明
          </label>
        </div>
      </div>
      <div>
        <div
          class="error col-sm-12">
          Field is required
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
  </fieldset>
</template>

<script>
import { required, numeric, email } from 'vuelidate/lib/validators'
export default {
  name: 'InputUserInfo',
  validations: {
    applicant: {
      name: {
        required
      },
      mobile: {
        required,
        numeric
      },
      phone: {
        required,
        numeric
      },
      email: {
        required,
        email
      }
    }
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
    applicant: {
      isResident: true,
      district: '',
      name: '',
      mobile: '',
      phone: '',
      email: ''
    },
    districts: [
      '松山區', '信義區', '士林區', '北投區', '內湖區', '文山區', '中山區', '大同區', '中正區', '萬華區', '南港區', '大安區'
    ]
  }),
  methods: {
    submit () {
      console.log('submit!')
      this.$v.$touch()

      this.next()
      if (this.$v.$invalid) {
        console.log('form error')
      } else {
        console.log('form pass')
      }
    }
  }
}
</script>

<style lang="css" scoped>
</style>
