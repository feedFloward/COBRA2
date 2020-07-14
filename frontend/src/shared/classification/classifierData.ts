//all specs in snake case for python backend

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
            number_estimators: 100
        }
    }
]

const svmSpecs = {
    kernel: ['rbf', 'linear']
}

// random forest obere und untere grenze für num_estimators hier definieren!

const modelSpecData = {
    svmSpecs
}

const trainingSpecs = {
    test_size: 0.1
}

export const classifierData = {
    classifiers,
    modelSpecData,
    trainingSpecs
}