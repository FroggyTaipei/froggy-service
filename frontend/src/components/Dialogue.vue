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
  BottomGameDialog(:title="dialogMessage" v-show="isShowMainContent || isShowBtnBar")
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
      successMessage: ['好的，沒問題！我已經發了一封確認信到你的Email裡，然後我們會用最快的速度為你服務！'],
      dialogue: [
        {
          showTime: [5, 12],
          textContent: ['早安，平安喜樂，迎接新的一天。我是Youtuber呱吉，也是台北市議員邱威傑，我這個人最不喜歡的就是浪費時間，所以你若需要幫助，不囉唆，我們直接處理。有什麼我能協助你的嗎？'],
          froggyImage: ['morning_1.png', 'morning_2.png', 'morning_3.png']
        }, {
          showTime: [12, 21],
          textContent: ['哈囉，午安！鋤禾日當午，汗滴禾下土，為選民服務，是我的任務。我是台北市議員邱威傑，也就是你們認識的呱吉。以前常有人拜託我一些雞毛蒜皮的小事，我都會說「干我什麼事」？但當選議員之後，任何的我過去認為的小事也許是市民們心中的大事，直接說吧，我能幫上什麼忙？'],
          froggyImage: ['noon_1.png', 'noon_2.png', 'noon_3.png']
        }, {
          showTime: [21, 5],
          textContent: ['晚安，食飽未（tsia̍h-pá-buē）？ 現在時候已經不早了，但我的服務還沒有打烊，你會來找我，除了是想和我約會之外，一定是對台北市政還有所期許吧？來吧，快告訴我，讓這個夜晚充滿想像與可能（附註：僅限市政問題）。'],
          froggyImage: ['night_1.png', 'night_2.png', 'night_3.png']
        }
      ]
    }
  },
  methods: {
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
      if (this.$route.params.success === true) {
        return this.imageStorageUrl + this.dialogue[this.sceneCount].froggyImage[2]
      } else {
        return this.imageStorageUrl + this.dialogue[this.sceneCount].froggyImage[0]
      }
    },
    dialogMessage: function () {
      if (this.$route.params.success === true) {
        return this.successMessage
      } else {
        return [this.dialogue[this.sceneCount].textContent[0]]
      }
    }
  },
  created: function () {
  },
  mounted: function () {
    console.log('params: ')
    console.log(this.$route.params)
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
  props: []
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
