<template lang="pug">
el-container.page3
  transition(name="fade")
    el-row.about-main(type="flex" align="middle" justify="center")
      el-col(:span=22 :offset=2)
        h1 公開透明。
      el-col(:span=22 :offset=2)
        el-row(type="flex" align="middle" justify="center")
          el-col(:span=16)
            article
              .about-content
                span 我們都知道，這是一個已經喊了十幾年的口號，但時間過去了，政治，仍然是一件跟人心一樣複雜的事。
                br
                br
                span 市議員選舉前，我揭露了商業電視台業配新聞的真相，也開啟了「民主開箱」的這條路。過去我們所認為的選民服務，可能不外乎就是一個字「喬」——搶床位、喬事情，我想問的是：民意代表的專業在哪裡？有為大眾發揮監督的功能嗎？
                br
                br
                span 這個「選服魔鏡號」是我的政見之一，只要你生活在台北市，你的意見、你覺得政府該做而沒做好、或是不知道該請誰幫忙的，都可以找我們協助。
                br
                br
                span 但，只關乎個人利益的，我們不碰；不屬於民代職權的，我們不做！我的團隊會在收到案件後進行隱私處理，並在第一時間向全體市民公布：一個市議員，到底做了什麼、又應該做些什麼？
                br
                br
                span 這是「民主開箱」第一步，未來四年，我們繼續前進！
                br
                br
                h2 邱威傑
          el-col(:span=8)
            img.froggyServantImg(:src="froggyservantUrl")
  BottomGameDialog(:title="title")
</template>

<script>
import BottomGameDialog from './BottomGameDialog.vue'
export default {
  name: 'About',
  components: { BottomGameDialog },
  data: function () {
    return {
      title: ['選服魔鏡號 市民看得到', '－台北市議員邱威傑市民服務系統...'],
      froggyservantUrl: 'https://s3-ap-southeast-1.amazonaws.com/o-r-z/froggy-service/froggy_servant.png'
    }
  },
  props: ['lorem']
}
</script>

<style lang="sass" scoped>
.page3
  background-image: linear-gradient(rgba(255,255,255,0),rgba(61,78,87,0.8),rgba(0,0,0,0.9), rgba(0,0,0,1),rgba(0,0,0,1)), linear-gradient(#EFCACD, #DE8F95, #C480A2, #B69FC6, #A2CEE5, #FFFFFF)
  background-position: center, center
  background-size: contain
  background-repeat: no-repeat,no-repeat
  overflow: hidden
  height: 100%
  width: 100%
  flex-direction: column

.el-row
  width: 100%
.about-main
  flex: 3
  flex-direction: column
.row-dialog
  flex: 1
h1
  color: white
  font-size: 3em
article
  overflow: scroll
  .about-content
    // max-height: 60vh
    overflow: scroll
    color: white
    span
      font-size: 1em

.froggyServantImg
  width: 100%
  transform: scale(1.5) translate3d(-5px ,50px,0)
.text-center
  text-align: center

.footer-row
  margin: auto auto 0 auto
  height: 50px
  .footer
    bottom: 0
    text-align: center
    color: white
.fade-enter-active, .fade-leave-active
  transition: opacity .5s
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */
  opacity: 0
</style>
