# _*_ coding : UTF-8 _*_
# @Time : 2022/10/10 19:37
# @Author : GYH
# @File : getContent
# @Project : zhiHuHot

# 找规律：
# https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&
# period=hour
# https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&
# limit=20&offset=20&period=hour
# https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&
# limit=20&offset=40&period=hour


import urllib.request
import urllib.parse
import random


def create_request(_page, _flag):
    base_url = 'https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&'
    data1 = {
        'limit': 20,
        'offset': (_page - 1) * 20,
        'period': 'hour'
    }  # get请求
    data2 = {
        'limit': 20,
        'offset': (_page - 1) * 20,
        'period': 'day'
    }
    data3 = {
        'limit': 20,
        'offset': (_page - 1) * 20,
        'period': 'week'
    }
    if _flag == 1:
        data1 = urllib.parse.urlencode(data1)
        if _page == 1:
            url = base_url + 'period=hour'
        else:
            url = base_url + data1
    elif _flag == 2:
        data2 = urllib.parse.urlencode(data2)
        if _page == 1:
            url = base_url + 'period=day'
        else:
            url = base_url + data2
    elif _flag == 3:
        data3 = urllib.parse.urlencode(data3)
        if _page == 1:
            url = base_url + 'period=week'
        else:
            url = base_url + data3

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    _request = urllib.request.Request(url=url, headers=headers)
    return _request


def get_content(_request):
    # 代理池，使用代理池作为随机ip来防止网页封我ip
    # proxies_poll = [
    #     {'http': '58.20.184.187:9091'},
    #     {'http': '39.108.101.55:1080'},
    #     {'http': '223.96.90.216:8085'},
    #     {'http': '121.13.252.58:41564'},
    #     {'http': '61.216.185.88:60808'},
    # ]
    # # 获得代理
    # proxies = random.choice(proxies_poll)
    # # 获得handler对象
    # handler = urllib.request.ProxyHandler(proxies)
    # # 获得opener对象
    # opener = urllib.request.build_opener(handler)
    # # 使用open方法
    #
    # response = opener.open(_request)
    response = urllib.request.urlopen(_request)
    _content = response.read().decode('utf-8')
    return _content


def down_load(_page, _content, _flag):
    if _flag == 1:
        with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\zhiHuHot\\hot_hour\\json\\hot_hour_' + str(_page) + '.json',
                  'w', encoding='utf-8') as fp:
            fp.write(_content)
            fp.close()
    elif _flag == 2:
        with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\zhiHuHot\\hot_day\\json\\hot_day_' + str(_page) + '.json', 'w',
                  encoding='utf-8') as fp:
            fp.write(_content)
            fp.close()
    elif _flag == 3:
        with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\zhiHuHot\\hot_week\\json\\hot_week_' + str(_page) + '.json',
                  'w', encoding='utf-8') as fp:
            fp.write(_content)
            fp.close()


if __name__ == '__main__':
    flag = int(input('请输入热点榜单类型（1表示小时榜；2表示日榜；3表示周榜）：'))
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))
    for page in range(start_page, end_page + 1):
        # 获取请求
        request = create_request(page, flag)
        print('请求获取成功！')
        # 获取响应的内容
        content = get_content(request)
        print('内容获取成功！')
        # 下载
        down_load(page, content, flag)
        print('下载成功！')
