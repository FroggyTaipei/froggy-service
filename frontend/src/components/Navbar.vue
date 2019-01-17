<template lang="pug">
el-row(type="flex" align="middle" justify="center")
  el-menu(theme='dark', default-active='0', mode='horizontal', :router='false')
    el-menu-item(index='#firstPage')
      a(href="#firstPage") 我要找呱吉
    el-menu-item(index='#secondPage')
      a(href="#secondPage") 呱吉做什麼
    el-menu-item(index='#thirdPage')
      a(href="#thirdPage") 關於魔鏡號
</template>

<script>
export default {
  name: 'NavBar',
  data: function () {
    return {}
  },
  methods: {},
  mounted () {},
  destroyed () {}
}
</script>

<style lang="sass">
// .el-menu--horizontal
//   border: none
// .el-menu--horizontal>.el-menu-item.is-active
//   border-bottom-color: transparent
//   border-bottom: none
// .el-menu-item
//   a
//     text-decoration: none
</style>
