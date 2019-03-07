<template lang='pug'>
el-container.page2
  transition(name="fade" @after-leave="redirect")
    el-row.row-table(type='flex' align='middle',justify='center' v-show="showMainContent")
      el-col.searchField(:span=22 style="max-width: 1024px")
        el-input.searchInput(v-model="query" size="small"  @keyup.enter.native="search(query)" clearable=true placeholder="請輸入編號或內容")
        el-button.searchButton(type="primary" size="small"  @click="search(query)") 搜尋
      el-col(:span=22 style="max-width: 1024px")
        v-server-table(v-if="mounted" ref="dataTable" url='/api/cases/vuetable', :columns='columns', :options='options' @row-click="click")

        el-dialog(title='' :visible.sync='dialogVisible' @closed="closeDialog")
          .upper-block
            .upper-block-bkg
              .case-content-type-header {{selectedCaseDetails.type}}
          .case-content
            .case-content-type-body 案件類別：{{selectedCaseDetails.type}}
            .case-content-title 案件標題：{{selectedCaseDetails.title}}
            .case-content-date 時間：{{selectedCaseDetails.create_time.split('-')[0]}} 年 {{selectedCaseDetails.create_time.split('-')[1]}} 月 {{selectedCaseDetails.create_time.split('-')[2]}} 日
            .case-content-location(v-if="selectedCaseDetails.location !== null") 地點：{{selectedCaseDetails.location}}
            hr
            .case-content-details 案件內容：
            br
            div(v-html="selectedCaseDetails.content")
            hr
            div(v-if="selectedCaseDetails.state === '不受理' && selectedCaseDetails.disapprove_info !== ''")
              .case-disapproved 案件不受理原因：
              br
              .disapprove-info {{selectedCaseDetails.disapprove_info}}
            div(v-if="selectedCaseDetails.state !== '不受理' && selectedCaseDetails.arranges.length !== 0")
              .arranges-title 案件處理進度：
              br
              .case-content-arranges(v-for="arrange,index in reverseCaseProcess")
                hr(v-if="index > 0")
                div.arrange-title 處理主旨： {{ arrange.title }}
                div.arrange-time 處理時間： {{arrange.arrange_time}}
                div.arrange-content(v-html="arrange.content")
            div(style="text-align: center; display:block")
          .dialog-footer(slot='footer')
            .footer-block
              .content-status 處理進度：{{ selectedCaseDetails.state }}

  BottomGameDialog(:title='dialogTitle')
</template>

<script>
import BottomGameDialog from './BottomGameDialog.vue'
import { Event } from 'vue-tables-2'

