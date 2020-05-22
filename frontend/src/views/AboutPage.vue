<template>
  <About id="about"></About>
</template>

<script>
import About from '@/components/About.vue'

export default {
  name: 'Home',
  data: function () {
    return {
    }
  },
  components: { About }
}
</script>

<style lang="sass">

@import '@/assets/css/style.sass'

.about-main .el-dialog
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
      .content-state
        flex: 1
        padding: 0px 20px 0px 20px
        text-align: right

.el-loading-mask.is-fullscreen, .el-loading-mask
  z-index: 9999 !important

.el-loading-spinner>i,.el-loading-text
  color: $color_white !important
</style>
