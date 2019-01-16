<template>
  <div class="container panel">
    <button type="button" class="close" aria-label="Close" @click="closeInput">
      <span aria-hidden="true">×</span>
    </button>
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
            <div class="container">
              <div class="row">
                <div
                  v-for="item in $store.state.types"
                  :key="item.index"
                  class="col-md-3 col-sm-6 col-xs-6"
                  @click="selectCaseType(item.id)">
                  <div
                    class="col-12 categories-item"
                    :style="{ 'background-color': categories[item.id-1].color }">
                    {{ item.name }}
                  </div>
                </div>
              </div>
            </div>
          </fieldset>
          <!-- Page two -->
          <InputCase
            v-show="step == 1"
            @next="next"
            @previous="previous"
            :isClose="isClose"/>
          <!-- Page three -->
          <InputUserInfo
            v-show="step == 2"
            @previous="previous"
            :isClose="isClose"/>
        </div>
      </div>
    </div>
    <!-- /.MultiStep Form -->
  </div>
</template>

<script>
import InputUserInfo from './InputUserInfo.vue'
import InputCase from './InputCase.vue'
export default {
  name: 'InputDialog',
  components: {
    InputUserInfo,
    InputCase
  },
  data: () => ({
    step: 0,
    isClose: false,
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
    ]
  }),
  created () {
    console.log('input dialog init')
    this.$store.dispatch('getRegionsList')
    this.$store.dispatch('getTypeList')
  },
  methods: {
    closeInput () {
      this.step = 0
      this.isClose = true
      this.$emit('closeInput')
    },
    selectCaseType (type) {
      this.$store.commit('setCase', { type: type })
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
  overflow-y: auto;
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

.container .input-close {
    position: absolute;
    z-index: 999;
    right: 20px;
}

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
