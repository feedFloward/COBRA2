const classifiers = [
    {
        text: 'logistic regression',
        value: 'logistic'
    },
    {
        text: 'svm',
        value: 'svm',
        specs: {
            kernel: undefined
        }
    },
    {
        text: 'neural net',
        value: 'nn'
    },
    {
        text: 'random forest',
        value: 'random_forest',
        specs: {

        }
    }
]

const svmSpecs = {
    kernel: ['rbf', 'linear']
}

const modelSpecData = {
    svmSpecs
}

export const classifierData = {
    classifiers,
    modelSpecData
}