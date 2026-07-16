class ModelWrapper:

    def __init__(self, model=None):

        self.model = model

    def set_model(self, model):

        self.model = model

    def infer(self, data):

        if self.model is None:
            raise RuntimeError("Model not loaded")

        return self.model(data)