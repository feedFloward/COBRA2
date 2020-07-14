from collections.abc import Mapping

class JsonParser(Mapping):
    def __init__(self, data, inputspace, model, train_specs, *args, **kwargs):
        self.data = data
        self.inputspace = inputspace
        self.model = model
        self.train_specs = train_specs

    def _parse_data(self):
        X = []
        y = []
        for cls_ in self.data:
            for point in cls_['points']:
                X.append(point)
                y.append(cls_['index'])
        return X, y

    def _parse_inputspace(self):
        return tuple((self.inputspace['inputspaceHeight'], self.inputspace['inputspaceWidth']))

    def _parse_model(self):
        return self.model

    def _parse_train_specs(self):
        return self.train_specs

    def __iter__(self):
        yield 'X'
        yield 'y'
        yield 'inputspace'
        yield 'model'
        yield 'train_specs'

    def __len__(self):
        return 5

    def __getitem__(self, item):
        if item == 'X': return self._parse_data()[0]
        if item == 'y': return self._parse_data()[1]
        if item == 'inputspace': return self._parse_inputspace()
        if item == 'model': return self._parse_model()
        if item == 'train_specs': return self._parse_train_specs()