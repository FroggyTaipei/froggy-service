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
    console.log(inapp)

    if (inAppBrowser.indexOf(inapp.browser) < 0) {
      if (inapp.isMobile) {
        this.$store.commit('setIsMobile', true)
      } else {
        this.$store.commit('setIsMobile', false)
      }
    } else {
      this.router.push({ path: 'home', query: { openExternalBrowser: 1 } })
    }
  }
}
</script>

<style lang="sass">
@import '@/assets/css/style.sass'
</style>
