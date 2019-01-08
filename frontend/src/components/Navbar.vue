<template lang="pug">
nav.navbar.navbar-expand-lg.navbar-light.fixed-top.bg-custom.scroll(:class="{scrolled:scrolled}")
  .container
    a.navbar-brand(href='#') LOGO 在這邊
    button.navbar-toggler(type='button', data-toggle='collapse', data-target='#navbarSupportedContent', aria-controls='navbarSupportedContent', aria-expanded='false', aria-label='Toggle navigation')
      span.navbar-toggler-icon
    #navbarSupportedContent.collapse.navbar-collapse
      ul.navbar-nav.ml-auto
        li.nav-item
          a.nav-link(href='#dialogue') 我要找呱吉
        li.nav-item
          a.nav-link(href='#cases') 呱吉做什麼
        li.nav-item
          a.nav-link(href='#about') 關於公開選服
</template>

<script>
export default {
  name: 'NavBar',
  data: function () {
    return {
      scrolled: false
    }
  },
  methods: {
    checkScroll () {
      var startY = window.innerHeight / 2
      this.scrolled = window.scrollY > startY
    }
  },
  mounted () {
    window.addEventListener('scroll', this.checkScroll)
  },
  destroyed () {
    window.removeEventListener('scroll', this.checkScroll)
  }
}
</script>

<style lang="sass">

</style>
