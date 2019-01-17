<template>
    <!-- Page two -->
    <fieldset>
    <div class="form-row">
        <label
        for="caseSubject"
        class="col-sm-2 col-form-label">
        案件主旨
        </label>
        <input
        type="text"
        name="主旨"
        id="caseSubject"
        class="form-control col-sm-10"
        placeholder="請輸入案件主旨"
        v-validate="'required|max:20'"
        v-model.trim="cases.title">
        <div class="col-sm-12 invalid-feedback">
            {{ errors.first('主旨') }}
        </div>
    </div>
    <div class="form-row">
        <label
        for="caseContent"
        class="col-sm-2 col-form-label">
        案件內容
        </label>
        <textarea
        rows="5"
        name="案件內容"
        id="caseContent"
        class="form-control col-sm-10"
        placeholder="請輸入案件內容"
        v-validate="'required|max:150'"
        v-model.trim="cases.content" />
        <div class="col-sm-12 invalid-feedback">
            {{ errors.first('案件內容') }}
        </div>
    </div>
    <div class="form-row">
        <label
        for="location"
        class="col-sm-2 col-form-label">
        地點
        </label>
        <input
        type="text"
        name="相關地點"
        id="location"
        class="form-control col-sm-10"
        placeholder="e.g. 信義路三段"
        v-validate="'required|max:20'"
        v-model.trim="cases.location">
        <div class="col-sm-12 invalid-feedback">
            {{ errors.first('相關地點') }}
        </div>
    </div>
    <div class="form-row">
        <label
            for="fileUpload"
            class="col-sm-2 col-form-label">
            上傳附件
        </label>
        <FileUpload
            class="btn btn-primary col-sm-5"
            post-action="/api/files/temp/"
            :headers="$store.state.header"
            :data="upload_data"
            extensions="gif,jpg,jpeg,png,webp"
            accept="image/png,image/gif,image/jpeg,image/webp"
            :multiple="true"
            :size="1024 * 1024 * 10"
            v-model="files"
            @input-filter="inputFilter"
            @input-file="inputFile"
            ref="upload">
            <i class="fa fa-plus" />
            Select files
        </FileUpload>
        <div
            class="col-md-10  offset-md-2 file"
            v-for="file in files"
            :key="file.id">
            <button
            type="button"
            class="btn btn-primary"
            @click="remove(file)">
            {{ file.name }} <span class="badge">
                Ｘ
            </span>
            </button>
        </div>
      </div>
    </div>
    <div class="form-group row">
        <div class="col-md-12">
        <small
            id="fileUploadHelpBlock"
            class="form-text text-muted">
            1.上傳總容量限制為40MB，最多10個檔案，附檔檔名請使用半形中英數字命名。2.可上傳的檔案類型為 jpg, jpeg, gif, bmp, png, tif, tiff, doc, docx, xls, xlsx, txt, rtf, ppt, pptx, pdf, odf, odg, odp, ods, odt, mpg, mpeg, avi, wmv, rm, mov, mkv, dat, 3gp, mp3, mp4, m4v, wav, zip, rar, 7z。
        </small>
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
        name="next"
        class="next action-button"
        value="Next"
        @click="completeCaseData">
    </fieldset>
</template>

<script>
import FileUpload from 'vue-upload-component'
export default {
  name: 'InputCase',
  components: {
    FileUpload
  },
  created () {
    console.log('input case init')

    this.cases.uuid = this.$uuid.v1()
    this.upload_data.case_uuid = this.cases.uuid
  },
  data: () => ({
    files: [],
    upload_data: {
      case_uuid: ''
    },
    cases: {
      uuid: '',
      title: '',
      content: '',
      location: ''
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

<style lang="css" scoped>
</style>
