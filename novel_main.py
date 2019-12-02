from read_novel import read_data, summarize
from novel_train import vectorize

novel_1 = './data/Novel_1.txt'
novel_2 = './data/Novel_2.txt'
novel_3 = './data/Novel_3.txt'

# 소설 데이터를 읽어와 정규식을 통해 소설의 내용을 정제하여 가져옵니다.
text = read_data(novel_2)

chars, char_indices, indices_char = summarize(text)

vectorize(char_indices, text, chars)

