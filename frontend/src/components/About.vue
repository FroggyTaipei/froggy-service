<template lang="pug">
el-container(style="align-items: center;").page3
  transition(name="fade" @after-leave="redirect")
    el-row.about-main(type="flex" align="middle" justify="center" style="max-width: 1024px" v-show="showMainContent")
      el-col.about-title-wrapper(:span=22)
        .about-title 公開透明。
      el-col.about-content-wrapper(:span=22)
        el-row(type="flex" align="middle" justify="center")
          el-col.noScrollbar(:span=15 :sm="24" :xs="24" style="height: 100%;")
            article
              .about-content
                span 口號喊了十幾年，政治仍然跟人心一樣複雜。
                br
                br
                span 密室的會談，檯面下的交換。我們用作秀來度量政治的專業，用喬事的廣度來判斷代議士服務的態度。要杜絕喬罰單與床位這類弊病，選民服務應該要和市政質詢一樣，可以被公開監督。
                br
                br
                span 「選服魔鏡號」是我的政見。只要你生活在台北市，你的意見、你覺得政府該做而沒做好、或是不知道該請誰幫忙的，都可以找我們協助。
                br
                br
                span 但，只關乎個人利益的，我們不碰；不屬於民代職權的，我們不做！
                br
                br
                span 我的團隊會在收到案件後進行隱私處理，並在第一時間向全體市民公布：一個市議員，到底做了什麼、又應該做些什麼？
                br
                br
                span 這是「民主開箱」第一步，未來四年，我們繼續前進！
                br
            img.signImg(:src="froggySignUrl")
          el-col.hidden-xs-only(:span=8 :offset=1)
            img.froggyServantImg( v-lazy="froggyAboutUrl" )
  BottomGameDialog(:title="aboutTitle")
</template>

<script>
import BottomGameDialog from './BottomGameDialog.vue'
export default {
  name: 'About',
  components: { BottomGameDialog },
  data: function () {
    return {
      showMainContent: false,
      aboutTitle: ['「選民魔鏡號，市民看得到！」－台北市議員邱威傑市民服務系統⋯⋯', '不要再點了，上面我說的話好好看！'],
      froggyservantUrl: 'https://storage.googleapis.com/froggy-service/frontend/images/about/froggy_servant.png',
      froggyAboutUrl: 'https://storage.googleapis.com/froggy-service/frontend/images/about/g2-2_s_center.png',
      froggySignUrl: 'https://storage.googleapis.com/froggy-service/frontend/images/about/froggy_sign_s.png'
    }
  },
  mounted () {
    this.showMainContent = true
  },
  methods: {
    toggleLeaveAnimation: function (destination) {
      this.showMainContent = false
    },
    redirect: function () {
      let direction = this.$store.state.redirectTo
      this.$router.push(direction)
    }
  }
}
</script>

<style lang="sass" scoped>
@import '@/assets/css/style.sass'

.page3
  background-image: linear-gradient(#EFCACD, #DE8F95, #C480A2, #B69FC6, #A2CEE5, #FFFFFF)
  background-position: center
  background-size: contain
  background-repeat: no-repeat
  overflow: hidden
  height: 100%
  width: 100%
  flex-direction: column

.el-row
  width: 100%

.darkBackground
  position: absolute
  z-index: 2
  height: 100%
  width: 100%
  background-position: center
  background-size: contain
  background-repeat: no-repeat

.about-main
  z-index: 5
  flex: $flex_mainContentPart
  flex-direction: column
  flex-shrink: 0
  @media screen and (max-width: $break_small)
    flex: 8
.row-dialog
  z-index: 5
  flex: $flex_dialogPart
  @media screen and (max-width: $break_small)
    flex: 2

.about-title-wrapper
  color: white
  font-size: 2em
  min-height: 100px
  font-weight: bold
  .about-title
    padding: 30px 0 0 0
.about-content-wrapper
  display: flex

article
  .about-content
    color: white
    span
      font-size: 1em
.signImg
  width: 150px

.froggyServantImg
  width: 100%
  transform: scale(1.5) translate3d(-5px ,-15px,0)
  -webkit-mask-image: -webkit-gradient(linear, left 90%, left bottom, from(rgba(0,0,0,1)), to(rgba(0,0,0,0)))

.text-center
  text-align: center

.footer-row
  margin: auto auto 0 auto
  height: 50px
  .footer
    font-size: 12px
    bottom: 0
    text-align: center
    color: white

.noScrollbar
  overflow: scroll
  overflow: -moz-scrollbars-none
  -ms-overflow-style: none
  &::-webkit-scrollbar
      width: 0 !important
</style>
