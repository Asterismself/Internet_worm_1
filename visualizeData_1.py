# _*_ coding : UTF-8 _*_
# @Time : 2022/10/18 21:59
# @Author : GYH
# @File : visualizeData
# @Project :
#
# import pandas
# import numpy
# import matplotlib.pyplot
# import seaborn
# # %matplotlib inline
# matplotlib.pyplot.style.use('fivethirtyeight')
# seaborn.set_style({'font.sans-serif': ['Simhei', 'Arial']})
# original = pandas.read_csv('E:\\python_learning\\Internet_worm_learning\\zhiHuHot\\hot_hour\\csv\\zhihu_data_hour_datalist.csv')
# original.info()
import matplotlib.pyplot as plt
from pylab import mpl
import numpy as np
import json
# 获取数据
flag = int(input('请输入想要分析的榜单(1表示小时榜，2表示日榜，3表示周榜)：'))
if flag == 1:
    with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\zhiHuHot\\hot_hour\\list\\hot_hour_list.json', 'r', encoding='utf-8') as fp:
        content = fp.read()
        fp.close()
        data = json.loads(content)
elif flag == 2:
    with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\zhiHuHot\\hot_day\\list\\hot_day_list.json', 'r', encoding='utf-8') as fp:
        content = fp.read()
        fp.close()
        data = json.loads(content)
elif flag == 3:
    with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\zhiHuHot\\hot_week\\list\\hot_week_list.json', 'r', encoding='utf-8') as fp:
        content = fp.read()
        fp.close()
        data = json.loads(content)
# rint(data)
# 统计数据
labels = ['法律', '社会', '游戏', '国际', '大学', '互联网', '军事']
data_num = []
dataSum = 0
for i in range(0, len(labels)):
    num = 0
    for j in range(0, len(data)):
        if data[j]['topics'].find(labels[i], 0, len(data) - 1) != -1:
            # print(data[i]['topics'])
            num = num + 1
    data_num.append(num)
    dataSum = dataSum + num
# print(dataSum)
# print(data_num)
for k in range(0, len(data_num)):
    data_num[k] = data_num[k]/dataSum*100
# print(data_num)
# 数据可视化
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
plt.pie(data_num, labels=labels, autopct='%1.3f%%', shadow=True)  # labels :(每一块)饼图外侧显示的说明文字
plt.axis('equal')  # 该行代码使饼图长宽相等
plt.legend()  # 添加图例
plt.show()
