from .classification import Classification

from sklearn.linear_model import LogisticRegression

class LogisticRegressionWrapper(Classification):
    def __init__(self, *args, **kwargs):
        super(LogisticRegressionWrapper, self).__init__(*args, **kwargs)
        self.model = LogisticRegression()