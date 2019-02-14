<template lang='pug'>
el-container.page2
  transition(name="fade" @after-leave="redirect")
    el-row.row-table(type='flex' align='middle',justify='center' v-show="showMainContent")
      el-col(:span=22 style="max-width: 1024px")
        v-server-table(url='/api/cases/vuetable', :columns='columns', :options='options' @row-click="click" @loading="loadingTable")

        el-dialog(title='', :visible.sync='dialogVisible' @closed="closeDialog")
          .upper-block
            .upper-block-bkg
              .case-content-type-header {{selectedCaseDetails.type}}
          .case-content
            .case-content-type-body 案件類別：{{selectedCaseDetails.type}}
            .case-content-title 案件標題：{{selectedCaseDetails.title}}
            .case-content-date 時間：{{selectedCaseDetails.create_time.split('-')[0]}} 年 {{selectedCaseDetails.create_time.split('-')[1]}} 月 {{selectedCaseDetails.create_time.split('-')[2]}} 日
            .case-content-location 地點：{{selectedCaseDetails.location}}
            hr
            .case-content-details 案件內容：
            br
            div(v-html="selectedCaseDetails.content") {{selectedCaseDetails.content}}
            hr
            div(v-if="selectedCaseDetails.state === '不受理'")
              .case-disapproved 案件不受理原因：
              .disapprove-info {{selectedCaseDetails.disapprove_info}}
            div(v-if="selectedCaseDetails.state !== '不受理'")
              .arranges-title 案件處理進度：
              .case-content-arranges(v-for="arrange,index in reverseCaseProcess")
                h4 處理回報（{{ reverseCaseProcess.length - index}}）
                div.arrange-title {{ arrange.title }}
                div.arrange-content(v-html="arrange.content") {{ arrange.content }}
                div.arrange-time {{arrange.arrange_time}}
              br
              br
            div(style="text-align: center; display:block") ---------- End ----------
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
      showMainContent: false,
      dialogVisible: false,
      isTableLoaded: false,
      isDetailLoaded: false,
      selectedRow: null,
      selectedCaseDetails: {
        'id': 1,
        'number': '000001',
        'create_time': '2019-01-02',
        'title': '上班時段計程車過多',
        'content': '小弟我是台北市民，常常看到很多路上的小黃為了載客硬切慢車道差點造成意外，到了深夜路上的小黃更是快比自用車還多，請問大家會不會覺得台北市的計程車太多了呀？',
        'location': '台北市松山區復興北路',
        'type': '交通運輸',
        'state': '已完結',
        'arranges': [
          {
            'title': '發文交通部1',
            'content': '<p>面對UBER競爭，計程車司機的日子是越來越難過？<img src="https://i.pinimg.com/564x/a8/ec/82/a8ec828bbda82c7793e49e90aebcb5d1.jpg">交通部每2年進行1次計程車營運狀況調查近日公佈，去年專職計程車駕駛每月平均收入為4萬6045元，較104減少1583元；但營業支出卻微幅增加266元。交通部表示，UBER於102年就進入台灣，104年專職計程車駕駛收入有成長2333元，這個統計數字無法呈現是否是受UBER競爭所致，且抽樣統計時約有3%誤差，相差千餘元不一定代表駕駛所得真的下跌</p>',
            'arrange_time': '2018-01-10'
          },
          {
            'title': '發文交通部2',
            'content': '<p>面對UBER競爭，計程車司機的日子是越來越難過？交通部每2年進行1次計程車營運狀況調查近日公佈，去年專職計程車駕駛每月平均收入為4萬6045元，較104減少1583元；但營業支出卻微幅增加266元。交通部表示，UBER於102年就進入台灣，104年專職計程車駕駛收入有成長2333元，這個統計數字無法呈現是否是受UBER競爭所致，且抽樣統計時約有3%誤差，相差千餘元不一定代表駕駛所得真的下跌</p>',
            'arrange_time': '2018-01-12'
          }
        ],
        'disapprove_info': '拒絕理由'
      },
      dialogTitle: ['在這裡，你可以看到對呱吉來說最重要的事情⋯⋯'],
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
          // count: '顯示 {count} 比資料中的第 {from} 到 {to} 筆資料 | 共有 {count} 筆資料 | One record',
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
        sortable: ['id'],
        filterable: ['id', 'title', 'state'],
        listColumns: {
          state: [
            { id: '已結案', text: '已結案' },
            { id: '處理中', text: '處理中' }
          ]
        },
        // filterByColumn: true,
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
  },
  mounted () {
    this.showMainContent = true
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
        .then(response => (this.selectedCaseDetails = response.data))
        .catch(e => console.log(e))
        .finally(() => {
          this.dialogVisible = true
          loading.close()
        }
        )
    },
    loadingTable: function () {
      this.isTableLoaded = false
      const loading = this.$loading({
        lock: true,
        text: '資料讀取中',
        target: '.row-table',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)'
      })
      Event.$on('vue-tables.loaded', function (data) {
        this.isTableLoaded = true
        loading.close()
      })
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
