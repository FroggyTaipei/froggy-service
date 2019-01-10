<template lang="pug">
//- 呈現案件編號、陳情日期、案件主旨(受編輯)、處理進度(受選擇)
//- 有關地點(受編輯)、案件內容(受編輯)、處理內容(由團隊編輯)、結案日期(由團隊編輯)
.container-fluid.section
  h1 呱吉做什麼
  span {{lorem}}
  .container.h-100
    .d-flex.justify-content-start.h-100
      .searchbar
        input.search_input(type='text', name='', placeholder='Search...')
        a.search_icon(href='#')
          i.fas.fa-search
  table.table.table-striped
    thead
      tr
        th(scope='col' class='text-center' @click="sortCases('id')") 案件編號
        th(scope='col' @click="sortCases('username')") 陳情日期
        th(scope='col' @click="sortCases('name')") 案件類別
        th(scope='col') 案件主旨
        th(scope='col') 處理進度
    tbody
      tr(@click="clickRow" v-for="data, key in sortedCases" data-toggle="modal" :data-target="'#case'+data.id")
        th(scope='row' class='text-center') {{data.id}}
        td {{data.username}}
        td {{data.name}}
        td {{data.address.city}}
        td {{data.address.geo.lng}}
        // Modal
        .modal.fade(tabindex='-1', role='dialog', aria-labelledby='exampleModalCenterTitle', aria-hidden='true', ref="modal", :id="'case'+data.id")
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

  //- nav.pag(aria-label='Page navigation example')
  ul.pagination.justify-content-center
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
      dataLoaded: false
    }
  },
  mounted(){
    this.axios
    .get('https://jsonplaceholder.typicode.com/users')
    .then((response) => {
      this.info = response
      this.dataLoaded = true
      }).catch(error => console.log(error))
  },
  methods:{
    clickBtn(){},
    clickRow(){},
    sortCases: function(sortBy) {
      if(sortBy === this.sort){
        this.sortDir = this.sortDir === 'asc'?'desc':'asc'
      }
      this.sort = sortBy
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
  // width: 0
  width: 450px
  caret-color:transparent
  line-height: 40px
  transition: width 0.4s linear

.search_icon
  height: 40px
  width: 40px
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
</style>
