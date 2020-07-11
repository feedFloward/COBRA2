from . import SvmWrapper

def prepare(func, *args, **kwargs):
    def pass_specs(model, *args, **kwargs):
        selected_model = func(*args, **model, **kwargs)
        return selected_model
    return pass_specs


@prepare
def select_model(value, specs, *args, **kwargs):
    '''
    returns a classifier
    '''
    switcher = {
        'svm': SvmWrapper(*args, **specs, **kwargs)
    }
    return switcher.get(value)