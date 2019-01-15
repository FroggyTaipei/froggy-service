<template lang="pug">
.container-fluid.section
  h1 呱吉做什麼
  span {{lorem}}
  //- .container.h-100
    .d-flex.justify-content-start.h-100
      .searchbar
        input.search_input(type='text', name='', placeholder='Search...')
        //- a.search_icon(href='#')
          i.fas.fa-search
  .row
    //- table.table.table-striped.col-sm-12
      thead
        tr
          th(scope='col' class='text-center' @click="sortCases('number')") 案件編號
          th.d-none.d-sm-table-cell(scope='col' @click="sortCases('create_time')") 陳情日期
          th(scope='col' @click="sortCases('type')") 案件類別
          th(scope='col') 案件主旨
          th.d-none.d-sm-table-cell(scope='col') 處理進度
      tbody
        tr(@click="clickRow" v-for="data, key in sortedCases" data-toggle="modal" :data-target="'#case'+data.id")
          th(scope='row' class='text-center') {{data.id}}
          td.d-none.d-sm-table-cell {{data.username}}
          td {{data.name}}
          td {{data.address.city}}
          td.d-none.d-sm-table-cell {{data.address.geo.lng}}
          // Modal
          .modal.fade.col-sm-12(tabindex='-1', role='dialog', aria-labelledby='exampleModalCenterTitle', aria-hidden='true', ref="modal", :id="'case'+data.id")
            .modal-dialog.modal-dialog-centered(role='document')
              .modal-content
                .modal-header
                  h5#exampleModalLongTitle.modal-title 案件編號: {{data.id}}  案件主旨: {{data.username}}
                  button.close(type='button', data-dismiss='modal', aria-label='Close')
                    span(aria-hidden='true') ×
                .modal-body
                  h6 陳情日期
                  h5 處理進度(受選擇)
                  h5 有關地點(受編輯)
                  span {{lorem}}
                  h5 案件內容(受編輯)
                  span {{lorem}}
                  h5 處理內容(由團隊編輯)
                  span {{lorem}}
                  h5 結案日期(由團隊編輯)
                .modal-footer
                  button.btn.btn-secondary(type='button', data-dismiss='modal') 關閉
                  //- button.btn.btn-primary(type='button') Save changes

    //- ul.pagination.justify-content-center.col-sm-12
      li.page-item
        a.page-link(href='#') Previous
      li.page-item
        a.page-link(href='#') 1
      li.page-item
        a.page-link(href='#') 2
      li.page-item
        a.page-link(href='#') 3
      li.page-item
        a.page-link(href='#') Next
  #caseTable
    //- v-server-table(url="/api/cases/vuetable/", :columns="columns", :options='options')
    v-server-table(url="http://localhost:3000/datas", :columns="columns", :options='options')
      a(slot="create_time" slot-scope="props" @click="toggleModal(props.row)") {{props.row.date}}
  
  //- button#show-modal(@click='showModal = true') Show Modal
  modal(v-if='showModal', @close='showModal = false' :caseInfo="selectedCaseInfo")
    h3(slot='header') custom header
</template>

<script>
import Modal from './Modal.vue'

export default {
  name: 'CaseList',
  components: {Modal},
  data(){
    return {
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
        perPage:5,
        perPageValues:[5],
        responseAdapter({data}) {
          return {
            data: data.data,
            count: data.count,
          }
        },
        filterable: false,
        customFilters: [],
        // columnsClasses:{'number':'bgy'},
        pagination: { nav: 'fixed' },
        templates:{
          edit: (h, row) => {
            return <button on-click={ () => this.showItem(row) } class="btn btn-primary btn-sm"><i class="glyphicon glyphicon-edit"></i></button>
            }
        },
      }
    }
  },
  mounted(){},
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
table
  margin: 50px 0px

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
