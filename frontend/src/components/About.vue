<template lang="pug">
el-container.page3
  el-main
    el-row.about-main(type="flex" align="middle" justify="center")
      el-col(:span=24)
        .about-title
          h1 公開透明。
      el-col(:span=24)
        el-row(type="flex" align="middle" justify="center")
          el-col(:span=14)
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
          el-col(:span=10)
            img.froggyServantImg(:src="froggyservantUrl")
    BottomGameDialog(:title="title")
    el-row.footer-row(type="flex" align="middle" justify="center")
      el-col.footer
        span
          |「選服魔鏡號」台北市議員邱威傑市民服務系統
          | 110 台北市信義區仁愛路四段507號 台北市議會 752研究室
          | 02-27297708 分機 7152、7252
          | 02-87862707
          | servant@65535studio.com
</template>

<script>
import BottomGameDialog from './BottomGameDialog.vue'
export default {
  name: 'About',
  components: {BottomGameDialog},
  data: function(){
    return{
      title: ['選服魔鏡號 市民看得到', '－台北市議員邱威傑市民服務系統...'],
      froggyservantUrl: 'https://s3-ap-southeast-1.amazonaws.com/o-r-z/froggy-service/froggy_servant.png'
    }
  },
  props: ['lorem']
}
</script>

<style lang="sass" scoped>
.page3
  background-image: url('https://s3-ap-southeast-1.amazonaws.com/o-r-z/froggy-service/dark_gradient_background.png')
  // background-position: center
  overflow: hidden

.el-main
  display: flex
  flex-shrink: 0
  flex-grow: 1
  flex-direction: column
  width: 100%
  height: 100vh
  align-items: center
  justify-content: center

.el-row
  width: 100%
.about-main
  flex: 7
  flex-direction: column
.row-dialog
  flex: 1
.about-title
    margin-top: 20px
    margin-bottom: 20px
    color: white
    h1
      font-size: 24px
article
  .about-content
    max-height: 60vh
    overflow: scroll
    color: white
    span
      font-size: 0.8em

.froggyServantImg
  width: 100%

.text-center
  text-align: center

.footer-row
  margin: auto auto 0 auto
  height: 50px
  .footer
    bottom: 0
    text-align: center
    color: white
</style>
