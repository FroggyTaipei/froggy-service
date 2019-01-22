<template>
  <div class="container">
      <About id="about" :lorem="lorem"></About>
  </div>
</template>

<script>
import About from '@/components/About.vue'

export default {
  name: 'Home',
  data: function () {
    return {
      lorem: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet dolor at autem quas asperiores, dolore iure, assumenda nemo tenetur perferendis voluptates, doloribus iusto voluptate. Ipsa, laudantium. Tenetur totam repellat aliquam?'
    }
  },
  components: { About }
}
</script>

<style lang="sass">
</style>
