<template lang="pug">
  el-row.row-dialog(type="flex" align="middle" justify="center" style="height:100%")
    el-col.bottom-dialog-wrapper
      .bottom-dialog-left
        h3(v-for="t in title") {{ t }}
      .bottom-dialog-right
        span.bottom-dialog-options
          router-link(to="/")
            a 我要服務
        span.bottom-dialog-options
          router-link(to="/cases")
            a 呱吉做什麼
        span.bottom-dialog-options
          router-link(to="/about")
            a 關於魔鏡號
        span.bottom-dialog-options
            a -
    //- el-col.footer
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
  props: ['title']
}
</script>

<style lang="sass" scoped>
.row-dialog
  display: flex
  flex-direction: column

.bottom-dialog-wrapper
  display: flex
  flex-direction: row
  flex: 9
  // padding: 5px
  background-color: rgba(0,0,0,1)
  width: 100%
  // height: 100%
  .bottom-dialog-left
    background-color: white
    border: solid 5px gray
    border-radius: 20px
    margin-right: 5px
    flex: 3
    h3
      padding: 0px 10px 0px 10px
  .bottom-dialog-right
    background-color: white
    border: solid 5px gray
    border-radius: 20px
    flex: 2
    display: flex
    flex-direction: row
    flex-wrap: wrap
    align-items: center
    justify-content: center
    .bottom-dialog-options
      flex-basis: calc(50%)
      justify-content: center
      flex-direction: column
      text-align: center
    a
      text-decoration: none
      font-size: 1.2em
      color: black
      font-weight: 700

.footer
  flex: 1
  color: white
  padding: 5px
  text-align: center
  background-color: black
</style>
