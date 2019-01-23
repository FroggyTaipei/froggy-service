<template>
  <el-container style="height:100%">
    <!-- Page one -->
    <el-row type="flex" class="panel category-page" v-show="step == 0">
      <transition name="page" @after-leave="categoryAfterLeave">
        <div v-show="category.background" class="bg-unit bg-deco"></div>
      </transition>
      <div class="category-content">
        <el-row type="flex" class="category-content-row1">
          <el-col :xs="24" :sm="12">
            <transition name="person-slide-fade">
              <img v-show="category.interface" class="category-content-namebar" src="https://storage.googleapis.com/froggy-service/frontend/images/dialog/category/namebar.png">
            </transition>
          </el-col>
          <el-col :sm="12" class="hidden-xs-only">
          </el-col>
        </el-row>
        <el-row type="flex" justify="center" class="category-content-row2">
            <el-col :sm="12" class="hidden-xs-only category-content-person">
              <transition name="person-slide-fade">
                <img v-show="category.avatar" src="https://storage.googleapis.com/froggy-service/frontend/images/dialog/category/person.png">
              </transition>
            </el-col>
            <el-col :xs="24" :sm="12">
              <transition name="froggy-slide-fade">
                <img v-show="category.avatar" class="category-content-center category-content-froggy" :src="this.images.froggy">
              </transition>
              <transition name="froggy-slide-fade">
                <img v-show="category.interface" class="category-content-progress" src="https://storage.googleapis.com/froggy-service/frontend/images/dialog/category/progress.png">
              </transition>
            </el-col>
        </el-row>
      </div>
      <transition name="person-slide-fade">
        <el-row v-show="category.interface" type="flex" class="category-footer">
          <el-col :span="15" style="margin-right:5px;" class="hidden-xs-only">
            <el-row class="category-footer-row">
              <el-col
                :span="6"
                v-for="item in $store.state.types"
                :key="item.id">
                <div class="category-item">
                  <div
                    class="category-btn"
                    @click="selectCaseType(item)">
                    {{ item.name }}
                  </div>
                  <div class="category-icon">
                    <i class="el-icon-caret-right"></i>
                  </div>
                </div>
              </el-col>
            </el-row>
          </el-col>
          <el-col :xs="24" :span="10">
            <div class="hidden-xs-only category-footer-row">
            <el-row>
              <el-col :span="12">
                <div class="category-item">
                  <div class="category-btn">
                    -
                  </div>
                </div>
              </el-col>
               <el-col :span="12">
                <div class="category-item">
                  <div class="category-btn">
                    -
                  </div>
                </div>
              </el-col>
            </el-row>
            <el-row>
              <el-col :span="12">
                <div class="category-item">
                  <div class="category-btn">
                    -
                  </div>
                </div>
              </el-col>
               <el-col :span="12">
                <div class="category-item">
                  <div class="category-btn"
                    @click="back">
                    回首頁
                  </div>
                  <div class="arrow-icon">
                    <i class="el-icon-caret-right"></i>
                  </div>
                </div>
              </el-col>
            </el-row>
            </div>
            <div class="hidden-sm-and-up category-footer-mobile">
              <select v-model="selected">
                <option disabled value="">請選擇類別</option>
                <option
                  v-for="item in $store.state.types"
                  :key="item.id"
                  :value="item"
                  :label="item.name"></option>
              </select>
            </div>
          </el-col>
        </el-row>
      </transition>
      <div class="back-btn hidden-sm-and-up">
        <el-button type="info" icon="el-icon-circle-close" circle @click="back"></el-button>
      </div>
      <transition name="screen-slide-left" @after-leave="screenAfterLeave">
        <div v-if="screenActive" class="screen screen1"></div>
      </transition>
      <transition name="screen-slide-right">
        <div v-if="screenActive" class="screen screen2"></div>
      </transition>
    </el-row>
    <el-row type="flex" class="panel form-page" :gutter="10" v-show="step > 0">
      <div class="bg-unit bg-logo"></div>
      <el-col :span="12" class="col1 hidden-xs-only">
        <el-container>
          <transition name="person-slide-fade" @after-leave="formAfterLeave">
            <div v-show="form.interface" class="footer">
              <img style="width:90%" :src="this.images.froggy" >
              <transition name="fade" mode="in-out">
                <img key="33" v-if="progressState" class="progress-bar" src="https://storage.googleapis.com/froggy-service/frontend/images/dialog/input/progress33.png" >
                <img key="66" v-else class="progress-bar" src="https://storage.googleapis.com/froggy-service/frontend/images/dialog/input/progress66.png" >
              </transition>
            </div>
          </transition>
        </el-container>
      </el-col>
      <el-col :xs="24" :span="12" class="col2">
        <transition name="froggy-slide-fade">
          <div v-show="form.interface" class="input-dialog">
            <!-- Page two -->
            <InputUserInfo
              v-show="step == 1"
              @next="next"
              @showAgreement="showAgreementDialog"
              @previous="formLeaveAnimation"
              :dialogAgreement="agreement"/>
            <!-- Page three -->
            <InputCase
              v-show="step == 2"
              @previous="previous"/>
          </div>
        </transition>
      </el-col>
      <el-dialog
        title="提示"
        :visible.sync="agreementDialogVisible"
        width="30%"
        @close="makeDisagree()"
        center>
        <span>需要注意的是内容是默认不居中的</span>
        <span slot="footer" class="dialog-footer">
          <el-button @click="agreementDialogVisible=false">不同意</el-button>
          <el-button type="success" @click="makeAgree()">同意</el-button>
        </span>
      </el-dialog>
    </el-row>
  </el-container>
