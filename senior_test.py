# _*_ coding=utf-8 _*_


import requests

# 文件上传
# files = {'file': open('favicon.ico', 'rb')}
# res = requests.post('http://httpbin.org/post', files=files)
# print(res.text)

# 获取Cookies
# res = requests.get('http://www.baidu.com')
# print(res.cookies)
# for k, v in res.cookies.items():
#     print(k + ":" + v)

# 设置cookie，发送请求
headers = {
    'Cookie': 'BIDUPSID=EDBD62A1D608B5CDC72B06CA0C59680A; PSTM=1546959880; BDUSS=BCSHh3OVMtTW5XUnB6SEF4UFExUFhPRUc5Ty1sV'
              'FRkRERvRWZ3bE9sWlN2Y0ZjQVFBQUFBJCQAAAAAAAAAAAEAAABW7900TGltaXTSwcrW1drM7AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
              'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFIwmlxSMJpcV3; MCITY=-340%3A; BAIDUID=5C140375092D783C088CEA7282B89772'
              ':FG=1; delPer=0; PSINO=5; BDRCVFR[bLbo9QmdyQn]=aeXf-1x8UdYcs; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; '
              'H_PS_PSSID=1427_21108_29064_28519_29099_28831_28585_22157; PHPSESSID=63vpocfpukn41u0h1nolsluq95; '
              'Hm_lvt_4010fd5075fcfe46a16ec4cb65e02f04=1558949858; Hm_lpvt_4010fd5075fcfe46a16ec4cb65e02f04=1558949858',
    'Host':'i.baidu.com'
}
res = requests.get('http://i.baidu.com/', headers=headers)
print(res.text)