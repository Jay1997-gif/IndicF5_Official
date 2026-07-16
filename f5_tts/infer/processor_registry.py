PROCESSORS = {}


def register(name, processor):

    PROCESSORS[name] = processor


def get(name):

    return PROCESSORS.get(name)


def all_processors():

    return PROCESSORS