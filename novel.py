from keras.callbacks import LambdaCallback
from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np

import random
import sys
import io
import re

def novel_data(path):
    with io.open(path, encoding='utf-8') as f:
        text = f.read().lower()

    text = re.sub(r'<.*>', '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r' +', ' ', text)

    print('corpus length:', len(text))