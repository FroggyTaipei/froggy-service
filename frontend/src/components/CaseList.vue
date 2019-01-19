<template lang='pug'>
el-container.page2
  el-row.row-table(type='flex' align='middle',justify='center')
    el-col(:span=22)
      v-server-table(url='http://localhost:8000/api/cases/vuetable', :columns='columns', :options='options')
      //- v-server-table.v-tb(url=' http://localhost:4000/datas', :columns='columns', :options='options')
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
    preventParentsScroll: function () {
      console.log('scrolling')
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
