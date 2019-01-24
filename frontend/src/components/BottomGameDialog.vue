<template lang="pug">
  el-row.row-dialog(type="flex" align="middle" justify="center" style="height:100%")
    el-col.bottom-dialog-wrapper
      .bottom-dialog-left
        .text-left(@click="changeText")
          .div {{ title[messageCount] }}
          font-awesome-icon.downAngle(icon="angle-double-down")
      .bottom-dialog-right
        span.bottom-dialog-options(@click="toggleParentAnimation('create')")
          a 我需要服務
          .arrow-icon
            i.el-icon-caret-right
        span.bottom-dialog-options(@click="toggleParentAnimation('cases')")
          a 呱吉做什麼
          .arrow-icon
            i.el-icon-caret-right
        span.bottom-dialog-options(@click="toggleParentAnimation('about')")
          a 關於魔鏡號
          .arrow-icon
            i.el-icon-caret-right
        span.bottom-dialog-options(@click="toggleParentAnimation('home')")
          a 回首頁
          .arrow-icon
            i.el-icon-caret-right
    el-col.hidden-xs-only.footer
      span
        |「選服魔鏡號」台北市議員邱威傑市民服務系統
        | 110 台北市信義區仁愛路四段507號 台北市議會 752研究室
        br
        | 02-27297708 分機 7152、7252
        | 或 02-87862707
        | servant@65535studio.com
</template>

<script>
export default {
  name: 'BottomGameDialog',
  data: function () {
    return {
      messageCount: 0
    }
  },
  methods: {
    toggleParentAnimation (to) {
      this.$emit('test', '456')
      let reservedUrl = ['/create', '/cases', '/about', '/home', '/success', '/home/success']
      let destination = '/' + to
      let currentPath = this.$route.fullPath
      this.$store.commit('setRedirectDestination', destination)
      if (destination === this.$route.fullPath) {
        // console.log('redirect situation 1 : nothing')
        return false
      } else if (reservedUrl.includes(currentPath) === false) {
        // console.log('redirect situation 2 : outer link')
        this.$router.push({ name: 'home', params: { success: '#' } })
        this.$router.push(destination)
      } else {
        // console.log('redirect situation 3 : redirect')
        this.$parent.$parent.toggleLeaveAnimation(destination)
      }
    },
    changeText () {
      let contentLength = this.title.length
      if (this.messageCount === contentLength - 1) {
        this.messageCount = 0
      } else {
        this.messageCount += 1
      }
    }
  },
  props: ['title']
}
</script>

<style lang="sass" scoped>
@import '@/assets/css/style.sass'

.row-dialog
  display: flex
  flex-direction: column

.bottom-dialog-wrapper
  display: flex
  flex-direction: row
  flex: 9
  // padding: 10px
  // background-color: rgba(0,0,0,0.5)
  padding: 10px
  width: 100%
  height: 100%
  @media screen and (max-width: $break_medium)
    flex-direction: column
    // border: $dialog_border_style
    // border-radius: 16px
    padding: 0px
    // background-color: rgba(255,255,255,0.8)
  .bottom-dialog-left
    background-color: rgba(255,255,255,0.8)
    border: $dialog_border_style
    border-radius: 16px
    margin-right: 5px
    overflow: hidden
    flex: 3
    @media screen and (max-width: $break_medium)
      flex: $flex_small_dialog_left
      background-color: rgba(255,255,255,0.8)
      overflow: hidden
      border: none
      border-radius: 4px
      margin: 10px
      box-shadow: 3px 4px #a9a1a1
    .text-left
      height: 90%
      position: relative
      padding: 5px 5px 0px 5px
      font-weight: 600
      margin: 5px
      overflow: hidden
      @media screen and (min-width: $break_large)
        font-size: $dialog_left_font_large
      @media screen and (max-width: $break_medium)
        font-size: $dialog_left_font_medium
        padding: 5px
      @media screen and (max-width: $break_small)
        padding: 5px
        font-size: $dialog_left_font_small
      .downAngle
        position: absolute
        padding: 10px
        right: 5px
        bottom: 5px
        color: #942f2f
        animation: jump 0.7s infinite ease
        @media screen and (max-width: $break_small)
          bottom: 10px
  .bottom-dialog-right
    background-color: rgba(255,255,255,0.8)
    border: $dialog_border_style
    border-radius: 16px
    flex: 2
    display: flex
    flex-direction: row
    flex-wrap: wrap
    align-items: center
    justify-content: center
    @media screen and (max-width: $break_medium)
      flex: $flex_small_dialog_right
      border: solid 5px rgba(0,0,0,0.6)
      border-radius: 5px
      background-color: rgba(255,255,255,0.8)
      margin: 5px 10px 10px 10px
    .bottom-dialog-options
      flex-basis: calc(50%)
      display: flex
      justify-content: center
      flex-direction: row-reverse
      text-align: center
      cursor: pointer
      &:hover
        .arrow-icon
          i.el-icon-caret-right
            color: black
      a
        text-decoration: none
        cursor: pointer
        font-size: 1.5em
        color: black
        font-weight: 700
        letter-spacing: 2px
        @media screen and (min-width: $break_large)
          font-size: $dialog_right_font_large
        @media screen and (max-width: $break_medium)
          font-size: $dialog_right_font_medium
        @media screen and (max-width: $break_small)
          font-size: $dialog_right_font_small

      .arrow-icon
        i.el-icon-caret-right
          margin: auto
          font-size: 1.5em
          color: transparent
          @media screen and (max-width: $break_medium)
            font-size: 1em

.footer
  flex: 1
  font-size: 0.8em
  color: white
  padding: 5px
  text-align: center
  background-color: black

@keyframes jump
  0% 100%
    transform: translateY(0px)
  50%
    transform: translateY(3px)
</style>
