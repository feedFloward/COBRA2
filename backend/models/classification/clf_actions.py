from . import SvmWrapper

def select_model(model, *args, **kwargs):
    '''
    returns a classifier
    '''
    switcher = {
        'svm': SvmWrapper(*args, **kwargs)
    }
    return switcher.get(model['value'])