from konlpy.tag import Twitter
import nltk
from nltk import FreqDist
from nltk.tokenize import word_tokenize

from wordcloud import WordCloud

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def wordclouding(text):
    twitter = Twitter()
    tokens = twitter.pos(text, stem=True)
    
    tokens_noun = []
    for token in tokens:
        if token[1] == "Noun":
            tokens_noun.append(token[0])

    texts_noun  = " ".join(tokens_noun)

    tokens  = word_tokenize(texts_noun)
    freqtxt = pd.Series(dict(FreqDist(tokens))).sort_values(ascending=False)
    
    mask = np.array(Image.open("./image/icon.png"))

    wcloud = WordCloud(
        font_path='/Library/Fonts/NanumSquareRegular.ttf',
        mask=mask,
        width = 500,
        height = 500,
        background_color='white'
    )
    wcloud = wcloud.generate_from_frequencies(freqtxt)

    fig = plt.figure(figsize=(10, 10))
    plt.imshow(wcloud, interpolation="bilinear")
    plt.show()
    fig.savefig('./image/wordcloud_without_axisoff.png')