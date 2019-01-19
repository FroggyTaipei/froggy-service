<template lang="pug">
el-container.page2
  el-row.row-table(type="flex" align="middle",justify="center")
    el-col(:span=20)
      el-table.caseTable(:data='tableData', ref="casetb" ,style='width: 100%' max-height="500")
        //- el-table-column(type='expand')
          template(slot-scope='props')
            el-form.demo-table-expand(label-position='left', inline='')
              el-form-item(label='內容')
                span {{ props.row.content }}
              el-form-item(label='地點')
                span {{ props.row.location }}
              el-form-item(label='案件類型')
                span {{ props.row.type }}
              el-form-item(label='處理進度')
                span {{ props.row.state }}
        el-table-column(prop='id', label='案件編號', width='100', sortable)
          //- template(slot-scope='props')
            span {{ props.row.location }}
            el-popover(trigger='hover', placement='top')
              p 姓名:  {{ props.row.number }}
              p 住址:
              .name-wrapper(slot='reference')
                el-tag(size='medium')
        el-table-column(prop='type', label='案件類型', width='120')
        el-table-column(prop='create_time', label='日期')
        el-table-column(prop='title', label='案件主旨', width='180')
        el-table-column(prop='state', label='處理進度')
      //- el-col(:span=18)
        el-pagination(layout='prev, pager, next', :total='50')
    //- el-dialog(title='提示', :visible.sync='dialogVisible', width='30%', :before-close='handleClose')
      span 这是一段信息
      span.dialog-footer(slot='footer')
        el-button(@click='dialogVisible = false') 取 消
        el-button(type='primary', @click='dialogVisible = false') 确 定
  BottomGameDialog(:title="title")
</template>

<script>
import Modal from './Modal.vue'
import Navbar from './Navbar.vue'
import BottomGameDialog from './BottomGameDialog.vue'

export default {
  name: 'CaseList',
  components: { Modal, Navbar, BottomGameDialog },
  data () {
    return {
      title: ['呱吉做什麼.......'],
      tableData: [],
      clickdata: null,
      showModal: false,
      selectedCaseInfo: null,
      sort: 'number',
      sortDir: 'asc',
      columns: ['number', 'create_time', 'type', 'title', 'state']
    }
  },
  mounted () {
    // this.axios
    // .get('http://localhost:5566/data')
    // .then(response => (this.tableData = response.data))
    this.tableData = [
      {
        'id': 5,
        'number': '000005',
        'create_time': '2018年2月12日 22:00',
        'title': '道路垃圾清運',
        'content': '小弟我是台北市民，常常看到很多人亂倒垃圾，請問大家會不會覺得台北市的人太沒道德？',
        'location': '台北市信義區鬍鬚張附近',
        'type': '環境建管',
        'state': '不受理'
      },
      {
        'id': 4,
        'number': '000004',
        'create_time': '2017年11月12日 21:59',
        'title': '呱吉有沒有吃過大便？',
        'content': '小弟我是台北市民，常常看到很多人說呱吉吃大便，請問呱吉到底有沒有吃過大便？',
        'location': '台北市松山區復興北路',
        'type': '其他服務',
        'state': '不受理'
      },
      {
        'id': 3,
        'number': '000003',
        'create_time': '2016年4月12日 21:57',
        'title': '路燈故障或損壞',
        'content': '小弟我是台北市民，常常看到很多路上的路燈故障或損壞，請問大家會不會覺得台北市的路燈故障或損壞太多了呀？',
        'location': '台北市中正區中正廟附近',
        'type': '警消政風',
        'state': '處理中'
      },
      {
        'id': 2,
        'number': '000002',
        'create_time': '2019年6月12日 21:56',
        'title': '環境公害污染',
        'content': '小弟我是台北市民，常常看到很多環境公害污染，請問大家會不會覺得台北市的環境公害污染太多了呀？',
        'location': '台北市忠孝橋附近',
        'type': '環境建管',
        'state': '處理中'
      },
      {
        'id': 1,
        'number': '000001',
        'create_time': '2019年1月2日 15:07',
        'title': '上班時段計程車過多',
        'content': '小弟我是台北市民，常常看到很多路上的小黃為了載客硬切慢車道差點造成意外，到了深夜路上的小黃更是快比自用車還多，請問大家會不會覺得台北市的計程車太多了呀？',
        'location': '台北市松山區復興北路',
        'type': '交通運輸',
        'state': '已結案'
      }
    ]
    var first = document.getCookie('test')
    console.log(first)
  },
  methods: {
    preventParentsScroll: function () {
      console.log('scrolling')
    }
  },
  computed: {},
  props: ['lorem']
}
</script>

<style lang="sass" scoped>
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

.row-table
  flex: 3
  flex-direction: column
.row-dialog
  flex: 1

</style>
