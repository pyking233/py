from requests_html import HTMLSession
import csv
import re


def main(offset):
    url = "https://maoyan.com/board/4?offset=" + str(offset)
    r = session.get(url=url, headers=MaoYanHeaders)
    if r.status_code == 200:
        for j in range(1, 11):
            css1 = "#app > div > div > div.main > dl > dd:nth-child({}) > div > div > div.movie-item-info > p.name > a".format(
                j)
            css2 = "#app > div > div > div.main > dl > dd:nth-child({}) > div > div > div.movie-item-info > p.releasetime".format(
                j)
            name = r.html.find(css1, first=True)
            dateinfo = r.html.find(css2, first=True)
            date = re.search("[-0-9]+", dateinfo.element.text)
            csvwriter.writerow([name.element.text, date.group()])
    else:
        print("ERROR", r.status_code)


session = HTMLSession()

MaoYanHeaders = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "uuid=1A6E888B4A4B29B16FBA1299108DBE9CDFE0F270F2640051092C5B91D4925C7A; _lx_utm=utm_source%3Dbaidu%26utm_medium%3Dorganic; __mta=219052582.1507114997794.1507115797315.1507118482776.11; _lxsdk_s=af27c2388b4347ab08f2353fe7c8%7C%7C4",
    "Host": "maoyan.com",
    "Referer": "http://maoyan.com/board/4?offset=90/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}
file = open("movies.csv", "w", newline='', encoding='utf-8')
csvwriter = csv.writer(file)
csvwriter.writerow(['名称', '上映日期'])
for i in range(10):
    main(i*10)
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
