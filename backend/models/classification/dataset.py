import numpy as np

class Dataset:
    def __init__(self, X, y, inputspace, *args, **kwargs):
        self.inputspace = tuple(inputspace)
        self.X = X
        self.y = y
        
        mesh_x, mesh_y = np.meshgrid(np.linspace(0, self.inputspace[1], num=self.inputspace[1])
                                     ,np.linspace(0, self.inputspace[0], num=self.inputspace[0]))
        
        self.inputspace_meshgrid = np.c_[mesh_x.ravel(), mesh_y.ravel()]