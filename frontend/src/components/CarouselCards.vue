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
    :centerMode="true"
    :autoplay="false"
    :loop="false"
    :navigationEnabled="true"
    :spacePadding="25"
    :paginationEnabled="false"
    :paginationPosition="`bottom`"
  >
    <slide v-for="i in 5">
      <div class="card-case" @mousemove="mousemove" @mouseleave="mouseleave">
        <img
          class="card-logo"
          :src="require('@/assets/images/card_logo.png')"
          alt=""
        />
        <div class="card-content">
          <div class="card-info">
            <div class="card-info-title">案件標題：案件標題{{ i }}</div>
            <div class="card-info-title">時間：2020 年 02 月 26 日</div>
            <div class="card-info-title">地點：台北市信義區鬍鬚張附近</div>
          </div>
          <hr />
          <div class="card-details">
            <div class="card-info-title">案件內容</div>
            <div class="card-details-text">
              小弟我是台北市民，常常看到很多人亂倒垃圾，請問大家會不會覺得台北市的人太沒道德？
            </div>
          </div>
          <hr />
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
    // box-shadow: -3px -3px 3px 0 rgba(#26e6f7, 0.6),
    //   3px 3px 3px 0 rgba(#f759e4, 0.6), 0 0 6px 2px rgba(#ffe759, 0.6),
    //   0 35px 25px -15px rgba(0, 0, 0, 0.5);
    box-shadow: 0px 0px 2px 0 rgba(#000,0.3), 5px 5px  5px 0 rgba(#000,0.3);
    border-radius: 5%;
    // border: #fff 0.1rem solid;
    margin: 10px 10px;
    color: black;
    overflow: hidden;
    &:before,
    &:after {
      content: "";
      position: absolute;
      left: 0;
      right: 0;
      bottom: 0;
      top: 0;
      // background-image: linear-gradient(
      //   115deg,
      //   transparent 0%,
      //   rgba(#a2cee5, 1) 20%,
      //   rgba(#b69fc6, 1) 40%,
      //   rgba(#c480a2, 1) 60%,
      //   rgba(#de8f95, 1) 80%,
      //   transparent 100%
      // );
      background-position: 0% 0%;
      background-repeat: no-repeat;
      background-size: 400% 400%;
      mix-blend-mode: color-dodge;
      opacity: 1;
      z-index: 15;
      // animation: holoGradient 15s ease infinite;
    }
    &:after {
      background-image: url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/13471/sparkles.gif");
      background-position: center;
      background-size: 180%;
      mix-blend-mode: color-dodge;
      opacity: 0;
      z-index: 20;
      animation: holoSparkle 20s ease infinite;
    }
    &.active:before {
      opacity: 1;
      animation: holoGradient 1.5s ease-out forwards;
      transition: none;
      // background-image: linear-gradient(
      //   115deg,
      //   transparent 0%,
      //   transparent 25%,
      //   rgba(0, 231, 255, 0.7) 45%,
      //   rgba(255, 0, 231, 0.7) 55%,
      //   transparent 70%,
      //   transparent 100%
      // );
      background-image: linear-gradient(
        115deg,
        transparent 0%,
        rgba(#02151f, 1) 50%,
        rgba(#b69fc6, 1) 55%,
        rgba(#c480a2, 1) 60%,
        rgba(#de8f95, 1) 65%,
        transparent 100%,
      );
    }
    .card-content {
      color: #606266;
      width: 80%;
      height: calc(100% - 60px);
      border-radius: 5%;
      background-color: #fff;
      z-index: 10;
      margin-top: 40px;
      padding: 5px 10px;
      .card-info-title {
        font-size: 0.8em;
        font-weight: bold;
        line-height: 2em;
      }
      .card-details-text,
      .card-info-text,
      .card-progress-text {
        font-size: 0.8em;
      }
      .card-progress-icon {
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

@keyframes holoGradient {
  0% {
    background-position: 100% 100%;
  }
  100% {
    background-position: -100% -100%;
  }
}
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
  methods: {
    mousemove(e) {
      let card = e.target;
      let l = e.offsetX;
      let t = e.offsetY;
      let h = card.clientHeight;
      let w = card.clientWidth;
      let lp = Math.abs(Math.floor((100 / w) * l) - 100);
      let tp = Math.abs(Math.floor((100 / h) * t) - 100);
      let bg = `background-position: ${lp}% ${tp}% !important;`;
      let style = `.card-case.active:before { ${bg}}`;
      card.classList.add("active");
      // document.getElementsByClassName("hover")[0].innerHTML = style;
    },
    mouseleave(e) {
      let card = e.target;
      card.classList.remove("active");
    }
  },
  computed: {},
  mounted() {
    // var styleElem = document.createElement("style");
    // styleElem.className = "hover";
    // document.head.appendChild(styleElem);
  }
};
</script>
