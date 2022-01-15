import requests  ## for request acquiring and processing requests from user
import lxml  ## for conversion of xml files
from bs4 import BeautifulSoup  ## for conversion of text and content from files

url = "https://www.rottentomatoes.com/top/bestofrt/"
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}  ## browser header imformation for avoiding blocking.
f = requests.get(url, headers=headers)
movies_list = []  #array for storing data likewise.
soup = BeautifulSoup(f.content, 'lxml')  #declaration of xml parser.
movies = soup.find('table', {
    'class': 'table'
}).find_all('a')  #find information
num = 0
for anchor in movies:  #extraction of information in consecutive order for realtime analysis.
    urls = 'https://www.rottentomatoes.com' + anchor['href']
    movies_list.append(urls)
    num = num + 1
    movie_url = urls
    movie_f = requests.get(movie_url, headers=headers)
    movie_soup = BeautifulSoup(movie_f, 'lxml')
    movie_content = movie_soup.find(
        'div', {'class': 'movie_synopsis clamp clamp-6 js-clamp'})
print(num, urls, '\n', 'Movie:', +anchor.string.strip())  ##output printing.
print('Movie info:', +movie_content.string.strip())