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
        <el-col class="about-title-wrapper" :span="22">
          <div class="about-title">公開透明。</div>
        </el-col>
        <el-col class="about-content-wrapper" :span="22">
          <el-row type="flex" align="middle" justify="center">
            <el-col
              class="noScrollbar"
              :span="15"
              :sm="24"
              :xs="24"
              style="height: 100%;"
            >
              <article>
                <div class="about-content">
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
              <img class="froggyServantImg" :src="froggyAboutUrl" />
            </el-col>
          </el-row>
        </el-col>
        <el-col class="report" :span="22">
          <div class="report-content-wrapper">
            <div class="report-intro">
              <h1 class="report-header">
                選服魔鏡號一週年報告！
              </h1>
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
              <ul>
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
              <br />
              <!-- <img class="report-flowchart" :src="require('@/assets/images/flowchart_fake.jpg')" alt=""> -->
              <img
                class="report-flowchart"
                :src="require('@/assets/images/workflow.png')"
                alt=""
              />
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
              <h3 class="chart-title">大家最關心的案件類型</h3>
              <div class="report-chart report-chart-reverse">
                <div id="chart-casetype" class="chart-graph chart-content">
                  <!-- <img :src="require('@/assets/images/chart2.png')" alt="" /> -->
                </div>
                <div class="chart-text chart-content">
                  我們分析了所有透過魔鏡號向我們尋求協助的案件，在七個議題分類中，大家最關心的就是「交通運輸」，超過三分之一以上的朋友跟我們反應包括機車停車、公車行駛安全、待轉區狹小等問題；其次則是「環境建管」中，舉凡違建拆除、低頻噪音、河川污染等都屬於這個案件類型！
                </div>
              </div>
              <h3 class="chart-title">什麼關鍵字最常被提到？</h3>
              <div class="report-chart">
                <div id="chart-wordcloud" class="chart-graph chart-content">
                  <!-- <img :src="require('@/assets/images/chart3.jpg')" alt="" /> -->
                </div>
                <div class="chart-text chart-content">
                  你知道嗎？「機車」是過去一年來，大家最常在魔鏡號跟我們提到的關鍵字，一共出現超過550次，出現在危險路段、禁行機車段、專用道等問題；第二名的關鍵字是「停車」，包含停車格太少、佔用通道；第三名則是「人行道」。點一下關鍵字，你就可以看到跟它相關的案件！
                </div>
              </div>
              <!-- <div class="chart-paragraph">
                （內文－簡單說明上面幾個數字）指些修。些發統變存響是化美他直研動國種人空！動陸了就媽事，地家業也當價到正他片得可下，過放食我頭情，意多到社源成光。
              </div> -->
            </div>
            <el-divider></el-divider>
            <h2 class="report-title">你在哪一區？</h2>
            <SvgMap></SvgMap>
            <el-divider></el-divider>
            <h2 class="report-title">隨機看案件，歡迎進入魔鏡號！</h2>
            <CarouselCards></CarouselCards>
            <!-- <div class="report-recent-cases">
              <img
                class=""
                :src="require('@/assets/images/kaobei.png')"
                alt=""
              />
            </div> -->
            <!-- <el-divider></el-divider>
            <h2 class="report-title">（小標－未來的方向）團隊接下來要幹嘛，你可以做什麼？</h2>
            <div class="report-future">
              <ul>
                <li> 發 PR </li>
                <li> 捐錢給開發團隊 </li>
                <li> 看 Youtube 頻道 </li>
              </ul>
            </div> -->
          </div>
        </el-col>
      </el-row>
    </transition>
    <BottomGameDialog :title="aboutTitle"></BottomGameDialog>
  </el-container>
</template>

<script>
import BottomGameDialog from "./BottomGameDialog.vue";
import SvgMap from "./SvgMap.vue";
import CarouselCards from "./CarouselCards.vue";
var Highcharts = require("highcharts");
require("highcharts/highcharts-more")(Highcharts);
require("highcharts/modules/wordcloud.js")(Highcharts);

