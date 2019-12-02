from crawler import crawler
from word_clouding import wordclouding

# url을 수정할 때 crawler.py에서 수동으로 div class 또는 id를 바꾸십쇼
url = 'http://www.dbhs.co.kr/zbxe/index.php?mid=a27&document_srl=243457'
crawl_data = crawler(url)
print('데이터 수집 완료')

wordclouding(crawl_data)