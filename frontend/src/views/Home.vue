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
@mixin placeholder-color
  &::-webkit-input-placeholder
      color: #3819e6

table
  background-color: transparent

.el-table th, .el-table tr, .el-table, .el-table__expanded-cell
  background-color: transparent !important
  color: white

.el-table--enable-row-hover .el-table__body tr:hover>td
  color: black !important

.el-table .cell
  font-size: 24px
  line-height: 30px !important

form
  .el-textarea__inner,.el-input__inner
    background-color: rgba(#fff, .9) !important
    border-color: transparent !important
    +placeholder-color
  .el-form-item__label
    padding: 0px !important
    color: white
    font-size: larger
.form-footer-btn
  display: flex;
  justify-content: space-between;
  padding-top: 16px
  button
    background-color: rgba(#fff, .7)
    border-color: transparent
    font-weight: bold
.el-form-item__label:before, .el-form-item__error
  color: #b33600 !important
.el-checkbox
  color: #ffffff !important

#category-select
  color: #fff
  margin-bottom: 1vh
  .el-form-item__content
    font-size: larger
  .el-input__inner
    font-size: x-large
    background-color: transparent !important
    width: 9vw
    min-width: 144px
    color: #fff
    &::-webkit-input-placeholder
      color: #fff
  .el-select__caret
    color: #fff
</style>
