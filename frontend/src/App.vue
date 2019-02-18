<template lang="html">
  <div class="container">
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
    ismobile: false
  }),
  created () {
    const inapp = new InApp(navigator.userAgent || navigator.vendor || window.opera)
    this.ismobile = inapp.isMobile
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
      if (inapp.browser === 'line') {
        location.href = 'home?openExternalBrowser=1'
      }
      if (inapp.browser === 'facebook' || inapp.browser === 'messenger') {
        this.$alert('請使用外部瀏覽器已獲得最佳瀏覽體驗', '友情提示', {
          type: 'warning'
        })
      }
    }
  }
}
</script>

<style lang="sass">
@import '@/assets/css/style.sass'
</style>
