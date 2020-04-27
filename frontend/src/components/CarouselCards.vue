<template>
  <carousel
    class="carousel"
    :perPage="1"
    :perPageCustom="[
      [0, 1],
      [768, 2],
      [1024, 3]
    ]"
    :scrollPerPage="false"
    :centerMode="false"
    :loop=true
    :paginationEnabled="false"
    :spacePadding="35"
  >
    <slide v-for="i in 5">
      <div class="card-case">
        <img
          class="card-logo"
          :src="require('@/assets/images/card_logo.png')"
          alt=""
        />
        <div class="card-content">
          <div class="card-info">
            <div class="card-info-title">案件標題：案件標題</div>
            <div class="card-info-title">時間：2020 年 02 月 26 日</div>
            <div class="card-info-title">地點：台北市信義區鬍鬚張附近</div>
          </div>
          <hr>
          <div class="card-details">
            <div class="card-info-title">案件內容</div>
            <div class="card-details-text">
              小弟我是台北市民，常常看到很多人亂倒垃圾，請問大家會不會覺得台北市的人太沒道德？
            </div>
          </div>
          <hr>
          <div class="card-progress">
            <div class="card-info-title">案件處理進度</div>
            <div class="card-progress-text">
              無法幫忙，謝謝指教
            </div>
            <div class="card-progress-icon">
              處理進度：已結案
            </div>
          </div>
        </div>
      </div>
    </slide>
  </carousel>
</template>

<style lang="scss" scoped>
@import "@/assets/css/style.sass";

.carousel {
  .card-case {
    position: relative;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    height: 400px;
    background-image: linear-gradient(
      #ffffff,
      #a2cee5,
      #b69fc6,
      #c480a2,
      #de8f95,
      #efcacd
    );
    background-position: center;
    background-size: contain;
    background-repeat: no-repeat;
    border-radius: 5%;
    border: #fff 0.6rem solid;
    margin: 0 10px;
    color: black;
    overflow: hidden;
    .card-content {
      color:#606266;
      width: 80%;
      height: calc(100% - 60px);
      border-radius: 5%;
      background-color: #fff;
      z-index: 10;
      margin-top: 40px;
      padding: 5px 10px;
      .card-info-title{
        font-size: 0.8em;
        font-weight: bold;
        line-height: 2em;
      }
      .card-details-text, .card-info-text, .card-progress-text{
        font-size: 0.8em;
      }
      .card-progress-icon{
        border: 2px solid #606266;
        width: fit-content;
        border-radius: 15px 5px 15px 5px;
        margin-top: 10px;
        padding: 8px 5px;
        float: right;
      }
    }
    .card-logo {
      position: absolute;
      right: 0;
      top: 0;
      width: 60%;
      max-width: 150px;
      transform: translate3D(20px, -25px, 0);
      z-index: 5;
    }
  }
}

// .carousel {
//   width: 100%;
//   display: flex;
//   flex-direction: row;
//   align-items: flex-start;
//   justify-content: center;

//   @media screen and (max-width: $break_small) {
//     flex-direction: column;
//     align-items: center;
//     justify-content: center;
//   }
// }
</style>

<script>
import { Carousel, Slide } from "vue-carousel";

export default {
  name: "CarouselCard",
  components: {
    Carousel,
    Slide
  },
  props: {},
  data() {
    return {};
  },
  watch: {},
  methods: {},
  computed: {},
  mounted() {}
};
</script>
