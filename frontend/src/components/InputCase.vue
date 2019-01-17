<template>
  <fieldset>
    <el-form label-position="top" :model="cases" label-width="80px" :rules="rules" ref="form">
      <el-form-item label="案件主旨" prop="tltle">
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
        action="https://jsonplaceholder.typicode.com/posts/"
        :on-preview="handlePreview"
        :on-remove="handleRemove"
        :before-remove="beforeRemove"
        multiple
        :limit="3"
        :on-exceed="handleExceed"
        :file-list="fileList">
        <el-button size="small" type="primary">上傳附件</el-button>
        <div slot="tip" class="el-upload__tip">1.上傳總容量限制為40MB，最多5個檔案。</div>
        <div slot="tip" class="el-upload__tip">2.可上傳的檔案類型為jpg, jpeg, png, mpg, mpeg, avi, wmv, mp3, mp4, zip, rar, 7z。</div>
      </el-upload>
      <el-button @click="$emit('previous')">上一頁</el-button>
        <el-button type="primary" @click="completeCaseData">送出！</el-button>
    </el-form>
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
export default {
  name: 'InputCase',
  components: {
  },
  created () {
    console.log('input case init')

    this.cases.uuid = this.$uuid.v1()
    this.upload_data.case_uuid = this.cases.uuid
  },
  data: () => ({
    fileList: [{ name: 'food.jpeg', url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100' }, { name: 'food2.jpeg', url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100' }],
    files: [],
    caseCompletePopup: false,
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
      tltle: [{
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
  props: {
    isClose: {
      type: Boolean,
      default: () => {
        return false
      }
    }
  },
  watch: {
    isClose: function (value) {
      if (value) {
        this.$validator.errors.clear()
        this.applicant = {
          uuid: '',
          title: '',
          content: '',
          location: '',
          type: 1
        }
      }
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
      this.axios.delete('/api/files/temp/' + id, { headers: this.$store.state.header })
        .then(response => {
          console.log(response)
        })
        .catch(e => { console.log(e) })
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
    },
    completeCaseData () {
      this.$validator.validateAll().then((result) => {
        if (result) {
          this.$store.commit('setCase', this.cases)
          this.$emit('next')
          return
        }
        console.log('Correct the errors!')
      })
    },
    remove (file) {
      this.removeFile(file.response.id)
      this.$refs.upload.remove(file)
    },
    inputFilter (newFile, oldFile, prevent) {
      if (newFile && !oldFile) {
        // Before adding a file
        // Filter system files or hide files
        if (/(\/|^)(Thumbs\.db|desktop\.ini|\..+)$/.test(newFile.name)) {
          return prevent()
        }
        // Filter php html js file
        if (/\.(php5?|html?|jsx?)$/i.test(newFile.name)) {
          return prevent()
        }
      }
    },
    inputFile (newFile, oldFile) {
      if (newFile && !oldFile) {
        // add
        console.log('add', newFile)
        newFile.active = true
      }
      if (newFile && oldFile) {
        // 上传进度
        if (newFile.progress !== oldFile.progress) {
          console.log('progress', newFile.progress, newFile)
        }

        // 上传错误
        if (newFile.error !== oldFile.error) {
          console.log('error', newFile.error, newFile)
        }

        // 上传成功
        if (newFile.success !== oldFile.success) {
          console.log('success', newFile.success, newFile)
        }
      }
      if (!newFile && oldFile) {
        // remove
        console.log('remove', oldFile)
      }
    }
  }
}
</script>

<style lang="css">
</style>
