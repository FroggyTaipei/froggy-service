<template>
  <div class="container">
    <Navbar></Navbar>
    <Dialogue id="dialogue"></Dialogue>
    <hr>
    <CaseList id="cases" :lorem="lorem"></CaseList>
    <hr>
    <About id="about" :lorem="lorem"></About>
    <hr>
    <Footer></Footer>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import Dialogue from '@/components/Dialogue.vue'
import CaseList from '@/components/CaseList.vue'
import About from '@/components/About.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'Home',
  data: function(){
    return{
      lorem: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet dolor at autem quas asperiores, dolore iure, assumenda nemo tenetur perferendis voluptates, doloribus iusto voluptate. Ipsa, laudantium. Tenetur totam repellat aliquam?"
    }
  },
  components:{Navbar, Dialogue, CaseList, About, Footer}
}
</script>

<style lang="sass">
@import "@/assets/css/all.sass"

*
  // border: solid 1px

</style>
