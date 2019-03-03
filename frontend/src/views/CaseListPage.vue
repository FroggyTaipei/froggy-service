<template>
  <CaseList id="cases"></CaseList>
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
@import url('https://use.fontawesome.com/releases/v5.7.2/css/all.css')

.searchField
  height: auto !important
  margin-top: 20px
  .searchInput
    width: auto !important
    margin-right: 20px
  .el-input__inner:focus
    border-color: $color_gray !important
  .searchButton
    background-color: $color_gray !important
    border-color: $color_gray !important
    color: $color_white

table
  width: 100%
  color: white
  border-spacing: unset
  border-collapse: collapse
  thead
    border-bottom: solid 2px white !important
    line-height: 2em
  tbody:before
    content: "-"
    display: block
    line-height: 1em
    color: transparent
  thead>tr>th
    font-size: $fz_sub_header_small
    @media screen and (max-width: $break_small)
      font-size: $fz_sub_header_small
  tbody>tr
    transition: 0.1s
    &:hover
      color: black
      background-color: white
      transition: 0.2s
      cursor: pointer
    &>td
      font-size: $fz_p
      padding: 0px 5px
      text-align: center
      line-height: 1.8em
      @media screen and (max-width: $break_small)
        font-size: $fz_p_small
      &:nth-child(4)
        text-align: left

.VueTables.VueTables--server
  height: 100%
  display: flex
  flex-direction: column
  align-items: center
  justify-content: flex-start
  &>.row>.col-md-12
    margin: 10px 0px 20px 0px
  .table-responsive
    width: 100%
    overflow: scroll
    border-bottom: 2px solid white
    margin-bottom: 100px
    &::-webkit-scrollbar
      width: 0 !important

.VueTables__sort-icon
  margin-left: 5px

.VueTables__search-field
  display: none
  color: $color_white
  margin-top: 50px
  @media screen and (max-width: $break_small)
    margin-top: 20px
  label
    margin-right: 20px
    font-size: $fz_p_small
  input
    font-size: 14px
    border-radius: 4px !important
    border: none
    height: 30px
    padding-left: 15px

.VuePagination
  position: absolute
  bottom: 0

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
      font-size: 20px
      color: $color_gray
      font-weight: 600
      @media screen and (max-width: 480px)
        font-size: 24px

.VuePagination li.disabled, .VuePagination__pagination li.disabled, .VuePagination__count li.disabled
  >a
    color: transparent

.VuePagination li.active, .VuePagination__pagination li.active, .VuePagination__count li.active
  cursor: pointer
  >a
    color: $color_white
    border-bottom: solid white 1px

.VuePagination__pagination-item.page-item
  @media screen and (max-width: 480px)
    a[role='button']
      display: none

nav
  width: 100%
  color: $color_white

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
  background-image: linear-gradient(to right, #63B8B7, #3FA8BC, #5676AC, #7F5596, #BB4577)
  border-radius: 5px 5px 0 0

  .el-dialog__headerbtn
    top: 0px
    right: 8px
  .el-icon-close
    color: white !important
    &:before
      vertical-align: -15%
      font-weight: 700

.case-content-type-header
  color: white
  font-size: $fz_p_header
  font-weight: 700
  position: absolute
  top: 75px
  left: 25px
  @media screen and (max-width: $break_small)
    display: none

.case-content-type-body
  font-size: $fz_p
  font-weight: 700
  @media screen and (min-width: $break_small)
    display: none

.el-dialog__body
  box-sizing: border-box !important
  border-width: 5px 5px 0px 5px
  padding: 0 !important
  background-color: $color_white
  .case-content
    padding: 20px 20px 5px 20px !important
    max-height: 50vh !important
    overflow: scroll
    white-space: pre-line
    &::-webkit-scrollbar
      width: 0 !important
    .case-content-title, .case-content-date, .case-content-location, .case-content-details, .arranges-title
      font-size: $fz_sub_header_small
      font-weight: 700
      margin-top: 5px

.case-disapproved
  font-size: $fz_p
  font-weight: bold
.disapprove-info
  font-weight: normal

.arrange-content
  white-space: normal

.arrange-content>p>img, .arrange-content img
  width: 50% !important
  height: auto !important
  margin: 10px
  display: block
  @media screen and (max-width: $break_small)
    width: 100% !important

.el-dialog__footer
  height: 100px
  align-items: center
  display: flex !important
  box-sizing: border-box !important
  border-radius: 0px 0px 5px 5px
  background-color: $color_white
  padding: 5px 10px 10px 10px !important
  @media screen and (max-width: $break_small)
    height: 80px
  .dialog-footer
    width: 100%
    height: 100%
    display: flex !important
    align-items: center
    justify-content: flex-end
    color: $color_black
    .footer-block
      display: flex !important
      align-items: center
      justify-content: center
      height: 80%
      min-width: 200px
      border: solid 3px #606266 !important
      color: #606266
      right: 25px!important
      box-sizing: border-box
      border-radius: 25px 10px
      background-color: white !important
      font-size: $fz_sub_header
      font-weight: 700
      @media screen and (max-width: $break_small)
        font-size: calc(12px + 1.5vw)
        border-radius: 15px 5px
      .content-status
        flex: 1
        padding: 0px 20px 0px 20px
        text-align: right

.el-loading-mask.is-fullscreen, .el-loading-mask
  z-index: 9999 !important

.el-loading-spinner>i,.el-loading-text
  color: $color_white !important
</style>
