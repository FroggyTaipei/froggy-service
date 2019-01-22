<template lang="pug">
el-container.page1
  transition(name="introIn" @after-leave="showMainContent")
    el-row.intro-wrapper(type="flex" justify="center" align="middle" v-show="isShowIntro")
      img.intro-img(:src="logoUrl")
      .intro-text(v-show="isShowIntroText") START
  transition(name="fade" @after-leave="redirect")
    el-row.forggyImage-wrapper(type="flex" align="bottom" justify="center" v-show="isShowMainContent")
      img.bkg-logo-img(:src="logoUrl")
      img.froggyImage(:src="froggyImageUrl")
  BottomGameDialog(:title="welcomeText" v-show="isShowMainContent || isShowBtnBar")
</template>

<script>
import BottomGameDialog from '@/components/BottomGameDialog.vue'

export default {
  name: 'Dialogue',
  components: { BottomGameDialog },
  data: function () {
    return {
      isShowIntro: false,
      isShowMainContent: false,
      isShowIntroText: false,
      isShowBtnBar: false,
      imageStorageUrl: 'https://s3-ap-southeast-1.amazonaws.com/o-r-z/froggy-service/',
      logoUrl: 'https://s3-ap-southeast-1.amazonaws.com/o-r-z/froggy-service/intro.png',
      dialogue: [
        {
          showTime: [5, 12],
          textContent: ['早安，你好！我是呱吉，也是台北市議員邱威傑，平常我一天都睡 4、5 個小時，作為 43 歲的「年輕市議員」，時間不能浪費！ 有什麼我能協助你的嗎？'],
          froggyImage: ['morning_1.png', 'morning_2.png', 'morning_3.png']
        }, {
          showTime: [12, 21],
          textContent: ['哈囉，你好！我是台北市議員邱威傑，也就是你們認識的呱吉。以前別人跟我拜託，我都會說「干我什麼事」，但當選議員之後，我知道服務台北市民就是我的責任，所以說吧，你需要我什麼幫忙！'],
          froggyImage: ['noon_1.png', 'noon_2.png', 'noon_3.png']
        }, {
          showTime: [21, 5],
          textContent: ['晚安，你好！現在時候已經不早了，但你會來找我一定是有些台北市沒做好的事吧？來吧，快告訴我，反正我每天都2、3點才睡覺！'],
          froggyImage: ['night_1.png', 'night_2.png', 'night_3.png']
        }
      ]
    }
  },
  methods: {
    setCookie (name, value) {
      document.cookie = name + '=' + (value || '') + '; path=/'
    },
    toggleLeaveAnimation: function (destination) {
      this.isShowMainContent = false
    },
    showMainContent: function () {
      this.isShowMainContent = true
      this.isShowBtnBar = true
    },
    redirect: function () {
      let direction = this.$store.state.redirectTo
      this.$router.push(direction)
    }
  },
  computed: {
    sceneCount: function () {
      let now = new Date()
      let hour = now.getHours()
      switch (true) {
        case (this.dialogue[0].showTime[0] <= hour && hour < this.dialogue[0].showTime[1]):
          return 0
        case (this.dialogue[1].showTime[0] <= hour && hour < this.dialogue[1].showTime[1]):
          return 1
        case (this.dialogue[2].showTime[0] <= hour || hour < this.dialogue[2].showTime[1]):
          return 2
        default:
          break
      }
    },
    froggyImageUrl: function () {
      return this.imageStorageUrl + this.dialogue[this.sceneCount].froggyImage[0]
    },
    welcomeText: function () {
      return [this.dialogue[this.sceneCount].textContent[0]]
    }
  },
  created: function () {
  },
  mounted: function () {
    let visited = this.$store.state.firstVisit
    if (visited) {
      console.log('visited')
      this.isShowMainContent = true
      this.isShowBtnBar = true
      return false
    } else {
      console.log('not visited')
      this.$store.commit('setVisited', true)
      this.isShowIntro = true
      setTimeout(() => {
        this.isShowIntroText = true
        setTimeout(() => { this.isShowIntro = false }, 1500)
      }, 1000)
    }
  },
  props: ['lorem']
}
</script>

<style lang="sass" scoped>
@import '@/assets/css/style.sass'

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
  position: absolute
  top: 10%
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
    font-size: 4em
    color: white
    font-weight: bold
    position: absolute
    bottom: 20vh
    animation: blinker 1.5s forwards
    &:hover
      cursor: pointer

.forggyImage-wrapper
  flex: 3
  @media screen and (max-width: $break_small)
    flex: 3
  .froggyImage
    width: 100%
    max-width: 500px
    transform: translateY(1000px)
    animation: flyin 1.5s forwards
    @media screen and (max-width: $break_small)
      animation: flyin-mobile 1.5s forwards

.row-dialog
  flex: 1
  @media screen and (max-width: $break_small)
    flex: 2

@keyframes blinker
  0%
    opacity: 0
  25%
    opacity: 0
  26%
    opacity: 1
  40%
    opacity: .1
  78%
    opacity: 0
    transform: scale(1)
  80%
    opacity: 1
    transform: scale(1.1)
  85%
    opacity: .1
  99%
    opacity: .1
    transform: scale(1)
  100%
    opacity: 1
    transform: scale(1.3)

@keyframes flyin
  100%
    transform: translateY(20px)

@keyframes flyin-mobile
  100%
    transform: translateY(50px)

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
