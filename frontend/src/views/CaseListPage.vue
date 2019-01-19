<template>
  <div class="container">
      <!-- <Dialogue id="dialogue" class="" :lorem="lorem"></Dialogue> -->
      <CaseList id="cases" :lorem="lorem"></CaseList>
      <!-- <About id="about" :lorem="lorem"></About> -->
  </div>
</template>

<script>
import CaseList from '@/components/CaseList.vue'

export default {
  name: 'CaseListPage',
  data: function () {
    return {
      data: [],
      title: [],
      lorem: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet dolor at autem quas asperiores, dolore iure, assumenda nemo tenetur perferendis voluptates, doloribus iusto voluptate. Ipsa, laudantium. Tenetur totam repellat aliquam?'
    }
  },
  components: { CaseList }
}
</script>

<style lang="sass">
*
  // border: solid 1px
  font-family: PingFangSC-Regular

html,body
  margin: auto
  width: 100vw
  width: 100%
  height: 100vh
  height: 100%
  // background-color: gray

.container
  height: 100%
  width: 100%

.VueTables__search-field
  padding: 0px 0px 30px 0px!important

table
  width: 100%
  color: white
  border-spacing: unset
  thead>tr>th
    font-size: 1.2em
  tbody>tr
    transition: 0.1s
    &:hover
      color: black
      background-color: white
      transition: 0.2s
      cursor: pointer
    &>td
      padding: 0
      text-align: center
      line-height: 2em
.VuePagination ,.VuePagination__pagination, .VuePagination__count, ul
  display: flex !important
  align-items: center
  justify-content: center
  padding: 0

  li
    list-style-type: none!important
    margin: 10px
    a
      text-decoration: none!important
      font-size: 1em
      color: white
nav
  width: 100%
  color: white
</style>
