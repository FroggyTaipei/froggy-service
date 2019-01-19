<template>
  <div class="container">
      <!-- <Dialogue id="dialogue" class="" :lorem="lorem"></Dialogue> -->
      <CaseList id="cases" :lorem="lorem"></CaseList>
      <!-- <About id="about" :lorem="lorem"></About> -->
  </div>
</template>

<script>
import CaseList from '@/components/CaseList.vue'

export default {
  name: 'Home',
  data: function () {
    return {
      lorem: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet dolor at autem quas asperiores, dolore iure, assumenda nemo tenetur perferendis voluptates, doloribus iusto voluptate. Ipsa, laudantium. Tenetur totam repellat aliquam?'
    }
  },
  components: { CaseList }
}
</script>

<style lang="sass">
*
  // border: solid 1px
  font-family: PingFangSC-Regular

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

// .el-table .ascending .sort-caret.ascending
//   border-bottom-color: black !important
// .el-table .descending .sort-caret.descending
//   border-bottom-color: black !important

form
  textarea,.el-input__inner
    background-color: rgba(#fff, .3) !important
    border-color: transparent !important
  .el-form-item__label
    padding: 0px !important
    color: white
    font-size: larger
</style>
