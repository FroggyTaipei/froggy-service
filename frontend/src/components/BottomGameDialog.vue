<template lang="pug">
  el-row.row-dialog(type="flex" align="middle" justify="center" style="height:100%")
    .bottom-dialog-wrapper
      .bottom-dialog-left
        h2(v-for="t in title") {{ t }}
      .bottom-dialog-right
        span.bottom-dialog-options
          a(href="#firstPage") 我要服務
        span.bottom-dialog-options 
          a(href="#secondPage") 呱吉做什麼
        span.bottom-dialog-options
          a(href="#thirdPage") 關於魔鏡號
        span.bottom-dialog-options -
</template>

<script>
export default {
  name: 'BottomGameDialog',
  props: ['title']
}
</script>

<style lang="sass" scoped>

.bottom-dialog-wrapper
  flex: 1
  position: absolute
  display: flex
  flex-direction: row
  // bottom: 0
  padding: 5px
  background-color: rgba(0,0,0,1)
  width: 100%
  height: 100%
  .bottom-dialog-left
    background-color: white
    border: solid 5px gray
    border-radius: 20px
    margin-right: 5px
    flex: 3
    h2
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
      font-size: 1.2em
</style>
