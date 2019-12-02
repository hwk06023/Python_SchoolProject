import io
import re

def read_data(path):
    with io.open(path, encoding='cp949') as f:
        text = f.read().lower()

    text = re.sub(r'<.*>', '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r' +', ' ', text)

    return text

def summarize(text):
    chars = sorted(list(set(text)))
    char_indices = dict((c, i) for i, c in enumerate(chars))
    indices_char = dict((i, c) for i, c in enumerate(chars))

    return chars, char_indices, indices_char