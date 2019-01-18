<template lang="pug">
el-container.page2
  el-main
    el-row.row-table(type="flex" align="middle" v-on:scroll="preventParentsScroll",justify="center")
      el-col(:span=24)
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
          el-table-column(prop='number', label='案件編號', width='140', sortable)
            //- template(slot-scope='props')
              span {{ props.row.location }}
              el-popover(trigger='hover', placement='top')
                p 姓名:  {{ props.row.number }}
                p 住址: 
                .name-wrapper(slot='reference')
                  el-tag(size='medium') 
          el-table-column(prop='create_time', label='陳情日期')
          el-table-column(prop='type', label='案件類別', width='120')
          el-table-column(prop='title', label='案件主旨', width='180')
          el-table-column(prop='state', label='處理進度')
      //- el-row(type="flex" align="middle" justify="center")
      //-   el-col(:span=18)
      //-     el-pagination(layout='prev, pager, next', :total='50')
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
  components: {Modal, Navbar, BottomGameDialog},
  data(){
    return {
      title:['呱吉做什麼.......'],
      tableData: [],
      clickdata: null,
      showModal: false,
      selectedCaseInfo : null,
      sort: 'number',
      sortDir: 'asc',
      columns: ['number', 'create_time','type', 'title', 'state'],
    }
  },
  mounted(){
      this.axios
      .get('http://localhost:5566/data')
      .then(response => (this.tableData = response.data))
  },
  methods:{
    preventParentsScroll: function(){
      console.log('scrolling')
    }
  },
  computed:{},
  props:['lorem']
}
</script>

<style lang="sass" scoped>
.page2
  background-image: url('https://s3-ap-southeast-1.amazonaws.com/o-r-z/froggy-service/gradient_background.png')
  background-position: center
  overflow: hidden

.el-main
  display: flex
  flex-shrink: 0
  flex-grow: 1
  flex-direction: column
  width: 100%
  height: 100vh
  align-items: center
  justify-content: center

.el-row
  width: 100%

.row-table
  flex: 7
.row-dialog
  flex: 1

</style>
