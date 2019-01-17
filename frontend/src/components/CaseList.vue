<template lang="pug">
el-container.page2
  el-main
    //- Navbar
    el-row(type="flex" align="middle" justify="center")
      el-menu(theme='dark', default-active='0', mode='horizontal', :router='false')
        el-menu-item(index='#firstPage')
          a(href="#firstPage") 我要服務
        el-menu-item(index='#secondPage')
          a(href="#secondPage") 呱吉做什麼
        el-menu-item(index='#thirdPage')
          a(href="#thirdPage") 關於魔鏡號
    el-row(type="flex" align="middle" justify="center")
      el-col(:span=18)
        h1 呱吉做什麼

    el-row(type="flex" align="middle" justify="center")
      el-col(:span=18)
        el-table.caseTable(:data='tableData', style='width: 100%' max-height="800")
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
          el-table-column(prop='number', label='案件編號', width='100', sortable)
            //- template(slot-scope='props')
              span {{ props.row.location }}
              el-popover(trigger='hover', placement='top')
                p 姓名:  {{ props.row.number }}
                p 住址: 
                .name-wrapper(slot='reference')
                  el-tag(size='medium') 
          el-table-column(prop='create_time', label='陳情日期')
          el-table-column(prop='type', label='案件類別', width='100')
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

</template>

<script>
import Modal from './Modal.vue'
import Navbar from './Navbar.vue'

export default {
  name: 'CaseList',
  components: {Modal, Navbar},
  data(){
    return {
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
.el-menu--horizontal
  border: none
.el-menu--horizontal>.el-menu-item.is-active
  border-bottom-color: transparent
  border-bottom: none
.el-menu-item
  a
    text-decoration: none
.el-main
  width: 100%
</style>
