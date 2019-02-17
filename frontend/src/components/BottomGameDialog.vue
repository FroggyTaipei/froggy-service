<template lang="pug">
  el-row.row-dialog(type="flex" align="middle" justify="center" style="height:100%")
    el-col.bottom-dialog-wrapper
      .bottom-dialog-left(:class="{hideDialog: !showSmallDialog}")
        .text-left(@click="changeText")
          .div {{ title[messageCount] }}
          font-awesome-icon.downAngle(icon="angle-double-down" :class="{blackArrow: lastLine}")
      .bottom-dialog-right
        span.bottom-dialog-options(@click="toggleParentAnimation('create')")
          a 我需要服務
          .arrow-icon
            i.el-icon-caret-right(:class="{showArrow: showArrow[0]}")
        span.bottom-dialog-options(@click="toggleParentAnimation('cases')")
          a 呱吉做什麼
          .arrow-icon
            i.el-icon-caret-right(:class="{showArrow: showArrow[1]}")
        span.bottom-dialog-options(@click="toggleParentAnimation('about')")
          a 關於魔鏡號
          .arrow-icon
            i.el-icon-caret-right(:class="{showArrow: showArrow[2]}")
        span.bottom-dialog-options(@click="toggleParentAnimation('home')")
          a 首頁
          .arrow-icon
            i.el-icon-caret-right(:class="{showArrow: showHomeArrow}")
    el-col.hidden-xs-only.footer
      span
        |「選服魔鏡號」台北市議員邱威傑市民服務系統
        | 110 台北市信義區仁愛路四段507號 台北市議會 752研究室
        br
        | 02-27297708 分機 7152、7252 &nbsp;
        a(href="mailto:servant@65535studio.com") servant@65535studio.com
        | &nbsp;&nbsp;
        a.githubLink(href="https://github.com/FroggyTaipei/froggy-service" target="_blank")
          font-awesome-icon(:icon="['fab', 'github']" href="https://github.com/FroggyTaipei/froggy-service")
          span 「選服魔鏡號」GitHub 專案

</template>

<script>
export default {
  name: 'BottomGameDialog',
  data: function () {
    return {
      messageCount: 0,
      showSmallDialog: true,
      showArrow: [false, false, false],
      showHomeArrow: false,
      lastLine: false
    }
  },
  methods: {
    toggleParentAnimation (to) {
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
      if (this.messageCount === contentLength - 1) {
        this.lastLine = true
      } else {
        this.lastLine = false
      }
    }
  },
  mounted () {
    // console.log(this.$route.fullPath)
    if (this.$route.fullPath.includes('about') || this.$route.fullPath.includes('cases')) {
      this.showSmallDialog = false
    }

    if (this.$route.fullPath.includes('create')) {
      this.showArrow[0] = true
    } else if (this.$route.fullPath.includes('cases')) {
      this.showArrow[1] = true
    } else if (this.$route.fullPath.includes('about')) {
      this.showArrow[2] = true
    } else {
      this.showHomeArrow = true
    }

    let contentLength = this.title.length
    if (this.messageCount === contentLength - 1) {
      this.lastLine = true
    }
  },
  props: ['title']
}
</script>

<style lang="sass">
@import '@/assets/css/style.sass'

.row-dialog
  display: flex
  flex-direction: column

.bottom-dialog-wrapper
  background-color: rgba($color_black,0.8)
  display: flex
  flex-direction: row
  flex: 9
  padding: 5px
  width: 100%
  height: 100%
  @media screen and (max-width: $break_small)
    background-color: rgba($color_black,0)
    flex-direction: column
    padding: 0px

.bottom-dialog-left
  background-color: rgba(255,255,255,0.8)
  border: $dialog_border
  border-radius: 10px
  margin-right: 5px
  padding: 5px 5px
  overflow: hidden
  flex: 3
  @media screen and (max-width: $break_small)
    flex: $flex_small_dialog_left
    background-color: rgba(255,255,255,0.8)
    overflow: hidden
    border: none
    border-radius: 4px
    margin: 0px 12px 10px 12px
    box-shadow: 3px 4px #a9a1a1
  .text-left
    font-size: $dialog_left_font
    letter-spacing: 1.5px
    height: 90%
    position: relative
    padding: 5px 5px 0px 10px
    font-weight: 600
    // margin: 5px
    overflow: hidden
    @media screen and (max-width: $break_small)
      font-size: $dialog_left_font_small
      padding: 5px

.hideDialog
  @media screen and (max-width: $break_small)
    flex: 0
    display: none

.downAngle
  position: absolute
  padding: 5px
  right: 15px
  bottom: 0px
  color: $color_red
  animation: jump 0.7s infinite ease
  @media screen and (max-width: $break_small)
    bottom: 10px

.blackArrow
  color: $color_gray
  animation: none

.bottom-dialog-right
  background-color: rgba(255,255,255,0.8)
  border: $dialog_border
  border-radius: 10px
  flex: 2
  display: flex
  flex-direction: row
  flex-wrap: wrap
  align-items: center
  justify-content: center
  @media screen and (max-width: $break_small)
    flex: $flex_small_dialog_right
    border: solid 3px rgba(0,0,0,0.6)
    border-radius: 5px
    background-color: rgba(255,255,255,0.8)
    margin: 0px 10px 5px 10px

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
        color: rgba($color_black,0.6)
  a
    text-decoration: none
    cursor: pointer
    font-size: $dialog_right_font
    font-weight: 700
    // text-shadow: 1px 1px white
    letter-spacing: 2px
    color: $color_black
    @media screen and (max-width: $break_small)
      font-size: $dialog_right_font_small

  .arrow-icon
    i.el-icon-caret-right
      margin: auto
      font-size: $dialog_right_font
      color: transparent
      @media screen and (max-width: $break_small)
        font-size: $dialog_right_font_small

//更好的寫法？
.showArrow
  color: $color_black !important

.footer
  flex: 1
  font-size: $fz_tooltip
  letter-spacing: 0.5px
  color: $color_white
  padding: 5px
  text-align: center
  background-color: $color_black
  a
    text-decoration: none
    color: white

@keyframes jump
  0% 100%
    transform: translateY(0px)
  50%
    transform: translateY(3px)
</style>
