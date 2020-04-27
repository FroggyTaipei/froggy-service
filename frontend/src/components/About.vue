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
                大標題）選服魔鏡號重大回顧OOXX
              </h1>
              <span>
                引文）前方白於同世。足無品統人玩我軍視轉比晚出、全爭而於媽子系動們自品當夫倒看合拿人給謝且入乎道。級道了消然……到男為組：題府水。相南同己加很紀府事險岸？推確腦基、點市沒負營調神話題了行一心縣麗是勢二狀全想就我顯生和不保。國據能式實毒大業分影整，說他知。
              </span>
            </div>
            <el-divider></el-divider>
            <h2 class="report-title">
              小標）我們重視你的每個聲音－案件處理流程與
            </h2>
            <div class="report-flow">
              <div>
                可以提到處理流程（流程圖）、處理上的困難（像是主要的退件原因、是否有與市民交流的困難、在與主管機關溝通的瓶頸），跟是否有項目可以跟議員本人的施政成果相呼應？
              </div>
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
              <h2 class="report-title">市民最在意的事...</h2>
              <h3 class="chart-title">總案件數（數字+ 折線圖）</h3>
              <div class="report-chart">
                <div id="chart-casesum" class="chart-graph chart-content">
                  <!-- <img :src="require('@/assets/images/chart1.png')" alt="" /> -->
                </div>
                <div class="chart-text chart-content">
                  指些修。些發統變存響是化美他直研動國種人空！動陸了就媽事，地家業也當價到正他片得可下，過放食我頭情，意多到社源成光，門樂緊通意人下成我十圖天。是世代到保，品作為再說裡即解種？的就線錯位這？片先資我待都上生個把空居出車費一前推：水們小發健，經接盡司中道沒種特我存腦城爸信了我城。
                </div>
              </div>
              <h3 class="chart-title">最關心案件類型（圓餅 / 泡泡圖？）</h3>
              <div class="report-chart report-chart-reverse">
                <div id="chart-casetype" class="chart-graph chart-content">
                  <!-- <img :src="require('@/assets/images/chart2.png')" alt="" /> -->
                </div>
                <div class="chart-text chart-content">
                  指些修。些發統變存響是化美他直研動國種人空！動陸了就媽事，地家業也當價到正他片得可下，過放食我頭情，意多到社源成光，門樂緊通意人下成我十圖天。是世代到保，品作為再說裡即解種？的就線錯位這？片先資我待都上生個把空居出車費一前推：水們小發健，經接盡司中道沒種特我存腦城爸信了我城。
                </div>
              </div>
              <h3 class="chart-title">最重要關鍵字（文字雲）</h3>
              <div class="report-chart">
                <div id="chart-wordcloud" class="chart-graph chart-content">
                  <!-- <img :src="require('@/assets/images/chart3.jpg')" alt="" /> -->
                </div>
                <div class="chart-text chart-content">
                  指些修。些發統變存響是化美他直研動國種人空！動陸了就媽事，地家業也當價到正他片得可下，過放食我頭情，意多到社源成光，門樂緊通意人下成我十圖天。是世代到保，品作為再說裡即解種？的就線錯位這？片先資我待都上生個把空居出車費一前推：水們小發健，經接盡司中道沒種特我存腦城爸信了我城。
                </div>
              </div>
              <div class="chart-paragraph">
                （內文－簡單說明上面幾個數字）指些修。些發統變存響是化美他直研動國種人空！動陸了就媽事，地家業也當價到正他片得可下，過放食我頭情，意多到社源成光。
              </div>
            </div>
            <el-divider></el-divider>
            <h2 class="report-title">用戶地區與地區熱門案件</h2>
            <SvgMap></SvgMap>
            <el-divider></el-divider>
            <h2 class="report-title">最近大家在靠北什麼？隨機顯示案件</h2>
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
    this.showMainContent = true;
    this.showChartTotalCases();
    this.showChartCaseType();
    this.showChartWordCloud();
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
            title: {
              text: "總案件數"
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
                pointInterval: 24 * 3600 * 1000 * 30,
                pointStart: Date.UTC(2019, 3, 1),
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
                data: [60, 150, 250, 360, 480, 520, 590, 680, 750, 800, 910, 1100]
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
          text: "最關心案件類型"
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
            text: "最重要關鍵字"
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
          width: 100%
          padding: 0px
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
