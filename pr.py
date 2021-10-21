# a, b = input("数字a:"), input("数字b:")
# print("a^2+b^2=" + str(eval(a) ** 2 + pow(eval(b), 2)))
# str01 = ["北京", "上海", "广州", "深圳", "成都", "郑州", "曹县"]
# print(str01)
# str01.insert(2, "南京")
# print(str01)
# str01[2] = "石家庄"
# print(str01)
# str01[2] = str01[2][::-1]
# print(str01)
# a = []
# for i in range(5, 10):
#     a.append(i)
# print(a)
# print(sum(a))
# print(a.sort(reverse=True))
# print([n for n in a if n > 6])
# 我 = a[3]
# print(我)
# import main
# import time
# time_be=time.time()
# a = sum(i ** 2 for i in range(1000001) if i % 2 == 0)
# print(a)
# time_be=time.time()-time_be
# print(time_be)
# main.fun01()
# dict55 = {'Google': 'www.google.com', 'baidu': 'www.baidu.com', 'taobao': 'www.taobao.com'}
# print("字典值 :%s " % dict55.items())
# for key, value in dict55.items():
#     print(key, value)
# j = 0
# for i in range(100):
#     for a in str(i):
#         if a == "6":
#             j += 1
# print(j)
# gen51 = (2*x + 1 for x in range(10))
# print(type(gen51))
# while True:
#     try:
#         print(next(gen51), end=" ")
#     except StopIteration:
#         break
# def sum_in(*lis):
#     if len(lis) > 4:
#         lis = lis[:4]
#     return lis


di = {"k1": "ok!", "k2": [1, 2, 3, 4], "k3": [10, 20]}


def cut(dic):
    for key, value in dic.items():
        if len(value) > 2:
            dic[key] = value[:2]
    return dic


print(cut(di))
