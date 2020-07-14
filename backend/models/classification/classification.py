from .dataset import Dataset
from .answer_dict import AnswerDict
from sklearn.metrics import confusion_matrix

answer_dict = AnswerDict()

class Classification:
    def __init__(self, *args, **kwargs):
        self.dataset = Dataset(*args, **kwargs)
        
    def fit(self):
        self.model.fit(self.dataset.X_train, self.dataset.y_train)
    
    @answer_dict
    def predict_inputspace(self):
        Z = self.model.predict(self.dataset.inputspace_meshgrid)
        Z = Z.reshape(self.dataset.inputspace)
        return Z

    @answer_dict
    def evaluate(self):
        y_pred = self.model.predict(self.dataset.X_test)
        cm = confusion_matrix(y_true= self.dataset.y_test, y_pred=y_pred)
        return cm