import Vue from 'vue'
import Vuex from 'vuex'
import { classObject, clfObject } from '@/types/classification'
import { colorMap } from "@/shared";
import { classifierData } from '@/shared/classification'


Vue.use(Vuex)
// Vue.config.devtools = true


export default new Vuex.Store({
  state: {
    classes: Array<classObject>(),
    currentClass: {} as classObject,
    classifiers: Array<clfObject>(),
    selectedClassifier: {} as clfObject | undefined,
  },
  mutations: {
    loadClassifierData(state) {
      state.classifiers = classifierData.classifiers
    },
    selectClassifier(state, clfVal) {
      // state.selectedOptimizer = clf
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
      state.currentClass.points.push(pointTuple)
    },
    removeAllClasses(state) {
      state.classes = []
    }
  },
  actions: {
  },
  modules: {
  },
  getters: {
    getCurrentClassIndex(state) {
      return state.currentClass.index
    },
    getClassifierData(state) {
      return state
    }
  }
})
