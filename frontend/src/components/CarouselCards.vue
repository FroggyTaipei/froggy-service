<template>
  <div class="card-cases">
    <div class="wrapper" v-for="(c, i) in cases">
      <div class="hidden-froggy">
        <img
          src=""
          alt=""
          :src="
            `https://storage.googleapis.com/froggy-service/frontend/images/about/froggy_report_${froggy_imgs.urls[i]}.png`
          "
        />
      </div>
      <div
        class="card-case"
        @mousemove="mousemove"
        @mouseleave="mouseleave"
        @click="click(c.id)"
      >
        <img
          class="card-logo"
          src="https://storage.googleapis.com/froggy-service/frontend/images/about/card_logo.png"
          alt=""
        />
        <div class="card-content">
          <div class="card-info">
            <div class="card-info-title">{{ c.title }}</div>
            <div class="card-info-title">
              時間：{{ c.create_time.split("-")[0] }} 年
              {{ c.create_time.split("-")[1] }} 月
              {{ c.create_time.split("-")[2] }} 日
            </div>
            <div class="card-info-title">地點：{{ c.location }}</div>
          </div>
          <hr />
          <div class="card-details">
            <div class="card-info-title">案件內容</div>
            <div class="card-details-text">
              {{
                c.content.length > 50
                  ? `${c.content.slice(0, 50)}...`
                  : c.content
              }}
            </div>
          </div>
          <!-- <hr /> -->
          <div class="card-progress">
            <!-- <div class="card-info-title">案件處理進度</div>
            <div class="card-progress-text">
              {{c.state}}
            </div> -->
            <div class="card-progress-icon">處理進度：{{ c.state }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "@/assets/css/style.sass";

// .carousel
.card-cases {
  display: flex;
  position: relative;
  .wrapper {
    position: relative;
    width: 100%;
    height: 400px;
    overflow: hidden;
    padding-bottom: 20px;
    .hidden-froggy {
      position: absolute;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      height: 100%;
      img {
        height: 90%;
      }
    }
  }
  .card-case {
    // opacity: 0.5;
    position: relative;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    height: 100%;
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
    box-shadow: 0px 0px 2px 0 rgba(#000, 0.3), 5px 5px 5px 0 rgba(#000, 0.3);
    border-radius: 5%;
    margin: 10px 10px;
    color: black;
    overflow: hidden;
    transition: 0.5s;
    &:hover {
      cursor: pointer;
    }
    &:before,
    &:after {
      content: "";
      position: absolute;
      border-radius: 5%;
      left: 0;
      right: 0;
      bottom: 0;
      top: 0;
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
      border-radius: 5%;
      animation: holoGradient 1.5s ease-out forwards;
      transition: none;
      background-image: linear-gradient(
        115deg,
        transparent 0%,
        rgba(#02151f, 1) 50%,
        rgba(#b69fc6, 1) 55%,
        rgba(#c480a2, 1) 60%,
        rgba(#de8f95, 1) 65%,
        transparent 100%
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
        position: absolute;
        right: 10%;
        bottom: 20px;
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
      transform: translate3D(15px, -20px, 0);
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
    return {
      cardNum: 3,
      froggy_imgs: { urls: [...Array(6).keys()].map(i => i + 1) },
      cases: [],
      excludes: [],
      timer: null,
      clickable: true
    };
  },
  methods: {
    randomCase() {
      let cards = document.getElementsByClassName("card-case");

      // this.timer = setTimeout(() => {
      //   this.clickable = true;
      // }, 400* cards.length);
      // if (!this.clickable) return;
      // this.clickable = false;

      this.shuffleImg();
      setTimeout(() => {
        this.getRandomCases();
      }, 350 * cards.length);
      setTimeout(() => {
        for (let i = 0; i < cards.length; i++) {
          setTimeout(() => {
            cards[i].style.transform = "translateX(-200%)";
            setTimeout(() => {
              cards[i].style.transform = "translateX(0)";
            }, 300 * cards.length);
          }, 200 * i);
        }
      }, 350);
    },
    shuffleImg() {
      let urls = this.froggy_imgs.urls;
      for (let i = urls.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [urls[i], urls[j]] = [urls[j], urls[i]];
      }
      this.froggy_imgs = {}; //update template
      this.froggy_imgs["urls"] = urls;
      this.clickable = false;
    },
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
    },
    click(id) {
      this.$parent.$parent.$parent.$parent.click(id);
    },
    getRandomCases() {
      axios
        .get(
          `/api/cases?ordering=?&limit=${
            this.cardNum
          }&exclude_ids=${this.excludes.join()}`
        )
        .then(res => {
          let cases = res.data.results;
          let excludes = cases.map(c => c.id);
          this.cases = cases;
          this.excludes = this.excludes.concat(excludes);
        });
    },
    setCardNum() {
      let width = window.innerWidth;
      let num = 3;
      if (width < 768) {
        num = 1;
      }
      if (width >= 768 && width < 1024) {
        num = 2;
      }
      this.cardNum = num;
    }
  },
  mounted() {
    this.setCardNum();
    window.addEventListener("resize", this.setCardNum);
    this.getRandomCases();
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.setCardNum);
  }
};
</script>
