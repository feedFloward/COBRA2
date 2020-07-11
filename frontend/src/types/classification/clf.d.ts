import { classObject } from './cls'

export type clfObject = {
    text: string,
    value: string,
    specs?: Object<Array>
}

interface ClfResponse {
    Z: number[]
}

interface SvmSpecs {
    kernel: string[]
}

interface ModelSpecs {
    svmSpecs: SvmSpecs
}

export interface ClfState {
    classes: classObject[],
    currentClass: classObject,
    classifiers: clfObject[],
    selectedClassifier: clfObject | undefined,
    inputspace : Object,
    modelSpecData: ModelSpecs
    clfResponse: ClfResponse
}