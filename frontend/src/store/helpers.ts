import { mapState, mapGetters, mapActions } from 'vuex'
import { ClfState } from '@/types/classification'

export const svmSpecsComputed = {
    ...mapState({
        kernels: (state) => (state as ClfState).modelSpecData.svmSpecs.kernel,
    }),
}
export const svmSpecsMethods = {
    ...mapActions([
        'chooseKernel'
    ])
}
export const randomForestMethods = {
    ...mapActions([
        'rfChooseNumEst'
    ])
}

export const inputspaceComputed = {
    ...mapGetters([
        'currentClassIndex'
    ])
}

export const classifierSelectionMethods = {
    ...mapActions([
        'loadClassifierData',
        'selectClassifier'
    ])
}
export const classifierSelectionComputed = {
    ...mapState({
        classifiers: (state) => (state as ClfState).classifiers
    })
}

export const classDefinitionComputed = {
    ...mapActions([
        'setTrainTestSplit'
    ])
}