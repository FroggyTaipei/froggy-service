<template>
  <el-container class="page2">
    <transition name="fade" @after-leave="redirect">
      <el-row
        class="row-table"
        type="flex"
        align="middle"
        justify="center"
        v-show="showMainContent"
      >
        <el-col class="searchField" :span="22" style="max-width: 1024px;">
          <el-input
            class="searchInput"
            v-model="query"
            size="small"
            @keyup.enter.native="search(query)"
            clearable="clearable"
            placeholder="請輸入編號或內容"
          ></el-input>
          <el-button
            class="searchButton"
            type="primary"
            size="small"
            @click="search(query)"
            >搜尋</el-button
          >
        </el-col>
        <el-col class="filterTags" :span="22" style="max-width: 1024px;">
          <div
            class="typeTag"
            v-for="(t, index) in types"
            size="mini"
            @click="selectType(t.id)"
            :class="{ tagSelected: t.id === options.selectedType }"
            :key="index + '-type'"
          >
            {{ t.text }}
          </div>
          <div class="clearTag" size="mini" @click="selectType()">
            <i class="fas fa-times-circle"></i>
          </div>
          <div class="break"></div>
          <div
            class="stateTag"
            v-for="(s, index) in states"
            size="mini"
            @click="selectState(s.id)"
            :class="{ tagSelected: s.id === options.selectedState }"
            :key="index + '-state'"
          >
            {{ s.text }}
          </div>
          <div class="clearTag" size="mini" @click="selectState()">
            <i class="fas fa-times-circle"></i>
          </div>
        </el-col>
        <el-col :span="22" style="max-width: 1024px;">
          <v-server-table
            v-if="mounted"
            ref="dataTable"
            url="/api/cases/vuetable"
            :columns="columns"
            :options="options"
            @row-click="click"
          ></v-server-table>
          <!-- <CardDetail :dialogVisible="dialogVisible"></CardDetail> -->
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
                時間：{{ selectedCaseDetails.create_time.split("-")[0] }} 年
                {{ selectedCaseDetails.create_time.split("-")[1] }} 月
                {{ selectedCaseDetails.create_time.split("-")[2] }} 日
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
                  <div class="arrange-title">
                    處理主旨： {{ arrange.title }}
                  </div>
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
        </el-col>
      </el-row>
    </transition>
    <BottomGameDialog :title="dialogTitle"></BottomGameDialog>
  </el-container>
</template>

<script>
import BottomGameDialog from "./BottomGameDialog.vue";
import CardDetail from "./CardDetail.vue";
import { Event } from "vue-tables-2";

