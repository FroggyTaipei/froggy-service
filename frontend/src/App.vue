<template lang="html">
  <!-- <div> -->
  <router-view/>
  <!-- </div> -->
</template>

<script>
var MobileDetect = require('mobile-detect')

export default {
  name: 'App',
  created () {
    var md = new MobileDetect(window.navigator.userAgent)
    if (md.mobile()) {
      this.$store.commit('setIsMobile', true)
    } else this.$store.commit('setIsMobile', false)
  }
}
</script>

<style lang="sass">
@import '@/assets/css/style.sass'
</style>
