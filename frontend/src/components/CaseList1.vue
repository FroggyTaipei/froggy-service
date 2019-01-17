<template lang="pug">
.container.section

  h1 呱吉做什麼
  span {{lorem}}
  .row
    #caseTable.col-sm-12
      v-server-table(url="http://localhost:3000/datas", :columns="columns", :options='options')
        a(slot="create_time" slot-scope="props" @click="toggleModal(props.row)") {{props.row.date}}
      //- v-server-table(url="/api/cases/vuetable/", :columns="columns", :options='options')
        a(slot="create_time" slot-scope="props" @click="toggleModal(props.row)") {{props.row.date}}
    //- Modal.col-sm-12(v-if='showModal', @close='showModal = false' :caseInfo="selectedCaseInfo")
    //- button#show-modal(@click='showModal = true') Show Modal

    //- el-table(:data='tableData', style='width: 100%')
      el-table-column(type='expand')
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
      el-table-column(prop='number', label='日期', width='180' sortable)
        template(slot-scope='props')
          span {{ props.row.location }}
          el-popover(trigger='hover', placement='top')
            p 姓名:  {{ props.row.number }}
            p 住址: 
            .name-wrapper(slot='reference')
              el-tag(size='medium') 
      el-table-column(prop='date', label='姓名', width='180')
      el-table-column(prop='title', label='地址')
    el-dialog(title='提示', :visible.sync='dialogVisible', width='30%', :before-close='handleClose')
      span 这是一段信息
      span.dialog-footer(slot='footer')
        el-button(@click='dialogVisible = false') 取 消
        el-button(type='primary', @click='dialogVisible = false') 确 定

</template>

<script>
import Modal from './Modal.vue'

export default {
  name: 'CaseList',
  components: {Modal},
  data(){
    return {
      tableData: [],
      clickdata: null,
      showModal: false,
      selectedCaseInfo : null,
      sort: 'number',
      sortDir: 'asc',
      columns: ['number', 'create_time','type', 'title', 'state'],
      options: {
        onRowClick: function(row){
          this.clickdata = row
        },
        headings: {
          number: "案件編號",
          create_time: "陳情日期",
          title: "案件主旨",
          content: "案件內容",
          location: "地點",
          type: "案件類別",
          state: "處理進度"
        },
        sortIcon: { base:'glyphicon', up:'glyphicon-chevron-up', down:'glyphicon-chevron-down', is:'glyphicon-sort' },
        sortable:['number', 'create_time','type', 'title', 'state'],
        perPage:5,
        perPageValues:[5],
        requestAdapter(data) {
        return {
          sort: data.orderBy ? data.orderBy : 'number',
          direction: data.ascending ? 'asc' : 'desc'
        }
      },
        responseAdapter({data}) {
          return {
            data: data.data,
            count: data.count,
          }
        },
        filterable: false,
        customFilters: [],
        // columnsClasses:{'number':'bgy'},
        // pagination: { nav: 'fixed' },
        templates:{
          edit: (h, row) => {
            return <button on-click={ () => this.showItem(row) } class="btn btn-primary btn-sm"><i class="glyphicon glyphicon-edit"></i></button>
            }
        },
      }
    }
  },
  mounted(){
      // this.axios
      // .get('http://localhost:5566/data')
      // .then(response => (this.tableData = response.data))
  },
  methods:{
    clickCase: function(a){
      console.log('case number: ' + a)
    },
    toggleModal: function(caseInfo){
      this.showModal= true
      this.selectedCaseInfo = caseInfo
    }
  },
  computed:{},
  props:['lorem']
}
</script>

<style lang="sass" scoped>
el-table
  height: 80%

#caseTable
  // margin: 100px 0px

tbody>tr:hover
  cursor: pointer

.modal-body>h5
  margin-top: 15px

.searchbar
  margin-bottom: auto
  margin-top: 50px
  height: 60px
  background-color: #f4f4f4
  border-radius: 30px
  padding: 10px

.search_input
  color: black
  border: 0
  outline: 0
  background: none
  width: 100%
  caret-color:transparent
  line-height: 40px
  transition: width 0.4s linear

.search_icon
  height: 20px
  width: 20px
  float: right
  display: flex
  justify-content: center
  align-items: center
  border-radius: 50%
  background: white
  transition: 0.4s linear

// .searchbar:hover > .search_input
//   padding: 0 10px
//   width: 450px
//   caret-color:red
//   transition: width 0.4s linear

.searchbar:hover > .search_icon
  background: #007bff
  transition: 0.4s linear

.modal-mask 
  position: fixed
  z-index: 9998
  top: 0
  left: 0
  width: 100%
  height: 100%
  background-color: rgba(0, 0, 0, .5)
  display: table
  transition: opacity .3s ease


.modal-wrapper 
  display: table-cell
  vertical-align: middle


.modal-container 
  width: 300px
  margin: 0px auto
  padding: 20px 30px
  background-color: #fff
  border-radius: 2px
  box-shadow: 0 2px 8px rgba(0, 0, 0, .33)
  transition: all .3s ease
  font-family: Helvetica, Arial, sans-serif


.modal-header h3 
  margin-top: 0
  color: #42b983


.modal-body 
  margin: 20px 0


.modal-default-button 
  float: right


/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter 
  opacity: 0


.modal-leave-active 
  opacity: 0


.modal-enter .modal-container,
.modal-leave-active .modal-container 
  -webkit-transform: scale(1.1)
  transform: scale(1.1)

</style>
