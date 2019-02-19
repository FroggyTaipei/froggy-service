<template lang="html">
  <div class="container" v-if="!inLineApp">
    <ThemeSong v-if="!ismobile"/>
    <router-view/>
  </div>
</template>

<script>
import InApp from 'detect-inapp'
import ThemeSong from '@/components/ThemeSong.vue'

export default {
  name: 'App',
  components: { ThemeSong },
  data: () => ({
    ismobile: false,
    inLineApp: false
  }),
  created () {
    const inapp = new InApp(navigator.userAgent || navigator.vendor || window.opera)
    this.ismobile = inapp.isMobile
    if (inapp.ua.indexOf('Edge') > -1) {
      this.$store.commit('setBrowser', 'edge')
    } else if (inapp.ua.indexOf('Trident') > -1 || inapp.ua.indexOf('MSIE') > -1) {
      this.$store.commit('setBrowser', 'ie')
    } else {
      this.$store.commit('setBrowser', inapp.browser)
    }
    if (inapp.isMobile) {
      this.$store.commit('setIsMobile', true)
      if (inapp.isInApp === true) {
        if (inapp.browser === 'line') {
          location.href = 'home?openExternalBrowser=1'
          this.inLineApp = true
        }
      }
    } else {
      this.$store.commit('setIsMobile', false)
    }

    if (this.$store.state.types.length === 0 && this.$store.state.regions.length === 0) {
      this.$store.dispatch('getRegionsList')
      this.$store.dispatch('getTypeList')
    }
  }
}
</script>

<style lang="sass">
@import '@/assets/css/style.sass'
</style>
