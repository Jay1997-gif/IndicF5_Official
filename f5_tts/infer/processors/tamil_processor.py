from ..processor_registry import register

def process(token):
    return token

register("TEXT", process)