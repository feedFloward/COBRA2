from .classification import Classification

from sklearn.svm import SVC

class SvmWrapper(Classification):
    def __init__(self, *args, **kwargs):
        super(SvmWrapper, self).__init__(*args, **kwargs)
        self.model = SVC()