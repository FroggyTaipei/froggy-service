<template>
  <div class="container">
      <About id="about"></About>
  </div>
</template>

<script>
import About from '@/components/About.vue'

export default {
  name: 'Home',
  data: function () {
    return {
    }
  },
  components: { About }
}
</script>

<style lang="sass">
</style>
