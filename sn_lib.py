import time
import requests
import re


class SNLib:
    def __init__(self):
        self.anime_data = []
        self.local_data_dic = {}
        self.anime_web_dic = {}
        return

    def crawl_sn_web(self):
        url = "https://sn-video.com/data/ajax/function/ajax_mainPage.php"
        data = {
            'index': 'true'
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
        }
        response = requests.post(url, data=data, headers=headers)
        if response.status_code != 200:
            print("連線失敗...")
            return False

        subject = re.findall(r'"subject":".*?"',
                             response.content.decode('unicode-escape'))

        for i in range(0, len(subject)):
            subject[i] = subject[i].strip('"subject":').strip('"')
            title = ""
            ep = ""
            flag = 0
            for j in range(0, len(subject[i])):
                if(subject[i][j] != '【' and flag == 0):
                    title += str(subject[i][j])
                else:
                    flag = 1

                if flag == 1:
                    ep += str(subject[i][j])
            title = title.strip()
            ep = ep.strip()
            self.anime_web_dic[title] = ep
        if len(self.anime_web_dic) == 0:
            print("沒有資料")
            return False
        else:
            return True

    def read_anime(self):
        with open('./anime_list.txt', 'r', encoding="utf-8") as f:
            while True:
                line = f.readline()
                if line:
                    s = line.split('\t')
                    self.local_data_dic[s[0]] = [s[1], s[2].strip()]
                else:
                    break
        f.close()
        return

    def write_anime(self, anime, episode, date):
        file = open('./anime_list.txt', 'a', encoding="utf-8")
        file.write(anime+"\t"+episode+"\t"+date+"\n")
        file.close()

    def collect_anime(self):
        # print(self.anime_web_dic)
        date = self.get_current_time()
        anime_name = str(input("請輸入動漫名稱: "))
        if self.anime_web_dic.get(anime_name) == None:
            print("動漫: " + anime_name + " 找不到")
        else:
            print(anime_name, self.anime_web_dic[anime_name])
            if (self.local_data_dic.get(anime_name) == None):
                self.write_anime(
                    anime_name, self.anime_web_dic[anime_name], date)
                print("寫入 "+anime_name+" 至本地")
            else:
                print("已收藏此動漫")

    def get_current_time(self):
        localtime = time.localtime()
        result = time.strftime("%Y-%m-%d", localtime)
        return result

    def print_update_anime_web(self):
        print(self.anime_web_dic)

    def print_local_anime(self):
        for a in self.local_data_dic:
            print(a+" "+self.local_data_dic[a]
                  [0]+" "+self.local_data_dic[a][1])

    def check_anime_update(self):
        is_update = False
        for a in self.local_data_dic:
            if(self.anime_web_dic.get(a)):
                if(self.anime_web_dic[a] != self.local_data_dic[a][0]):
                    print(a + " " + self.anime_web_dic[a])
                    self.local_data_dic[a][0] = self.anime_web_dic[a]
                    self.local_data_dic[a][1] = self.get_current_time()
                    is_update = True
        return is_update

    def write_anime_update(self):
        file = open('./anime_list.txt', 'w', encoding="utf-8")
        for a in self.local_data_dic:
            file.write(
                a+"\t"+self.local_data_dic[a][0]+"\t"+self.local_data_dic[a][1])
        file.write("\n")
        file.close()
