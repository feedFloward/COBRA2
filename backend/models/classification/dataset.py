import numpy as np
from sklearn.model_selection import train_test_split

class Dataset:
    def __init__(self, X, y, inputspace, test_size, *args, **kwargs):
        self.inputspace = tuple(inputspace)

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=test_size)
        
        mesh_x, mesh_y = np.meshgrid(np.linspace(0, self.inputspace[1], num=self.inputspace[1])
                                     ,np.linspace(0, self.inputspace[0], num=self.inputspace[0]))
        
        self.inputspace_meshgrid = np.c_[mesh_x.ravel(), mesh_y.ravel()]