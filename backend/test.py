import functools

import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Dropout, BatchNormalization
from tensorflow.keras.optimizers import SGD, Adam, RMSprop
from tensorflow.keras.utils import to_categorical

from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import PolynomialFeatures

from xgboost import DMatrix, XGBClassifier

    
class Dataset:
    def __init__(self, data, inputspace, *args, **kwargs):
        self.inputspace = tuple(inputspace)
        self.X = []
        self.y = []
        for label, cls_ in enumerate(data):
            for point in cls_:
                self.X.append([point[dimension] for dimension in point.keys()]) #also works for more than 2 dimensions
                self.y.append(label)
                
        self.X = np.asarray(self.X)
        self.y = np.asarray(self.y)
        
        mesh_x, mesh_y = np.meshgrid(np.linspace(0, self.inputspace[1], num=self.inputspace[1])
                                     ,np.linspace(0, self.inputspace[0], num=self.inputspace[0]))
        
        self.inputspace_meshgrid = np.c_[mesh_x.ravel(), mesh_y.ravel()]
        

class AnswerDict:
    def __init__(self):
        self.answer_dict = {}
        
    def __call__(self, func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            if func.__name__ == "predict_inputspace":
                self.answer_dict['Z'] = func(*args, **kwargs).tolist()
        return wrap
                
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
    
            
                        
        
class LogisticRegressionWrapper(Classification):
    def __init__(self, *args, **kwargs):
        super(LogisticRegressionWrapper, self).__init__(*args, **kwargs)
        self.model = LogisticRegression()
        
class SvmWrapper(Classification):
    def __init__(self, *args, **kwargs):
        super(SvmWrapper, self).__init__(*args, **kwargs)
        self.model = SVC()
        

def test(model, *args, **kwargs):
    

    if model['val'] == 'logistic':
        clf = LogisticRegressionWrapper(*args, **kwargs)
    if model['val'] == 'svm':
        clf = SvmWrapper(*args, **kwargs)
        
    clf.fit()
    clf.predict_inputspace()
    
    return answer_dict.answer_dict