<template>
  <div class="container">
    <CaseList id="cases"></CaseList>
  </div>
</template>

<script>
import CaseList from '@/components/CaseList.vue'

export default {
  name: 'CaseListPage',
  data: function () {
    return {
      data: [],
      title: []
    }
  },
  components: { CaseList }
}
</script>

<style lang="sass">
@import '@/assets/css/style.sass'
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

.VueTables.VueTables--server
  height: 100%
  display: flex
  flex-direction: column
  align-items: center
  justify-content: center
  &>.row>.col-md-12
    margin: 10px 0px 20px 0px
  .table-responsive
    width: 100%
    overflow: scroll
    &::-webkit-scrollbar
      width: 0 !important
    // height: 80%

.VueTables__search-field
  color: white
  label
    margin-right: 20px
    font-size: 1.2em
  input
    font-size: 1em
    border-radius: 5px !important
    border: none
    height: 30px
    padding-left: 10px

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
      color: #565758
      font-weight: 600

.VuePagination li.disabled, .VuePagination__pagination li.disabled, .VuePagination__count li.disabled
  >a
    color: transparent

.VuePagination li.active, .VuePagination__pagination li.active, .VuePagination__count li.active
  cursor: pointer
  >a
    color: white
    border-bottom: solid white 1px

nav
  width: 100%
  color: white

// dialog-content

.el-dialog
  width: 60% !important
  max-height: 50%
  margin-top: 5vh !important
  box-shadow: 0 0 0 !important
  background: transparent !important
  @media screen and (max-width: $break_small)
    width: 80% !important
    max-height: 70%

.upper-block-bkg
  height: 100px
  width: 100%
  background-image: url('https://storage.googleapis.com/froggy-service/frontend/images/cases/case-logo.png'), linear-gradient(to right, #63B8B7, #3FA8BC, #5676AC, #7F5596, #BB4577)
  background-position: top right, center
  background-size: auto 100%, 100%
  background-repeat: no-repeat, no-repeat
  overflow: hidden
  @media screen and (max-width: $break_small)
    display: none

.el-dialog__header
  background: linear-gradient(#004BE0, #9eaeca 0.05, #004BE0 0.1)
  padding-top: 30px !important
  border-radius: 10px 10px 0 0
  .el-dialog__title
    &:before
      background-image: url('https://storage.googleapis.com/froggy-service/frontend/images/cases/disk_icon.png')
      background-size: auto 100%
      background-repeat: no-repeat
      position: absolute
      width: 200px
      height: 20px
      top: 15px
      left: 12px
      font-size: 12px
      color: white
      content: "\00a0\00a0\00a0\00a0\00a0\00a0 C:\\邱威傑議員研究室"

  .el-dialog__headerbtn
    top: 10px
    right: 8px
  .el-icon-close
    border: white 1px solid
    border-radius: 3px
    background-color: #DC4C2C
    color: white !important
    width: 20px
    height: 20px
    &:before
      vertical-align: -15%
      font-weight: 700

.case-content-type-header
  color: white
  font-size: 2em
  font-weight: 500
  position: absolute
  top: 95px
  left: 25px
  @media screen and (max-width: 650px)
    display: none

.case-content-type-body
  font-size: 1.2em
  font-weight: 700
  @media screen and (min-width: 650px)
    display: none

.el-dialog__body
  box-sizing: border-box !important
  border-width: 5px 5px 0px 5px
  padding: 0 !important
  border-style: solid
  border-color: #004BE0
  background-color: #EEECE0
  .case-content
    padding: 20px 20px 5px 20px !important
    max-height: 50vh !important
    overflow: scroll
    &::-webkit-scrollbar
      width: 0 !important
    .case-content-title, .case-content-details, .arranges-title
      font-size: 1.2em
      font-weight: 700
    .case-content-date
      font-size: 1em
      font-weight: normal
.case-disapproved
  font-size: 1.2em
  font-weight: 700
.disapprove-info
  font-size: 1em
  font-weight: normal

.arrange-content>p>img
  width: 50%
  margin: 10px
  float: right
  display: block
  @media screen and (max-width: $break_medium)
    width: 100%

.el-dialog__footer
  height: 100px
  align-items: center
  display: flex !important
  box-sizing: border-box !important
  border-width: 0px 5px 5px 5px
  border-style: solid
  border-radius: 0px 0px 5px 5px
  border-color: #004BE0
  background-color: #EEECE0
  padding: 5px 10px 10px 10px !important
  @media screen and (max-width: $break_small)
    height: 80px
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
      height: 80%
      border: solid 3px black !important
      right: 25px!important
      box-sizing: border-box
      border-radius: 25px 10px
      background-color: white !important
      font-size: 1.5em
      font-weight: 700
      @media screen and (max-width: $break_small)
        font-size: calc(12px + 1.5vw)
        border-radius: 15px 5px
      .content-status
        flex: 1
        padding: 0px 20px 0px 20px
        text-align: right
</style>
