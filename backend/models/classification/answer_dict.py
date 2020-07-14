import functools

class AnswerDict:
    def __init__(self):
        self.response = {}
        
    def __call__(self, func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            if func.__name__ == "predict_inputspace":
                self.response['Z'] = func(*args, **kwargs).tolist()
            if func.__name__ == 'evaluate':
                self.response['cm'] = func(*args, **kwargs).tolist()
        return wrap