import requests
import re


class Lib:
    def __init__(self):
        url = "https://sn-video.com/data/ajax/function/ajax_mainPage.php"
        data = {
            'index': 'true'
        }
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        }
        self.response = requests.post(
            url, data=data, headers=headers).content.decode('unicode-escape')

    def get_online_update_anime():
        print("hello")
        # info = re.findall(r'"subject":".*?"', self.response)
        # dic = {}
        # for i in range(0, len(info)):
        #     info[i] = info[i].strip('"subject":"').strip('"')
        #     x = info[i].split('【', 1)
        #     x[1] = x[1].strip('】')

        #     dic[x[0]] = x[1]
        # print(dic)
        # return dic


lib = Lib()
lib.get_online_update_anime()


# info = re.findall(r'"subject":".*?"', response.content.decode('unicode-escape'))
# dic = {}
# for i in range(0, len(info)):
#     info[i] = info[i].strip('"subject":"').strip('"')
#     x = info[i].split('【', 1)
#     x[1] = x[1].strip('】')

#     dic[x[0]] = x[1]
# print(dic)


# subject = open('name.txt', 'w')
# subject.write(u"平凡職業造就世界最強 第二季")
# subject.close()
# with open('name.txt') as f:
#     contents = f.read()
#     print(contents)
#     print(dic.get(contents))
