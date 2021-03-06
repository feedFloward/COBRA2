from . import SvmWrapper
from . import RandomForestWrapper
from . import LogisticRegressionWrapper

switcher = {
    'svm': SvmWrapper,
    'random_forest': RandomForestWrapper,
    'logistic': LogisticRegressionWrapper,
}

# bigge Idee zum restrukturieren:
# ähnlich wie select_model eine function die train_model oder so heißt und DA dann das answer_dict als decorator rein...

def prepare(func, *args, **kwargs):
    def pass_specs(model, train_specs, *args, **kwargs):
        selected_model = func(*args, **model, **train_specs, **kwargs)
        return selected_model
    return pass_specs


@prepare
def select_model(value, specs, *args, **kwargs):
    '''
    returns a classifier
    '''

    model = switcher.get(value)
    return model(*args, **specs, **kwargs)