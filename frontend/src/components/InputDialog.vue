<template>
  <div class="container panel">
    <!-- MultiStep Form -->
    <div class="row">
      <div class="col-md-12 col-md-offset-6">
        <div id="msform">
          <!-- progressbar -->
          <ul id="progressbar">
            <li
              v-for="item in steps"
              :key="item.step"
              :class="{active: item.step <= step}"
              @click="checkStep(item)">
              {{ item.text }}
            </li>
          </ul>
          <!-- fieldsets -->
          <!-- Page one -->
          <fieldset v-show="step == 0">
            <h2 class="fs-title">
              Personal Details
            </h2>
            <h3 class="fs-subtitle">
              Tell us something more about you
            </h3>
            <div class="container">
              <div class="row">
                <div
                  v-for="item in categories"
                  :key="item.index"
                  class="col-md-3"
                  @click="selectCaseType(item.text)">
                  <div
                    class="col-md-12 categories-item"
                    :style="{ 'background-color': item.color }">
                    {{ item.text }}
                  </div>
                </div>
              </div>
            </div>
          </fieldset>
          <!-- Page two -->
          <fieldset v-show="step == 1">
            <h2 class="fs-title">
              Social Profiles
            </h2>
            <h3 class="fs-subtitle">
              Your presence on the social network
            </h3>
            <div class="form-inline row">
              <label
                for="caseSubject"
                class="col-sm-2 col-form-label">
                案件主旨
              </label>
              <div class="col-sm-10">
                <input
                  type="text"
                  name="caseSubject"
                  id="caseSubject"
                  placeholder="請輸入案件主旨">
              </div>
            </div>
            <div class="form-inline row">
              <label
                for="caseContent"
                class="col-sm-2 col-form-label">
                案件內容
              </label>
              <div class="col-sm-10">
                <textarea
                  class="form-control"
                  rows="5"
                  id="caseContent"
                  placeholder="請輸入案件內容" />
              </div>
            </div>
            <div class="form-group row">
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
              @click="previous">
            <input
              type="button"
              name="next"
              class="next action-button"
              value="Next"
              @click="next">
          </fieldset>
          <!-- Page three -->
          <InputUserInfo
            v-show="step == 2"
            :next="next"
            :previous="previous" />
        </div>
      </div>
    </div>
    <!-- /.MultiStep Form -->
  </div>
</template>

<script>
import InputUserInfo from './InputUserInfo.vue'
export default {
  name: 'InputDialog',
  components: {
    InputUserInfo
  },
  data: () => ({
    step: 0,
    countryCode: '+886',
    phoneNumber: '0938926812',
    steps: [
      { step: 0, text: '選擇案件分類', active: true, complete: false },
      { step: 1, text: '輸入案件內容', active: false, complete: false },
      { step: 2, text: '輸入個人資料', active: false, complete: false }
    ],
    categories: [
      { index: 0, text: '交通運輸', color: '#FD8D95' },
      { index: 1, text: '公共設施', color: '#CAABA4' },
      { index: 2, text: '衛福勞動', color: '#60B9D5' },
      { index: 3, text: '文教科技', color: '#52C59A' },
      { index: 4, text: '環境建管', color: '#79AAD3' },
      { index: 5, text: '警消政風', color: '#D5B272' },
      { index: 6, text: '市政議題', color: '#FEB28c' },
      { index: 7, text: '其他服務', color: '#949FCC' }
    ],
    header: { Authorization: 'Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b' },
    regions: []
  }),
  created () {
    console.log('input dialog init')
    this.getRegion()
  },
  methods: {
    getRegion () {
      return this.axios.get('/api/regions')
        .then(response => { this.regions = response.data })
        .catch(e => { console.log(e) })
    },
    getType () {
      return this.axios.get('/api/types')
        .then(response => { this.types = response.data })
        .catch(e => { console.log(e) })
    },
    selectCaseType (type) {
      console.log(type)
      this.next()
    },
    next () {
      if (this.step < 3) {
        this.step += 1
        console.log('go to page', this.step)
      }
    },
    previous () {
      if (this.step > 0) {
        this.step -= 1
        console.log('go to previous page')
      }
    },
    checkStep (steps) {
      if (steps.complete) {
        this.step = steps.step
      }
    }
  }
}
</script>

