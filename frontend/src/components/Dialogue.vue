<template lang="pug">
.container.section
  .row.vertical-center 
    div(:class="{'col-sm-8':!showInput,'col-sm-3':showInput, 'froggyImage': !showInput, 'froggyImage-input':showInput}")
      img.img-fluid(:src="froggyImageUrl")
    //- button.btn.toggleInputBtn.btn-danger.btn-lg(v-show="showInput" @click="showInput = !showInput") Close Input
    InputDialog(v-show="showInput")
    .col-sm-10.conversation(v-show="!showInput")
      .row
        .name 邱威傑：
        span {{dialogue[sceneCount].textContent[0]}}
      .row.justify-content-center
        .options.col-sm-4
          .row.justify-content-center
            .text(:class="{selected: isFindFroggy}" @click="clickOption('findFroggy')") 我要找呱吉
          .row.justify-content-center
            .text(:class="{selected: isFroggyDoing}" @click="clickOption('froggyDoing')") 呱吉做什麼
        .col-sm-2.align-self-end.buttonWrapper
          button.btn.btn-lg.btn-success.goButton(@click="dialogAction") GO

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
      showInput: true
    }
  },
  methods: {
    closeInputDialog: function () {
      this.showInput = false
    },
    clickOption: function (action) {
      if (action == 'findFroggy') {
        if (this.isFindFroggy) {
          this.isFindFroggy = !this.isFindFroggy
        } else if (this.isFroggyDoing) {
          this.isFindFroggy = !this.isFindFroggy
          this.isFroggyDoing = !this.isFroggyDoing
        } else {
          this.isFindFroggy = !this.isFindFroggy
        }
      } else if (action == 'froggyDoing') {
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
        var element = document.getElementById('cases')
        var top = element.offsetTop
        window.scrollTo(0, top - 50)
      } else {
        console.log('no action')
      }
    },
    toggleInput: function () {
      this.showInput = !this.showInput
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
  props: ['lorem']
}
</script>

<style lang="sass" scoped>
.section
  position: relative
  height: 100vh
.section:after
  content: ""
  display: block
  background-image: url('https://i.cdn.turner.com/adultswim/big/img/2018/12/04/whiteTiles.jpg')
  position: absolute
  top: 0
  left: 0
  width: 100%
  height: 100%
  opacity: 0.5
  z-index: -1
  filter: blur(3px)

InputDialog
  z-index: 0

.froggyImage
  z-index: 1
  position: relative
  height: 100%
  left: 0px
  bottom: 0
  transition:  2s
  pointer-events: none
.froggyImage-input
  z-index: 1
  position: absolute
  left: 0
  bottom: 0
  transition: 2s
  pointer-events: none
.toggleInputBtn
  margin-top: 50px

.conversation
  z-index: 2
  width: 100%
  position: absolute
  top: 50vh
  padding: 30px
  border-radius: 10px
  // color: black
  background-color: #fff
  border: 3px solid black
  .name
    font-size: 32px
    font-weight: bold
  span
    margin-bottom: 5px
    font-size: 20px
    font-weight: bold
  .options
    font-size: 28px
    font-weight: bold
    padding: 10px
    .text
      box-sizing: border-box
      border: solid 3px transparent
      padding: 5px
      width: fit-content
      cursor: pointer
      &:hover
        border: 3px solid
        // background-color: pink
        border-radius: 10px
    .arrow
      box-sizing: border-box
      border: solid 3px transparent
      padding: 10px
      width: fit-content
    .selected
      // border: 3px solid
      border-radius: 10px
      background-color: pink
  .buttonWrapper
    padding: 10px
    .goButton
      width: 100%

.vertical-center
  min-height: 100%
  min-height: 100vh
  display: flex
  align-items: center
</style>
