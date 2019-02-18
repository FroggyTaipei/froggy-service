<template>
  <fieldset>
    <el-form label-position="top" :model="cases" label-width="80px" :rules="rules" ref="form">
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
      <el-form-item label="案件主旨" prop="title">
        <el-input placeholder="請輸入案件主旨" v-model.trim="cases.title"></el-input>
      </el-form-item>
      <el-form-item label="案件內容" prop="content">
        <el-input rows="5" type="textarea" placeholder="請輸入案件內容" v-model="cases.content"></el-input>
      </el-form-item>
      <el-form-item label="相關地點" prop="location">
        <el-input placeholder="e.g. 信義路三段" v-model.trim="cases.location"></el-input>
      </el-form-item>
      <el-upload
        class="upload-demo"
        ref="upload"
        action="/api/files/temp/ "
        :on-change="handleChange"
        :on-remove="handleRemove"
        :on-exceed="handleExceed"
        :on-success="handleSuccess"
        :on-error="handleError"
        :before-upload="beforeUpload"
        :before-remove="beforeRemove"
        :headers="$store.state.jwt"
        :data="upload_data"
        :accept="acceptFileType"
        :limit="5">
        <el-button slot="trigger" type="primary">上傳檔案</el-button>
        <div slot="tip" class="el-upload__tip">1.上傳單檔限制為10MB，最多5個檔案。</div>
        <div v-if="!$store.state.isMobile" slot="tip" class="el-upload__tip">2.可上傳的檔案類型為jpg, jpeg, png, mpg, mpeg, avi, wmv, mp3, mp4, zip, rar, 7z, txt, doc, docx, ppt, pptx, pdf, odt, xls, xlsx, key, pages, numbers。</div>
        <div v-if="$store.state.isMobile" slot="tip" class="el-upload__tip">2.可上傳的檔案類型為jpg, jpeg, png。</div>
      </el-upload>
    </el-form>
    <div class="form-footer-btn">
      <el-button @click="$emit('previous')">上一頁</el-button>
      <el-button @click="completeCaseData">送出！</el-button>
    </div>
  </fieldset>
</template>

<script>
export default {
  name: 'InputCase',
  created () {
    this.cases.uuid = this.$uuid.v1()
    this.upload_data.case_uuid = this.cases.uuid
    if (!this.$store.state.isMobile) {
      this.acceptFileType += ',.mpg,.mpeg,.avi,.wmv,.mp3,.mp4,.zip,.rar,.7z,.doc,.docx,.ppt,.pptx,.pdf,.odt,.xls,.xlsx,.key,.pages,.numbers,.txt'
    }
  },
  data: () => ({
    caseCompletePopup: false,
    acceptFileType: '.jpg,.jpeg,.png',
    wrongFileType: false,
    fileOverSize: false,
    type: '',
    upload_data: {
      case_uuid: ''
    },
    cases: {
      uuid: '',
      title: '',
      content: '',
      location: ''
    },
    rules: {
      title: [{
        required: true,
        message: '請輸入案件主旨',
        trigger: 'blur'
      },
      {
        max: 30,
        message: '字數上限為 30 字',
        trigger: 'blur'
      }],
      content: [{
        required: true,
        message: '請輸入案件內容',
        trigger: 'blur'
      }, {
        max: 800,
        message: '字數上限為 800 字',
        trigger: 'blur'
      }],
      location: [{
        max: 30,
        message: '字數上限為 30 字',
        trigger: 'blur'
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
  methods: {
    updateCSRFToken () {
      this.axios.get('api/csrftoken/')
        .then(response => {
          console.log('get new CSRF token', response.data['token'])
          this.axios.defaults.headers.common['X-CSRFToken'] = response.data['token']
        })
        .catch(e => { console.log(e) })
    },
    removeFile (id) {
      console.log('remove cloud file', id)
      this.axios.delete('/api/files/temp/' + id, { headers: this.$store.state.jwt })
        .then(response => {
          console.log(response)
        })
        .catch(e => { console.log(e) })
    },
    submitCase () {
      const loading = this.$loading({
        lock: true,
        text: '拼命送出中',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)'
      })
      this.postCases(this.cases).then(response => {
        this.$router.push({ name: 'home', params: { success: true } })
        setTimeout(() => {
          loading.close()
        }, 500)
      }).catch(e => {
        console.log(e)
        console.log(e.response)
        loading.close()
        if (e.response.data.detail && e.response.data.detail.indexOf('expired') > -1) {
          this.$alert('請重新進行手機驗證', '憑證過期', {
            confirmButtonText: '確定',
            type: 'error',
            callback: action => {
              this.$store.commit('setAuthenticated', false)
            }
          })
        }
      })
    },
    postCases (cases) {
      return this.axios.post('/api/cases', cases, { headers: this.$store.state.jwt })
    },
    completeCaseData () {
      this.$refs.form.validate((valid) => {
        if (valid) {
          this.cases = Object.assign(this.cases, this.$store.state.case)
          this.submitCase()
        } else {
          console.log('Correct the errors!')
          this.$emit('validateFail')
        }
      })
    },
    beforeUpload (file) {
      console.log('before upload')
      const fileLimit = 10485760
      const fileRegExp = this.$store.state.isMobile ? /\.(jpg?|jpeg?|png?)$/i : /\.(jpg?|jpeg?|png?|mpg?|mpeg?|avi?|wmv?|mp3?|mp4?|zip?|rar?|7z?|doc?|docx?|ppt?|pptx?|pdf?|odt?|xls?|xlsx?|key?|pages?|numbers?|txt?)$/i
      if (!fileRegExp.test(file.name)) {
        this.$refs.upload.abort()
        this.wrongFileType = true
        return false
      }
      if (file.size > fileLimit) {
        this.fileOverSize = true
        return false
      }
    },
    beforeRemove (file, fileList) {
      if (this.wrongFileType) {
        this.$alert('請上傳符合格式的檔案', '提示', {
          type: 'warning'
        })
        this.wrongFileType = false
      } else if (this.fileOverSize) {
        this.$alert('請勿上傳超過 10MB 的檔案', '提示', {
          type: 'warning'
        })
        this.fileOverSize = false
      } else {
        return this.$confirm(`確定要移除 ${file.name}？`, '提示', {
          confirmButtonText: '確定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(
        )
      }
    },
    handleRemove (file, fileList) {
      console.log('remove', file)
      if (file.response) {
        this.removeFile(file.response.id)
      }
    },
    handleExceed (files, fileList) {
      return this.$alert('請勿上傳超過 5 個檔案', '提示', {
        type: 'warning'
      })
    },
    handleChange (file, fileList) {
      console.log('change', fileList)
    },
    handleSuccess (response, file, fileList) {
      console.log(response)
    },
    handleError (err, file, fileList) {
      console.log(err.status)
      console.log(err.message)
      var errMsg = ''
      if (err.message.indexOf('expired') > -1) {
        errMsg = '憑證過期，請重新進行手機驗證'
      } else {
        errMsg = err.message.slice(2, -2)
      }
      this.$alert(errMsg, '很抱歉', {
        type: 'error',
        callback: action => {
          if (err.message.indexOf('expired') > -1) {
            this.$store.commit('setAuthenticated', false)
          }
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
    }
  }
}
</script>

<style lang="css">
</style>
