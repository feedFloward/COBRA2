from .classification import Classification

from sklearn.ensemble import RandomForestClassifier

class RandomForestWrapper(Classification):
    def __init__(self, *args, **kwargs):
        super(RandomForestWrapper, self).__init__(*args, **kwargs)
        self.model = RandomForestClassifier()