<template lang="pug">
//- 呈現案件編號、陳情日期、案件主旨(受編輯)、處理進度(受選擇)
//- 有關地點(受編輯)、案件內容(受編輯)、處理內容(由團隊編輯)、結案日期(由團隊編輯)
.container-fluid.section
  h1 Cases
  h1 {{dat}}
  button(v-on:click="btn")
  table.table.table-sm.table-dark
    thead
      tr
        th(scope='col') #
        th(scope='col') First
        th(scope='col') Last
        th(scope='col') Handle
    tbody
      tr
        th(scope='row') 1
        td Mark
        td Otto
        td @mdo
      tr
        th(scope='row') 2
        td Jacob
        td Thornton
        td @fat
      tr
        th(scope='row') 3
        td(colspan='2') Larry the Bird
        td @twitter

</template>

<script>
export default {
  name: "CaseList",
  data() {
    return {
      dat: "a",
      info: null
    };
  },
  created: function() {
  },
  methods: {
    btn: function (event) {
      this.axios
      .get("https://jsonplaceholder.typicode.com/todos/1")
      .then(function(response) {
        this.info = response
        })
        .catch(function(error) {
          console.log(error);
        });
      }
  }
};
</script>

<style lang="scss" scoped>
</style>
