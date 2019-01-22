<template>
  <fieldset>
    <el-form label-position="top" :model="cases" label-width="80px" :rules="rules" ref="form">
      <el-form-item :label="$store.state.typeText">
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
        :before-upload="beforeUpload"
        :before-remove="beforeRemove"
        :headers="$store.state.jwt"
        :data="upload_data"
        :accept="acceptFileType"
        :limit="5">
        <el-button slot="trigger" type="primary">上傳檔案</el-button>
        <div slot="tip" class="el-upload__tip">1.上傳單檔限制為10MB，最多5個檔案。</div>
        <div slot="tip" class="el-upload__tip">2.可上傳的檔案類型為jpg, jpeg, png, mpg, mpeg, avi, wmv, mp3, mp4, zip, rar, 7z。</div>
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
  },
  data: () => ({
    caseCompletePopup: false,
    acceptFileType: '.jpg,.jpeg,.png,.mpg,.mpeg,.avi,.wmv,.mp3,.mp4,.zip,.rar,.7z',
    wrongFileType: false,
    fileOverSize: false,
    uploadFail: false,
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
      console.log(this.cases)
      this.$router.push({ name: 'home', params: { success: true } })
      this.axios.post('/api/cases', this.cases, { headers: this.$store.state.jwt })
        .then(response => {
          console.log('submit success')
          this.$alert('案件已送出', '恭喜你', {
            type: 'success'
          }).then(
          )
        })
        .catch(e => {
          console.log(e)
          console.log(e.response)
        })
    },
    completeCaseData () {
      this.$refs.form.validate((valid) => {
        if (valid) {
          this.cases = Object.assign(this.cases, this.$store.state.case)
          this.submitCase()
          return
        }
        console.log('Correct the errors!')
      })
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
    beforeUpload (file) {
      console.log('before upload')
      const fileLimit = 10485760

      if (!/\.(jpg?|jpeg?|png?|mpg?|mpeg?|avi?|wmv?|mp3?|mp4?|zip?|rar?|7z?)$/i.test(file.name)) {
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
        this.$alert('請上傳符合格式的檔案')
        this.wrongFileType = false
      } else if (this.fileOverSize) {
        this.$alert('請勿上傳超過 10MB 的檔案')
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
    handleChange (file, fileList) {
      console.log('change', fileList)
      if (!this.uploadFail && file.status === 'fail') {
        this.$alert('上傳發生錯誤，請稍後再試', '很抱歉', {
          type: 'error'
        }).then(
        )
      }
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
