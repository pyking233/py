import selenium.common.exceptions
from selenium import webdriver
from time import sleep
from random import random
import csv


url_a = "https://www.qcc.com/g_BJ"
driver = webdriver.Edge()  # 使用Edge
driver.get(url_a)
sleep(20)  # 等待登陆
# driver.minimize_window()  #最小化窗口（未测试）
file = open("company.csv", "a", newline='', encoding='utf-8')
csvwriter = csv.writer(file)
# csvwriter.writerow(['企业名称', '统一社会信用代码', '地址', '所属行业', '企业类型', '企业员工规模', '登记状态', '参保人数', '注册地址', '网址'])  # 预备写入csv文件
for area in range(16, 17):  # 区县循环  1=东城区 2=西城区 3=朝阳区 4=丰台区 5=石景山区 6=海淀区 7=门头沟区 8=房山区 9=通州区 10=顺义区 11=昌平区 12=大兴区 13=怀柔区 14=平谷区 15=密云区 16=延庆区
    driver.find_element_by_css_selector(
        "body > div.container.m-t-md > div > div.col-md-9.no-padding > div:nth-child(1) > div:nth-child(2) > div > div.pills-after > a:nth-child({})".format(
            area)).click()
    sleep(1.5)  # 等待加载，下同
    for page in range(500):  # 500页
        for i in range(1, 11):  # 每页10条
            name = credit_code = address = industry = company_type = staff_size = status = insured_num = reg_address = ""
            for retry1 in range(5):
                try:
                    driver.find_element_by_css_selector(
                        "#searchlist > table > tbody > tr:nth-child({}) > td:nth-child(2) > a".format(i)).click()
                    break
                except selenium.common.exceptions.NoSuchElementException:
                    sleep(600)
                    driver.refresh()
            sleep(1.5)
            current_windows = driver.window_handles
            driver.switch_to.window(current_windows[-1])  # 切换至新选项卡
            print("\r" + driver.current_url, end=" ")
            for retry2 in range(3):
                try:
                    driver.find_element_by_partial_link_text("基本信息").click()
                    sleep(1.5)
                    name = driver.find_element_by_css_selector(
                        "#cominfo > div:nth-child(2) > table > tr:nth-child(1) > td:nth-child(4) > div > span.copy-value").text
                    try:
                        credit_code = driver.find_element_by_css_selector(
                            "#cominfo > div:nth-child(2) > table > tr:nth-child(4) > td:nth-child(6) > div > span.copy-value").text
                    except selenium.common.exceptions.NoSuchElementException:
                        pass
                    try:
                        address = driver.find_element_by_css_selector(
                            "body > div:nth-child(2) > div.company-detail > div.company-header > div > div.nheader > div.infos.clearfix > div.content > div.contact-info > div:nth-child(3) > span.f.head—dz > div > span.val > a.texta > span").text
                    except selenium.common.exceptions.NoSuchElementException:
                        pass
                    try:
                        industry = driver.find_element_by_css_selector(
                            "#cominfo > div:nth-child(2) > table > tr:nth-child(6) > td:nth-child(2)").text
                    except selenium.common.exceptions.NoSuchElementException:
                        pass
                    try:
                        company_type = driver.find_element_by_css_selector(
                            "#cominfo > div:nth-child(2) > table > tr:nth-child(5) > td:nth-child(2)").text
                    except selenium.common.exceptions.NoSuchElementException:
                        pass
                    try:
                        staff_size = driver.find_element_by_css_selector(
                            "#cominfo > div:nth-child(2) > table > tr:nth-child(7) > td:nth-child(2)").text
                    except selenium.common.exceptions.NoSuchElementException:
                        pass
                    try:
                        status = driver.find_element_by_css_selector(
                            "#cominfo > div:nth-child(2) > table > tr:nth-child(2) > td:nth-child(4)").text
                    except selenium.common.exceptions.NoSuchElementException:
                        pass
                    try:
                        insured_num = driver.find_element_by_css_selector(
                            "#cominfo > div:nth-child(2) > table > tr:nth-child(7) > td:nth-child(4) > span").text
                    except selenium.common.exceptions.NoSuchElementException:
                        pass
                    try:
                        reg_address = driver.find_element_by_css_selector(
                            "#cominfo > div:nth-child(2) > table > tr:nth-child(9) > td:nth-child(2) > div > span:nth-child(1) > a.text-dk.copy-value").text
                    except selenium.common.exceptions.NoSuchElementException:
                        pass
                    break
                except selenium.common.exceptions.NoSuchElementException:
                    sleep(300)
                    driver.refresh()
            csvwriter.writerow(
                [name, credit_code, address, industry, company_type, staff_size, status, insured_num, reg_address,
                 driver.current_url])
            driver.close()
            driver.switch_to.window(current_windows[0])  # 切换回原选项卡
            sleep(random() * 1.5)
        driver.find_element_by_class_name("next").click()  # 翻页
        sleep(1.5)
file.close()
