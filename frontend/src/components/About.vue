<template>
  <el-container class="page3" style="align-items: center;">
    <transition name="fade" @after-leave="redirect">
      <el-row
        class="about-main"
        type="flex"
        align="middle"
        justify="start"
        style="max-width: 1024px;"
        v-show="showMainContent"
        ref="main"
      >
        <!-- <el-col class="about-title-wrapper" :span="22">
          <div class="about-title"></div>
        </el-col> -->
        <el-col class="about-content-wrapper" :span="22">
          <el-row type="flex" align="middle" justify="center">
            <el-col class="noScrollbar" :span="15" :sm="24" :xs="24">
              <article>
                <div class="about-content">
                  <div class="about-title">公開透明。</div>
                  <span>口號喊了十幾年，政治仍然跟人心一樣複雜。</span>
                  <br />
                  <br />
                  <span
                    >密室的會談，檯面下的交換。我們用作秀來度量政治的專業，用喬事的廣度來判斷代議士服務的態度。要杜絕喬罰單與床位這類弊病，選民服務應該要和市政質詢一樣，可以被公開監督。</span
                  >
                  <br />
                  <br />
                  <span
                    >「選服魔鏡號」是我的政見。只要你生活在台北市，你的意見、你覺得政府該做而沒做好、或是不知道該請誰幫忙的，都可以找我們協助。</span
                  >
                  <br />
                  <br />
                  <span
                    >但，只關乎個人利益的，我們不碰；不屬於民代職權的，我們不做！</span
                  >
                  <br />
                  <br />
                  <span
                    >我的團隊會在收到案件後進行隱私處理，並在第一時間向全體市民公布：一個市議員，到底做了什麼、又應該做些什麼？</span
                  >
                  <br />
                  <br />
                  <span>這是「民主開箱」第一步，未來四年，我們繼續前進！</span>
                  <br />
                </div>
              </article>
              <img class="signImg" :src="froggySignUrl" />
            </el-col>
            <el-col class="hidden-xs-only" :span="8" :offset="1">
              <img
                class="froggyServantImg"
                src="https://storage.googleapis.com/froggy-service/frontend/images/about/g2-2_s_center.png"
              />
            </el-col>
          </el-row>
        </el-col>
        <el-col class="report" :span="22">
          <div class="report-content-wrapper">
            <div class="report-intro">
              <!-- <h1 id="report" class="report-header">
                選服魔鏡號一週年報告！
              </h1> -->
              <img
                id="report"
                class="report-logo"
                src="https://storage.googleapis.com/froggy-service/frontend/images/about/report_logo.png"
                alt="report-logo"
              />
              <span>
                從2019年3月，我們的「選服魔鏡號－台北市議員邱威傑市民服務系統」正式上線以來，已經整整過一年啦！在這一年來，我和我的團隊處理了超過一千一百件的市民服務需求，有來自對台北市的政策建議、交通問題反應、個人問題陳情，我們特別將所有資料視覺化，一起來看看有哪些有趣的結果吧！
              </span>
            </div>
            <el-divider></el-divider>
            <h2 class="report-title">
              你最愛的：魔鏡號裡到底在幹嘛？
            </h2>
            <div class="report-flow">
              <div>
                每當我們接到你透過魔鏡號（或者是直接打電話給我們）告訴我們的服務需求，我們就會立刻發送一封E-mail到你的信箱，確認我們已經收到並開始著手處理；接下來，我們會先將涉及隱私的資訊進行處理，確保每位朋友的身分不會被輕易辨識出來，同時我們會將案件進行初步分類，通常有以下幾種情形：
              </div>
              <br />
              <Workflow v-if="!isSmall"></Workflow>
              <img
                v-if="isSmall"
                class="report-flowchart"
                src="https://storage.googleapis.com/froggy-service/frontend/images/about/workflow.svg"
                alt=""
              />
              <br />
              <ul v-if="isSmall">
                <li>
                  可處理：沒錯，這些都是跟我們有關的案件！作為台北市議員，我們可以把你所遇到的問題或政策建議，透過舉辦會勘要求市府各局處一同檢討，或納入我們的質詢選題，要求市府做出正式、可追蹤的改善回覆。
                </li>
                <li>
                  可處理但涉及中央或其他縣市：這些事情都是很重要的公共議題，但是它們可能不完全在台北市議員能夠處理的範圍。所以，我們會聯絡相關的辦公室，無論是立法委員、其他縣市的縣市議員辦公室，只要我們找得到人的，就一定會幫忙轉介你所遇到的問題，請我的好朋友們協助解決！
                </li>
                <li>
                  無法處理：等等，你是不是搞錯了什麼？如果遇到這個分類，通常你是提出了一些與公益無關的要求，或者是與台北市議員職務無關的訊息。我們有遇過幫忙做寒假作業、腦內思想被讀取（？）、喬當兵時間等等的，實在是不好意思，我們會給你一個大大的「不受理」！
                </li>
              </ul>
            </div>
            <el-divider></el-divider>
            <div class="report-charts">
              <h2 class="report-title">一起來看看大家最愛用魔鏡號做什麼！</h2>
              <h3 class="chart-title">「魔鏡號」一週年案件數量</h3>
              <div class="report-chart">
                <div id="chart-casesum" class="chart-graph chart-content">
                  <!-- <img :src="require('@/assets/images/chart1.png')" alt="" /> -->
                </div>
                <div class="chart-text chart-content">
                  從2019年3月至今，我們一共處理了超過一千一百多件的市民服務案件，每個月平均經手近百件，雖然不一定是全台北市議會最多的，但絕對是不少的！市民朋友們的陳情，也都成為我們累積市政監督經驗最重要的養分，我們還會繼續努力下去！
                </div>
              </div>
              <el-divider></el-divider>
              <h3 class="chart-title">大家最關心的案件類型</h3>
              <div class="report-chart report-chart-reverse">
                <div id="chart-casetype" class="chart-graph chart-content">
                  <!-- <img :src="require('@/assets/images/chart2.png')" alt="" /> -->
                </div>
                <div class="chart-text chart-content">
                  我們分析了所有透過魔鏡號向我們尋求協助的案件，在七個議題分類中，大家最關心的就是「交通運輸」，超過三分之一以上的朋友跟我們反應包括機車停車、公車行駛安全、待轉區狹小等問題；其次則是「環境建管」中，舉凡違建拆除、低頻噪音、河川污染等都屬於這個案件類型！
                </div>
              </div>
              <el-divider></el-divider>
              <h3 class="chart-title">什麼關鍵字最常被提到？</h3>
              <div class="report-chart report-chart-wordcloud">
                <div id="chart-wordcloud" class="chart-graph chart-content">
                  <!-- <img :src="require('@/assets/images/chart3.jpg')" alt="" /> -->
                </div>
                <div class="chart-text chart-content">
                  你知道嗎？「機車」是過去一年來，大家最常在魔鏡號跟我們提到的關鍵字，一共出現超過550次，出現在危險路段、禁行機車段、專用道等問題；第二名的關鍵字是「停車」，包含停車格太少、佔用通道；第三名則是「交通」。點一下關鍵字，你就可以看到跟它相關的案件！
                </div>
              </div>
              <!-- <div class="chart-paragraph">
                （內文－簡單說明上面幾個數字）指些修。些發統變存響是化美他直研動國種人空！動陸了就媽事，地家業也當價到正他片得可下，過放食我頭情，意多到社源成光。
              </div> -->
            </div>
            <el-divider></el-divider>
            <h2 class="report-title region-title">你在哪一區？</h2>
            <SvgMap></SvgMap>
            <el-divider></el-divider>
            <div class="report-title random-title">
              <div>
                隨機看案件，歡迎進入魔鏡號！
              </div>
              <a class="randomcase" @click="randomCase">
                <img
                  src="https://storage.googleapis.com/froggy-service/frontend/images/about/icon_change.png"
                  alt="change-icon"
                />
              </a>
            </div>

            <CarouselCards ref="carouselCards"></CarouselCards>
          </div>
        </el-col>
        <el-dialog title :visible.sync="dialogVisible" @closed="closeDialog">
          <div class="upper-block">
            <div class="upper-block-bkg">
              <div class="case-content-type-header">
                {{ selectedCaseDetails.type }}
              </div>
            </div>
          </div>
          <div class="case-content">
            <div class="case-content-type-body">
              案件類別：{{ selectedCaseDetails.type }}
            </div>
            <div class="case-content-title">
              案件標題：{{ selectedCaseDetails.title }}
            </div>
            <div class="case-content-date">
              時間：{{ selectedCaseDetails.create_time.split("-")[0] }} 年 {{ selectedCaseDetails.create_time.split("-")[1] }} 月 {{ selectedCaseDetails.create_time.split("-")[2] }} 日
            </div>
            <div
              class="case-content-location"
              v-if="selectedCaseDetails.location !== null"
            >
              地點：{{ selectedCaseDetails.location }}
            </div>
            <hr />
            <div class="case-content-details">案件內容：</div>
            <br />
            <div v-html="selectedCaseDetails.content"></div>
            <hr />
            <div
              v-if="selectedCaseDetails.state === '不受理' &amp;&amp; selectedCaseDetails.disapprove_info !== ''"
            >
              <div class="case-disapproved">案件不受理原因：</div>
              <br />
              <div class="disapprove-info">
                {{ selectedCaseDetails.disapprove_info }}
              </div>
            </div>
            <div
              v-if="selectedCaseDetails.state !== '不受理' &amp;&amp; selectedCaseDetails.arranges.length !== 0"
            >
              <div class="arranges-title">案件處理進度：</div>
              <br />
              <div
                class="case-content-arranges"
                v-for="(arrange, index) in reverseCaseProcess"
                :key="index"
              >
                <hr v-if="index &gt; 0" />
                <div class="arrange-title">處理主旨： {{ arrange.title }}</div>
                <div class="arrange-time">
                  處理時間： {{ arrange.arrange_time }}
                </div>
                <div class="arrange-content" v-html="arrange.content"></div>
              </div>
            </div>
            <div style="text-align: center; display:block;"></div>
          </div>
          <div class="dialog-footer" slot="footer">
            <div class="footer-block">
              <div class="content-state">
                處理進度：{{ selectedCaseDetails.state }}
              </div>
            </div>
          </div>
        </el-dialog>
      </el-row>
    </transition>
    <BottomGameDialog :title="aboutTitle"></BottomGameDialog>
  </el-container>
