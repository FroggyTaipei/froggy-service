<template lang="pug">
el-container.page1
  transition(name="fade")
    el-row(type="flex" justify="center" align="middle" v-show="showIntro")
      img.intro-img(:src="introUrl")
      h1.intro-text START
  transition(name="fade")
    el-row.forggyImage-wrapper(type="flex" align="bottom" justify="center" v-show="showFroggy")
      img.froggyImage(:src="froggyImageUrl")
  //佔空間用
  el-row.forggyImage-wrapper(type="flex" align="bottom" justify="center" v-show="!showFroggy")
  BottomGameDialog(v-show="!showIntro" :title="welcomeText")

</template>

<script>
import BottomGameDialog from '@/components/BottomGameDialog.vue'

export default {
  name: 'Dialogue',
  components: { BottomGameDialog },
  data: function () {
    return {
      showIntro: true,
      imageStorageUrl: 'https://s3-ap-southeast-1.amazonaws.com/o-r-z/froggy-service/',
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
      ],
      openInput: false,
      bkgUrl: 'https://s3-ap-southeast-1.amazonaws.com/o-r-z/froggy-service/gradient_background.png',
      introUrl: 'https://s3-ap-southeast-1.amazonaws.com/o-r-z/froggy-service/intro.png',
      showFroggy: false
    }
  },
  methods: {
    makeInvisible () {
      this.showIntro = !this.showIntro
      setTimeout(() => {
        this.showFroggy = true
      }, 1000)
    },
    toggleInput () {
      this.showFroggy = !this.showFroggy
      this.openInput = !this.openInput
    },
    hover (index) {
      if (index === 1) {
        this.mouse1 = true
      } else if (index === 2) {
        this.mouse2 = true
      }
    },
    leave (index) {
      if (index === 1) {
        this.mouse1 = false
      } else if (index === 2) {
        this.mouse2 = false
      }
    },
    beforePageDestroyed: function (event) {
      console.log('beforePageDestroyed')
    },
    setCookie (name, value) {
      document.cookie = name + '=' + (value || '') + '; path=/'
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
    this.visited = document.getCookie('visited')
    console.log('visited ' + this.visited)
    if (this.visited) {
      this.showIntro = false
    } else {
      this.setCookie('visited', true)
    }
    window.addEventListener('beforeunload', function (e) {
      document.eraseCookie('visited')
    })
  },
  mounted: function () {
    let introTime = 1500
    let showFroggyTime = 500
    if (this.visited) {
      introTime = 0
      showFroggyTime = 0
    }
    setTimeout(() => {
      this.showIntro = false
      setTimeout(() => {
        this.showFroggy = true
      }, showFroggyTime)
    }, introTime)
  },
  props: ['lorem']
}
</script>

<style lang="sass" scoped>
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

.intro-img
  width: 100%

.forggyImage-wrapper
  flex: 3
  .froggyImage
    width: 100%
    max-width: 500px
    transform: translateY(1000px)
    animation: flyin 1.5s forwards

.bottom
  width: 100%
  position: absolute
  bottom: 0px
  left: 0px

.bottom-btn
  width: 80%
  text-align: right
  padding: 16px 48px
  color: white
  display: flex
  .space
    flex: auto
  .btn-wrapper
    flex-basis: 120px
    felx: 0 0 120px

.text-button
  color: white
  margin-right: 20px

.text-block-back
  display: flex
  position: absolute
  background-color: rgba(255,255,255,0.6)
  width: 100%
  height: 20vh
  bottom: 0
  border-radius: 10px
  .text-block-front
    display: flex
    flex-direction: column
    margin: auto
    color: white
    background-color: rgba(26,110,99,0.8)
    width: 95%
    height: 98%
    border-radius: 10px
    h1
      padding: 20px 20px 0px 20px
      margin-bottom: 0px
    span
      padding: 0px 20px 10px 20px
      font-size: 1em

.row-dialog
  flex: 1

.intro-text
  font-size: 80px
  color: white
  font-weight: bold
  position: absolute
  bottom: 10vh
  animation: blinker 2s linear infinite
  &:hover
    cursor: pointer

@keyframes blinker
  50%
    opacity: 0

@keyframes flyin
  100%
    transform: translateY(20px)

// Vue animation
.fade-enter-active, .fade-leave-active
  transition: opacity .5s
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */
  opacity: 0s
</style>
