<template>
  <el-container style="height:100%">
    <!-- Page one -->
    <el-row type="flex" class="panel category-page" v-show="step == 0">
          <div class="category-content">
            <el-row type="flex" class="category-content-row1">
              <el-col :sm="24">
                <img src="https://00e9e64bacb0eb0ec7db292b21fcb05852b8f686822ddf2723-apidata.googleusercontent.com/download/storage/v1/b/froggy-service/o/frontend%2Fimages%2Fdialog%2Fcategory%2Fnamebar.png?qk=AD5uMEtftqVXjXUG8TYGwdsNbR_ysOhy6w1sbgplFSczryoBZPtfdw4ArUXz5ErDiPxzsTsxiqfgpC2Dhja4xQvjJtptBvopLS3ItGzyeC5FobkKudeBBNVdFJvCGXOFK0y6jB5jqj1VkMKQMyTla52xWJCOasy2WJm0ue98xwLBv7hUcbosIugxMCxLVc1QnjS7YrFQJdW8Q8ypVlaBPLHkme47HgwQ-B4RH3aelanKGz_bMJh9bTxvXnqKCp7I7bKH1bV_Kng_PRX4aRWoO7DfzEOqihk9CIaDyLus2axLUeB4DUZfY0M9IUoJy65yVIRFduHtf7QXrTT3jjQ5HnWcxz3MSURmhiJoTwH9M0y4MJBJgLHqXMmOJ-D4hM5p16H5STV_KWvNudb01j3brZ_2oCcz8-UbQlntyiyXygYXkTFTKRQiJfmBJ6epTVKh6TNvFrdd1P4Ipq4mhZtw2GZc0KR9RjNfvk06bvhor3WTaZDCi4MZ-Kv5QrqnHzQqzXwzgKnM4eNMRFy50O57Rnp619mb7mfhGXo-DwpoUhd2b9eUqVTCv_iCjYYvOa0ooJgF8M58ZmqsywPmkKap4eLB67VXuEN6NWRUzbfmfjkVDWEZjf4oaIMCM3D4H9LfwCikXM3MCErIEQLXL6GcXGNTUwi0ZRknLvIRNoYcsTlW15-G9i3u803fiJsa7fQSHWw8hBR-ZEU7gvrbSBgnrQJOS1c5NYueXB2FxqylS5OGPs5h7RPi5nWzFVFyCUn6MeNiKDtOBxZMp9TE00BW0rpz_21MMmxYJ1OY4vCVfW7e08Q1G6BMjErJIaR-JP89xp3dSCCcX--b" height="68%">
              </el-col>
            </el-row>
            <el-row type="flex" justify="center" class="category-content-row2">
                <el-col :sm="12" class="hidden-xs-only category-content-person">
                  <img class="category-content-center" src="https://00e9e64bac56bf409b32256fa70c99cf4ef75d539cb6f122b8-apidata.googleusercontent.com/download/storage/v1/b/froggy-service/o/frontend%2Fimages%2Fdialog%2Fcategory%2Fperson.png?qk=AD5uMEs8fWdKknjdJinehZbvsF71Wz_5LIqvueGMs1cYdp34iFRbhheVQ96smpDz6pbr-OxhI_sn059ldWWuH1e8eek2KaZzcgIPwZ9Z7v3Wb1vGhWA_ye6IopvmxXiI1m4yuWU7JNJgbHX-htbL_Jzgk2POBvMSfCYp3e00-6eXWObKweI5lN8zsjJUELv3Fxn72izJbeIlWG1isOecLgZa3iyhQTXLItswWpJ5eq2fT0Q-6ruHwzTCezONBMMIl0Oj20U409861bnVX-jUIYI7NTtn5VlKlS3EQc84QH_hD76puozb7YwZrIpnepy78og1zjKbx8egmdVWXR8FQne6IxSEc4l5XQ9z5KzAuvvvLWOyjvH6QCmqXKhH3fPvHRihsFekXFMfEb4hIjcKoEvQmOR2jdeoqPsSCbpHyWbZYYcREgTEC_QxCtnTLexYfEP5QGggqyzB2uvRBao47oa09izDiQbcluyR8SAPD-rTmfz0Fa8Sr7qez0ttEYSGMOhi1mK6WSHXVryt3AV9CMwpcyGb98QlI3s8d1RqoEx1DEtRQpPccX4eSKuTNeEV7E-Yvbr63I7eijY03xvnfoW8Sp13P6bNBGcBwLk72VFPA60swE-xsx_VV4hbRbVpDSbjItaUJ3NzkSeW9PdgTjkHTolWp2XtEgFlhnfF2ui3kMFD1ih9SK3MDRaDMPyKBG1tNtpkQNB7D4a-nQes-QWABWL2LK9YPqb61aGx89DKpcTQebiyDJsd8-MgzgCnCpZQbbfD_NPtUgddeA-RNydCE4t8Qi7gSaE6x265cMvz57WzIGF2PhfdJ74FUCytniNifnecNBH3" width="80%">
                </el-col>
                <el-col :xs="24" :sm="12">
                  <img class="category-content-center category-content-froggy" src="https://00e9e64bacb78bb0bf3a0f27723707613660dd97036c9772eb-apidata.googleusercontent.com/download/storage/v1/b/froggy-service/o/frontend%2Fimages%2Fdialog%2Fcategory%2Ffroggy.png?qk=AD5uMEsBLYPnpPqXCw6Yeyte2MFKC-1SrhS4s7XPmfbSB4bLgF1oH9uX4KkJQkHutVoE8NOwTrDMfvn2PjErE1mBsb7f-X4un9G-DTe__g3lPdqxWMvA38wSvuv0-2LOR991OjcIQtGdLSfuTntDRBIOv1R3tZ_TXi6cUlT_mFyE1N-JK5ERS578RGgkw_j1hKkQFs7QmkGOd3RQppJz48b0kJ_9SVKLBy64BduLcoic-uIQnYOY0XZZrrw6HGlU7lOn3qYVmyXg-LIXNSBhZQi7AO1O_u1L620k-lE0MRKWee9QMhuHwhsIcWeZHYfh0iOrgaUJk9o7XmM6fUovSN6wJYIuujQlLYfHmDhvATVX2OQoBCjhjBOOZ6gsbgO6bo65DemUMs7II5Qm9rCxBPEE7Ll07wZ_nKod5JNDx_cvb2oqlFkghgvuZbzCDMFg-xX2UIjo6sSnsvw8qajHmA-ajizGwASNe7nD7DjZrm4Agwls3Ton6yqf3VZ4ItoyZD6n27vRMZL08P2yoVBPO4TAN39aDeUqy6TGdj-qBekvgZkJbqpycwKIF1RyoWis23jEKFbCWWosxVWFciTJrhVHxdTtJ2jhYXY0hpaSc3enBLwYWLhzgpXjaoexzZ8gXnupKIK4ljUm8K0lc2BfmjY6XlIqmylB7XscGCKx9jbdlzDZBScI8bO0cQVm90wvvl1QWzwN-cggQ82jZKOO1OfGMyPDRA15a_KerJ3FhZA_DxJaQyX9DNeRlz-c4nG_-6X9kWKJtjxdZ0V1wWtpbF51G_qr_hnQA-BIME7raQ4Akv4aKm5HarrUKRr912Yi3JaxF6wkErTl" width="75%">
                  <img src="https://00e9e64bacbf240e32f7617c8ee64e0114b00d7624b08a1101-apidata.googleusercontent.com/download/storage/v1/b/froggy-service/o/frontend%2Fimages%2Fdialog%2Fcategory%2Fprogress.png?qk=AD5uMEuYDIwWkjOllRFdKxsOsPVIv_oj94QfV4nCHfOTFRaAab_gcqiaIAnx07cQ8lmyMXBsQKSwShEZRr0WKMhJoTubCg7R8I_svCvRQMQJlbRLr9IFGS7EfwWkKh4AJGu0vpvYbEyWB-tYDeNpYqF2avmEcEWfAWnTPEXDXh73-pE4C6h3jaT_dI3Wykcc3qP6r1JjGdMWtqIryDTQ_ZlQ7ubXa2oNeIb4UvEt5Fjd6QGLL8hz-GzB_RJsaQw41o3KXDrox8XGBMjcXbVGI-UCAHQmK_lqFBn7tUjFZH_ND9Psy8nL1SO1BhRkhCM0IiYi-QmMWbqJ3onApJ4YdW1o0czhD9qV7wFFkrH2nRYBljbUb3C-AWNhEM4Wjtms2dlhk3oEIgySzSzNywSHrGTAZiohsHteVTfPB6tH5DqTslwksvy5uOKeJ40dAmIeuYX4G8KK1bCel6G1foG15hBwxQAzU1USiOKOkZrF8IjUty_bzHhIDQIAtWvzm_ESIknxFZL2VY3DaVPDgh9Nbvs6v4TVb1WWPgpO4VBIPrYALrdkLqgQXya8muFPd5Jke-6dVbqZ5bqB8bCJjtzIsb_mspftgyEjYgi2rZKL6CSGme1UZs5k3m5N7kifz4Awp_FN6IYhJzrzC0GiPKPg0vvcpjLaH9VZF-EpTrk1MPFfVqXZ6YFTOVCxmN4OYWSvnkx68zO0R6JRPM8pZQBmJiJYPoJTQ8xBmIxjz7B_KIEL-fI4D-1IiouS8ulqPM36NFcus1KoYOCI-h9typYL-OAWkR-qMQp0b_3oT0gSmqBek04Hicx86-d0Q7E-TyRF_lsjMscJqAlQ" width="95%">
                </el-col>
            </el-row>
          </div>
          <div class="category-footer">
            <img src="https://00e9e64bacee1bddae2a2e491cf61d76bd0d345f270f8a0daf-apidata.googleusercontent.com/download/storage/v1/b/froggy-service/o/frontend%2Fimages%2Fdialog%2Fcategory%2Ffooter.png?qk=AD5uMEuZBetNEZqqzOi7Fi8GjHPFcFBcSd6n-qkpUmEUuvVKa18V3gjXKCvtSQtLKgL-8fb3mjo2dQw-VrG508rnp2fpMzGEx0i9GX5XX9L9ylbRJq1CzruTtnrod1XDSY7MIEskdAefnjrg8o3-snX_6VSZxX2OwlBR2DD2M3Ah9GUw8CMaGZj_DS9yQafmuKBRXEGPnCOCuZMpnu-jGRTVv9DJ_eBTFYXuQeJe3jadjL0RJ96OZclJgWxoJFmN90aJexv2y5h5zqB3EJjbDlwIRm5G5k9LPLZubiLvpXMezL9EL_UXkP5mkAwX24AJ4XCXZvS_lHCuR0k1bk36Gg1xT8Z3eL3P1mbyxrPegAgsfRV8ur1bGCmlCa4lOZ3Nai6xFfSgx2v_4RIwY6J51Y0LtNXnutNXI4dXAYVN39_tU--PfU9r3TBD8KRJKj76qNC0DQ-2YYDKdJgmawlZa1-YsS4XnRJPvIQvPCaC7FlaIHpoXeTkduKAwZyXiBwtEY3aaFihDtMJ2I-3rQZWv0iYdVvdO1DV-k-4W1dQ1Ed3bp4u-2MgRfsq81tJVJyCtCwHaALq8LvP_ZGs1GmtOt-wTDiweWBcFbfrBhLuqgRbKTwPmF68ISFVy1r1pB6wC2riko66wLtkQJ6A8X96twj53IlJJjW0y7ZwS1lDMevdP-Rh5PkhaxRDzMvrIeYoQk9PhdgqX5Hk6M6ovosed6t7P6nDsRDWx-68VR3lrPrMp5MRELjUxYIpE5cPZK_drhcDxR1vP-5bZnXsOLJiYdogz6uEd6HllTzphq8pWNUzqz0L2kWOsXTd3l_luWO0WsBrdGu7nwLf" >
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
    </el-row>
    <el-row type="flex" class="panel form-page" :gutter="10" v-show="step > 0">
      <div class="bg-logo">
      </div>
      <el-col :span="12" class="col1 hidden-xs-only">
        <el-container>
          <div class="footer">
            <img style="width:90%" src="https://00e9e64bac6c651043a04bad24d63de76f51649329cf7d2f36-apidata.googleusercontent.com/download/storage/v1/b/froggy-service/o/frontend%2Fimages%2Fdialog%2Fcategory%2Ffroggy.png?qk=AD5uMEtAla3zplzhWT1DX1Wl82x20bis3i_Qp2hnBeYZCwhw_OsS9NDI2tkweobwgpfvGsFJ5IFvGJor3XjzFD1YzO5pCR4WThB1kyWwwx6fmkUz1_tFCakHWo3zQZiAU0z1iO_uNVgI7LcYUeo3uIjndQIgNOpXOzBt5A_Jr5L1LWKdYGBD7wF9wmTOwQyu668mWTozaoexUh4UFLG3fHhPNQZo9LKyd09toU6lRG86N69kqhIqIRBOeCuMLlzjJNsgBJM55gWP5s964pz301WHOFtRVmwOHAMMS4xHkvOd6SWmQPgYjmdQif2AsUbfFk-LOresNF0m3t_UsuJUirLa-ZJX4hiPoYXrNf50R5GqfpS-MgqKhLo2l91D_PTU-_eRDUhiqrN6FMQRIKBCsCD-4eGQXg8H_Jo4dmwLX6VvkVqZetsT5DMW5Cdgm9nhwNYnCO71I5gpNO5Zrp98f5a34n_D5_9gWLLBeLbz6aO_MXCguCi6F21UW7o4S_naEsG_b348isnlOMQdfb84RTuNF82ZMFepqLvfrYtc_B9KPS6Q0D3PhfxOxPRM_vxW5NBazUASjqZC-GVPApD0Pycaczev4p7qN3dcq3vYY_kgwV1Tevz7eE6pytD9D-3dXq9vnMN_2KFU0QX32oyTg3tGsZOly7QJBt62rG0lyGqyqmMFK7D0txNKdgwZG116F729bHW3gQonTuw_hRQX5STO6sgWv92EI4sW8O1iKsQfe0_AwS-GEGUlB68cRM5kcp8tzUv_XzDMCWIbkRHrTgdDgt9edlw8NeNlh9v3R3iXoXN1RkoaNVl9jn2WjZJFPWwrq_yPKMSV" >
            <img src="https://00e9e64bac327b503d3091ef53c7134b476a31e351de1582e6-apidata.googleusercontent.com/download/storage/v1/b/froggy-service/o/frontend%2Fimages%2Fdialog%2Fcategory%2Fprogress.png?qk=AD5uMEu7w-E7VTM6EbASM6d-sZOuzOVwlM29w5o97oRW7XjHqPg10AGmI0_ly9TDK33AIvonwkpkNmwHPmB-dUAb8r5Ly2jZhOO24EyhlmzEumCKRK1di6i64ERJq26jTSEAJBxtw0Y1IWbe65NgVg8AfUqixHwpEoPLqeS8D3TKO-k_B4UuNWxQkTVwPyWMDZxl1Xx9X_Ofbprij46jcZtFLPDOr8QYEayschDPQ3aTz2p6Bql3x0mo7Iv77o-NHGu8cEDf6SyKtMtfl_zdCR_TuCbZ28vdxExjm9Bp_-hmlzsjXZ5gOS79-HPY6lg6yghzYJAWKhuVZb8wNWuv8_CS3KStY9WmavNdgyNYJ8WBakRNEhBRcSNXLkMQp1tYuxQBANw6nduPSTyEP003_YTjc6tJFYgzwmxMf0iDHfMhJr1ZpzaPM1DXjpGOWjxwD3QxE6OnoraGvMkeR6L7GfvZ0BWbAm-M_Sw1672DwOPjdVzUquozPABHfc4uKwEmjtTm0ApNF7MZx2UcKUnQKihJADoN6kE5uBYHsdM8xKyvSQ7GQEemDhIysxabTZ2LpCvMuWkCPsCGqjfH8Uqes3mUy27WqxKxUwf6XJdQx5o8ZID_v9fH00TR7HwzW5mnXVh3i2wR4G5pgdmF3aybF0V--84KwUHXrqtBePKXIX3pRPc9yf6OSRvaWPMAT8mDwNSOP59fNuXKsbXYcECUJk2gsSo70Zji20thyro4rjj5R5YTOILSG5lnFOEKhly2e6Wq31UuM7CKaQRhR3-ASRx7_8VCGzD6yXbxaqAmvaUolVOlCTxfuHEJtaz0y4bnS2a-FcJozbAw" >
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
import InputUserInfo from './InputUserInfo.vue'
import InputCase from './InputCase.vue'
export default {
  name: 'InputDialog',
  components: {
    InputUserInfo,
    InputCase
  },
  data: () => ({
    step: 0,
    isClose: false,
    backgrounds: [
      'https://00e9e64bac26a44c0196acb2ad4389e15e827863a232953457-apidata.googleusercontent.com/download/storage/v1/b/froggy-service/o/frontend%2Fimages%2Fdialog%2Finput%2Fbackground.png?qk=AD5uMEumAn0uRKrkNjY_c6KUujsQCiM3I1vTXyQUkFx58BGOX-z-H_5yZfVRmsgPCCSEP9zo5PwozPGb9gdL1J7aia_NX2Us-Z9AIiKxDk5ZQJkK_EnJM6OFYAbWLKbTQIZcavvn07ZNcpWpSC4SgouhlKUu1fFTyA1QGG7Pv-V4K57ZQzvPjKS_h02I9AhzAj5xokFDVdFmJZHHy9EyDE715gJ7b4_HGpYVhGaIgLAMA2exG11jb1eigiGu_BVqidTEdiEW51oIBwpb5UNLKliXR4vuWI7q7zyIR1ly_LmGcc6XqFBacb__mX-NGArtnsUgZfG2C512z-17n-4kUkj9lzvSAfH0E9rZtcd9PqtVul5GmfwPJSexdjnxH3AohzxlwbikMMfdP6qpIrXFWrJ9GqfEE3pZqNLOKJTTfPOkC6sxi-NlVFNhuyUquunZZKqeAxCTE8h5RaUKAfVmfy2rfore5xgxTrPL10g_yfVyD0ObCUy4YwwKMjks0x-FrJBsDEgKmODxPMZb9EQhjMJMIV-I57FdfXOXmGhXSSQqFgLlhgGD2EQQhMMjaaW2Q-i8TDhAVx2_Ivy4bpgwgYoxHlZbPibWX1m6Uh4uFOoiEFAc649QaKoRFQ1r-fw3Ebl81a1BVoGyp9KvTZZkeISW2jKaD6O_3Kl1z_4-mglYhd1HU1LYnbFCVdU6IBxFwSdKHvDUxM6hIin2ABlV1H4T0Wix5-bVLQP0_kpXIY6W4TaDtr2XiZ5Y5Kl3syZYY533SzSSGqfIStPleRVMXXv9RDJo76eDnmqJPs5gHC3cgXVXpH0dd0WVnL5unVVPAVV5ujkgsxtD',
      'https://00e9e64bac88b4c027e67b164697e46e92aadacb628b2ae811-apidata.googleusercontent.com/download/storage/v1/b/froggy-service/o/frontend%2Fimages%2Fdialog%2Fcategory%2Fbackground.png?qk=AD5uMEuTinuq4AQBbHn8XCp3Jy57I_a2rD0F_RXk58Surk_B8oF5ly5INL49lX7J5FQTg7PSzl8lQlv59OYnMCK_l8aRaRogQKUtKiaHWwzs4h8sLBX3sd-gJK2PiIuuDk5pPZ6K3U39lMyfjtodr0Reh7DXlCPCZPyRUfHHyayzZQxApcWt4aiHnIjmgw-UwrX3eodbW3_9qJTB8Arh1GkqWi3aYbYvV5W1om-YOVbEa4O6HTMlFt50So7qSvEXjM_E0jRTjXU3CUoK-hLEoVeEIzfhRHfKKCikPDEyNQMroi2tHLDgERRnIHWXjXmTQhCITZDeDKvNAPpvLInQbrm4b2CPVI2u_iL81-Eu3igM3oRdXRTzEYGsQ_aCt9hxO7Q7AONiQUaHpkd8QbMjf7zVSOigMBwXKjMNhTeBlrTfgvF_FXcGI2h9KbYM1jfRFR9OKN3TPvzzrLUbGoHxG3hAgi1cEQ64Q58B5KNYzPVhs900VzrhXda0p8AReIz1xFA7zy-faKxOxjrV7j9l1j4-SSYiZlrW2D9fdUjtYSbTxFb195_H_kSDscQuz-ZvaBI6qmF1SjmaJ_egqLdzsgx8z1HCZry1EuvC4qR7219SylPFt7Aj_3l7kyDR9_O7DR7PcOsKft1Kg6B8wz0liFzHFjO92gdvlpJhuXKrjrNjen-lfCtU1fS0VMUz3BPgh5y7c_rfUw-uCH5oeRDKmRaePt4CzAeb39Ii_cVP5UvcLriPwo5svz-pjuEBkZxr1xht_H_kOBu5MXC6PtDZF0HbegeCp_u12z2Q98wps-5WFaCKrjGx7dDBp0QCB351HEIIb1eBTwyc'
    ],
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
      console.log(type)

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

.panel {
    background-repeat: no-repeat;
    background-size: 100% auto;
    position: relative;
    width: -webkit-fill-available;
}
.form-page {
    background-image: url("https://00e9e64bac58b7770fd6e0de9934e3b062dbbaea5326778c02-apidata.googleusercontent.com/download/storage/v1/b/froggy-service/o/frontend%2Fimages%2Fdialog%2Finput%2Fbackground.png?qk=AD5uMEsM8sZH1Q0HfviWEQnTEjeudoR4ZDUIegaMscQ5PllmwD2YEqxehQ_sQC8Y_5wW9HnEURj-cNfXCLvNGP9_ObAJ4nYDfZcbiefg9lNCMYR2BVm-MFU2Mw8--wosf8hK6ZeGq4OM2ftSrkSDB7fvqzqCRVkvSJtKLDBkbBXR9rRxNbfjutYGq_4s3kxzoBEC1tBUtP0ot6LW7UKuxUWu1sBSSUqeJeRCwPrZJnVIwPT1o_uKogXtXTEGvTcdByuljKxyI761MCj19TpvPxYC78wVPInl7WrcAq1vlNdHYT7HaaJENOzHYMQNxk5BcmVkNfQpldkNvT8fU7zATB1EcJ6ZmN8BAfxRoTmYVBUYowHEOlJMS1pLs6uC_cipzrE6Ugsk9TktpE1b35TlJN5LgNlTVMXlRljHUQIni9TVqEgSeNmgjHlbQnqFiRY3ulOdNb9dyJqIJV2B3TSYCEmMj15gfByQ74ZM2w64CCcrsnj1BjB-0G4S6Eoeocj2h5LfdH_OIz65ptXf_HKHptADasyXTXZd2btquGdUs_IVCJMVPjAjAqSN8aiNZiMIfMr1te6uLmn6Yo8KV02r3v7xdNsHxMBdCXYM5vhOzVeX5NVxZWkQ-Z_UIb1VqSOs1lFFH_PqxVySuFDxKrvJ4Q8kNTu8bG1GrYB3ctTzpmeORGFhem66uWeWGNOHpCQGSDJ9agd0zntR3NIrbdA8GxLWGkxjVd81eW-_RVsEaAOsKtZWGA2QwXHzeGnbBg7yrNNBB6iBQlH86r5wh9jzHg8fZDnSv_oWDRWoJu2jWkMlgaN4GPswHFdtlEW8b3ab63k4PAaZ76Gl");
}
.category-page {
    background-image: url("https://00e9e64bacc1348d42ed3eb5d37bdbb2f8dc6e63fbb098605f-apidata.googleusercontent.com/download/storage/v1/b/froggy-service/o/frontend%2Fimages%2Fdialog%2Fcategory%2Fbackground.png?qk=AD5uMEvNhtYMVxr0Gwj5x-nuSNbc0gvi3dPaXR6kZVL81QUecseARIF2GTGz3JT8Ht65r2gGa8fCeqK6FbgMPfnn8O8aKNvriPH95vs39yXvXcDyn0w5lIlwgoIAUvGlE3zVCvlb4Q7LJxuInTSqG7LNDgjDKxccfe-39IZF7v3ygJWm7oWXUNeGtLn2vM2aYEltfFW-j5zXayamBHo9v_0c_v9If3V9BW3bdE3q5ABxUeKzx-vAHgdHgrBmKXlTXOszq62iDX0fdHD4thqg0iY4zUs-sOx_Dwxn93ZF0Qup_UMjcYBrXkD9E3U_dj5SROVrnNVpGe--b6xVzHRoyzf5bGbvN8VwxVuKmjCHHFqhz0gPau--2qzCuWe85MoZe9Rz4bug568IRyC09NSoR9hxMYtraFcod_nl08hbfMkm0F0mCuOW5TMwFhLWT9u7mw4Bo6FLU6EeTy2MtRGXZh5WXkZ6g46fduWf_SrQ6a4HD0WBvfFLnom1oLrzj3SmSQkM8ydTIKPlZjYGokEmtuP-ZQX5otU7VEiD7UiL1xODSVcbzNvgUV1WQVVDLC4xiwY-Eg5wFFFRjVPsdOVQ3yb1QW4mIX7s9sLmpgJyygIGtl2bxZSw8QRpWgXgTPiC28VyChiT6KOLUKONUdCsBo6KCD78zaiNJXio40Cq38mK2mVKG6ovR_trloH_bq-A1krbv4be-mrHhMEZYEfLvu6l91-y6tyydvJVTOm-ftuQT28OtKj-CRjF6Md7KRxLFXp9Rq9priqm65HbK3jD3hIlBUbhTYdOoHz98a7htBfPowtCqKdIUA7984L6D06XE4yf09Su3yJ1");
    flex-direction: column;
}
.category-page > div {
  display: flex;
}
.category-content {
  flex: 1;
  flex-direction: column;
  width: 90%;
  margin: auto;
}
.category-content > div.el-row {
  flex: 1;
}

.category-content-row1 img {
  padding: 16px;
  margin-left: 15vh;
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
  bottom: -12vh !important;
}
.category-content-froggy {
  bottom: 6vh !important;
}
.category-footer {
    background-image: url("https://00e9e64bac69a5f464ab72b190c25b33ff6170689c89c88fc3-apidata.googleusercontent.com/download/storage/v1/b/froggy-service/o/frontend%2Fimages%2Fdialog%2Fcategory%2Ffooter.png?qk=AD5uMEsnfSfs1wFzHVi6hJXnCa_cYE8dVqkDZ5GKhRwH2sohztvCKryTUyWsJohdNRLn5tbE47P_Aq6hooiO3P1hOfwZsKTvwRFcoUjJ10kwPlYsuLkbLzdppxgchKC8n98IrZ1aHqH8UYKJKtfJnj7XecbjabowbPbHlB1XYVCx3gBygXpVFKR1jnyqejFyfONWj7rIUjJR9AWQUBiZyqx8VSTWuKC3TxdY71sBJmjJt6t_Tv9P6VMO_00Ex50NuRU75GzLlgYOJ17SZ1SpSe1hNemeXHm-pbiq1irIC0pQ9mN8spVUGkGVrN03NobulzPW5QG2PtIJJYQcgqFijQcW8NceHPA54KUvMki7svMbbAqW3qidwrQkIbWHhKn_LrgcOfAR_RdSJzWWT-TJXcy-ZV_tjovIf97nRaaQ5WjvJrvF1L5M-4fYx0T27Bi8bqQUAoc-ulOSvsx5Uh-FVoS6TY8qRmRZ8A75wMVN7ImrjtHFr1zPWz3DILtdGhCy-7kTTpada9L9h-vJu-ZVTE1r2YG_BUn1oJpmuipm9U4Omm7JdzLacnmi_ioXIZzRtayHjJUjZclqdyayI-0jZ2fquKtT9qlo4jV7fchmkfDc-PzvyExhUMoxDQSNx50ehoT_CxnIpY0k0iYAkAjrXtKExJGQLoBguOYid-LwaXCfXZMvsoUiI4yKboiIQmtRbPBWoHnq6PCAjL6frZ8TY6YJCQQEKzekT4e0rZifvEMuDf8AoRWFk2hUrWygRLtGGZXFLJoCnFGfC2hAVQthlLhqIaNr7pbYioZgZ6LPzTV86NCjyT3OqzCIqg4dtHQehgrYX2SwKppf");
    background-repeat: no-repeat;
    background-size: 100% auto;
    background-position: center;
    position: relative;
    flex-direction: column;
    align-self: flex-end;
}
.category-footer > img {
    vertical-align: top;
    width: 100%;
    opacity: 0;
}
.category-footer > .el-row {
  position: absolute;
  top: 0;
  width: 100%;
  height: 100%;
  padding: 28px 30px;
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
  font-size: 12vh;
  align-self: center;
  color: transparent;
}
.category-btn {
  flex: 4;
  justify-content: center;
  align-items: center;
  font-size: 8vh;
  font-weight: 600;
  cursor: pointer;
}
div.category-btn:hover + div {
  color: black;
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
.bg-logo {
  position: absolute;
  top: 0;
  left: 0px;
  right: 0px;
  height: 100%;
  opacity: 0.5;
  text-align: -webkit-center;
  background-image: url("https://00e9e64bac30609361aa9139f28000075f1bfbd9ff4a911e39-apidata.googleusercontent.com/download/storage/v1/b/froggy-service/o/frontend%2Fimages%2Fdialog%2Finput%2Flogo.png?qk=AD5uMEu2vxnYSDraNs9c6UQarXJCjLC7VC3W0zRB693b1y7awLHg2LZV-EJQdMcjWIbU4QdfdhvmA7HEYya1IIIb3zsYr5poIhE9nspnZty-bHI9Gz8WKPLu9HknBg28Cf3SU8YXFhV2oZ-BAI_fd9nBFP3ggKYhRfAvS3Y5xFemWVXM-sygiFQnAwXbag3wC29WVgwTeKK3Umr-maBhFo5r8tfWOorMK0OYvhAFYezzI6wJkEdwYEbpgQBtaLpz4Md_n95zz_Bwyjp5f0jTX-Er-xKi5nMsv5CHizb9XXHRiv3DcR2XSTm8qnXmxWgjDWdndUngcvewPRHdWuoyxb77YAzd105cqCXwp_r8RR5-s2C5Z2vhq_s_DFTBufmxJbheblq4AHtlsrpxT3wCGKWeqwj_EzMFagp72Y_Ej0jbwYFbQDBXe8RMzR7WN8YBl9gLwfJ3SwCiOPq693yRskbWh1YUbopH589JV_7R3LBaX34k0VwBewybdcIgyj-EnGJaI6lSa1faNLsu-WjB2AbegMxaqNywajy_tX-n9iEJRqnSbr3UeaHf3qfkEOiyjr_w3WjrOuTDC4X0Oyl1OefvX4z1fyfgzaDiYmXPOO-jm8qXb67olnVuK-VRn8P32lRlZ8inTGiP9C1uktqmNPgA1u1tcKszO20qMEGpvnS96QOZPXDy21GislOhR-0mUb4Q_LsHQXip4F_cPFRa3WuYV7Z8OYulGj1ApVxBJeWiQyH-PQCmLHIJEtdM_S0ZrnMwShD-e88BcRWVWocTbyBKAv-_ALD59Egqekr7aTavtP5DKkdu8lI");
  background-repeat: no-repeat;
  background-size: 100% auto;
  background-position: center;
}
.input-dialog {
  height: 95%;
  z-index: 999;
  opacity: 0.9;
  border: 1px solid transparent;
  border-radius: 10px;
  background-image: url("https://00e9e64bac403ecb6aa9b51e40eea5a3ff58eee35bc0d8c4d4-apidata.googleusercontent.com/download/storage/v1/b/froggy-service/o/frontend%2Fimages%2Fdialog%2Finput%2FinputBackground.png?qk=AD5uMEsOuqX1H_nJs5siHTFgkDTu645gV7H2Imgu5xrVuqBqTlss8qECs62_NyVe2kuwgSc8_6CwyB__s5SjMr8suSglHJUS3UgrscxjIgNn67HXT0LaaqpC6UDwWX7vRZwssqiHqS0zO7Za4jhExtCpmSglIKvZZWpok4efHHt5XhAfDX8AfUnwRhPSbOyXRQKe9Sw1XNL5H6biuO3BTVwKI71_YJ5uO2injUyFecsP_i6f9GqwXN90SfoBhwg7CBCHryk-Lr4uy-SG5uZyyC_i2-Uu88kAGcLQ6Z7Pwr0GKY0LCCJXsgmr39ToyEThCIR3zYzhPLxsPqX1wsQfhrpGEJeG7qZxwdoTaFR8jxQe-kN88wiTidzl1_GT1m8ykwFlSzSfRZEGf-ciek6xITAVrfEcQyj2Wr98rse7J6HLPYzVijQJSZrtBIBwdJxRNFaKz_zxcuOgQwws27KpS48xuBs9OvV4CtpaenCBaDToIILGaMoIHIyGcGjhj8esgC10e3yQiqngF7RexbTut5f55MRg3Wu2B74wbvALk39gnuJ_MHgt6CExkMEuCacDaC16lo5Ed68Kw49Bt9v2rZfoedlIk6GKYC3LBz_mlViB3EsMyo6fwxtqt8QmGKXObbZSlyPOgv_ke0LwPbCjDY4hvAFCkLaartKV1cIAIA_kDEhGl9U_varRWEgoTnprfoiTc4N8r_oB7rBC6w59O0lEscyXMX-aBMikrVkT0pWsW4nAZzQDANDWJ7AfsPMTBEjQgXL7QUcQ7gBJq_4N8gpJvNNyVaQNucbgiIpSe29ELDebWL3LawrREcBeHwLEfPasq2HDFmaC");
  background-repeat: no-repeat;
  background-size: cover;
  padding: 16px;
  overflow-y: auto;
  max-width: 80%;
  margin: 0 auto;
}
.input-dialog > fieldset {
  height: 90%;
  border-color: transparent;
  position: relative;
}
</style>
