from .sentence_splitter import split_sentences
from .tokenizer import tokenize
from .context_processor import process_token
from .rebuilder import rebuild


def process_document(text):

    final = []

    sentences = split_sentences(text)

    for sentence in sentences:

        tokens = tokenize(sentence)

        processed = []

        for token in tokens:
            processed.append(process_token(token))

        final.append(rebuild(processed))

    return final