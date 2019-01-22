<template>
  <div class="container">
    <Dialogue id="dialogue" :lorem="lorem"></Dialogue>
  </div>
</template>

<script>
import Dialogue from '@/components/Dialogue.vue'

export default {
  name: 'Home',
  data: function () {
    return {
      lorem: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet dolor at autem quas asperiores, dolore iure, assumenda nemo tenetur perferendis voluptates, doloribus iusto voluptate. Ipsa, laudantium. Tenetur totam repellat aliquam?',
      showIntro: true
    }
  },
  created: function () {
    console.log('home init')
    console.log(this.$route.params)
  },
  mounted: function () {
    console.log('home mounted')
  },
  components: { Dialogue }
}
</script>

<style lang="sass">
@mixin placeholder-color
  &::-webkit-input-placeholder
      color: #7b68eeba

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
    font-size: larger;
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
