<template>
  <el-row class="container-fluid section panel" :gutter="10">
    <el-col :span="12" class="col1 hidden-xs-only">
      <el-container>
        <div class="footer">
          <img src="../assets/images/dialog/person.png" >
          <img src="../assets/images/dialog/footer.png" >
        </div>
      </el-container>
    </el-col>
    <el-col :xs="24" :span="12" class="col2">
      <el-container>
        <div class="input-dialog">
          <!-- Page one -->
          <fieldset v-show="step == 0">
            <el-row :gutter="20">
              <el-col
                :xs="12"
                :sm="6"
                v-for="item in $store.state.types"
                :key="item.index">
                <div
                  class="grid-content"
                  :style="{ 'background-color': categories[item.id-1].color }"
                  @click="selectCaseType(item.id)">
                  {{ item.name }}
                </div>
              </el-col>
            </el-row>
          </fieldset>
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
      </el-container>
    </el-col>
  </el-row>
</template>

<script>
import InputUserInfo from './InputUserInfo.vue'
import InputCase from './InputCase.vue'
export default {
  name: 'InputDialog',
  components: {
    InputUserInfo,
    InputCase
  },
  data: () => ({
    step: 2,
    isClose: false,
    steps: [
      { step: 0, text: '選擇案件分類', active: true, complete: false },
      { step: 1, text: '輸入案件內容', active: false, complete: false },
      { step: 2, text: '輸入個人資料', active: false, complete: false }
    ],
    categories: [
      { index: 0, text: '交通運輸', color: '#FD8D95' },
      { index: 1, text: '公共設施', color: '#CAABA4' },
      { index: 2, text: '衛福勞動', color: '#60B9D5' },
      { index: 3, text: '文教科技', color: '#52C59A' },
      { index: 4, text: '環境建管', color: '#79AAD3' },
      { index: 5, text: '警消政風', color: '#D5B272' },
      { index: 6, text: '市政議題', color: '#FEB28c' },
      { index: 7, text: '其他服務', color: '#949FCC' }
    ]
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
    checkStep (steps) {
      if (steps.complete) {
        this.step = steps.step
      }
    }
  }
}
</script>

<style lang="css" scoped>
/*custom font*/
@import url(https://fonts.googleapis.com/css?family=Montserrat);

/*basic reset*/

.panel {
    background-image: url("../assets/images/dialog/background.png");
    background-repeat: no-repeat;
    background-size: 100% auto;
    position: relative;
}

.panel .el-col {
  height: 100%
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
  width: 100%;
  position: absolute;
  bottom: 0px
}
.col2 .el-container {
  height: 100%;
  align-items: center;
}

.input-dialog{
  height: 95%;
  border: 1px solid transparent;
  border-radius: 10px;
  background-image: url("../assets/images/dialog/inputBackground.png");
  background-repeat: no-repeat;
  background-size: cover;
  padding: 16px;
  overflow-y: auto;
}
</style>
