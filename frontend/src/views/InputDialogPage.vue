<template>
  <el-container style="height:100%">
    <!-- Page one -->
    <el-row type="flex" class="panel category-page" v-show="step == 0">
          <div class="category-content">
            <el-row type="flex" class="category-content-row1">
              <el-col :sm="24">
                <img src="https://storage.googleapis.com/froggy-service/frontend/images/dialog/category/namebar.png" height="54%">
              </el-col>
            </el-row>
            <el-row type="flex" justify="center" class="category-content-row2">
                <el-col :sm="12" class="hidden-xs-only category-content-person">
                  <img src="https://storage.googleapis.com/froggy-service/frontend/images/dialog/category/person.png" width="80%">
                </el-col>
                <el-col :xs="24" :sm="12">
                  <img class="category-content-center category-content-froggy" src="https://storage.googleapis.com/froggy-service/frontend/images/dialog/category/froggy.png" width="90%">
                  <img src="https://storage.googleapis.com/froggy-service/frontend/images/dialog/category/progress.png" width="95%">
                </el-col>
            </el-row>
          </div>
          <div class="category-footer">
            <el-row>
                <el-col
                  :xs="24"
                  :sm="6"
                  v-for="item in $store.state.types"
                  :key="item.id">
                  <div class="category-item">
                    <div
                      class="category-btn"
                      @click="selectCaseType(item.id)">
                      {{ item.name }}
                    </div>
                    <div class="category-icon">
                      <i class="el-icon-caret-right"></i>
                    </div>
                  </div>
                </el-col>
              </el-row>
          </div>
          <div class="back-btn">
            <el-button type="info" icon="el-icon-error" circle @click="back"></el-button>
          </div>
    </el-row>
    <el-row type="flex" class="panel form-page" :gutter="10" v-show="step > 0">
      <div class="bg-logo">
      </div>
      <el-col :span="12" class="col1 hidden-xs-only">
        <el-container>
          <div class="footer">
            <img style="width:90%" src="https://storage.googleapis.com/froggy-service/frontend/images/dialog/input/froggy.png" >
            <img src="https://storage.googleapis.com/froggy-service/frontend/images/dialog/input/progress.png" >
          </div>
        </el-container>
      </el-col>
      <el-col :xs="24" :span="12" class="col2">
        <div class="input-dialog">
          <!-- Page two -->
          <InputUserInfo
            v-show="step == 1"
            @next="next"
            @previous="previous"
            :isClose="isClose"/>
          <!-- Page three -->
          <InputCase
            v-show="step == 2"
            @previous="previous"
            :isClose="isClose"/>
        </div>
      </el-col>
    </el-row>
  </el-container>
</template>

<script>
import InputUserInfo from '@/components/InputUserInfo.vue'
import InputCase from '@/components/InputCase.vue'
export default {
  name: 'InputDialog',
  components: {
    InputUserInfo,
    InputCase
  },
  data: () => ({
    step: 0,
    isClose: false
  }),
  created () {
    console.log('input dialog init')
    this.$store.dispatch('getRegionsList')
    this.$store.dispatch('getTypeList')
  },
  methods: {
    closeInput () {
      this.step = 0
      this.isClose = true
      this.$emit('closeInput')
    },
    selectCaseType (type) {
      this.$store.commit('setCase', { type: type })
      this.next()
    },
    next () {
      if (this.step < 3) {
        this.step += 1
        console.log('go to page', this.step)
      }
    },
    previous () {
      if (this.step > 0) {
        this.step -= 1
        console.log('go to previous page')
      }
    },
    back () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    }
  }
}
</script>

<style lang="css" scoped>
/*custom font*/
@import url(https://fonts.googleapis.com/css?family=Montserrat);

.panel {
    background-repeat: no-repeat;
    background-size: 100% auto;
    position: relative;
    width: -webkit-fill-available;
}
.form-page {
    background-image: url("https://storage.googleapis.com/froggy-service/frontend/images/dialog/input/background.png");
}
.category-page {
    background-image: url("https://storage.googleapis.com/froggy-service/frontend/images/dialog/category/background.png");
    flex-direction: column;
}
.category-page > div {
  display: flex;
}
.category-content {
  flex: 4;
  flex-direction: column;
  width: 90%;
  margin: auto;
}
.category-content > div.el-row {
  flex: 1;
}

.category-content-row1 img {
  margin-top: 5vh;
  margin-left: 10vw;
}

.category-content-row2 > div.el-col {
  position: relative;
}

.category-content-row2 > div.el-col img {
  position: absolute;
  bottom: 0px

}
.category-content-center {
  margin: auto;
  left: 0;
  right: 0;

}
.category-content-person > img {
  bottom: -10vh !important;
  right: 2vw;
}
.category-content-froggy {
  bottom: 5vh !important;
}
.category-footer {
    background-image: url("https://storage.googleapis.com/froggy-service/frontend/images/dialog/category/footer.png");
    background-repeat: no-repeat;
    background-size: 100% 100%;
    background-position: center;
    width: 100%;
    position: relative;
    flex-direction: column;
    align-self: flex-end;
    flex: 1;
}
.category-footer > .el-row {
  position: absolute;
  margin: auto;
  left: 0;
  right: 0;
  top: 0;
  height: 100%;
  padding: 3vh 2vw;
  width: 80%;
}
.category-footer .el-col-sm-6 {
  height: 50%
}
.category-item {
  height: 100%;
  display: flex;
  flex-direction: row-reverse;
}
.category-item > div {
  display: flex;
}
.category-icon {
  flex: 1;
  font-size: 4rem;
  align-self: center;
  color: transparent;
  margin-right: -32px
}
.category-btn {
  flex: 4;
  justify-content: center;
  align-items: center;
  font-size: 3rem;
  font-weight: 600;
  cursor: pointer;
  margin-left: -16px
}
div.category-btn:hover + div {
  color: black;
}
.back-btn {
  position: fixed;
  right: 1vw;
  top: 1vh;
}
.col1 .el-container {
  height: 100%
}
.col1 .el-main {
  padding: 0px
}
.footer {
  height: 100%;
  width: 100%;
  position: relative;
}
.footer img{
  width: 85%;
  position: absolute;
  bottom: 0px;
  right: 0;
}
.col2 {
  padding: 5vh 0;
}
.bg-logo {
  position: absolute;
  top: 0;
  left: 0px;
  right: 0px;
  height: 100%;
  opacity: 0.5;
  text-align: -webkit-center;
  background-image: url("https://storage.googleapis.com/froggy-service/frontend/images/dialog/input/logo.png");
  background-repeat: no-repeat;
  background-size: 100% auto;
  background-position: center;
}
.input-dialog {
  height: fill-available;
  z-index: 999;
  opacity: 0.9;
  border: 1px solid transparent;
  border-radius: 10px;
  background-image: url("https://storage.googleapis.com/froggy-service/frontend/images/dialog/input/inputBackground.png");
  background-repeat: no-repeat;
  background-size: cover;
  padding: 16px;
  overflow-y: auto;
  max-width: 80%;
}
.input-dialog > fieldset {
  height: 90%;
  border-color: transparent;
  position: relative;
}
</style>
