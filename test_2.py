from core import *

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "Referer": "https://www.bilibili.com/",
    "Cookie": "CURRENT_FNVAL=4048; buvid3=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc; b_nut=1721567317; _uuid=67165DF10-7B77-BDE8-3C63-732C2FCAF4D520375infoc; enable_web_push=DISABLE; buvid4=0245F01B-6C4B-CD5A-2EC5-BC060EC0777D18433-024072113-zRTpkL0r94scQqxGfSYKhQ%3D%3D; home_feed_column=5; header_theme_version=CLOSE; rpdid=|(Y|RJRR)Y~0J'u~kulY~Rkk; DedeUserID=1611307689; DedeUserID__ckMd5=b0865dba0b3ced5b; buvid_fp_plain=undefined; is-2022-channel=1; b_lsid=D8542F24_191412D93C0; bsource=search_bing; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; browser_resolution=1659-943; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM2MzQ1OTMsImlhdCI6MTcyMzM3NTMzMywicGx0IjotMX0.Ox8rnEpQH5i1H_wQfH2z5CzZC0y8PlqQCy1KVa8XEfQ; bili_ticket_expires=1723634533; SESSDATA=f567fef6%2C1738927393%2C5d207%2A82CjAh2pSUKwDLr1XiI6ncU5B6NXEfWKS7ES6mDC8yGxM6aT3-BTdvK0KAlYpMhCXtEXgSVkl2aTlQWUNacTZOZ0ZNXzJwZ21QT2ozMXFXcWtFc1FpNnBIWlNWbml2Y3BxNV80bUNMZTBVN1dyb3h0STU1ZklDM0MwckJvanRmTmNkeTBFcW5qYl9RIIEC; bili_jct=8d788bcb503d69ba2ded7dfbb53f6e58; sid=71po5kkf; fingerprint=0c7279b7c69b9542a76b8d9df9b7872a; buvid_fp=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc; bp_t_offset_1611307689=964382000909647872"
}

# target_url = "https://www.bilibili.com/video/BV1Tq1yYxENk"
# target_url = "https://www.bilibili.com/video/BV1rN411P7i6"
# target_url = "https://www.bilibili.com/video/BV1eH4y1E7xn"
# target_url = "https://www.bilibili.com/video/BV1Tq1yYxENk"
# video_response = requests.get(target_url, headers=head)
# with open("BV_return_合集" + ".html", "w", encoding="utf-8") as f:
#     f.write(video_response.text)
# print("BV_return_合集")
# episode_num = re.findall(, video_response.text)
# target_url = "https://www.bilibili.com/video/BV1jS4y1L7oW"
# video_response = requests.get(target_url, headers=head)
# with open("BV_return_分集" + ".html", "w", encoding="utf-8") as f:
#     f.write(video_response.text)
# print("BV_return_分集")
#
# target_url = "https://www.bilibili.com/video/BV12F411u7my"
# video_response = requests.get(target_url, headers=head)
# with open("BV_return_一般" + ".html", "w", encoding="utf-8") as f:
#     f.write(video_response.text)
# print("BV_return_一般")
#
# target_url = "https://www.bilibili.com/bangumi/play/ss39288"
# video_response = requests.get(target_url, headers=head)
# with open("ss_return" + ".html", "w", encoding="utf-8") as f:
#     f.write(video_response.text)
# print("ss_return")
#
# target_url = "https://www.bilibili.com/bangumi/play/ep90842"
# video_response = requests.get(target_url, headers=head)
# with open("ep_return" + ".html", "w", encoding="utf-8") as f:
#     f.write(video_response.text)
# print("ep_return")
# collection_id_list = re.findall("data-key=\".*?\"", video_response.text)
# collection_title_list = re.findall("<div class=\"simple-base-item normal\"><div title=\".*?\" class=\"title\">",
#                                    video_response.text)
# collection_name = re.findall("spm_id_from=.*?\" title=\".*?\" class=\"title jumpable\"", video_response.text)
# collection_name = re.findall("title=\".*?\"", collection_name[0])
# for i in range(len(collection_id_list)):
#     collection_id_list[i] = collection_id_list[i][10:-1]
# for i in range(len(collection_title_list)):
#     collection_title_list[i] = collection_title_list[i][49:-16]
# collection_name=collection_name[0][7:-1]
# print(collection_title_list)
# print(collection_id_list)
# print(collection_name)
# standard_list = ["BV1c34y137Z9", "BV13u4y1w7Cm", "BV1ss41117Z8", "BV13u4y1w7Cm", "BV1ss41117Z8"]
# standard_list = list(set(standard_list))  # 去重
# standard_list.sort()  # 排序
# print(standard_list)

#
# test = [1, [1], 1]
# test_2 = [1]
# test_2.append(test)
# print(test_2)
# ID_list 目标格式 [[视频id(BVAV与SSEP)/关键词, 选择集数列表[], 总集数，视频标题，视频类型标签(0: 一般视频，1: 番剧电影,2:分集视频，3:合集视频), 模式],...]
# ep90842
# id_list=["ss39288"]
# for id in id_list:
#     target_url = "https://www.bilibili.com/bangumi/play/" +id
#     video_response = requests.get(target_url, headers=head)
#     with open("ss_return" + ".html", "w", encoding="utf-8") as f:
#         f.write(video_response.text)
#     # "title": "【高清修复】东方幻想万华镜全集",
#     episode_num=re.findall("全\d*?话",video_response.text)
#     episode_num= episode_num[0][1:-1]
#     episode_num=eval(episode_num)
#     title = re.findall("<meta property=\"og:title\" content=\".*?\"/>",video_response.text)
#     title = title[0][35:-3]
#     print(title)
# id_list=["ep90842","ss3093","ep80460","ep827835","ss48011"]
# for id in id_list:
#     target_url = "https://www.bilibili.com/bangumi/play/" +id
#     video_response = requests.get(target_url, headers=head)
#     with open("ep_return" + ".html", "w", encoding="utf-8") as f:
#         f.write(video_response.text)
#     # "title": "【高清修复】东方幻想万华镜全集",
#     episode_num=re.findall("全\d*?话",video_response.text)
#     print(episode_num)
#     episode_num= episode_num[0][1:-1]
#     episode_num=eval(episode_num)
#     print(episode_num)
#     title = re.findall("<meta property=\"og:title\" content=\".*?\"/>",video_response.text)
#     title = title[0][35:-3]
#     print(title)
