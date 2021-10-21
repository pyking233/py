from requests_html import HTMLSession
from time import sleep
from fake_useragent import UserAgent
import csv

session = HTMLSession()

file = open("movies.csv", "w", newline='', encoding='utf-8')
csvwriter = csv.writer(file)
csvwriter.writerow(['名称', '上映日期'])
for i in range(0, 99, 10):
    if i == 40:
        sleep(60)
    url = "https://maoyan.com/board/4?offset={}".format(i)
    headers = {'User-Agent': str(UserAgent().random)}
    r = session.get(url=url, headers=headers)
    if r.status_code == 200:
        for j in range(1, 11):
            css1 = "#app > div > div > div.main > dl > dd:nth-child({}) > div > div > div.movie-item-info > p.name > a".format(j)
            css2 = "#app > div > div > div.main > dl > dd:nth-child({}) > div > div > div.movie-item-info > p.releasetime".format(j)
            name = r.html.find(css1, first=True)
            date = r.html.find(css2, first=True)
            csvwriter.writerow([name.element.text, date.element.text[5:15]])
    else:
        print("ERROR", r.status_code)
        break
file.close()
# from requests_html import HTMLSession
# from time import sleep
# from fake_useragent import UserAgent
#
#
# session = HTMLSession()
#
# file = open("movies.csv", "w", newline='', encoding='utf-8')
# for i in range(0, 250, 25):
#     url = "https://movie.douban.com/top250?start={}&filter=".format(i)
#     headers = {'User-Agent': str(UserAgent().random)}
#     r = session.get(url=url, headers=headers)
#     if r.status_code == 200:
#         for j in range(1, 26):
#             css1 = "#content > div > div.article > ol > li:nth-child({0}) > div > div.info > div.hd > a > span:nth-child({0})".format(j)
#             name = r.html.find(css1, first=True)
#             file.write(name.element.text)
#
#     else:
#         print("ERROR", r.status_code)
#         break
# file.close()
