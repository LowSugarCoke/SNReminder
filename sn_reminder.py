import requests
import time
import os
import re

localtime = time.localtime()
result = time.strftime("%Y-%m-%d", localtime)
print(result)

file = open('./data.txt', 'a')
file.write("\nhello")
file.close()


# url = "https://sn-video.com/data/ajax/function/ajax_mainPage.php"

# data = {
#     'index': 'true'
# }

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
# }

# response = requests.post(url, data=data, headers=headers)
# response.encoding = 'big5'
# # print(response.content.decode('unicode-escape'))

# subject = re.findall(r'"subject":".*?"',
#                      response.content.decode('unicode-escape'))
# # print(subject)

# for i in range(0, len(subject)):
#     subject[i] = subject[i].strip('"subject":').strip('"')
#     # print(subject[i])
#     title = ""
#     ep = ""
#     flag = 0
#     for j in range(0, len(subject[i])):
#         if(subject[i][j] != '【' and flag == 0):
#             title += str(subject[i][j])
#         else:
#             flag = 1

#         if flag == 1:
#             ep += str(subject[i][j])

#     print(title)
#     print(ep)