export default {
  name: "About",
  components: { BottomGameDialog, SvgMap, CarouselCards },
  data: function() {
    return {
      chartRendered: [false, false, false],
      showMainContent: false,
      aboutTitle: [
        "「選民魔鏡號，市民看得到！」－台北市議員邱威傑市民服務系統⋯⋯",
        "不要再點了，上面我說的話好好看！"
      ],
      froggyservantUrl:
        "https://storage.googleapis.com/froggy-service/frontend/images/about/froggy_servant.png",
      froggyAboutUrl:
        "https://storage.googleapis.com/froggy-service/frontend/images/about/g2-2_s_center.png",
      froggySignUrl:
        "https://storage.googleapis.com/froggy-service/frontend/images/about/froggy_sign_s.png"
    };
  },
  mounted() {
    let _this = this;
    this.$refs.main.$el.onscroll = function(e) {
      let chartOffset = document.getElementsByClassName('report-charts')[0].offsetTop - 300;
      if (this.scrollTop > chartOffset  && !_this.chartRendered[0]) {
        _this.chartRendered[0] = true
        _this.showChartTotalCases();
      }
      if (this.scrollTop > chartOffset+300  && !_this.chartRendered[1]) {
        _this.chartRendered[1] = true
        _this.showChartCaseType();
      }
      if (this.scrollTop > chartOffset+400  && !_this.chartRendered[2]) {
        _this.chartRendered[2] = true
        _this.showChartWordCloud();
      }
    };
    this.showMainContent = true;
    Highcharts.theme = {
      colors: [
        "#A16BC6",
        "#60B3DF",
        "#C65B90",
        "#DB6069",
        "#EC8089"

        // "#a2cee5",
        // "#ffffff",
        // "#b69fc6",
        // "#c480a2",
        // "#de8f95",
        // "#efcacd"

        // "#058DC7",
        // "#50B432",
        // "#ED561B",
        // "#DDDF00",
        // "#24CBE5",
        // "#64E572",
        // "#FF9655",
        // "#FFF263",
        // "#6AF9C4"
      ],
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
            // [0, "rgba(10,128,256,0.5)"],
            // [1, "rgba(255, 255, 255,0.5)"]
            // [0, "rgba(239, 202, 205,0.2)"],
            // [1, "rgba(222, 143, 149,0.4)"],
            // [2, "rgba(196, 128, 162,0.6)"],
            // [3, "rgba(182, 159, 198,0.8)"],
            // [4, "rgba(162,206,229,1)"],
          ]
        }
      },
      title: {
        text: null,
        style: {
          color: "#fff",
          font: 'bold 16px "Trebuchet MS", Verdana, sans-serif'
        }
      },
      subtitle: {
        style: {
          color: "#666666",
          font: 'bold 12px "Trebuchet MS", Verdana, sans-serif'
        }
      },
      legend: {
        itemStyle: {
          font: "9pt Trebuchet MS, Verdana, sans-serif",
          color: "black"
        },
        itemHoverStyle: {
          color: "gray"
        }
      }
    };
    // Apply the theme
    Highcharts.setOptions(Highcharts.theme);

    // this.showChartTotalCases();
    // this.showChartCaseType();
    // this.showChartWordCloud();
  },
  methods: {
    toggleLeaveAnimation: function(destination) {
      this.showMainContent = false;
    },
    redirect: function() {
      let direction = this.$store.state.redirectTo;
      this.$router.push(direction);
    },
    showChartTotalCases: () => {
      let d = axios
        .get("/api/cases/insights/case_type_line_monthly")
        .then(res => {
          Highcharts.chart("chart-casesum", {
            chart: {
              renderTo: "container",
              type: "spline"
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
              accessibility: {
                // rangeDescription: ""
              }
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
                pointInterval: 24 * 3600 * 1000 * 30,
                pointStart: Date.UTC(2019, 3, 1),
                shadow: true
              }
            },
            xAxis: {
              min: Date.UTC(2019, 3, 1),
              max: Date.UTC(2020, 3, 31),
              allowDecimals: false,
              type: "datetime",
              tickInterval: 24 * 3600 * 1000 * 30, //one day
              labels: {
                rotation: 1
              }
            },
            series: [
              {
                name: "案件總數",
                // type : "area",
                data: [
                  60,
                  150,
                  250,
                  360,
                  480,
                  520,
                  590,
                  680,
                  750,
                  800,
                  910,
                  1100
                ]
              }
            ]
          });
        });
    },
    showChartCaseType: () => {
      Highcharts.chart("chart-casetype", {
        chart: {
          type: "packedbubble"
          // height: "100%"
        },
        plotOptions: {
          packedbubble: {
            minSize: "100%",
            maxSize: "200%",
            zMin: 0,
            zMax: 888,
            layoutAlgorithm: {
              splitSeries: false,
              gravitationalConstant: 0.02
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
                value: 10
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
        series: [
          {
            name: "交通運輸",
            data: [
              {
                name: "交通運輸",
                value: 888
              }
            ]
          },
          {
            name: "公共設施",
            data: [
              {
                name: "公共設施",
                value: 25
              }
            ]
          },
          {
            name: "衛福勞動",
            data: [
              {
                name: "衛福勞動",
                value: 444
              }
            ]
          },
          {
            name: "文教科技",
            data: [
              {
                name: "文教科技",
                value: 66
              }
            ]
          },
          {
            name: "環境建管",
            data: [
              {
                name: "環境建管",
                value: 24
              }
            ]
          },
          {
            name: "警消政風",
            data: [
              {
                name: "警消政風",
                value: 11
              }
            ]
          },
          {
            name: "市政議題",
            data: [
              {
                name: "市政議題",
                value: 11
              }
            ]
          },
          {
            name: "其他服務",
            data: [
              {
                name: "其他服務",
                value: 11
              }
            ]
          }
        ]
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
              name: "數量"
            }
          ],
          title: {
            // text: "最重要關鍵字"
            text: null
          }
        });
      });
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
  z-index: 5
  flex: $flex_mainContentPart
  flex-direction: column
  flex-shrink: 0
  overflow: scroll
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
  min-height: calc(80vh - 100px)
  display: flex
  align-items: center
  justify-content: center

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
  mask-image: linear-gradient(rgba(0, 0, 0, 1.0), 90% ,transparent)

.text-center
  text-align: center

.report
  margin-bottom: 100px
  color: white
  ul
    list-style-type: trad-chinese-informal
  .report-flowchart
    width: 100%
  .report-charts
    // & > *
    //   border: 1px solid black
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
    .report-chart-reverse
      flex-direction: row-reverse
    @media screen and (max-width: $break_small)
      .report-chart
        flex-direction: column
        .chart-content
          margin-top: 20px
          width: 100%
          padding: 0px
      .chart-title
        padding-left: 0px
    .chart-paragraph
      margin-top: 20px
  .report-region
    // &> *
    //   border: solid 1px black
    width: 100%
    display: flex
    flex-direction: row
    align-items: flex-start
    justify-content: center
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
    img
      width: 100%

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
