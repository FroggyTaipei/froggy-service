<template>
  <el-container class="page1">
    <transition name="introIn" @after-leave="showMainContent">
      <el-row
        class="intro-wrapper"
        type="flex"
        justify="center"
        align="middle"
        v-show="isShowIntro"
      >
        <img class="intro-img" :src="logoUrl" />
        <div class="intro-text" v-show="isShowIntroText" @click="start">START</div>
      </el-row>
    </transition>
    <transition name="fade" @after-leave="redirect">
      <el-row
        class="forggyImage-wrapper"
        type="flex"
        align="bottom"
        justify="center"
        v-show="isShowMainContent"
      >
        <img class="bkg-logo-img" :src="logoUrl" />
        <VTextMarquee ref="marquee" :speed="70">{{marqueeStr}}</VTextMarquee>
        <img class="froggyImage" :src="froggyImageUrl" />
        <img class="reportArrow" @click="$router.push({name:'about', hash: '#report'})" :src="require('@/assets/images/report_arrow.png')" />
      </el-row>
    </transition>
    <BottomGameDialog :title="dialogMessage" v-show="isShowMainContent || isShowBtnBar"></BottomGameDialog>
  </el-container>
</template>

<script>
import BottomGameDialog from "@/components/BottomGameDialog.vue";
import VTextMarquee from "@/components/TextMarquee.vue";

