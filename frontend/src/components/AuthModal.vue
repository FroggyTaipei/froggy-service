<template>
    <transition name="modal">
        <div class="modal-mask">
            <div class="modal-wrapper">
              <div class="modal-container">
                <div class="close-btn" v-show="!isClosed">
                  <el-button icon="el-icon-close" type="text" @click="cancel('DISMISS')" circle plain></el-button>
                </div>
                <div id="firebaseui-auth-container"></div>
              </div>
            </div>
        </div>
    </transition>
</template>

<script>
export default {
  name: 'AuthModal',
  data: () => ({
    config: {},
    isClosed: false,
    ui: ''
  }),
  created () {
    if(!window.firebase.apps.length){
      window.firebase.initializeApp({
        apiKey: "AIzaSyCADQFj1yBxgdS-ODn2v_oJvd4MCDXjWHk",
        authDomain: "froggy-service.firebaseapp.com",
        databaseURL: "https://froggy-service.firebaseio.com",
        projectId: "froggy-service",
        storageBucket: "froggy-service.appspot.com",
        messagingSenderId: "638935759889",
        appId: "1:638935759889:web:0a255e89625132df3c05b0",
        measurementId: "G-57RSKS8KH1"
      });
    }
  },
  mounted() {
    if(window.firebase.auth()){
      this.ui = new window.firebaseui.auth.AuthUI(window.firebase.auth());
      this.ui.start('#firebaseui-auth-container', {
        callbacks: {
          signInSuccessWithAuthResult: (authResult, redirectUrl) => {
            this.cancel(`SUCCESS,${authResult.user.phoneNumber}`)
            return false
          },
        },
        credentialHelper: firebaseui.auth.CredentialHelper.ACCOUNT_CHOOSER_COM,
        signInOptions: [
          {
            provider: window.firebase.auth.PhoneAuthProvider.PROVIDER_ID,
            recaptchaParameters: {
              type: 'image', // 'audio'
              size: 'normal', // 'invisible' or 'compact'
              badge: 'inline' //' bottomright' or 'inline' applies to invisible.
            },
            defaultCountry: 'TW',
            whitelistedCountries: ['TW', '+886']
          }
        ]
      });
    } else {
      console.info('firebase not exist')
    }
  },
  methods: {
    cancel(status) {
      this.isClosed = true
      this.$emit('cancel', status)
      this.ui.delete()
    }
  }
}
</script>

<style lang="css" scoped>
.close-btn {
  text-align: right;
}

.close-btn > button:hover, .close-btn > button:focus {
  border-color: white !important;
}

.modal-mask {
  position: fixed;
  z-index: 999;
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
  max-width: 360px;
  margin: 0px auto;
  background-color: #fff;
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

@media only screen and (max-width: 767px) {
  .modal-container {
    max-width: 360px;
  }
  .modal-body {
    margin: 0;
  }
}

@media only screen and (max-width: 359px) {
  .modal-container {
    min-width: 0 !important;
    max-width: 100vw;
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
/* IE10+ CSS styles go here */
@media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {
  .modal-body {
    max-height: 60vh;
  }
}
</style>
