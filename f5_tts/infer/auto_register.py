import pkgutil
import importlib

from . import processors


def auto_register():

    for _, module_name, _ in pkgutil.iter_modules(processors.__path__):

        importlib.import_module(
            f"f5_tts.infer.processors.{module_name}"
        )