export default {
  name: "Dialogue",
  components: { BottomGameDialog, VTextMarquee },
  data: function() {
    return {
      isShowIntro: false,
      isShowMainContent: false,
      isShowIntroText: false,
      isShowBtnBar: false,
      froggyImageStorageUrl:
        "https://storage.googleapis.com/froggy-service/frontend/images/froggy/",
      logoUrl:
        "https://storage.googleapis.com/froggy-service/frontend/images/intro.png",
      successMessage: [
        "好的，沒問題！我已經發了一封確認信到你的Email裡，然後我們會用最快的速度為你服務！"
      ],
      dialogue: [
        {
          showTime: [5, 12],
          textContent: [
            "早安，平安喜樂，迎接新的一天。",
            "我是Youtuber呱吉，也是台北市議員邱威傑。我這個人最不喜歡的就是浪費時間，所以你若需要幫助，不囉唆，我們直接處理。",
            "有什麼我能協助你的嗎？"
          ],
          textContent_mobile: [
            "早安，平安喜樂，迎接新的一天。",
            "我是Youtuber呱吉，也是台北市議員邱威傑。",
            "我這個人最不喜歡的就是浪費時間，所以你若需要幫助，不囉唆，我們直接處理。",
            "有什麼我能協助你的嗎？"
          ],
          froggyImage: ["morning_1.png", "morning_2.png", "morning_3.png"]
        },
        {
          showTime: [12, 21],
          textContent: [
            "哈囉！鋤禾日當午，汗滴禾下土，為選民服務，是我的任務。我是台北市議員邱威傑，也就是你們認識的呱吉。",
            "以前常有人拜託我一些雞毛蒜皮的小事，我都會說「干我什麼事」？",
            "但當選議員之後，任何的我過去認為的小事也許是市民們心中的大事。",
            "直接說吧，我能幫上什麼忙？"
          ],
          textContent_mobile: [
            "哈囉！鋤禾日當午，汗滴禾下土，為選民服務，是我的任務。",
            "我是台北市議員邱威傑，也就是你們認識的呱吉。",
            "以前常有人拜託我一些雞毛蒜皮的小事，我都會說「干我什麼事」？",
            "但當選議員之後，任何的我過去認為的小事也許是市民們心中的大事。",
            "直接說吧，我能幫上什麼忙？"
          ],
          froggyImage: ["noon_1.png", "noon_2.png", "noon_3.png"]
        },
        {
          showTime: [21, 5],
          textContent: [
            "晚安，食飽未（tsia̍h-pá-buē）？ 現在時候已經不早了，但我的服務還沒有打烊。",
            "你會來找我，除了是想和我約會之外，一定是對台北市政還有所期許吧？",
            "來吧，快告訴我，讓這個夜晚充滿想像與可能（附註：僅限市政問題）。"
          ],
          textContent_mobile: [
            "晚安，食飽未（tsia̍h-pá-buē）？",
            "現在時候已經不早了，但我的服務還沒有打烊。",
            "你會來找我，除了是想和我約會之外，一定是對台北市政還有所期許吧？",
            "來吧，快告訴我，讓這個夜晚充滿想像與可能（附註：僅限市政問題）。"
          ],
          froggyImage: ["night_1.png", "night_2.png", "night_3.png"]
        }
      ]
    };
  },
  methods: {
    toggleLeaveAnimation: function(destination) {
      this.isShowMainContent = false;
    },
    showMainContent: function() {
      this.isShowMainContent = true;
      this.isShowBtnBar = true;
    },
    redirect: function() {
      let direction = this.$store.state.redirectTo;
      this.$router.push(direction);
    },
    start: function() {
      this.isShowIntro = false;
      setTimeout(() => this.$refs.marquee.start(), 800);
    },
    autoInappAlert: function() {
      if (
        this.$store.state.browser === "edge" ||
        this.$store.state.browser === "ie"
      ) {
        this.$alert(
          "要使用 Chrome 瀏覽器開啟才能獲得最佳瀏覽體驗喔！",
          "呱吉提示",
          {
            type: "warning",
            confirmButtonText: "好！"
          }
        );
      }
      if (
        this.$store.state.browser === "facebook" ||
        this.$store.state.browser === "messenger"
      ) {
        this.$alert(
          "要使用手機瀏覽器開啟才能獲得最佳瀏覽體驗喔！",
          "呱吉提示",
          {
            type: "warning",
            confirmButtonText: "好！"
          }
        );
      }
    }
  },
  computed: {
    sceneCount: function() {
      let now = new Date();
      let hour = now.getHours();
      switch (true) {
        case this.dialogue[0].showTime[0] <= hour &&
          hour < this.dialogue[0].showTime[1]:
          this.$store.commit("setTime", 0);
          return 0;
        case this.dialogue[1].showTime[0] <= hour &&
          hour < this.dialogue[1].showTime[1]:
          this.$store.commit("setTime", 1);
          return 1;
        case this.dialogue[2].showTime[0] <= hour ||
          hour < this.dialogue[2].showTime[1]:
          this.$store.commit("setTime", 2);
          return 2;
        default:
          break;
      }
    },
    froggyImageUrl: function() {
      if (this.$route.params.success === true) {
        return (
          this.froggyImageStorageUrl +
          this.dialogue[this.sceneCount].froggyImage[2]
        );
      } else {
        return (
          this.froggyImageStorageUrl +
          this.dialogue[this.sceneCount].froggyImage[0]
        );
      }
    },
    dialogMessage: function() {
      if (this.$route.params.success === true) {
        return this.successMessage;
      } else {
        if (this.$store.state.isMobile === true) {
          return this.dialogue[this.sceneCount].textContent_mobile;
        } else return this.dialogue[this.sceneCount].textContent;
      }
    },
    marqueeStr: function() {
      let message = "";
      this.$store.state.marqueeMessages.forEach( msg => { if (msg.display) { message += `${msg.message} `;}});
      return message;
    }
  },
  created: function() {},
  mounted: function() {
    let visited = this.$store.state.firstVisit;
    if (visited) {
      this.isShowMainContent = true;
      this.isShowBtnBar = true;
      this.$refs.marquee.start();
      return false;
    } else {
      this.$store.commit("setVisited", true);
      this.isShowIntro = true;
      setTimeout(() => {
        this.isShowIntroText = true;
        setTimeout(() => {
          this.isShowIntro = false;
          this.autoInappAlert();
          setTimeout(() => this.$refs.marquee.start(), 1600);
        }, 1500);
      }, 1000);
    }
  },
  props: []
};
</script>

