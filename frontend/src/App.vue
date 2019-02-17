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
    const inAppBrowser = ['messenger', 'facebook', 'line', 'twitter', 'wechat', 'instagram']
    const inapp = new InApp(navigator.userAgent || navigator.vendor || window.opera)

    if (inapp.isInApp === false) {
      if (inapp.isMobile) {
        this.$store.commit('setIsMobile', true)
      } else {
        this.$store.commit('setIsMobile', false)
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