</template>

<script>
import InputUserInfo from '@/components/InputUserInfo.vue'
import InputCase from '@/components/InputCase.vue'
export default {
  name: 'InputDialog',
  components: {
    InputUserInfo,
    InputCase
  },
  data: () => ({
    step: 0,
    isClose: false,
    progressState: true,
    agreement: true,
    agreeClicked: true,
    agreementDialogVisible: false,
    transitionState: false,
    category: {
      background: true,
      avatar: false,
      interface: true
    },
    form: {
      background: false,
      interface: false
    },
    images: {
      froggy: ''
    },
    froggyImage: ['morning_2.png', 'noon_2.png', 'night_3.png'],
    screenActive: true,
    selected: ''
  }),
  watch: {
    selected: function (value) {
      if (value) {
        this.selectCaseType(value)
      }
    }
  },
  created () {
    console.log('input dialog init')
    if (this.$store.state.currentTime === '') {
      this.back()
    } else {
      this.images.froggy = this.$store.state.storageDomain + 'froggy/' + this.froggyImage[this.$store.state.currentTime]
    }
    if (this.$store.state.types.length === 0 && this.$store.state.regions.length === 0) {
      this.$store.dispatch('getRegionsList')
      this.$store.dispatch('getTypeList')
    }
  },
  mounted () {
    console.log('input dialog mounted')
    setTimeout(() => {
      this.screenActive = false
    }, 500)
  },
  methods: {
    screenAfterLeave () {
      // show category avatar
      setTimeout(() => {
        this.categoryAvatarAnimation()
      }, 300)
    },
    categoryAfterLeave () {
      // when category background animation finished
      // transitionState, true: p2>p1, false: p1>p2
      if (this.transitionState) {
        console.log('page 2 to page 1')
      } else {
        this.next()
        setTimeout(() => {
          this.formInterfaceAnimation()
        }, 100)
      }
    },
    formAfterLeave () {
      // when form background animation finished
      // transitionState, true: p2>p1, false: p1>p2
      if (this.transitionState) {
        this.previous()
        this.categoryBackgroundAnimation()
        setTimeout(() => {
          this.categoryAvatarAnimation()
          this.categoryInterfaceAnimation()
        }, 500)
      } else {
        console.log('page 1 to page 2')
      }
    },
    categoryBackgroundAnimation () {
      this.category.background = !this.category.background
    },
    categoryAvatarAnimation () {
      this.category.avatar = !this.category.avatar
    },
    categoryInterfaceAnimation () {
      this.category.interface = !this.category.interface
    },
    formBackgroundAnimation () {
      this.form.background = !this.form.background
    },
    formInterfaceAnimation () {
      this.form.interface = !this.form.interface
    },
    formLeaveAnimation () {
      this.transitionState = true
      this.formInterfaceAnimation()
      setTimeout(() => {
        this.formBackgroundAnimation()
      }, 300)
    },
    closeInput () {
      this.step = 0
      this.isClose = true
      this.$emit('closeInput')
    },
    selectCaseType (type) {
      let typeText = '您選擇的類別是：' + type.name
      this.$store.commit('setCase', { type: type.id })
      this.$store.commit('setTypeText', typeText)
      // avatar and interface leave first, then background disappear
      this.transitionState = false
      this.categoryAvatarAnimation()
      this.categoryInterfaceAnimation()
      setTimeout(() => {
        this.categoryBackgroundAnimation()
      }, 500)
    },
    makeAgree () {
      this.agreement = true
      this.agreeClicked = true
      this.agreementDialogVisible = false
    },
    makeDisagree () {
      if (!this.agreeClicked) {
        this.agreement = false
      }
    },
    showAgreementDialog () {
      this.agreement = true
      this.agreeClicked = false
      this.agreementDialogVisible = true
    },
    next () {
      if (this.step < 3) {
        this.step += 1
        console.log('go to page', this.step)
        if (this.step === 2) {
          this.progressState = false
        }
      }
    },
    previous () {
      if (this.step > 0) {
        console.log('go to previous page')
        this.step -= 1
        if (this.step === 1) {
          this.progressState = true
        }
      }
    },
    back () {
      this.$router.push('/')
    }
  }
}
</script>

