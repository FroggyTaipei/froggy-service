<template>
  <el-container style="height:100%">
    <!-- Page one -->
    <el-row type="flex" class="panel category-page" v-show="step == 0">
      <transition name="page" @after-leave="categoryAfterLeave">
        <div v-show="category.background" class="bg-unit bg-logo"></div>
      </transition>
      <div class="category-content hidden-xs-only">
        <el-row type="flex" class="category-content-row1">
          <el-col :xs="24" :sm="12">
            <transition name="person-slide-fade">
              <img v-show="category.interface" class="category-content-namebar category-content-progress" src="https://storage.googleapis.com/froggy-service/frontend/images/dialog/category/namebar.png">
            </transition>
          </el-col>
          <el-col :sm="12">
          </el-col>
        </el-row>
        <el-row type="flex" justify="center" class="category-content-row2">
            <el-col :sm="12" class="category-content-person">
              <transition name="person-slide-fade">
                <img v-show="category.avatar" src="https://storage.googleapis.com/froggy-service/frontend/images/dialog/category/person.png">
              </transition>
            </el-col>
            <el-col :xs="24" :sm="12">
              <transition name="froggy-slide-fade">
                <div v-show="category.avatar"  class="category-content-center">
                  <img class="category-content-froggy-bottom" :src="this.images.FROGGY_BOTTOM">
                  <img class="category-content-froggy normal-froggy" v-show="!hitted&&!waving" :src="this.images.FROGGY">
                  <img class="category-content-froggy flip" v-show="hitted" :src="this.images.FROGGY_HITTED">
                  <img class="category-content-froggy" v-show="waving" src="https://storage.googleapis.com/froggy-service/frontend/assets/froggy_wave.gif">
                </div>
              </transition>
              <transition name="froggy-slide-fade">
                <img v-show="category.interface" class="category-content-progress" src="https://storage.googleapis.com/froggy-service/frontend/images/dialog/category/progress.png">
              </transition>
            </el-col>
        </el-row>
        <div class="bouncing-ball" :class="{ 'feeding-animation' : feeding }" v-show="feeding"></div>
        <transition name="screen-slide-left" @after-leave="screenAfterLeave">
          <div v-if="screenActive" class="screen screen1 hidden-xs-only"></div>
        </transition>
        <transition name="screen-slide-right">
          <div v-if="screenActive" class="screen screen2 hidden-xs-only"></div>
        </transition>
      </div>
      <!-- 下方 footer -->
      <transition name="person-slide-fade">
        <el-row v-show="category.interface" class="row-dialog category-footer hidden-xs-only" type="flex" align="middle" justify="center" style="height:100%">
          <el-col class="bottom-dialog-wrapper">
            <transition name="fade">
              <div v-show="category.footer" class="bottom-dialog-right left-actually">
                  <span class="bottom-dialog-options" @click="selectCaseType(item.id)" v-for="item in $store.state.types" :key="item.id">
                    <a>{{ item.name }}</a>
                    <div class="arrow-icon">
                      <i class="el-icon-caret-right"></i>
                    </div>
                  </span>
              </div>
            </transition>
            <transition name="fade">
              <div v-show="category.footer" class="bottom-dialog-right">
                <span class="bottom-dialog-options">
                  <a>-</a>
                  <div class="arrow-icon">
                    <i class="el-icon-caret-right" style="color: transparent;"></i>
                  </div>
                </span>
                <span class="bottom-dialog-options" @mouseenter="froggyWave(true)" @mouseleave="froggyWave(false)">
                  <a v-show="!waving">-</a>
                  <a v-show="waving">High起來！</a>
                  <div class="arrow-icon">
                    <i class="el-icon-caret-right" style="color: transparent;"></i>
                  </div>
                </span>
                <span class="bottom-dialog-options" @click="feedFroggy" id="feed">
                  <a class="normal-text">-</a>
                  <a class="color-egg" style="display: none;">餵食</a>
                  <div class="arrow-icon">
                    <i class="el-icon-caret-right"></i>
                  </div>
                </span>
                <span class="bottom-dialog-options" @click="categoryOutAnimation(true)">
                  <a>回首頁</a>
                  <div class="arrow-icon">
                    <i class="el-icon-caret-right"></i>
                  </div>
                </span>
              </div>
            </transition>
          </el-col>
          <el-col class="footer hidden-xs-only">
            <span>
            「選服魔鏡號」台北市議員邱威傑市民服務系統
             110 台北市信義區仁愛路四段507號 台北市議會 752研究室<br>
             02-27297708 分機 7152、7252&nbsp;
             <a href="mailto:servant@65535studio.com">servant@65535studio.com</a>&nbsp;
             <a href="https://github.com/FroggyTaipei/froggy-service" class="githubLink" target="_blank">
              <font-awesome-icon :icon="['fab', 'github']"></font-awesome-icon>
              <span>「選服魔鏡號」GitHub 專案</span>
             </a>
            </span>
          </el-col>
        </el-row>

      </transition>
      <div class="mobile-title hidden-sm-and-up">
        <div class="back-btn" @click="back">
          <font-awesome-icon icon="home" />
        </div>
        <h2>
          選擇類別
        </h2>
      </div>

      <transition name="froggy-slide-fade">
        <div v-show="category.avatar" class="mobile-content hidden-sm-and-up">
          <div class="mobile-category-select">
            <div class="mobile-category-button" v-for="item in $store.state.types" :key="item.id" @click="selectCaseType(item.id)">
              <button type="button">{{ item.name }}</button>
            </div>
          </div>
        </div>
      </transition>
    </el-row>
    <el-row type="flex" class="panel form-page" :gutter="10" v-show="step > 0">
      <div class="bg-unit bg-logo"></div>
      <el-col :span="12" class="col1 hidden-xs-only">
        <el-container>
          <transition name="person-slide-fade" @after-leave="formAfterLeave">
            <div v-show="form.interface" class="form-footer">
              <img style="width:55%;right:6vw;" :class="{ 'validate-error-animation' : validateFail }" :src="this.images.FROGGY" >
              <transition name="fade" mode="in-out">
                <img key="33" v-if="progressState" class="progress-bar" src="https://storage.googleapis.com/froggy-service/frontend/images/dialog/input/progress33.png" >
                <img key="66" v-else class="progress-bar" src="https://storage.googleapis.com/froggy-service/frontend/images/dialog/input/progress66.png" >
              </transition>
            </div>
          </transition>
        </el-container>
      </el-col>
      <el-col :xs="24" :span="12" class="col2">
        <div class="mobile-title hidden-sm-and-up">
          <div class="back-btn" @click="back">
            <font-awesome-icon icon="home" />
          </div>
          <h2>
            您的資料
          </h2>
        </div>
        <transition name="froggy-slide-fade">
          <div v-show="form.interface" class="input-dialog mobile-content">
            <!-- Page two -->
            <InputUserInfo
              v-show="step == 1"
              :selectedType="selectedType"
              @next="next"
              @previous="formLeaveAnimation"
              @validateFail="validateErrorAnimation"/>
            <!-- Page three -->
            <InputCase
              v-show="step == 2"
              :selectedType="selectedType"
              @previous="previous"
              @validateFail="validateErrorAnimation"/>
          </div>
        </transition>
      </el-col>
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
    hitted: false,
    waving: false,
    isClose: false,
    validateFail: false,
    progressState: true,
    transitionState: false,
    feeding: false,
    category: {
      background: true,
      avatar: false,
      interface: true,
      footer: false
    },
    form: {
      background: false,
      interface: false
    },
    images: {
      FROGGY: '',
      FROGGY_BOTTOM: '',
      FROGGY_HITTED: ''
    },
    screenActive: true,
    selectedType: ''
  }),
  created () {
    if (this.$store.state.currentTime === '') {
      this.back()
    } else {
      this.images.FROGGY = this.$store.state.storageDomain + 'froggy/froggyForm.png'
      this.images.FROGGY_BOTTOM = this.$store.state.storageDomain + 'dialog/category/froggy_bottom.png'
      this.images.FROGGY_HITTED = this.$store.state.storageDomain + 'froggy/froggyForm_hitted.png'
    }
    // clear stroe
    this.$store.commit('setCase', {})
    this.$store.commit('setAuthenticated', false)
    this.$store.commit('setJWT', {})
  },
  mounted () {
    if (this.$store.state.isMobile) {
      this.categoryAvatarAnimation()
    } else {
      setTimeout(() => {
        this.screenActive = false
      }, 500)
    }
    this.category.footer = true
  },
  methods: {
    froggyWave (value) {
      if (!this.feeding) {
        this.waving = value
      }
    },
    validateErrorAnimation () {
      this.validateFail = true
      setTimeout(() => {
        this.validateFail = false
      }, 1500)
    },
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
        this.back()
      } else {
        var sec = this.$store.state.isMobile ? 0 : 100
        this.next()
        setTimeout(() => {
          this.formInterfaceAnimation()
        }, sec)
      }
    },
    formAfterLeave () {
      // when form background animation finished
      // transitionState, true: p2>p1, false: p1>p2
      if (this.transitionState) {
        var sec = this.$store.state.isMobile ? 0 : 500
        this.previous()
        this.categoryBackgroundAnimation()
        setTimeout(() => {
          this.categoryAvatarAnimation()
          this.categoryInterfaceAnimation()
        }, sec)
      } else {
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
      var sec = this.$store.state.isMobile ? 0 : 300
      this.transitionState = true
      this.formInterfaceAnimation()
      setTimeout(() => {
        this.formBackgroundAnimation()
      }, sec)
    },
    closeInput () {
      this.step = 0
      this.isClose = true
      this.$emit('closeInput')
    },
    selectCaseType (type) {
      this.selectedType = type
      this.$store.commit('setCase', { type: type })
      // avatar and interface leave first, then background disappear
      this.categoryOutAnimation(false)
    },
    categoryOutAnimation (state) {
      var sec = this.$store.state.isMobile ? 0 : 500
      this.transitionState = state
      this.categoryAvatarAnimation()
      this.categoryInterfaceAnimation()
      setTimeout(() => {
        this.categoryBackgroundAnimation()
      }, sec)
    },
    feedFroggy () {
      if (!this.feeding) {
        this.feeding = true
        setTimeout(() => {
          this.hitted = true
        }, 1500)
        setTimeout(() => {
          this.hitted = false
        }, 2000)
        setTimeout(() => {
          this.feeding = false
        }, 1800)
      }
    },
    next () {
      if (this.step < 3) {
        this.step += 1
        if (this.step === 2) {
          this.progressState = false
        }
      }
    },
    previous () {
      if (this.step > 0) {
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
    width: stretch;
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
  position: fixed;
  top: 0px;
  left: 0px;
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
  position: relative;
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
  position: absolute;
  bottom: 20vh;
  margin: auto;
  left: 0;
  right: 0;
}

.category-content-center > img {
  margin: auto;
  left: 0;
  right: 0;
}

.category-content-froggy {
  height: 25vmax;
  bottom: 3vmax !important;
  -webkit-mask-image: -webkit-gradient(linear, left 90%, left bottom, from(rgba(0,0,0,1)), to(rgba(0,0,0,0)));
}

.category-content-froggy-bottom {
  width: 85%;
}

.flip {
  -webkit-transform: scaleX(-1);
  transform: scaleX(-1);
}

.category-content-person > img {
  width: 40vw;
  bottom: -4vmax !important;
  right: 2vw;
}

.category-content-progress {
  width: 90%;
}

.category-content-namebar {
  margin-top: 6vh;
  margin-left: 8vw;
}

.category-footer {
  flex: 1;
}

.left-actually > .bottom-dialog-options {
  flex-basis: calc(25%) !important;
}

.left-actually {
  flex: 3;
  margin-right: 5px;
}

.bottom-dialog-options:hover > a.normal-text {
  display: none;
}
.bottom-dialog-options:hover > a.color-egg {
  cursor: pointer;
  display: block !important;
}

.back-btn {
  margin: 2vh;
  position: absolute;
  background-color: rgba(0, 0, 0, 0.5);
  min-width: 6vmax;
  min-height: 6vmax;
  border-radius: 5px;
  text-align: center;
  display: flex;
}
.back-btn > svg {
  color: white;
  font-size: 4vmax;
  margin: auto;
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
  opacity: 0.3;
  text-align: center;
  background-image: url("https://storage.googleapis.com/froggy-service/frontend/images/dialog/input/logo.png");
  background-repeat: no-repeat;
  background-size: 100% auto;
  background-position: center;
}
/* Input page */
.form-page {
  background-image: linear-gradient(#EFCACD, #DE8F95, #C480A2, #B69FC6, #A2CEE5, #FFFFFF);
}
.input-dialog {
  height: stretch;
  z-index: 999;
  border: 1px solid transparent;
  border-radius: 10px;
  background-color: rgba(152, 208, 231, 0.8);
  padding: 16px;
  max-width: 80%;
  position: relative;
}
.input-dialog > fieldset {
  overflow-y: auto;
  width: stretch;
  max-height: stretch;
  border-color: transparent;
  position: relative;
}
.col1 .el-container {
  height: 100%
}
.col1 .el-main {
  padding: 0px
}
.form-footer {
  height: 100%;
  width: 100%;
  position: relative;
}
.form-footer img{
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
.validate-error-animation {
  animation: shake 0.5s;
  animation-iteration-count: 1;
  -webkit-animation: shake 0.5s;
  -webkit-animation-iteration-count: 1;
}

@keyframes shake {
  0% { transform: translateX(2px) rotate(0deg); }
  10% { transform: translateX(-1px) rotate(-1deg); }
  20% { transform: translateX(1px) rotate(1deg); }
  30% { transform: translateX(-3px) rotate(0deg); }
  40% { transform: translateX(2px) rotate(1deg); }
  50% { transform: translateX(-1px) rotate(-1deg); }
  60% { transform: translateX(1px) rotate(0deg); }
  70% { transform: translateX(-3px) rotate(-1deg); }
  80% { transform: translateX(2px) rotate(1deg); }
  90% { transform: translateX(-2px) rotate(0deg); }
  100% { transform: translateX(1px) rotate(-1deg); }
}
@-webkit-keyframes shake {
  0% { -webkit-transform: translateX(2px) rotate(0deg); }
  10% { -webkit-transform: translateX(-1px) rotate(-1deg); }
  20% { -webkit-transform: translateX(1px) rotate(1deg); }
  30% { -webkit-transform: translateX(-3px) rotate(0deg); }
  40% { -webkit-transform: translateX(2px) rotate(1deg); }
  50% { -webkit-transform: translateX(-1px) rotate(-1deg); }
  60% { -webkit-transform: translateX(1px) rotate(0deg); }
  70% { -webkit-transform: translateX(-3px) rotate(-1deg); }
  80% { -webkit-transform: translateX(2px) rotate(1deg); }
  90% { -webkit-transform: translateX(-2px) rotate(0deg); }
  100% { -webkit-transform: translateX(1px) rotate(-1deg); }
}

.bouncing-ball {
    width: 100px;
    height: 100px;
    background-size: 100% auto;
    background-image: url("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Emoji_u1f4a9.svg/177px-Emoji_u1f4a9.svg.png");
    position:absolute;
    bottom: 0;
    left: 20%;
}
.feeding-animation {
  animation: bounce 2s, move 2s;
}
@keyframes bounce{
  100% {
      left: 65vw;
  }
}

@keyframes move {
  50% {
      bottom: 70vh;
  }
  100% {
      bottom: 55vh;
  }
}
/* RWD */
@media only screen and (max-width: 768px) {
  .col2 {
    padding: 1vh 1vw;
    display: flex;
    flex-direction: column;
  }
  .col2 > div {
    display: flex;
  }
  .input-dialog {
    background-color: rgba(0, 0, 0, 0.5);
    max-width: 90vw;
    margin: 0 16px;
  }

  .mobile-title {
    flex: 1;
    display: inline-block;
    z-index: 1;
  }
  .mobile-title h2 {
    margin: auto
  }
  .mobile-content {
    flex: 9;
    padding: 0 16px;
    z-index: 1;
  }
  .mobile-category-select {
    display: flex;
    flex-direction: column;
    width: stretch;
    overflow-y: auto;
    position:relative;
    -webkit-overflow-scrolling: touch;
  }
  .mobile-category-button {
    text-align: center;
    margin-bottom: 2vh;
  }
  .mobile-category-button > button {
    min-width: 80vw;
    min-height: 15vh;
    background: rgba(0, 0, 0, 0.5);
    color: #fff;
    border: transparent;
    border-radius: 10px;
    font-size: x-large;
  }

}
</style>
