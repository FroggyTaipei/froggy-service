<template lang="pug">
.container.section
  .row
    .col.col-md-8.col-12
      h1 關於公開選服
      div(v-for="n in 5") 
        span {{lorem}} 
        br
        br
    .col.col-md-4
      h1 Image
      image

</template>

<script>
export default {
  name: 'About',
  props: ['lorem']
}
</script>

<style lang="scss" scoped>

</style>
