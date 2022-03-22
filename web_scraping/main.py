import requests
import bs4

HEADERS = {
'Cookie': '_ym_uid=1609341547512822598; _ga=GA1.2.669337776.1609341548; hl=ru; fl=ru; _ym_d=1640877494; feature_streaming_comments=true; __gads=ID=ce239cf2d7a1ffa1:T=1645133340:S=ALNI_MYQ9qMU-QwW_ySNE4FHeYRDraZlFg; visited_articles=456214:247373:531472:541256:193136:556942:483400:241223:196382:480022; habr_web_home_feed=/all/; _ym_isad=2; _gid=GA1.2.2027820782.1647891589; cto_bundle=yKnYbF8xWEk2R0hKQXNQRmZadXRzNmpkR1hVZGRQYlNNaG1HZ2RWRmJsWE9UYjJSbGNqWWNnZ0xNWDg4bjNDT1RHZnR5cXRPaDIwYlNEYmQwbUl2RVNMamhEM3V3dmVuNDBnayUyQjlaSlNkTWFVU0d0cXp6bkd2N1dEZWRFRVdmTmRNWDJs',
'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Cache-Control': 'no-cache',
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36',
'sec-ch-ua-mobile': '?1'
}

url = "https://habr.com/ru/all/"

HUBS = ['Машинное обучение', 'Data Engineering', 'Химия', 'программирование', 'программирования', 'GitHub']

response = requests.get(url, headers=HEADERS)
response.raise_for_status()
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
article = soup.find(class_="tm-article-snippet")
one_text = soup.select('.tm-article-body .article-formatted-body')
print(one_text)
print('')