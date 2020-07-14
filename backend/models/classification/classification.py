from .dataset import Dataset
from .answer_dict import AnswerDict

answer_dict = AnswerDict()

class Classification:
    def __init__(self, *args, **kwargs):
        self.dataset = Dataset(*args, **kwargs)
        
    def fit(self):
        self.model.fit(self.dataset.X, self.dataset.y)
    
    @answer_dict
    def predict_inputspace(self):
        Z = self.model.predict(self.dataset.inputspace_meshgrid)
        Z = Z.reshape(self.dataset.inputspace)
        return Z