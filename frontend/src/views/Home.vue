<template>
  <div class="container">
    <full-page ref="fullpage" :options="options" id="fullpage">
      <!-- <Navbar></Navbar> -->
      <div class="container section" >
        <AccountKit ref="accountKit">
          <button @click="login">認證</button>
        </AccountKit>
      </div>
      <hr>
      <CaseList id="cases" :lorem="lorem"></CaseList>
      <hr>
      <About id="about" :lorem="lorem"></About>
    </full-page>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import Dialogue from '@/components/Dialogue.vue'
import AccountKit from '@/components/AccountKit.vue'
import CaseList from '@/components/CaseList.vue'
import About from '@/components/About.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'Home',
  data: function () {
    return {
      lorem: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet dolor at autem quas asperiores, dolore iure, assumenda nemo tenetur perferendis voluptates, doloribus iusto voluptate. Ipsa, laudantium. Tenetur totam repellat aliquam?',
      options: {
        // menu: '#menu',
        anchors: ['0', '1', '2'],
        // sectionsColor: ['#41b883', '#ff5f45', '#0798ec'],
        licenseKey: 'A318C6D7-5E9F4CDF-B8952F52-A21EC44B'
      }
    }
  },
  components: { Navbar, Dialogue, CaseList, About, Footer, AccountKit },
  methods: {
    login () {
      this.$refs.accountKit.login(
        {
          countryCode: '+886'
        },
        this.loginCallback
      )
    },
    loginCallback (response) {
      console.log(response)
    }
  }
}
</script>

<style lang="sass">
@import "@/assets/css/all.sass"

*
  // border: solid 1px

/* Add the below transitions to allow a smooth color change similar to lyft */
.nav-menu
  background-color: $white
  -webkit-transition: all 0.6s ease-out
  -moz-transition: all 0.6s ease-out
  -o-transition: all 0.6s ease-out
  -ms-transition: all 0.6s ease-out
  transition: all 0.6s ease-out
  opacity: 0
  &.scrolled
    opacity: 1
</style>
