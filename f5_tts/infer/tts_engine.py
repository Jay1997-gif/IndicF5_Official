from .speech_engine import prepare
from .model_wrapper import ModelWrapper


class TTSEngine:

    def __init__(self):

        self.voice = "default"

        self.style = "default"

        self.model = ModelWrapper()

    def set_voice(self, name):

        self.voice = name

    def set_style(self, name):

        self.style = name

    def set_model(self, model):

        self.model.set_model(model)

    def preprocess(self, text):

        return prepare(
            text,
            voice=self.voice,
            style=self.style
        )

    def infer(self, text):

        prepared = self.preprocess(text)

        return self.model.infer(prepared)