import Vue from 'vue'
import Vuex from 'vuex'
import { ClfState, classObject, clfObject, ClfResponse } from '@/types/classification'
import { colorMap } from "@/shared";
import { classifierData, inputspace } from '@/shared/classification'


Vue.use(Vuex)
// Vue.config.devtools = true

// const state : ClfState = {
//   classes: [],
//   currentClass: {},
//   classifiers: [],
//   selectedClassifier: undefined,
//   inputspace: inputspace,
//   modelSpecData: classifierData.modelSpecData
// }

export default new Vuex.Store({
  // hier für state noch das interface einarbeiten
  state: {
    classes: Array<classObject>(),
    currentClass: {} as classObject,
    classifiers: Array<clfObject>(),
    selectedClassifier: {} as clfObject | undefined,
    inputspace : inputspace,
    modelSpecData: classifierData.modelSpecData,
    clfResponse: {} as ClfResponse
  },
  mutations: {
    loadClassifierData(state) {
      state.classifiers = classifierData.classifiers
    },
    selectClassifier(state, clfVal) {
      state.selectedClassifier = state.classifiers.find(clf => clf.value === clfVal)
    },
    addClass (state) {
      state.classes.push({
        index: state.classes.length+1,
        points: [],
        color: colorMap[state.classes.length+1],
      })
    },
    removeClass(state, idx) {
      state.classes = [...state.classes.filter(p => p.index !== idx)]
      state.classes.map(cls => cls.index = state.classes.indexOf(cls)+1) // restore indices
      state.classes.map(cls => cls.color = colorMap[cls.index])
    },
    selectClass(state, idx) {
      state.currentClass = state.classes[idx]
    },
    addPointsToClass(state, pointTuple) {
      state.currentClass!.points.push(pointTuple)
    },
    removeAllClasses(state) {
      state.classes = []
    },
    chooseKernel(state, kernel) {
      state.selectedClassifier!.specs.kernel = kernel
    }
  },
  actions: {
    loadClassifierData({ commit }) {
      commit('loadClassifierData')
    },
    selectClassifier({ commit }, clfVal) {
      commit('selectClassifier', clfVal)
    },
    chooseKernel({ commit }, kernel) {
      commit('chooseKernel', kernel)
    }
  },
  modules: {
  },
  getters: {
    currentClassIndex(state) {
      return state.currentClass!.index
    },
    getClassifierData(state) {
      return state
    }
  }
})
