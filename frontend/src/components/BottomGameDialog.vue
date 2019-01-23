<template lang="pug">
  el-row.row-dialog(type="flex" align="middle" justify="center" style="height:100%")
    el-col.bottom-dialog-wrapper
      .bottom-dialog-left
        .text-left
          .div(v-for="t in title") {{ t }}
            br
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
        | 02-87862707
        | servant@65535studio.com
</template>

<script>
export default {
  name: 'BottomGameDialog',
  data: function () {
    return {

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
        this.$router.push('/home')
        this.$router.push(destination)
      } else {
        // console.log('redirect situation 3 : redirect')
        this.$parent.$parent.toggleLeaveAnimation(destination)
      }
    }
  },
  props: ['title', 'showParent']
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
  background-color: rgba(0,0,0,0.5)
  padding: 10px
  width: 100%
  height: 100%
  @media screen and (max-width: $break_small)
    flex-direction: column
    border: $dialog_border_style
    border-radius: 16px
    padding: 5px
    background-color: rgba(255,255,255,0.8)
  .bottom-dialog-left
    background-color: rgba(255,255,255,0.8)
    border: $dialog_border_style
    border-radius: 16px
    margin-right: 5px
    overflow: scroll
    flex: 3
    @media screen and (max-width: $break_small)
      flex: 1
      overflow: scroll
      border: none
      border-radius: 0
      background-color: transparent
    .text-left
      padding: 10px
      font-weight: 600
      margin: 5px
      overflow: scroll
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
    @media screen and (max-width: $break_small)
      flex: 1
      border: none
      border-radius: 0
      background-color: transparent
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
        @media screen and (max-width: $break_medium)
          font-size: 1.2em
        @media screen and (max-width: $break_small)
          font-size: 1em
      .arrow-icon
        i.el-icon-caret-right
          margin: auto
          font-size: 1.5em
          color: transparent
          @media screen and (max-width: $break_small)
            font-size: 1em

.footer
  flex: 1
  font-size: 0.8em
  color: white
  padding: 5px
  text-align: center
  background-color: black
</style>