</template>

<script>
import BottomGameDialog from "./BottomGameDialog.vue";
import SvgMap from "./SvgMap.vue";
import Workflow from "./Workflow.vue";
import CarouselCards from "./CarouselCards.vue";
var Highcharts = require("highcharts");
require("highcharts/highcharts-more")(Highcharts);
require("highcharts/modules/wordcloud.js")(Highcharts);


export default {
  name: "About",
  components: { BottomGameDialog, Workflow, SvgMap, CarouselCards },
  data: function() {
    return {
      windowWidth: window.innerWidth,
      showMainContent: false,
      dialogVisible: false,
      isDetailLoaded: false,
      selectedCaseDetails: {
        id: 13,
        number: "000013",
        create_time: "2019-02-19",
        title: "台北101周邊交通亂象",
        content:
          "由（松廉路松智路口周邊）到（松智路）到（信義路五段）到（市府路），這段路，有很多計程車違規排班停等、自小客違規臨停、大客車併排停等上下客（加上計程車違規搗蛋，有時候一併就四排），車流常因上述違規打結，公車因上述違規無法停靠站，公車乘客因上述違規無法安全上下車等。\r\n\r\n松智路（世貿三館往101方向）本身就不寬，一排要違停，一排要左轉松廉路，就只剩中間車道可以行車，車流交織甚為嚴重。\r\n\r\n松廉路松智路口周邊也不時看到車輛因為車流交織而發生擦撞，已與市政單一陳情搞了好一陣子，行政單位都沒有打算認真看待此處的亂象。",
        location: "由松廉路松智路口周邊 到（松智路）到（信義路五段）到市府路",
        type: "交通運輸",
        state: "處理中",
        arranges: [],
        disapprove_info: ""
      },
      aboutTitle: [
        "「選民魔鏡號，市民看得到！」－台北市議員邱威傑市民服務系統⋯⋯",
        "不要再點了，上面我說的話好好看！"
      ],
      froggyservantUrl:
        "https://storage.googleapis.com/froggy-service/frontend/images/about/froggy_servant.png",
      froggyAboutUrl:
        "https://storage.cloud.google.com/froggy-service/frontend/images/about/g2-2_s_center.png",
      froggySignUrl:
        "https://storage.googleapis.com/froggy-service/frontend/images/about/froggy_sign_s.png"
    };
  },
  mounted() {
    window.addEventListener("resize", () => {
      this.windowWidth = window.innerWidth;
    });
    this.showMainContent = true;
    if (this.$route.hash) {
      setTimeout(() => (location.href = this.$route.hash), 1);
    }
    Highcharts.theme = {
      colors: ["#A16BC6", "#60B3DF", "#C65B90", "#DB6069", "#EC8089"],
      credits: {
        enabled: false
      },
      chart: {
        animation: {
          duration: 1500,
          easing: "easeOutBounce"
        },
        borderRadius: 5,
        backgroundColor: {
          linearGradient: { x1: 0.5, x2: 0.5, y1: 0, y2: 1 },
          stops: [
            [0, "rgba(255,255,255,0.3)"],
            [1, "rgba(255,255,255,0.7)"],
            [2, "rgba(255,255,255,1)"]
          ]
        }
      },
      title: {
        text: null,
        style: {
          color: "#fff",
          font:
            "bold 16px PingFangSC-Regular, Microsoft JhengHei, DejaVu Sans, sans-serif"
        }
      },
      subtitle: {
        style: {
          color: "#666666",
          font:
            "bold 12px PingFangSC-Regular, Microsoft JhengHei, DejaVu Sans, sans-serif"
        }
      },
      legend: {
        itemStyle: {
          font:
            "PingFangSC-Regular, Microsoft JhengHei, DejaVu Sans, sans-serif",
          color: "black"
        },
        itemHoverStyle: {
          color: "gray"
        }
      },
      lang: {
        loading: "讀取中...",
        months: [
          "1月",
          "2月",
          "3月",
          "4月",
          "5月",
          "6月",
          "7月",
          "8月",
          "9月",
          "10月",
          "11月",
          "12月"
        ],
        shortMonths: [
          "1月",
          "2月",
          "3月",
          "4月",
          "5月",
          "6月",
          "7月",
          "8月",
          "9月",
          "10月",
          "11月",
          "12月"
        ],
        weekdays: [
          "星期日",
          "星期一",
          "星期二",
          "星期三",
          "星期四",
          "星期五",
          "星期六"
        ]
      }
    };
    // Apply the theme
    Highcharts.setOptions(Highcharts.theme);
    this.showChartTotalCases();
    this.showChartCaseType();
    this.showChartWordCloud();
  },
  methods: {
    randomCase() {
      this.$refs.carouselCards.randomCase();
    },
    toggleLeaveAnimation: function(destination) {
      this.showMainContent = false;
    },
    redirect: function() {
      let direction = this.$store.state.redirectTo;
      this.$router.push(direction);
    },
    showChartTotalCases: () => {
      axios.get("/api/cases/insights/case_line").then(res => {
        let data = res["data"][0]["data"];
        let ts = data.map(d => d[0]);
        let amount = data.map(d => d[1]);

        Highcharts.chart("chart-casesum", {
          chart: {
            renderTo: "container",
            type: "spline",
            marginTop: "30"
          },
          title: {
            // text: "總案件數"
            text: null
          },
          yAxis: {
            title: {
              text: "數量"
            }
          },
          xAxis: {
            type: "datetime",
            categories: ts,
            labels: {
              format: "{value:%Y}"
            },
            tickInterval: 150,
            minTickInterval: 100
          },
          legend: {
            enabled: false,
            layout: "vertical",
            align: "right",
            verticalAlign: "middle"
          },
          plotOptions: {
            series: {
              label: {
                connectorAllowed: true
              },
              marker: {
                enabled: false
              },
              shadow: true
            }
          },
          tooltip: {
            xDateFormat: "%Y 年 %m 月 %d 日"
          },
          series: [
            {
              name: "案件總數",
              data: amount
            }
          ]
        });
      });
    },
    showChartCaseType: () => {
      axios.get("/api/cases/insights/case_type_packed_bubble/").then(res => {
        let values = res.data.map(e => e.data[0].value);
        let zMax = Math.max(...values);
        let zMin = Math.min(...values);
        Highcharts.chart("chart-casetype", {
          chart: {
            type: "packedbubble"
          },
          plotOptions: {
            series: {
              cursor: "pointer"
            },
            packedbubble: {
              minSize: window.innerWidth > 768 ? "80px" : "50px",
              maxSize: window.innerWidth > 768 ? "150px" : "150px",
              zMin: zMin,
              zMax: zMax,
              layoutAlgorithm: {
                splitSeries: false,
                gravitationalConstant: 0.01
              },
              dataLabels: {
                enabled: true,
                style: {
                  fontSize: "14"
                },
                format: "{point.name}",
                filter: {
                  property: "y",
                  operator: ">",
                  value: 0
                }
              },
              events: {
                click: function(event) {
                  let cat = event.point.name;
                  router.push({ name: "cases", query: { category: cat } });
                }
              }
            }
          },
          title: {
            // text: "最關心案件類型"
            text: null
          },
          legend: {
            enabled: false,
            layout: "vertical",
            align: "right",
            verticalAlign: "middle"
          },
          tooltip: {
            pointFormat: "<small>數量：{point.y}</small>"
          },
          series: res.data
        });
      });
    },
    showChartWordCloud: () => {
      axios.get("/api/cases/insights/case_content_wordcloud").then(res => {
        Highcharts.chart("chart-wordcloud", {
          accessibility: {
            screenReaderSection: {
              beforeChartFormat:
                "<h5>{chartTitle}</h5>" +
                "<div>{chartSubtitle}</div>" +
                "<div>{chartLongdesc}</div>" +
                "<div>{viewTableButton}</div>"
            }
          },
          series: [
            {
              type: "wordcloud",
              data: res.data,
              name: "數量",
              cursor: "pointer",
              events: {
                click: function(event) {
                  let keyword = event.point.name;
                  router.push({ name: "cases", query: { keyword: keyword } });
                }
              }
            }
          ],
          title: {
            // text: "最重要關鍵字"
            text: null
          }
        });
      });
    },
    click: function(caseId) {
      this.isDetailLoaded = false;
      const loading = this.$loading({
        lock: true,
        text: "案件資料讀取中",
        target: ".row-table",
        spinner: "el-icon-loading",
        background: "rgba(0, 0, 0, 0.7)"
      });
      this.axios
        .get("/api/cases/" + caseId)
        .then(response => {
          this.selectedCaseDetails = response.data;
          return true;
        })
        .then(() => {
          this.dialogVisible = true;
          loading.close();
        })
        .catch(e => console.log(e))
        .finally(() => {
          const t = document.getElementsByClassName("case-content")[0];
          t.scrollTo(0, 0);
        });
    },
    closeDialog: function() {
      this.isDetailLoaded = false;
      this.selectedCaseDetails = {
        id: 0,
        number: "0",
        create_time: "",
        title: "",
        content: "",
        location: "",
        type: "",
        state: "",
        arranges: [],
        disapprove_info: ""
      };
    }
  },
  computed: {
    reverseCaseProcess() {
      return this.selectedCaseDetails.arranges.slice(0).reverse();
    },
    isSmall() {
      return this.windowWidth <= 768;
    }
  }
};
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
  // z-index: 5
  height: 100%
  flex: $flex_mainContentPart
  flex-direction: column
  flex-shrink: 0
  overflow: scroll
  overflow-x: hidden
  line-height: 1.6
  @media screen and (max-width: $break_small)
    flex: 8
  .about-title
    line-height: initial
    color: white
    font-size: 2.5em
    margin-bottom: 10px
    font-weight: bold
  .about-content-wrapper
    margin-top: 20px
    min-height: calc(100vh - 100px)
    height: calc(100vh - 100px)
    display: flex
    align-items: center
    justify-content: center
    @media screen and (max-width: $break_small)
      // margin-top: 0px
      min-height: fit-content
      height: initial

