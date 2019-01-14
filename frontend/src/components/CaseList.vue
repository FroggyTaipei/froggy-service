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
          th(scope='col' class='text-center' @click="sortCases('id')") 案件編號
          th.d-none.d-sm-table-cell(scope='col' @click="sortCases('username')") 陳情日期
          th(scope='col' @click="sortCases('name')") 案件類別
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
  #people
    //- v-server-table(url="/api/cases/vuetable/", :columns="columns", :options='options')
</template>

<script>
export default {
  name: 'CaseList',
  data(){
    return {
      info: {
        data: null
      },
      sort: 'id',
      sortDir: 'asc',
      dataLoaded: false,
      columns: ['number', 'date', 'title', 'content','location','type','state'],
      tableData: [],
      options: {
        perPage:5,
        perPageValues:[5],
        requestAdapter(data) {
          return {
            sort: data.orderBy ? data.orderBy : 'name',
            direction: data.ascending ? 'asc' : 'desc'
            }
          },
        responseAdapter({data}) {
          return {
            data,
            count: data.length
          }
        },
        filterable: true,
        customFilters: [
          {
            name:'alphabet',
            callback: function(row, query) {
              return row.name[0] == query;
              }
          }
        ]
        // templates: {
        //   created_at(h, row) {
        //     return this.formatDate(row.created_at);
        //   },
        //   updated_at(h, row) {
        //     return this.formatDate(row.updated_at);
        //   },
        //   pushed_at(h, row) {
        //     return this.formatDate(row.pushed_at);
        //   }
        // }
      }
    }
  },
  mounted(){},
  methods:{
    clickBtn(){},
    clickRow(){},
    sortCases: function(sortBy) {
      if(sortBy === this.sort){
        this.sortDir = this.sortDir === 'asc'?'desc':'asc'
      }
      this.sort = sortBy
    },
    formatDate: function(date) {
      return moment(date).format('DD-MM-YYYY HH:mm:ss');
    }
  },
  computed:{
    sortedCases: function(){
      if(this.dataLoaded){
        return this.info.data.sort((a,b)=>{
          let modifier = 1
          if(this.sortDir === 'desc') modifier = -1
          if(a[this.sort] < b[this.sort]) return -1 * modifier
          if(a[this.sort] > b[this.sort]) return 1 * modifier
          return 0
        })
      }
    }
  },
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

.VueTables__child-row-toggler 
    width: 16px
    height: 16px
    line-height: 20px
    display: block
    margin: auto
    text-align: center
    background-color: yellow
 
.VueTables__child-row-toggler--closed::before 
    content: "+"
 
.VueTables__child-row-toggler--open::before 
    content: "-"


</style>
