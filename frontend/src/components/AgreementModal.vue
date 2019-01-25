<template>
    <transition name="modal">
        <div class="modal-mask">
            <div class="modal-wrapper">
                <div class="modal-container">

                <div class="modal-header">
                    <h2>「選服魔鏡號」台北市議員邱威傑市民服務系統使用說明及隱私權政策</h2>
                </div>
                <div class="modal-body">
                  <p>「選服魔鏡號」邱威傑市民服務系統（以下簡稱本網站）係為台北市議員邱威傑及其所屬團隊（以下簡稱本團隊）開發、維護及所有，範圍包含本網站之所有圖片、文字、動畫、音訊、影片及外觀設計、互動模式、服務流程等。</p>
                  <h3>資訊蒐集說明</h3>
                  <p>本網站會於您瀏覽時，依據您所進行的行為蒐集所輸入的案件資訊、個人資訊、附件檔案等，並儲存使用者紀錄以供聯絡服務使用。使用者個人資料之使用、處理期限，至您主動向本團隊提交終止服務通知為止（非指結案通知）。其目的為進行後續追蹤、所有服務案件總體分析（包含處理時間、案件類型、負責局處）之用，以利提供台北市民更好的市政體驗與提出台北市政府具體改善建議。</p>
                  <p>本網站承諾相關資料均依原來所說明的使用目的和範圍，除非事先說明、或依照相關法律規定， 否則本網站不會將使用者個人資料提供給第三人、或移作其他目的使用，亦不會成為本網站於開源後第三人所得獲取之資訊。</p>
                  <p>本網站會記錄使用者上站的IP位址、及在網站內瀏覽活動等資料，但這些資料僅供本團隊內部作網站流量和網路行為調查的總量分析，不會授予本團隊以外之任意第三人。</p>
                  <p>在下列情況下本團隊有可能會提供使用者個人資料給相關公機關，或主張其權利受侵害並向本團隊提示司法機關正式文件之第三人：</p>
                  <ul>
                    <li>基於法律之規定，或受司法機關與其他政府機關基於法定程序的要求。</li>
                    <li>在緊急情況下為維護第三人的合法權益。</li>
                    <li>為維護本網站的正常運作。</li>
                    <li>使用者有任何違反政府法令或本網站使用條款的情形。</li>
                  </ul>
                  <p>為了便利使用者的網頁瀏覽及操作，本網站可能使用 cookie 技術或其他類似技術，以提供更適合使用者個人需要的服務，cookie 是網站伺服器用來和使用者瀏覽器進行溝通的一種技術，它可能在使用者的電腦中儲存某些資訊，使用者可以經由瀏覽器的設定，取消或限制此項功能。</p>
                  <h3>資訊處理公開說明</h3>
                  <p>本網站實踐「透明監督」理念，將本團隊依使用者委託、請求、陳情之內容進行服務後去除隱私資訊後公開，所稱之去除隱私資訊包含以下內容，皆不會向本團隊以外之第三人呈現：</p>
                  <ul>
                    <li>足以辨識使用者個人、案件關係人、所屬團體、機關、身分之資訊，包含姓名、電話、Email、住址、有關地址、機關名稱、組織名稱、職稱、薪資、IP位址，或其他相類似之個人資訊。</li>
                    <li>使用者所上載的案件附件。</li>
                    <li>使用者所登錄僅供本團隊聯絡之用的個人資訊，包含姓名、電話、住址、Email。</li>
                  </ul>
                  <p>本團隊將會以刪除、編輯或輸入符號方式代替上述隱私內容，並於本網站呈現，本團隊保有使用者請求對前台呈現資料的變更、編輯的允許權利，亦受我國有關法律之適用。</p>
                  <p>本團隊有權對於顯非一般、通常能達成之情事、違背善良風俗，或顯屬惡意濫用本服務之使用者所提供內容不予處理，並為有效利於公眾使用本網站，不將其內容呈現於前台網站。</p>
                  <h3>一般條款</h3>
                  <p>用戶不得將本使用條款或任何本使用條款賦予您的權益或義務轉讓給他人。如本使用條款的任何規定在適當司法管轄權的法院被判定無效，該無效的規定不應影響該條款以外的其他規定之效力，其他規定仍應具有完全的執行力和效力。任何對使用條款的放棄，不得被視為對此條款或任何其他條款持續或永久之放棄。</p>
                  <h3>準據法與管轄法院</h3>
                  <p>本使用條款之解釋與適用，以及與本使用條款有關的爭議，均應依照中華民國法律予以處理，並排除國際私法之適用。 因本使用條款或使用本網站而引發任何求償或訴訟，您同意台灣台北地方法院有專屬管轄權。</p>
                </div>

                <div class="modal-footer">
                  <el-button @click="$emit('disagree')" plain>不同意</el-button>
                  <el-button @click="$emit('close')" type="success" plain>同意</el-button>
                </div>
                </div>
            </div>
        </div>
    </transition>
</template>

<script>
export default {
  name: 'AgreementModal'
}
</script>

<style lang="css" scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 50%;
  max-height: 90vh;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
  transition: all .3s ease;
  font-family: Helvetica, Arial, sans-serif;
  display: flex;
  flex-direction: column;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  max-height: 80vh;
  overflow-y: scroll;
  margin: 20px 0;
}

.modal-footer {
  text-align: center;
}

@media only screen and (max-width: 768px) {
  .modal-container {
    width: 80vw
  }
}
/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(0.9);
  transform: scale(0.9);
}
</style>
