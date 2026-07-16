from .processor_registry import register

from .processors.number_processor import process as number_processor
from .processors.english_processor import process as english_processor
from .processors.tamil_processor import process as tamil_processor
from .processors.other_processor import process as other_processor


register("NUMBER", number_processor)
register("ENGLISH", english_processor)
register("TEXT", tamil_processor)
register("OTHER", other_processor)