<template>
  <div class="container">
    <div id="app">
      <h3>Vue Tables 2 - Server Side Demo</h3>
      <div class="col-md-8 col-md-offset-2">
        <div id="people">
          <v-server-table
            url="http://localhost:8000/api/cases/vuetable"
            :columns="columns"
            :options="options"
          ></v-server-table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: "FirstComponent",
  methods: {
    formatDate(date) {
      return moment(date).format('DD-MM-YYYY HH:mm:ss');
    }
  },
  data: function(){
    return {
    columns: ["id", "create_time", "title", "state"],
    tableData: [],
    options: {
      perPage: 25,
      perPageValues: [25],
      requestAdapter(data) {
        return {
          sort: data.orderBy ? data.orderBy : "id",
          ascending: data.ascending ? "asc" : "desc"
        };
      },
      responseAdapter({ data }) {
        return {
          data: data.data,
          count: data.count
        };
      },
      filterable: false,
      templates: {
        created_at(h, row) {
          return row.created_at;
        },
        updated_at(h, row) {
          return row.updated_at;
        },
        pushed_at(h, row) {
          return row.pushed_at;
        }
      }
    }
  }
}
}
</script>

<style lang="scss" scoped>
#app {
  width: 95%;
  margin: 0 auto;
}

.VuePagination {
  text-align: center;
}

.vue-title {
  text-align: center;
  margin-bottom: 10px;
}

.vue-pagination-ad {
  text-align: center;
}

.glyphicon.glyphicon-eye-open {
  width: 16px;
  display: block;
  margin: 0 auto;
}

th:nth-child(3) {
  text-align: center;
}

.VueTables__child-row-toggler {
  width: 16px;
  height: 16px;
  line-height: 16px;
  display: block;
  margin: auto;
  text-align: center;
}

.VueTables__child-row-toggler--closed::before {
  content: "+";
}

.VueTables__child-row-toggler--open::before {
  content: "-";
}
</style>
