<template lang="pug">
  el-row.row-dialog(type="flex" align="middle" justify="center" style="height:100%")
    el-col.bottom-dialog-wrapper
      .bottom-dialog-left
        .text-left(v-for="t in title") {{ t }}
      .bottom-dialog-right
        span.bottom-dialog-options(@click="toggleParentAnimation('create')")
          a 我要服務
        span.bottom-dialog-options(@click="toggleParentAnimation('cases')")
          a 呱吉做什麼
        span.bottom-dialog-options(@click="toggleParentAnimation('about')")
          a 關於魔鏡號
        span.bottom-dialog-options(@click="toggleParentAnimation('home')")
          a 回首頁
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
      let destination = '/' + to
      this.$store.commit('setRedirectDestination', destination)
      if (destination === this.$route.path) {
        return false
      } else {
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
  padding: 10px
  background-color: rgba(0,0,0,0.5)
  width: 100%
  height: 100%
  @media screen and (max-width: $break_small)
    flex-direction: column
    border: solid 10px #5f5f5f
    border-radius: 16px
    padding: 5px
    background-color: rgba(255,255,255,0.8)
  .bottom-dialog-left
    background-color: rgba(255,255,255,0.8)
    border: solid 10px #5f5f5f
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
      padding: 0px 5px 0px 5px
      margin: 5px
      overflow: scroll
  .bottom-dialog-right
    background-color: rgba(255,255,255,0.8)
    border: solid 10px #5f5f5f
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
      justify-content: center
      flex-direction: column
      text-align: center
      cursor: pointer
      a
        text-decoration: none
        cursor: pointer
        font-size: 1.5em
        color: black
        font-weight: 700
        @media screen
          font-size: 1em

.footer
  flex: 1
  font-size: 0.8em
  color: white
  padding: 5px
  text-align: center
  background-color: black
</style>