.row-dialog
  z-index: 5
  flex: $flex_dialogPart
  @media screen and (max-width: $break_small)
    flex: 2

article
  .about-content
    color: white
    span
      font-size: 1em
.signImg
  width: 150px

.froggyServantImg
  width: 100%
  transform: scale(1.2) translate3d(-5px ,-15px,0)
  mask-image: linear-gradient(rgba(0, 0, 0, 1.0), 90% ,transparent)

.text-center
  text-align: center

.report
  margin-bottom: 100px
  color: white
  .report-logo
    display: block
    width: 300px
    margin-bottom: 25px
    @media screen and (max-width: $break_small)
      max-width: 90vw
  ul
    // list-style-type: trad-chinese-informal
    list-style-type: cjk-ideographic
    li
      margin-bottom: 15px
  .report-flowchart
    width: 100%
  .report-charts
    .chart-title
      padding-left: 20px
    .report-chart
      display: flex
      flex-direction: row
      .chart-graph
        width: 70%
      .chart-text
        width: 30%
      .chart-content
        padding: 20px
      img
        width: 100%
      &.report-chart-wordcloud
        flex-direction: column
        .chart-graph
          width: calc(100% - 40px)
        .chart-text
          width: calc(100% - 40px)
    .report-chart-reverse
      flex-direction: row-reverse
    @media screen and (max-width: $break_small)
      .report-chart
        flex-direction: column
        &.report-chart-wordcloud
          flex-direction: column
          .chart-graph
            width: calc(100%)
          .chart-text
            width: calc(100%)
        .chart-content
          margin-top: 20px
          width: 100%
          padding: 0px
      .chart-title
        padding-left: 0px
      .region-title
        margin-bottom: 0
    .chart-paragraph
      margin-top: 20px
  h2.report-title.region-title
        margin-bottom: 0px
        margin-block-end: 0px
  .report-region
    width: 100%
    display: flex
    flex-direction: row
    align-items: flex-start
    justify-content: flex-start
    .region-chart
      width: 50%
      display: flex
      align-items: center
      justify-content: center
      img
        width: 100%
    .region-data
      width: 50%
      min-height: 500px
      padding-left: 20px
      display: flex
      flex-direction: column
      justify-content: space-evenly
    @media screen and (max-width: $break_small)
      flex-direction: column
      align-items: center
      justify-content: center
      .region-chart
        width: 80%
        max-width: 300px
      .region-data
        width: 80%
        max-width: 300px
        padding-left: 0px
        min-height: 300px
  .report-recent-cases
    margin-top: 20px
    img
      width: 100%
  .random-title
    display: flex
    align-items: center
    vertical-align: middle
    @media screen and (max-width: 568px)
      flex-direction: column
    div
      font-size: 1.5em
      font-weight: bold
  .randomcase
    img
        height: 75px
    &:hover
      cursor: pointer

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
