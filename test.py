# # 测试用例程
import requests

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "Referer": "https://www.bilibili.com/",
    "Cookie": ""
}
id = 'ep693249'
target_url = "https://www.bilibili.com/bangumi/play/" + id
response = requests.get(target_url, headers=head)
with open('ep_return.html', 'w') as f:
    f.write(response.text)
    f.close()
id = "ss33802"
target_url = "https://www.bilibili.com/bangumi/play/" + id
response = requests.get(target_url, headers=head)
with open('ss_return.html', 'w') as f:
    f.write(response.text)
    f.close()
# ->BV
target_url = "https://www.bilibili.com/video/BV1mt4y1Q74Q/"
response = requests.get(target_url, headers=head)
with open('ss_to_BV_return.html', 'w') as f:
    f.write(response.text)
    f.close()
# ->md
target_url = "https://www.bilibili.com/bangumi/media/md28229233"
response = requests.get(target_url, headers=head)
with open('ss_to_md_return.html', 'w') as f:
    f.write(response.text)
    f.close()
