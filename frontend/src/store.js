import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const store = new Vuex.Store({
  strict: true,
  state: {
    case: {},
    regions: [],
    types: [],
    header: { Authorization: 'Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b' },
    jwt: {},
    currentTime: '',
    storageDomain: 'https://storage.googleapis.com/froggy-service/frontend/images/',
    redirectTo: null,
    firstVisit: false,
    isMobile: null,
    authentication: false
  },
  getters: {},
  mutations: {
    setIsMobile (state, isMobile) {
      state.isMobile = isMobile
    },
    setCase (state, cases) {
      Object.assign(state.case, cases)
    },
    setRegions (state, region) {
      state.regions = region
    },
    setTypes (state, type) {
      state.types = type
    },
    setJWT (state, jwt) {
      state.jwt = jwt
    },
    setTime (state, time) {
      state.currentTime = time
    },
    setRedirectDestination (state, to) {
      state.redirectTo = to
    },
    setVisited (state, visited) {
      state.firstVisit = visited
    },
    setAuthenticated (state, auth) {
      state.authentication = auth
    }
  },
  actions: {
    getRegionsList (context) {
      return axios.get('/api/regions')
        .then(response => { context.commit('setRegions', response.data) })
        .catch(e => { console.log(e) })
    },
    getTypeList (context) {
      return axios.get('/api/types')
        .then(response => { context.commit('setTypes', response.data) })
        .catch(e => { console.log(e) })
    }
  }
})

export default store