export default {
  name: 'CaseList',
  components: { BottomGameDialog },
  data: function () {
    return {
      query: '',
      showMainContent: false,
      dialogVisible: false,
      isDetailLoaded: false,
      selectedRow: null,
      mounted: false,
      selectedCaseDetails: {
        'id': 13,
        'number': '000013',
        'create_time': '2019-02-19',
        'title': '台北101周邊交通亂象',
        'content': '由（松廉路松智路口周邊）到（松智路）到（信義路五段）到（市府路），這段路，有很多計程車違規排班停等、自小客違規臨停、大客車併排停等上下客（加上計程車違規搗蛋，有時候一併就四排），車流常因上述違規打結，公車因上述違規無法停靠站，公車乘客因上述違規無法安全上下車等。\r\n\r\n松智路（世貿三館往101方向）本身就不寬，一排要違停，一排要左轉松廉路，就只剩中間車道可以行車，車流交織甚為嚴重。\r\n\r\n松廉路松智路口周邊也不時看到車輛因為車流交織而發生擦撞，已與市政單一陳情搞了好一陣子，行政單位都沒有打算認真看待此處的亂象。',
        'location': '由松廉路松智路口周邊 到（松智路）到（信義路五段）到市府路',
        'type': '交通運輸',
        'state': '處理中',
        'arranges': [],
        'disapprove_info': ''
      },
      dialogTitle: ['在這裡，你可以看到對呱吉來說最重要的事情⋯⋯', '事情好多⋯⋯，但是我還是會努力做完的！'],
      columns: ['id', 'type', 'create_time', 'title', 'state'],
      options: {
        headings: {
          id: '案件編號',
          type: '案件類型',
          create_time: '時間',
          title: '主旨',
          state: '處理進度'
        },
        texts: {
          // count: '顯示 {count} 筆資料中的第 {from} 到 {to} 筆資料 | 共有 {count} 筆資料 | One record',
          count: ' |  | ',
          filter: '搜尋：',
          filterPlaceholder: '輸入編號或內容',
          loading: '讀取中...',
          noResults: '找無相關記錄'
        },
        columnsDisplay: {
          id: 'min_tabletL',
          create_time: 'min_tabletL'
        },
        sortable: ['id', 'state', 'type', 'create_time'],
        filterable: ['id', 'title', 'state'],
        sortIcon: { base: 'fas', up: 'fa-sort-up', down: 'fa-sort-down', is: 'fa-sort' },
        listColumns: {
          state: [
            { id: '已結案', text: '已結案' },
            { id: '處理中', text: '處理中' }
          ]
        },
        perPage: 15,
        perPageValues: [10],
        requestAdapter (data) {
          return {
            limit: this.perPage,
            sort: data.orderBy ? data.orderBy : 'id',
            ascending: data.ascending ? 'desc' : 'asc',
            query: data.query,
            page: data.page
          }
        },
        responseAdapter ({ data }) {
          return {
            data: data.data,
            count: data.count
          }
        },
        templates: {
          create_time (h, row) {
            let dateList = row.create_time.split('-')
            let dateFormatted = dateList[0] + '年' + dateList[1] + '月' + dateList[2] + '日'
            return dateFormatted
          },
          title (h, row) {
            let showLimit = 10
            let title = row.title
            if (title.length > showLimit) {
              return title.substring(0, showLimit) + '...'
            } else {
              return title
            }
          }
        }
      }
    }
  },
  created () {
    if (this.$store.state.isMobile === true) {
      this.options.perPage = 10
    }
    const _this = this
    Event.$off(['vue-tables.pagination', 'vue-tables.loaded'])
    Event.$on('vue-tables.pagination', function () {
      if (_this.$store.state.isLoadingTable === false) {
        _this.$store.commit('setIsLoadingTable', true)
        this.loading = this.$loading({
          lock: true,
          text: '案件資料讀取中',
          target: '.row-table',
          spinner: 'el-icon-loading',
          background: 'rgba(0, 0, 0, 0.7)'
        })
      }
    })
    Event.$on('vue-tables.loaded', function () {
      if (_this.$store.state.isLoadingTable === true) {
        _this.$store.commit('setIsLoadingTable', false)
        this.loading.close()
      }
    })
  },
  mounted () {
    this.showMainContent = true
    this.mounted = true
  },
  methods: {
    click: function (clickedRow) {
      let caseId = clickedRow.row.id
      this.isDetailLoaded = false
      const loading = this.$loading({
        lock: true,
        text: '案件資料讀取中',
        target: '.row-table',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)'
      })
      this.axios
        .get('/api/cases/' + caseId)
        .then((response) => {
          this.selectedCaseDetails = response.data
          return true
        })
        .then(() => {
          this.dialogVisible = true
          loading.close()
        })
        .catch(e => console.log(e))
        .finally(() => {
          const t = document.getElementsByClassName('case-content')[0]
          t.scrollTo(0, 0)
        }
        )
    },
    closeDialog: function () {
      this.isDetailLoaded = false
      this.selectedCaseDetails = {
        'id': 0,
        'number': '0',
        'create_time': '',
        'title': '',
        'content': '',
        'location': '',
        'type': '',
        'state': '',
        'arranges': [],
        'disapprove_info': ''
      }
    },
    toggleLeaveAnimation: function (destination) {
      this.showMainContent = false
    },
    redirect: function () {
      let direction = this.$store.state.redirectTo
      this.$router.push(direction)
    },
    search: function (query) {
      this.$refs.dataTable.query = query
      this.$refs.dataTable.refresh()
    }
  },
  computed: {
    reverseCaseProcess () {
      return this.selectedCaseDetails.arranges.slice(0).reverse()
    }
  },
  props: []
}
</script>

<style lang='sass' scoped>
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
  @media screen and (max-width: $break_small)
    flex: 8
.row-dialog
  flex: $flex_dialogPart
  @media screen and (max-width: $break_small)
    flex: 2
</style>
