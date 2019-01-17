<template lang="pug">
el-container.page1
  el-main
    transition(name="fade")
      el-row(type="flex" justify="center" align="middle" v-show="showIntro")
        el-col
          .center(v-show="showIntro")
            img.introImg(:src="introUrl")
            h1.intro(@click="makeInvisible" ) START

        //- .main(v-show="showFroggy")
        //-   img.froggyImage(:src="froggyUrl")
    transition(name="fade")
      el-row(type="flex" align="middle" justify="center" v-show="showFroggy" @click='come')
        el-col(:span="18")
          img.froggyImage(:src="froggyUrl", @load='getHeight', ref='froggy', :class="{'slide-up': slide}", :style="{bottom:froggyHeight+'px'}")
          el-row(type="flex" align="middle" justify="center")
            el-col
              img.bottom(src='../assets/text.png')
            el-col
              .bottom.froggy-text
                h1 台北市議員邱威傑：
                span {{dialogue[sceneCount].textContent[0]}}
              .bottom.bottom-btn
                i.el-icon-caret-right(v-show='mouse1')
                el-button.text-button(type='text', @mouseover.native='hover(1)', @mouseleave.native='leave(1)') 我要找呱吉
                i.el-icon-caret-right(v-show='mouse2')
                el-button.text-button(type='text', @mouseover.native='hover(2)', @mouseleave.native='leave(2)') 呱吉做什麼
        //- img.froggyImage.bottom(:src="froggyImageUrl", @load='getHeight', ref='froggy', :class="{'slide-up': slide}", :style="{bottom:froggyHeight+'px'}")
        //- el-row
            //- el-col(:span="6")
            //- InputDialog(v-show="showInput" v-on:closeInput="closeInputDialog")
      //- el-row(type="flex" align="top" justify="center")
        el-col(:span="12")
          .conversation(v-show="!showInput")
            el-row(type="flex" align="top" justify="end")
              el-col(:span="24")
                h1 邱威傑：
                span {{dialogue[sceneCount].textContent[0]}}
            el-row(type="flex" align="middle" justify="center")
              el-col.text(:span="12" style="align-self: flex-end" :class="{selected: isFindFroggy}" @click="clickOption('findFroggy')") 我要找呱吉
              el-col.text(:span="12" :class="{selected: isFroggyDoing}" @click="clickOption('froggyDoing')") 呱吉做什麼
              el-button.goButton(type="success" @click="dialogAction") GO
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
      showInput: false,
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
    closeInputDialog: function () {
      this.showInput = false
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
    come () {
      console.log('come')
      this.slide = true
    },
    hover (index) {
      if (index) {
        this.mouse1 = true
      } else {
        this.mouse2 = true
      }
    },
    leave (index) {
      if (index) {
        this.mouse1 = false
      } else {
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
  mounted: function () {
    // setTimeout(()=>{
    //   this.showIntro = !this.showIntro
    // },500)
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
  height: 100vh
  align-items: center
  justify-content: center

.introImg
  width: 100%

.froggyImage
  width: 100%
//
.bottom
  width: 100%
  position: absolute
  bottom: 0px
  left: 0px

.froggy
  bottom: -623px

.bg
  background-image: url("https://s3-ap-southeast-1.amazonaws.com/o-r-z/froggy-service/gradient_background.png")
  background-repeat: no-repeat
  background-size: auto 100%
  position: relative

.slide-up
  transform: translateY(-100%)
  transition: .4s ease-in-out

.bottom-btn
  width: 80%
  text-align: right
  padding: 16px 48px
  color: white

.text-button
  color: white
  margin-right: 20px

.froggy-text
  color: white
  width: 80%
  padding: 48px
  textalign: center

//

.intro
  font-size: 80px
  color: white
  font-weight: bold
  position: absolute
  bottom: 15%
  animation: blinker 2s linear infinite
  &:hover
    cursor: pointer

@keyframes blinker
  50%
    opacity: 0

.fade-enter-active, .fade-leave-active
  transition: opacity .5s
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */
  opacity: 0
</style>
