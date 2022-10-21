# _*_ coding : UTF-8 _*_
# @Time : 2022/10/15 12:34
# @Author : GYH
# @File : contentAnalysis
# @Project : zhiHuHot
import json
import jsonpath
# 'E:python_learning/Internet_worm_learning/zhiHuHot/hot_hour/' + para[0] + str(para[1]) + '.json'

def get_data(*para):
    res_list = []
    # print('A')
    for i in range(1, para[1] + 1):
        # print(i)
        obj = '?'
        if para[0] == 'hot_hour_':
            obj = json.load(open('E:\\python_learning\\Internet_worm_learning\\reexamine\\zhiHuHot\\hot_hour\\json\\' + para[0] + str(i) + '.json', 'r', encoding='utf-8'))
        elif para[0] == 'hot_day_':
            obj = json.load(open('E:\\python_learning\\Internet_worm_learning\\reexamine\\zhiHuHot\\hot_day\\json\\' + para[0] + str(i) + '.json', 'r', encoding='utf-8'))
        elif para[0] == 'hot_week_':
            obj = json.load(open('E:\\python_learning\\Internet_worm_learning\\reexamine\\zhiHuHot\\hot_week\\json\\' + para[0] + str(i) + '.json', 'r', encoding='utf-8'))
        base_topic_list = jsonpath.jsonpath(obj, '$.data[*].question.topics')
        # print(len(base_topic_list[0]))
        # j = 0
        # topic_list = []
        # while j < len(base_topic_list) - 2:
        #     topic_list.append(base_topic_list[j] + ', ' + base_topic_list[j+1] + ', ' + base_topic_list[j+2])
        #     j = j + 3
        # print(len(topic_list))
        j = 0
        topic_list = []
        while j < len(base_topic_list):
            tmp = ''
            t = 0
            while t < len(base_topic_list[j]):
                if t == len(base_topic_list[j]) - 1:
                    tmp = tmp + base_topic_list[j][t]['name']
                else:
                    tmp = tmp + base_topic_list[j][t]['name'] + ','
                t = t + 1
            topic_list.append(tmp)
            j = j + 1

        title_list = jsonpath.jsonpath(obj, '$.data[*].question.title')
        # print(len(title_list))
        url_list = jsonpath.jsonpath(obj, '$.data[*].question.url')
        # print(url_list)
        score_list = jsonpath.jsonpath(obj, '$.data[*].reaction.score')
        # print(score_list)
        new_follow_num_list = jsonpath.jsonpath(obj, '$.data[*].reaction.new_follow_num')
        # print(type(hot))
        new_answer_num_list = jsonpath.jsonpath(obj, '$.data[*].reaction.new_answer_num')
        new_upvote_num_list = jsonpath.jsonpath(obj, '$.data[*].reaction.new_upvote_num')
        for k in range(0, len(title_list)):
            # print(k)
            hot = {}
            hot['topics'] = topic_list[k]
            # print(hot['topics'])
            hot['title'] = title_list[k]
            # print(hot['title'])
            hot['url'] = url_list[k]
            # print(hot['url'])
            hot['score'] = score_list[k]
            # print(hot['score'])
            hot['new_follow_num'] = new_follow_num_list[k]
            hot['new_answer_num'] = new_answer_num_list[k]
            hot['new_upvote_num'] = new_upvote_num_list[k]
            if para[0] == 'hot_hour_':
                # print(hot)
                res_list.append(hot)
                # print(hour_list)
            elif para[0] == 'hot_day_':
                res_list.append(hot)
            elif para[0] == 'hot_week_':
                res_list.append(hot)
    # print(res_list)
    return res_list


def down_load(_list, _datalist):
    _data = json.dumps(_datalist, ensure_ascii=False)
    # print(_data)
    if _list == 'hot_hour_':
        with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\zhiHuHot\\hot_hour\\list\\' + _list + 'list' + '.json', 'w',encoding='utf-8') as fp:
            fp.write(_data)
            fp.close()
    elif _list == 'hot_day_':
        with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\zhiHuHot\\hot_day\\list\\' + _list + 'list' + '.json', 'w', encoding='utf-8') as fp:
            fp.write(_data)
            fp.close()
    elif _list == 'hot_week_':
        with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\zhiHuHot\\hot_week\\list\\' + _list + 'list' + '.json', 'w', encoding='utf-8') as fp:
            fp.write(_data)
            fp.close()


if __name__ == '__main__':
    flag = int(input('请输入榜单类型（1为小时榜，2为日榜，3为周榜）：'))
    page = int(input('请输入页码数： '))
    List = '?'
    if flag == 1:
        List = 'hot_hour_'
    elif flag == 2:
        List = 'hot_day_'
    elif flag == 3:
        List = 'hot_week_'
    # 获取想要的数据
    data_list = get_data(List, page)
    print('数据获取成功！')
    # print('A')
    # print(data)
    # 下载数据
    down_load(List, data_list)
    print('下载成功！')
