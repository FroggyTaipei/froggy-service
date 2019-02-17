<template lang="html">
  <!-- <div> -->
  <router-view/>
  <!-- </div> -->
</template>

<script>
import InApp from 'detect-inapp'

export default {
  name: 'App',
  created () {
    const inapp = new InApp(navigator.userAgent || navigator.vendor || window.opera)
    if (inapp.isInApp === false) {
      if (inapp.isMobile) {
        this.$store.commit('setIsMobile', true)
      } else {
        this.$store.commit('setIsMobile', false)
      }
      if (this.$store.state.types.length === 0 && this.$store.state.regions.length === 0) {
        this.$store.dispatch('getRegionsList')
        this.$store.dispatch('getTypeList')
      }
    } else {
      location.href = 'home?openExternalBrowser=1'
    }
  }
}
</script>

<style lang="sass">
@import '@/assets/css/style.sass'
</style>
