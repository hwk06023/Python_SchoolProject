from read_novel import read_data, summarize
from novel_train import vectorize

from keras.callbacks import LambdaCallback
from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file

import numpy as np
import random
import sys

novel_1 = './data/Novel_1.txt'
novel_2 = './data/Novel_2.txt'
novel_3 = './data/Novel_3.txt'

# 소설 데이터를 읽어와 정규식을 통해 소설의 내용을 정제하여 가져옵니다.
text = read_data(novel_2)

chars, char_indices, indices_char = summarize(text)

x, y, sentences = vectorize(char_indices, text, chars)

print('Build model...')
model = Sequential()
model.add(LSTM(1024, input_shape=(40, len(chars))))
model.add(Dense(len(chars), activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer=RMSprop(lr=0.001))

def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


def on_epoch_end(epoch, _):
    print('\n----- Generating text after Epoch: %d' % epoch)

    start_index = random.randint(0, len(text) - 40 - 1)
#     for diversity in [0.2, 0.5, 1.0, 1.2]:
#         print('----- diversity:', diversity)

    generated = ''
    sentence = text[start_index: start_index + 40]
    generated += sentence
    print('----- Generating with seed: "' + sentence + '"')
    sys.stdout.write(generated)

    for i in range(400):
        x_pred = np.zeros((1, 40, len(chars)))
        for t, char in enumerate(sentence):
            x_pred[0, t, char_indices[char]] = 1.

        preds = model.predict(x_pred, verbose=0)[0]
        next_index = sample(preds, 0.5)
        next_char = indices_char[next_index]

        generated += next_char
        sentence = sentence[1:] + next_char

        sys.stdout.write(next_char)
        sys.stdout.flush()
    print()

print_callback = LambdaCallback(on_epoch_end=on_epoch_end)

model.fit(x, y, batch_size=128, epochs=60, callbacks=[print_callback])
