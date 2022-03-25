import requests
import bs4

HEADERS = {
    'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.2.528119004.1639149415; _gid=GA1.2.512914915.1639149415; habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru; _ym_isad=2; __gads=ID=87f529752d2e0de1-221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
    'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'sec-ch-ua-mobile': '?0'}

url = "https://habr.com/ru/all"
base_url = "https://habr.com"

KEYWORDS = ['Программирование', 'программирования', 'Машинное обучение', 'Системное администрирование', 'Python',
            'Здоровье', 'DevOps', 'Docker']

response = requests.get(url, headers=HEADERS)
response.raise_for_status()
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all(class_="tm-articles-list__item")
list_found_articles = list()
updated_info = ''
for item in articles:
    inner_text = item.text
    date_published = item.find(class_="tm-article-snippet__datetime-published").text
    title_for_article = item.find(class_="tm-article-snippet__title-link").text
    article_link = base_url + item.find(class_="tm-article-snippet__title-link").attrs['href']
    uniq_value = set(inner_text.split())
    for keyword in KEYWORDS:
        if keyword in uniq_value:
            full_info_about_articles = "{}, {}, {}".format(date_published, title_for_article, article_link)
            list_found_articles.append(full_info_about_articles)
            for item in list_found_articles:
                updated_info = '\n'.join(list_found_articles)
        else:
            continue
print(updated_info)
if not updated_info:
  print("Статьи по данным ключевым словам не найдены")