export default {
  name: "CaseList",
  components: { BottomGameDialog, CardDetail },
  data: function() {
    return {
      query: "",
      searched: false,
      showMainContent: false,
      dialogVisible: false,
      isDetailLoaded: false,
      selectedRow: null,
      mounted: false,
      types: [],
      states: [
        {
          id: "arranged",
          text: "處理中"
        },
        {
          id: "disapproved",
          text: "不受理"
        },
        {
          id: "closed",
          text: "已結案"
        }
      ],
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
      dialogTitle: [
        "在這裡，你可以看到對呱吉來說最重要的事情⋯⋯",
        "事情好多⋯⋯，但是我還是會努力做完的！"
      ],
      columns: ["id", "type", "create_time", "title", "state"],
      options: {
        headings: {
          id: "案件編號",
          type: "案件類型",
          create_time: "時間",
          title: "主旨",
          state: "處理進度"
        },
        texts: {
          // count: '顯示 {count} 筆資料中的第 {from} 到 {to} 筆資料 | 共有 {count} 筆資料 | One record',
          count: " |  | ",
          filter: "搜尋：",
          filterPlaceholder: "輸入編號或內容",
          loading: "讀取中...",
          noResults: "找無相關記錄",
          filterBy: "請輸入{column}",
          defaultOption: "選擇{column}"
        },
        columnsDisplay: {
          id: "min_desktop",
          create_time: "min_tabletL"
        },
        sortable: ["id", "state", "type", "create_time"],
        debounce: 800,
        // filterable: false,
        filterable: ["id", "title", "type", "state"],
        sortIcon: {
          base: "fas",
          up: "fa-sort-up",
          down: "fa-sort-down",
          is: "fa-sort"
        },
        filterByColumn: false,
        listColumns: {
          state: [
            { id: "arranged", text: "處理中" },
            { id: "closed", text: "已結案" },
            { id: "disapproved", text: "不受理" }
          ],
          type: []
        },
        customFilters: [
          {
            name: "alphabet",
            callback: function(row, query) {
              return row.id == query;
            }
          }
        ],
        initFilters: {
          GENERIC: ""
        },
        perPage: 10,
        perPageValues: [10],
        selectedType: null,
        selectedState: null,
        requestAdapter(data) {
          return {
            limit: this.perPage,
            sort: data.orderBy ? data.orderBy : "id",
            ascending: data.ascending ? "desc" : "asc",
            query: data.query,
            page: data.page,
            type: this.selectedType,
            state: this.selectedState
          };
        },
        responseAdapter({ data }) {
          return {
            data: data.data,
            count: data.count
          };
        },
        templates: {
          create_time(h, row) {
            let dateList = row.create_time.split("-");
            let dateFormatted =
              dateList[0] + "年" + dateList[1] + "月" + dateList[2] + "日";
            return dateFormatted;
          },
          title(h, row) {
            let showLimit = this.$store.state.isMobile ? 10 : 18;
            let title = row.title;
            if (title.length > showLimit) {
              return title.substring(0, showLimit) + "...";
            } else {
              return title;
            }
          }
        }
      }
    };
  },
  created() {
    if (this.$store.state.isMobile === true) {
      this.options.perPage = 8;
    }
    const _this = this;
    Event.$off(["vue-tables.pagination", "vue-tables.loaded"]);
    Event.$on("vue-tables.pagination", function() {
      if (_this.$store.state.isLoadingTable === false) {
        _this.$store.commit("setIsLoadingTable", true);
        this.loading = this.$loading({
          lock: true,
          text: "案件資料讀取中",
          target: ".row-table",
          spinner: "el-icon-loading",
          background: "rgba(0, 0, 0, 0.7)"
        });
      }
    });
    Event.$on("vue-tables.loaded", function() {
      if (_this.$store.state.isLoadingTable === true) {
        _this.$store.commit("setIsLoadingTable", false);
        this.loading.close();
      }
    });
  },
  mounted() {
    this.showMainContent = true;
    this.mounted = true;

    this.$store.dispatch("getTypeList").then(() => {
      let types = this.$store.state.types;
      let filterTypes = [];
      for (let key in types) {
        let type = { id: types[key]["id"], text: types[key]["name"] };
        filterTypes.push(type);
      }
      this.options.listColumns.type = filterTypes;
      this.types = filterTypes;
    });
    let keyword = this.$route.query.keyword || null;
    let category = this.$route.query.category || null;

    if (keyword) {
      this.query = keyword;
    }

    if (category) {
      let type = this.$store.state.types.find(t => {
        return t.name == category;
      });
      let typeId = type.id || null;
      this.options.selectedType = typeId;
    }
  },
  updated() {
    this.$nextTick(() => {
      if (!this.searched) {
        setTimeout(() => {
          this.search(this.query);
          this.searched = true;
        }, 150);
      }
    });
  },
  methods: {
    click: function(clickedRow) {
      let caseId = clickedRow.row.id;
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
    },
    toggleLeaveAnimation: function(destination) {
      this.showMainContent = false;
    },
    redirect: function() {
      let direction = this.$store.state.redirectTo;
      this.$router.push(direction);
    },
    search: function(query) {
      this.$refs.dataTable.query = query;
      this.$refs.dataTable.refresh();
    },
    selectType: function(typeId) {
      this.options.selectedType = typeId;
      this.search(this.query);
    },
    selectState: function(state) {
      this.options.selectedState = state;
      this.search(this.query);
    }
  },
  computed: {
    reverseCaseProcess() {
      return this.selectedCaseDetails.arranges.slice(0).reverse();
    }
  },
  props: []
};
</script>

<style lang="sass" scoped>
@import '@/assets/css/style.sass'

.page2
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
  height: 100%

.el-col
  height: 100%
  display: flex
  align-items: center
  justify-content: center
  .VueTables
    width: 100%

.row-table
  flex: $flex_mainContentPart
  flex-direction: column
  max-height: 80vh
  @media screen and (max-width: $break_small)
    flex: 8
.row-dialog
  flex: $flex_dialogPart
  @media screen and (max-width: $break_small)
    flex: 2
</style>