<style lang="css">
/*custom font*/
@import url(https://fonts.googleapis.com/css?family=Montserrat);

/*basic reset*/

* {
  margin: 0;
  padding: 0;
}

.panel {
  border: 5px solid red;
  border-radius: 10px;
  padding: 16px;
}
.row {
  justify-content: center;
}
body {
    font-family: montserrat, arial, verdana;
    background: transparent;
}

/*form styles*/
#msform {
    text-align: center;
    position: relative;
    margin-top: 30px;
}

#msform fieldset {
    background: white;
    border: 0 none;
    border-radius: 0px;
    padding: 20px 30px;
    box-sizing: border-box;
    width: 80%;
    margin: 0 10%;

    /*stacking fieldsets above each other*/
    position: relative;
}

#msform input[type="text"], #msform textarea {
    padding: 15px;
    border-radius: 0px;
    margin-bottom: 10px;
    width: 100%;
    box-sizing: border-box;
    font-family: montserrat;
    color: #2C3E50;
    font-size: 13px;
}

#msform .custom-file-label {
  border: 1px solid #ccc;
  border-radius: 0px !important;
  margin-left: 15px;
  margin-right: 15px;
}

#msform .custom-file-label::after {
  content: "＋"
}

#msform .categories-item {
  margin-bottom: 30px;
  height: 175px;
}

#msform .form-group--error input[type="text"], #msform .form-group--error textarea {
  border-color: #dc3545;
}

 #msform .form-group--error input:focus {
  outline-color: #dc3545;
 }

#msform .form-group--error .error {
  color: #28a745;
}

/*buttons*/
#msform .action-button {
    width: 100px;
    background: #ee0979;
    font-weight: bold;
    color: white;
    border: 0 none;
    border-radius: 25px;
    cursor: pointer;
    padding: 10px 5px;
    margin: 10px 5px;
}

#msform .action-button:hover, #msform .action-button:focus {
    box-shadow: 0 0 0 2px white, 0 0 0 3px #ee0979;
}

#msform .action-button-previous {
    width: 100px;
    background: #C5C5F1;
    font-weight: bold;
    color: black;
    border: 0 none;
    border-radius: 25px;
    cursor: pointer;
    padding: 10px 5px;
    margin: 10px 5px;
}

#msform .action-button-previous:hover, #msform .action-button-previous:focus {
    box-shadow: 0 0 0 2px white, 0 0 0 3px #C5C5F1;
}

.file button {
  width: 100%;
}

/*headings*/
.fs-title {
    font-size: 18px;
    text-transform: uppercase;
    color: #2C3E50;
    margin-bottom: 10px;
    letter-spacing: 2px;
    font-weight: bold;
}

.fs-subtitle {
    font-weight: normal;
    font-size: 13px;
    color: #666;
    margin-bottom: 20px;
}

/*progressbar*/
#progressbar {
    margin-bottom: 30px;
    overflow: hidden;
    /*CSS counters to number the steps*/
    counter-reset: step;
}

#progressbar li {
    list-style-type: none;
    color: black;
    text-transform: uppercase;
    font-size: 9px;
    width: 33%;
    float: left;
    position: relative;
    letter-spacing: 1px;
}

#progressbar li:before {
    content: counter(step);
    counter-increment: step;
    width: 24px;
    height: 24px;
    line-height: 26px;
    display: block;
    font-size: 12px;
    color: #333;
    background: #dfe3e4;
    border-radius: 25px;
    margin: 0 auto 10px auto;
}

/*progressbar connectors*/
#progressbar li:after {
    content: '';
    width: 100%;
    height: 2px;
    background: #dfe3e4;
    position: absolute;
    left: -50%;
    top: 9px;
    z-index: -1; /*put it behind the numbers*/
}

#progressbar li:first-child:after {
    /*connector not needed before the first step*/
    content: none;
}

/*marking active/completed steps green*/
/*The number of the step and the connector before it = green*/
#progressbar li.active:before, #progressbar li.active:after {
    background: #ee0979;
    color: white;
}

</style>