<style lang="sass" scoped>
@import '@/assets/css/style.sass'

@font-face
  font-family: 'aura'
  src: url('https://froggy-service.storage.googleapis.com/frontend/assets/Aura.woff2') format('woff2'),
  url('https://froggy-service.storage.googleapis.com/frontend/assets/Aura.woff') format('woff'),
  url('https://froggy-service.storage.googleapis.com/frontend/assets/Aura.ttf') format('opentype')

.page1
  background-image: linear-gradient(#EFCACD, #DE8F95, #C480A2, #B69FC6, #A2CEE5, #FFFFFF)
  background-position: center
  background-size: contain
  background-repeat: no-repeat
  overflow: hidden
  height: 100%
  width: 100%
  flex-direction: column

.el-row
  width: 100%
  height: 100%

.bkg-logo-img
  width: 100%
  max-width: 1024px
  position: absolute
  top: 10vh
  left: 50%
  transform: translateX(-50%)
  margin: auto
  opacity: 0.5

.intro-wrapper
  background-image: linear-gradient(#EFCACD, #DE8F95, #C480A2, #B69FC6, #A2CEE5, #FFFFFF)
  background-position: center
  background-size: contain
  background-repeat: no-repeat
  position: absolute
  z-index: 10000
  width: 100%
  height: 100%
  .intro-img
    width: 100%
  .intro-text
    font-size: calc(3em + 1.5vw)
    color: white
    font-weight: bold
    position: absolute
    bottom: 25vh
    animation: blinker 1s linear infinite
    &:hover
      cursor: pointer

.v-marquee
  font-family: aura
  background-color: rgba(#e68899,1)
  padding-top: 3px
  padding-bottom: 3px
  border-width: 10px
  position: absolute
  overflow: hidden
  border-style: double
  letter-spacing: 3px
  left: 50%
  transform: translateX(-50%)
  top: 30px
  height: 2em
  line-height: 2em
  font-size: calc(2em)
  font-weight: 700
  color: $color_green
  @media screen and (max-width: $break_small)
    font-size: calc(1.5em)
    border-width: 5px
  @media all and (-ms-high-contrast: none), (-ms-high-contrast: active)
    display: none

.forggyImage-wrapper
  flex: $flex_mainContentPart
  max-height: 80vh
  @media screen and (max-width: $break_small)
    flex: $flex_small_mainContentPart
    max-height: 60vh
  .froggyImage
    width: 100%
    max-width: 500px
    // max-height: 500px
    transform: translateY(1000px)
    animation: flyin 1.5s forwards
    @media screen and (max-width: $break_small)
      animation: flyin-mobile 1.5s forwards
      -webkit-animation: flyin-mobile 1.5s forwards
  .reportArrow
    position: absolute
    right: 50px
    bottom: 20px
    width: 200px
    &:hover
      cursor: pointer
    @media screen and (max-width: $break_small)
      width: 100px
      right: 20px
      bottom: 0px

.row-dialog
  flex: $flex_dialogPart
  @media screen and (max-width: $break_small)
    flex: $flex_small_dialogPart

@keyframes blinker
  0%, 100%
    opacity: 0
  50%
    opacity: 1

@keyframes blinker-in
  0%, 25%
    opacity: 0
  26%
    opacity: 1
  40%, 85
    opacity: .1
  78%
    opacity: 0
    transform: scale(1)
  80%
    opacity: 1
    transform: scale(1.1)
  99%
    opacity: .1
    transform: scale(1)
  100%
    opacity: 1
    transform: scale(1.3)

@keyframes flyin
  100%
    transform: translateY(50px)

@keyframes flyin-mobile
  100%
    transform: translateY(30vh)

.introIn-enter-active
  animation: intro-in 2s

.introIn-leave-active
  animation: intro-in .5s reverse

@keyframes intro-in
  0%
    opacity: 0
  25%
    opacity: 0
  100%
    opacity: 1
</style>
