import requests

# 发送POST请求
url = 'https://api3.myships.com/sp/region/latest/shipinfo'
data = {
    "rgn": "17928000,73068000,18126000,73506000",
    "age": 1
}
headers = {
    'User-Agent': 'PostmanRuntime/7.35.0',
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Connection':'keep-alive',
    'appKey':'5a07cc54d8904b6ca69be208c4beeb9c'
}
response = requests.post(url, data=data, headers=headers)

# 检查请求是否成功
if response.status_code == 200:
    # 打印响应内容
    print(response.text)
else:
    print('Failed to post data')