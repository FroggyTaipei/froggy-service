<template lang="pug">
el-container.page3
  el-main
    el-row(type="flex" align="middle" justify="center")
      el-menu(theme='dark', default-active='0', mode='horizontal', :router='false')
        el-menu-item(index='#firstPage')
          a(href="#firstPage") 我要服務
        el-menu-item(index='#secondPage')
          a(href="#secondPage") 呱吉做什麼
        el-menu-item(index='#thirdPage')
          a(href="#thirdPage") 關於魔鏡號
    el-row(type="flex" align="middle" justify="center")
      el-col(:span=18)
        el-row(type="flex" align="middle" justify="center")
          el-col(:span=14)
            article
              .about-title
                h1 選服魔鏡號 市民看得到
                h1 －台北市議員邱威傑市民服務系統
              .about-content
                span 公開透明。
                br
                br
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
            h1.text-center Image
            image
    el-row.footer-row(type="flex" align="middle" justify="center")
      el-col.footer
        h1 Footer
</template>

<script>
// import Footer from './Footer.vue'
export default {
  name: 'About',
  // components: {Footer},
  props: ['lorem']
}
</script>

<style lang="sass" scoped>
.page3
  background-image: url('https://s3-ap-southeast-1.amazonaws.com/o-r-z/froggy-service/gradient_background.png')
  background-position: center
  overflow: hidden

.el-main
  min-height: 100vh
  display: flex
  flex-direction: column

.el-menu--horizontal
  border: none
.el-menu--horizontal>.el-menu-item.is-active
  border-bottom-color: transparent
  border-bottom: none
.el-menu-item
  a
    text-decoration: none
article
  .about-title
    margin-top: 20px
    margin-bottom: 20px
    h1
      font-size: 24px
  .about-content
    max-height: 60vh
    overflow: scroll
    span
      font-size: 18px

.text-center
  text-align: center

.footer-row
  margin: auto auto 0 auto
  height: 20%
  width: 100%
  background-color: gray
  .footer
  bottom: 0
  text-align: center
</style>
