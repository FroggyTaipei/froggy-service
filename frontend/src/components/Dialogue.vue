<template lang="pug">
el-container.page1
  el-main
    transition(name="fade")
      el-row(type="flex" justify="center" align="middle" v-show="showIntro")
        el-col
          .center(v-show="showIntro")
            img.intro-img(:src="introUrl")
            h1.intro-text(@click="makeInvisible" ) START
    transition(name="fade")
      el-row(type="flex" align="middle" justify="center" v-show="showFroggy")
        el-col(:span="18")
          img.froggyImage(:src="froggyUrl")
          el-row(type="flex" align="end" justify="center")
            el-col
              .text-block-back
                .text-block-front
                  h1 台北市議員邱威傑：
                  span {{dialogue[sceneCount].textContent[0]}}
                  .bottom.bottom-btn
                    .space
                    .btn-wrapper
                      i.el-icon-caret-right(v-show='mouse1')
                      el-button.text-button(type='text', @mouseover.native='hover(1)', @mouseleave.native='leave(1)' @click.native="toggleInput") 我要找呱吉
                    .btn-wrapper
                      i.el-icon-caret-right(v-show='mouse2')
                      el-button.text-button(type='text', @mouseover.native='hover(2)', @mouseleave.native='leave(2)') 呱吉做什麼
    transition(name="fade")
      InputDialog(v-show="openInput")

</template>

<script>
import InputDialog from '@/components/InputDialog.vue'
export default {
  name: 'Dialogue',
  components: { InputDialog },
  data: function () {
    return {
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
      isFindFroggy: false,
      isFroggyDoing: false,
      openInput: false,
      bkgUrl: 'https://s3-ap-southeast-1.amazonaws.com/o-r-z/froggy-service/gradient_background.png',
      introUrl: 'https://s3-ap-southeast-1.amazonaws.com/o-r-z/froggy-service/intro.png',
      showIntro: true,
      showFroggy: false,
      froggyUrl: 'https://s3-ap-southeast-1.amazonaws.com/o-r-z/froggy-service/morning_1.png',
      slide: false,
      mouse1: false,
      mouse2: false,
      froggyHeight: 0
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
      console.log('clicked')
      this.showFroggy = !this.showFroggy
      this.openInput= !this.openInput
    },
    clickOption: function (action) {
      if (action === 'findFroggy') {
        if (this.isFindFroggy) {
          this.isFindFroggy = !this.isFindFroggy
        } else if (this.isFroggyDoing) {
          this.isFindFroggy = !this.isFindFroggy
          this.isFroggyDoing = !this.isFroggyDoing
        } else {
          this.isFindFroggy = !this.isFindFroggy
        }
      } else if (action === 'froggyDoing') {
        if (this.isFroggyDoing) {
          this.isFroggyDoing = !this.isFroggyDoing
        } else if (this.isFindFroggy) {
          this.isFindFroggy = !this.isFindFroggy
          this.isFroggyDoing = !this.isFroggyDoing
        } else {
          this.isFroggyDoing = !this.isFroggyDoing
        }
      }
    },
    dialogAction: function () {
      if (this.isFindFroggy) {
        this.isFindFroggy = false
        this.showInput = true
      } else if (this.isFroggyDoing) {
        this.isFroggyDoing = false
        this.showInput = false
        fullpage_api.moveTo('secondPage', 0)
      } else {
        console.log('no action')
      }
    },
    toggleInput: function () {
      this.showInput = !this.showInput
    },
    getHeight () {
      this.froggyHeight = -this.$refs.froggy.clientHeight
    },
    hover (index) {
      if (index===1) {
        this.mouse1 = true
      } else if(index===2) {
        this.mouse2 = true
      }
    },
    leave (index) {
      if (index===1) {
        this.mouse1 = false
      } else if(index===2) {
        this.mouse2 = false
      }
    }
  },
  computed: {
    sceneCount: function () {
      let now = new Date()
      let hour = now.getHours()
      switch (true) {
        case (this.dialogue[0].showTime[0] <= hour && hour < this.dialogue[0].showTime[1]):
          return 0
          break
        case (this.dialogue[1].showTime[0] <= hour && hour < this.dialogue[1].showTime[1]):
          return 1
          break
        case (this.dialogue[2].showTime[0] <= hour || hour < this.dialogue[2].showTime[1]):
          return 2
          break
        default:
          break
      }
    },
    froggyImageUrl: function () {
      return this.imageStorageUrl + this.dialogue[this.sceneCount].froggyImage[0]
    }
  },
    mounted: function(){
    setTimeout(()=>{
      this.showIntro = !this.showIntro
      setTimeout(()=>{
        this.showFroggy = true
      },500)
    },1500)
  },
  props: ['lorem']
}
</script>

<style lang="sass" scoped>
.page1
  background-image: url('https://s3-ap-southeast-1.amazonaws.com/o-r-z/froggy-service/gradient_background.png')
  background-position: center
  overflow: hidden

.center, .el-main
  display: flex
  width: 100%
  height: 100%
  flex-shrink: 0
  align-items: center
  justify-content: center

.el-row
  width: 100%

.intro-img
  width: 100%

.froggyImage
  width: 100%
  transform: translateY(1000px)
  animation: flyin 2s forwards
//
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

.intro-text
  font-size: 80px
  color: white
  font-weight: bold
  position: absolute
  bottom: 0
  animation: blinker 2s linear infinite
  &:hover
    cursor: pointer

@keyframes blinker
  50%
    opacity: 0

@keyframes flyin 
  100%
    transform: translateY(0)
// Vue animation
.fade-enter-active, .fade-leave-active
  transition: opacity .5s
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */
  opacity: 0
</style>
