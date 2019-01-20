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
  name: 'CaseListPage',
  data: function () {
    return {
      data: [],
      title: [],
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

.VueTables.VueTables--server
  height: 100%
  display: flex
  flex-direction: column
  align-items: center
  justify-content: center
  &>.row>.col-md-12
    margin: 50px 0px 20px 0px
    .VueTables__search-field
      color: white
      label
        margin-right: 20px
        font-size: 1.2em
      input
        font-size: 1em
  .table-responsive
    width: 100%
    height: 80%

.glyphicon
  width: 10px !important
  content: '66'
  position: absolute
  color: white
  width: 10px !important
  height: 10px !important

table
  width: 100%
  color: white
  border-spacing: unset
  thead>tr>th
    font-size: 1.2em
  tbody>tr
    transition: 0.1s
    &:hover
      color: black
      background-color: white
      transition: 0.2s
      cursor: pointer
    &>td
      padding: 0
      text-align: center
      line-height: 2em

.VuePagination, .VuePagination__pagination, .VuePagination__count
  display: flex !important
  align-items: center
  justify-content: center
  padding: 0
  li
    list-style-type: none!important
    margin: 10px
    a
      text-decoration: none!important
      font-size: 1em
      color: white
nav
  width: 100%
  color: white

.el-dialog
  width: 80% !important
  max-height: 50%
  margin-top: 5vh !important
  box-shadow: 0 0 0 !important
  background: transparent !important

.upper-block-bkg
  height: 100px
  width: 100%
  background: linear-gradient(to right, #63B8B7, #3FA8BC, #5676AC, #7F5596, #BB4577)
  overflow: hidden
.case-logo
  position: absolute !important
  height: 100%
  top: 45px
  right: 0px
  height: 100px

.el-dialog
  // position: absolute !important

.el-dialog__header
  background: linear-gradient(#0155E4, #ffffff 0.2, #0155E4)
  padding-top: 30px !important
  .el-dialog__headerbtn
    top: 10px
    right: 10px
  .el-icon-close
    border: white 1px solid
    background-color: orange
    color: white !important

.el-dialog__body
  box-sizing: border-box !important
  border-width: 5px 5px 0px 5px
  padding: 0 !important
  border-style: solid
  border-color: #0155E4
  background-color: #dcdcdc
  .case-content
    padding: 20px !important
    max-height: 40vh !important
    overflow: scroll
    .content-title
      font-size: 1.2em
      font-weight: 700

.el-dialog__footer
  height: 150px
  align-items: center
  display: flex !important
  box-sizing: border-box !important
  border-width: 0px 5px 7px 5px
  border-style: solid
  border-radius: 0px 0px 10px 10px
  border-color: #0155E4
  background-color: #dcdcdc
  .dialog-footer
    width: 100%
    height: 100%
    display: flex !important
    align-items: center
    justify-content: flex-end
    .footer-block
      display: flex !important
      align-items: center
      justify-content: center
      height: 90%
      width: 80%
      border: solid 10px black !important
      right: 20px!important
      box-sizing: border-box
      border-radius: 40px 10px
      background-color: white !important
      font-size: 1.5em
      font-weight: 700
      .content-id
        flex: 1
        padding: 0px 20px 0px 20px
        text-align: center
      .content-status
        flex: 1
        padding: 0px 20px 0px 20px
        text-align: left

</style>
