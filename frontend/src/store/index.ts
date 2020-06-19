import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
Vue.config.devtools = true

export default new Vuex.Store({
  state: {
    classes : []
  },
  mutations: {
    addClass (state) {
      state.classes.push(1)
    }
  },
  actions: {
  },
  modules: {
  }
})
