<template>
  <el-dialog title :visible.sync="dialogVisible" @closed="closeDialog">
    <div class="upper-block">
      <div class="upper-block-bkg">
        <div class="case-content-type-header">
          {{ selectedCaseDetails.type }}
        </div>
      </div>
    </div>
    <div class="case-content">
      <div class="case-content-type-body">
        案件類別：{{ selectedCaseDetails.type }}
      </div>
      <div class="case-content-title">
        案件標題：{{ selectedCaseDetails.title }}
      </div>
      <div class="case-content-date">
        時間：{{ selectedCaseDetails.create_time.split("-")[0] }} 年 {{ selectedCaseDetails.create_time.split("-")[1] }} 月 {{ selectedCaseDetails.create_time.split("-")[2] }} 日
      </div>
      <div
        class="case-content-location"
        v-if="selectedCaseDetails.location !== null"
      >
        地點：{{ selectedCaseDetails.location }}
      </div>
      <hr />
      <div class="case-content-details">案件內容：</div>
      <br />
      <div v-html="selectedCaseDetails.content"></div>
      <hr />
      <div
        v-if="selectedCaseDetails.state === '不受理' &amp;&amp; selectedCaseDetails.disapprove_info !== ''"
      >
        <div class="case-disapproved">案件不受理原因：</div>
        <br />
        <div class="disapprove-info">
          {{ selectedCaseDetails.disapprove_info }}
        </div>
      </div>
      <div
        v-if="selectedCaseDetails.state !== '不受理' &amp;&amp; selectedCaseDetails.arranges.length !== 0"
      >
        <div class="arranges-title">案件處理進度：</div>
        <br />
        <div
          class="case-content-arranges"
          v-for="(arrange, index) in reverseCaseProcess"
          :key="index"
        >
          <hr v-if="index &gt; 0" />
          <div class="arrange-title">處理主旨： {{ arrange.title }}</div>
          <div class="arrange-time">處理時間： {{ arrange.arrange_time }}</div>
          <div class="arrange-content" v-html="arrange.content"></div>
        </div>
      </div>
      <div style="text-align: center; display:block;"></div>
    </div>
    <div class="dialog-footer" slot="footer">
      <div class="footer-block">
        <div class="content-state">
          處理進度：{{ selectedCaseDetails.state }}
        </div>
      </div>
    </div>
  </el-dialog>
</template>

<script>
export default {
  name: "card-detail",
  props: ["dialogVisible"],
  data: () => ({
    isDetailLoaded: false,
    selectedCaseDetails: {
      id: 0,
      number: "0",
      create_time: "",
      title: "",
      content: "",
      location: "",
      type: "",
      state: "",
      arranges: [],
      disapprove_info: ""
    }
  }),
  created() {},
  methods: {
    closeDialog: function() {
      this.isDetailLoaded = false;
      this.selectedCaseDetails = {
        id: 0,
        number: "0",
        create_time: "",
        title: "",
        content: "",
        location: "",
        type: "",
        state: "",
        arranges: [],
        disapprove_info: ""
      };
    }
  }
};
</script>

<style lang="sass" scoped></style>