<style lang="css" scoped>
.panel {
    background-repeat: no-repeat;
    background-size: 100% auto;
    position: relative;
    width: -webkit-fill-available;
}
/* Category page */
.category-page {
  background-image: linear-gradient(#EFCACD, #DE8F95, #C480A2, #B69FC6, #A2CEE5, #FFFFFF);
  flex-direction: column;
}
.category-page > div {
  display: flex;
}
.screen {
  position: absolute;
  top: 0px;
  height: 100%;
  width: 100%;
}
.screen1 {
  background:repeating-linear-gradient(0deg, rgb(0, 0, 0) 0%, rgb(0, 0, 0) 10%, transparent 10%, transparent 20%);
}
.screen2 {
  background:repeating-linear-gradient(0deg, transparent 0%, transparent 10%, rgb(0, 0, 0) 10%, rgb(0, 0, 0) 20%);
}
.category-content {
  flex: 4;
  flex-direction: column;
  width: 90%;
  margin: auto;
}
.category-content > div.el-row {
  flex: 1;
}

.category-content-row2 > div.el-col {
  position: relative;
}

.category-content-row2 > div.el-col img {
  position: absolute;
  bottom: 0px

}

.category-content-center {
  margin: auto;
  left: 0;
  right: 0;

}

.category-content-person > img {
  width: 40vw;
  bottom: -5vmax !important;
  right: 2vw;
}

.category-content-froggy {
  height: 35vw;
}

.category-content-progress {
  width: 40vmax;
}

.category-content-namebar {
  width: 40vmax;
  margin-top: 5vh;
  margin-left: 8vw;
}

.category-footer {
    width: 100%;
    position: relative;
    flex-direction: row;
    align-self: flex-end;
    flex: 1;
    background-color: rgba(0,0,0,0.5);
    padding: 10px;
}
.category-footer-row {
    position: relative;
    top: 50%;
    transform: translateY(-50%);
}
.category-footer > .el-col {
    border: solid 10px #5f5f5f;
    border-radius: 16px;
    padding: 5px;
    background-color: rgba(255,255,255,0.8);
}
.category-item {
  height: 100%;
  margin-top: 1vh;
  display: flex;
  flex-direction: row-reverse;
  position: relative;
}
.category-item > div {
  display: flex;
}
.arrow-icon {
  left: 2vw;
  position: absolute;
  font-size: 4vw;
  color: transparent;
}
.category-icon {
  flex: 1;
  font-size: 4vw;
  align-self: center;
  color: transparent;
  margin-right: -1.5vw
}
.category-btn {
  flex: 4;
  justify-content: center;
  align-items: center;
  font-size: 2.5vw;
  font-weight: 600;
  cursor: pointer;
}
div.category-btn:hover + div {
  color: black;
}
.back-btn {
  position: fixed;
}
.bg-unit {
  position: absolute;
  top: 0;
  left: 0px;
  right: 0px;
  height: 100%;
}
.bg-deco {
  background:repeating-linear-gradient(0, rgba(255, 255, 255, 0.52) 0%, rgba(255, 255, 255, 0.53) 0.5%, rgba(0, 0, 0, 0) 0.5%, rgba(0, 0, 0, 0) 3%);
}
.bg-logo {
  opacity: 0.5;
  text-align: center;
  background-image: url("https://storage.googleapis.com/froggy-service/frontend/images/dialog/input/logo.png");
  background-repeat: no-repeat;
  background-size: 100% auto;
  background-position: center;
}
select {
    -webkit-appearance: none;
    -moz-appearance: none;
    text-indent: 1px;
    text-overflow: '';
    font-size: 2.5rem;
    font-weight: bold;
    border: transparent;
}
.category-footer-mobile {
  display: flex;
  justify-content: center;
  height: 100%;
}
/* Input page */
.form-page {
  background-image: linear-gradient(#EFCACD, #DE8F95, #C480A2, #B69FC6, #A2CEE5, #FFFFFF);
}
.input-dialog {
  height: fill-available;
  z-index: 999;
  opacity: 0.9;
  border: 1px solid transparent;
  border-radius: 10px;
  background-color: rgba(236, 148, 156, 0.9);
  padding: 16px;
  max-width: 80%;
}
.input-dialog > fieldset {
  overflow-y: auto;
  max-height: -webkit-fill-available;
  border-color: transparent;
  position: relative;
}
.col1 .el-container {
  height: 100%
}
.col1 .el-main {
  padding: 0px
}
.footer {
  height: 100%;
  width: 100%;
  position: relative;
}
.footer img{
  width: 80%;
  position: absolute;
  bottom: 0px;
  right: 0;
}
.col2 {
  padding: 5vh 0;
}
.progress-bar {
  margin-bottom:5vh;
  margin-right:2vw;
}
/* Animations */
.froggy-slide-fade-enter-active, .person-slide-fade-enter-active {
  transition: all .5s ease;
  /* Enable hardware acceleration to fix laggy transitions */
  -webkit-transform: translateZ(0);
  -moz-transform: translateZ(0);
  -ms-transform: translateZ(0);
  -o-transform: translateZ(0);
  transform: translateZ(0);
}
.froggy-slide-fade-leave-active, .person-slide-fade-leave-active {
  transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.froggy-slide-fade-enter, .froggy-slide-fade-leave-to {
  transform: translateX(10%);
  opacity: 0;
}
.person-slide-fade-enter, .person-slide-fade-leave-to {
  transform: translateX(-10%);
  opacity: 0;
}
.screen-slide-left-active, .screen-slide-left-leave-active, .screen-slide-right-active, .screen-slide-right-leave-active {
  transition: all 1s ease-in;
}
.screen-slide-left-leave-to {
  transform: translateX(-100%);
}
.screen-slide-right-leave-to {
  transform: translateX(100%);
}
.page-enter-active, .page-leave-active {
  transition: opacity .5s;
}
.page-enter, .page-leave-to {
  opacity: 0;
}
.progress-fade-enter-active, .progress-fade-leave-active {
  transition: opacity 0.5s ease;
}
.progress-fade-enter, .progress-fade-leave-to {
  opacity: 0;
}
/* RWD */
@media only screen and (max-width: 768px) {
  .col2 {
    padding: 1vh 1vw
  }
  .input-dialog {
    margin: auto;
    max-width: 90%;
  }
  .category-content-namebar {
    margin-left: 0px;
  }
  .category-content-froggy {
    width: unset;
    height: 150%;
    left: 25%;
    -webkit-transform: translateX(-50%);
    transform: translateX(-25%);
  }
}
</style>
