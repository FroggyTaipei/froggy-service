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
    header: { Authorization: 'Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b' }
  },
  getters: {},
  mutations: {
    setCase (state, cases) {
      Object.assign(state.case, cases)
    },
    setRegions (state, region) {
      state.regions = region
    },
    setTypes (state, type) {
      state.types = type
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
