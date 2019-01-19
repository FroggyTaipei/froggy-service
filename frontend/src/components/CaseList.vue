<template lang='pug'>
el-container.page2
  el-row.row-table(type='flex' align='middle',justify='center')
    el-col(:span=22)
      //- v-server-table.v-tb(url=' http://localhost:4000/datas', :columns='columns', :options='options')
      v-server-table(url='/api/cases/vuetable', :columns='columns', :options='options')
        div(slot="id" slot-scope="props" @click="click(props.row.id)") {{props.row.id}}
        div(slot="type" slot-scope="props" @click="click(props.row.id)") {{props.row.type}}
        div(slot="create_time" slot-scope="props" @click="click(props.row.id)") {{props.row.create_time}}
        div(slot="title" slot-scope="props" @click="click(props.row.id)") {{props.row.title}}
        div(slot="state" slot-scope="props" @click="click(props.row.id)") {{props.row.state}}

      el-dialog(title='', :visible.sync='dialogVisible')
        .upper-block
          .upper-block-bkg
          img.case-logo(src="https://s3-ap-southeast-1.amazonaws.com/o-r-z/froggy-service/case-logo.png")
        .case-content
          .content-title 案件標題：{{selectedCaseDetails.title}}
          .content-type 案件類型：{{selectedCaseDetails.type}}
          .content-date 時間： {{selectedCaseDetails.create_date}}
          .arranges-title 案件處理回報：
          .content-arranges(v-for="arrange,index in selectedCaseDetails.arranges")
            h4 處理細節－{{index}}
            div.arrange-title {{ arrange.title }}
            div.arrange-content(v-html="arrange.content") {{ arrange.content }}
            div.arrange-time {{arrange.arrange_time}}
          .content-location 地點：{{selectedCaseDetails.location}}
        .dialog-footer(slot='footer')
          .footer-block
            .content-id 案件編號：{{selectedCaseDetails.id}}
            .content-status 處理進度：{{ selectedCaseDetails.state }}

  BottomGameDialog(:title='dialogTitle')
</template>

<script>
import Modal from './Modal.vue'
import BottomGameDialog from './BottomGameDialog.vue'

export default {
  name: 'CaseList',
  components: { Modal, BottomGameDialog },
  data: function () {
    return {
      dialogVisible: false,
      selectedRow: null,
      selectedCaseDetails: { 'id': 1, 'number': '000001', 'create_time': '2019年1月2日 15:07', 'title': '上班時段計程車過多', 'content': '小弟我是台北市民，常常看到很多路上的小黃為了載客硬切慢車道差點造成意外，到了深夜路上的小黃更是快比自用車還多，請問大家會不會覺得台北市的計程車太多了呀？', 'location': '台北市松山區復興北路', 'type': '交通運輸', 'state': '已結案', 'arranges': [ { 'title': '發文交通部', 'content': '<p>面對UBER競爭，計程車司機的日子是越來越難過？交通部每2年進行1次計程車營運狀況調查近日公布，去年專職計程車駕駛每月平均收入為4萬6045元，較104減少1583元；但營業支出卻微幅增加266元。交通部表示，UBER於102年就進入台灣，104年專職計程車駕駛收入有成長2333元，這個統計數字無法呈現是否是受UBER競爭所致，且抽樣統計時約有3%誤差，相差千餘元不一定代表駕駛所得真的下跌</p>', 'arrange_time': '2018年1月12日 22:10' }, { 'title': '發文交通部', 'content': '<p>面對UBER競爭，計程車司機的日子是越來越難過？交通部每2年進行1次計程車營運狀況調查近日公布，去年專職計程車駕駛每月平均收入為4萬6045元，較104減少1583元；但營業支出卻微幅增加266元。交通部表示，UBER於102年就進入台灣，104年專職計程車駕駛收入有成長2333元，這個統計數字無法呈現是否是受UBER競爭所致，且抽樣統計時約有3%誤差，相差千餘元不一定代表駕駛所得真的下跌</p>', 'arrange_time': '2018年1月12日 22:10' } ] },
      dialogTitle: ['呱吉做什麼'],
      columns: ['id', 'type', 'create_time', 'title', 'state'],
      options: {
        headings: {
          id: '案件編號',
          type: '案件類型',
          create_time: '時間',
          title: '主旨',
          state: '處理進度'
        },
        sortable: ['id', 'title', 'state'],
        filterable: ['id', 'title', 'state'],
        filterByColumn: false,
        perPage: 10,
        perPageValues: [10],
        onRowClick: function (row) {
          console.log('clicked')
        },
        requestAdapter (data) {
          return {
            limit: 10,
            sort: data.orderBy ? data.orderBy : 'id',
            ascending: data.ascending ? 'asc' : 'desc',
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
          created_at (h, row) {
            return row.created_at
          },
          updated_at (h, row) {
            return row.updated_at
          },
          pushed_at (h, row) {
            return row.pushed_at
          }
        }
      }
    }
  },
  mounted () {},
  methods: {
    click: function (caseId) {
      this.axios
        .get('/api/cases/' + caseId)
        .then(response => (this.selectedCaseDetails = response.data))
        .catch(e => console.log(e))
      this.dialogVisible = true
    }
  },
  computed: {},
  props: ['lorem']
}
</script>

<style lang='sass' scoped>
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
  flex: 3
  flex-direction: column
.row-dialog
  flex: 1

</style>
