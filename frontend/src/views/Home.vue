<template>
  <div class="container">
    <Dialogue id="dialogue"></Dialogue>
  </div>
</template>

<script>
import Dialogue from '@/components/Dialogue.vue'

export default {
  name: 'Home',
  data: function () {
    return {
    }
  },
  created: function () {
    // console.log('home init')
    // console.log(this.$route)
  },
  mounted: function () {
    // console.log('home mounted')
  },
  components: { Dialogue }
}
</script>

<style lang="sass">
@import '@/assets/css/style.sass'

@mixin placeholder-color
  &::-webkit-input-placeholder
      color: #7b68eeba

table
  background-color: transparent

form
  .el-textarea__inner,.el-input__inner
    background-color: rgba(#fff, .3) !important
    border-color: transparent !important
    +placeholder-color
  .el-form-item__label
    padding: 0px !important
    color: white
    font-size: larger
.form-footer-btn
  float: right
  padding-top: 16px
  button
    background-color: rgba(#fff, .3)
    border-color: transparent
    font-weight: bold
.el-form-item__label:before, .el-form-item__error
  color: #655356 !important
.el-checkbox
  color: #ffffff !important
</style>
