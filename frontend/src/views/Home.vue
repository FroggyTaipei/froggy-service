<template>
  <div class="container">
      <!-- <Dialogue id="dialogue" :lorem="lorem"></Dialogue> -->
      <InputDialog></InputDialog>
  </div>
</template>

<script>
import Dialogue from '@/components/Dialogue.vue'
import InputDialog from '@/components/InputDialog.vue'

export default {
  name: 'Home',
  data: function () {
    return {
      lorem: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet dolor at autem quas asperiores, dolore iure, assumenda nemo tenetur perferendis voluptates, doloribus iusto voluptate. Ipsa, laudantium. Tenetur totam repellat aliquam?',
      showIntro: true
    }
  },
  created: function () {
  },
  mounted: function () {
  },
  components: { Dialogue, InputDialog }
}
</script>

<style lang="sass">
*
  // border: solid 1px
  font-family: PingFangSC-Regular
@mixin placeholder-color
  &::-webkit-input-placeholder
      color: #7b68eeba
html,body
  margin: auto
  width: 100vw
  width: 100%
  height: 100vh
  height: 100%
  // background-color: gray

.container
  height: 100%
  width: 100%

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
</style>
