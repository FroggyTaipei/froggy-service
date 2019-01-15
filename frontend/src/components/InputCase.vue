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
        name="caseSubject"
        id="caseSubject"
        class="form-control col-sm-10"
        placeholder="請輸入案件主旨"
        v-validate="'required|max:20'"
        v-model.trim="cases.title">
        <div class="col-sm-12 invalid-feedback">
            {{ errors.first('caseSubject') }}
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
        name="caseContent"
        id="caseContent"
        class="form-control col-sm-10"
        placeholder="請輸入案件內容"
        v-validate="'required|max:150'"
        v-model.trim="cases.content" />
        <div class="col-sm-12 invalid-feedback">
            {{ errors.first('caseContent') }}
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
        name="location"
        id="location"
        class="form-control col-sm-10"
        placeholder="e.g. 信義路三段"
        v-validate="'required|max:20'"
        v-model.trim="cases.location">
        <div class="col-sm-12 invalid-feedback">
            {{ errors.first('location') }}
        </div>
    </div>
    <div class="form-row">
        <label
            for="fileUpload"
            class="col-sm-2 col-form-label">
            上傳附件
        </label>
        <div class="custom-file col-sm-10">
            <input
            ref="file"
            type="file"
            class="custom-file-input input-style"
            id="fileUpload">
            <label
            class="custom-file-label"
            for="fileUpload" />
        </div>
    </div>
    <div class="form-group row">
        <div class="col-md-10  offset-md-2 file">
            <button type="button" class="btn btn-primary">
            Notifications <span class="badge">Ｘ</span>
            </button>
        </div>
        <div class="col-md-10  offset-md-2 file">
            <button type="button" class="btn btn-primary">
            Notifications <span class="badge">Ｘ</span>
            </button>
        </div>

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
export default {
  name: 'InputCase',
  created () {
    this.cases.uuid = this.$uuid.v1()
  },
  data: () => ({
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
    completeCaseData () {
      this.$validator.validateAll().then((result) => {
        if (result) {
          this.$store.commit('setCase', this.cases)
          this.$emit('next')
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
