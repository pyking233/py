from requests_html import HTMLSession
import re
import csv


head =  {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
'Cookie':'TYCID=ac1dfec0298b11e896d65952088acd0e; undefined=ac1dfec0298b11e896d65952088acd0e; ssuid=5431237103; RTYCID=a9b338e6798d4eb39fef9257fd6b9b9d; aliyungf_tc=AQAAAMBzHiKiTwgAqo/Y3f5KVHsxjcZG; csrfToken=oqv83ZlWDQkY1v32arJAja4V; jsid=SEM-BAIDU-PP-SY-000214; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1522481067,1522487432,1522586369,1522586370; bannerFlag=true; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTUzMDQ0OTM4OSIsImlhdCI6MTUyMjU4NjcxMywiZXhwIjoxNTM4MTM4NzEzfQ.lvI-NEDnqyN7eN_V4FFvMnsmf_2S8LvEr79r3xVutqXuIJ1F4VAkQk9DXasWiE9eC2dKGUsBG7ZyHSJpuuq-iw%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252215530449389%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTUzMDQ0OTM4OSIsImlhdCI6MTUyMjU4NjcxMywiZXhwIjoxNTM4MTM4NzEzfQ.lvI-NEDnqyN7eN_V4FFvMnsmf_2S8LvEr79r3xVutqXuIJ1F4VAkQk9DXasWiE9eC2dKGUsBG7ZyHSJpuuq-iw; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1522586767'}
session = HTMLSession()
r = session.get("https://bj.tianyancha.com/normal_company", headers=head)
urls_cate, page_end, url = [], [], []
file = open("company.csv", "w", newline='', encoding='utf-8')
csvwriter = csv.writer(file)
csvwriter.writerow(['企业名称', '统一社会信用代码', '地址', '所属行业', '企业类型', '企业员工规模', '登记状态', '参保人数', '注册地址', '网址'])
if r.status_code == 200:
    html = r.html.html
    urls_cate = re.findall('<a class="item" href="(.*?pany)">', html)
for url_cate in urls_cate:
    r = session.get(url_cate, headers=head)
    if r.status_code == 200:
        html = r.html.html
        page_end = re.search(r'<a class="num -end.*?>\.{3}(\d+)</a>', html, re.S)
    if page_end is None:
        continue
    else:
        for page in range(1, int(page_end.group(1)) + 1):
            url_for_page = url_cate[:30]+"p{}/normal_company".format(page)
            r = session.get(url_for_page, headers=head)
            if r.status_code == 200:
                html = r.html.html
                urls_per_page = re.findall(r'Company"\s+href="(.*?)" target=', html, re.S)
                for url_company in urls_per_page:
                    r = session.get(url_company, headers=head)
                    if r.status_code == 200:
                        html = r.html.html
                        name = re.search('<h1 class="name info-need-copy _title">(.*)?</h1>', html, re.S).group(1)
                        credit_code = re.search('creditcode">(.*?)</span>', html, re.S).group(1)
                        address = re.search('"detail-content element-need-copy">(.*?)&nbsp', html, re.S).group(1)
                        industry = re.search('行业</td><td>(.*?)<', html, re.S).group(1)
                        company_type = re.search('企业类型</td><td>(.*?)<', html, re.S).group(1)
                        staff_size = re.search('人员规模</td><td>(.*?)<', html, re.S).group(1)
                        status = re.search('">经营状态</td><td width.*?>(.*?)</td>', html, re.S).group(1)
                        insured_num = re.search('参保人数</td><td>(.*?)</td>', html, re.S).group(1)
                        reg_address = re.search('zhuceaddr">(.*?)</span>', html, re.S).group(1)
                        csvwriter.writerow([name, credit_code, address, industry, company_type, staff_size, status, insured_num, reg_address, url_company])
file.close()