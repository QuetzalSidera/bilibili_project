# 测试用例程

import requests
import re
from video import *
import jieba

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "Referer": "https://www.bilibili.com/",
    "Cookie": "CURRENT_FNVAL=4048; buvid3=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc; b_nut=1721567317; _uuid=67165DF10-7B77-BDE8-3C63-732C2FCAF4D520375infoc; enable_web_push=DISABLE; buvid4=0245F01B-6C4B-CD5A-2EC5-BC060EC0777D18433-024072113-zRTpkL0r94scQqxGfSYKhQ%3D%3D; home_feed_column=5; header_theme_version=CLOSE; rpdid=|(Y|RJRR)Y~0J'u~kulY~Rkk; DedeUserID=1611307689; DedeUserID__ckMd5=b0865dba0b3ced5b; buvid_fp_plain=undefined; is-2022-channel=1; b_lsid=D8542F24_191412D93C0; bsource=search_bing; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; browser_resolution=1659-943; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM2MzQ1OTMsImlhdCI6MTcyMzM3NTMzMywicGx0IjotMX0.Ox8rnEpQH5i1H_wQfH2z5CzZC0y8PlqQCy1KVa8XEfQ; bili_ticket_expires=1723634533; SESSDATA=f567fef6%2C1738927393%2C5d207%2A82CjAh2pSUKwDLr1XiI6ncU5B6NXEfWKS7ES6mDC8yGxM6aT3-BTdvK0KAlYpMhCXtEXgSVkl2aTlQWUNacTZOZ0ZNXzJwZ21QT2ozMXFXcWtFc1FpNnBIWlNWbml2Y3BxNV80bUNMZTBVN1dyb3h0STU1ZklDM0MwckJvanRmTmNkeTBFcW5qYl9RIIEC; bili_jct=8d788bcb503d69ba2ded7dfbb53f6e58; sid=71po5kkf; fingerprint=0c7279b7c69b9542a76b8d9df9b7872a; buvid_fp=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc; bp_t_offset_1611307689=964382000909647872"
}

target_url = "https://www.bilibili.com/anime/"
response = requests.get(target_url, headers=head)
result = "".join(re.findall(r'[\u4e00-\u9fa5]', response.text))
result = result[150:]
keyword_list = jieba.lcut(result)
print(keyword_list)
print(result)

# # with open('result.html','w') as f:
# #     f.write(response.text)

for keyword in keyword_list[6:]:
    keywords_to_selected_list(keyword, "bilibili", 0, -1)
#
#

# test="gggggg<ggGGGg>ggg<ggggG>GggG>GGGGGGGGGgg"
# text=re.findall("<.*?>",test)
# print(text)
def debug(info_list):
    display_title_list = []
    for info in info_list:
        display_title_list.append(info[1])
    print(len(display_title_list))
    in_law_index_list = list(range(1, len(display_title_list) + 1))
    for i in range(1, len(in_law_index_list) + 1):
        in_law_index_list[i - 1] = str(in_law_index_list[i - 1])

    print("关键词检索，交互模式，" + "目前展示所有检索结果，共" + str(
        len(display_title_list)) + "个视频,以下是可供选择的项目:")
    for i in range(1, len(display_title_list) + 1):
        # info_list格式 [[ID号,标题，集数，这是第..集，视频类型标签],[ID号,标题，集数，这是第..集，视频类型标签],[ID号,标题，集数，这是第..集，视频类型标签].....]
        # 视频类型标签(0:一般视频，1:番剧电影，2：分集视频，3:合集视频)
        info_index = i - 1
        title = info_list[info_index][1]
        episode_num = info_list[info_index][2]
        now_episode_index = info_list[info_index][3]
        video_type = info_list[info_index][-1]
        if video_type == 0:
            type_tag = "(一般视频)"
            episode_tag = ""
        elif video_type == 1:
            type_tag = "(番剧电影)"
            episode_tag = "(全" + str(episode_num) + "话)"
        elif video_type == 2:
            type_tag = "(分集视频)"
            episode_tag = "(全" + str(episode_num) + "话)"
        elif video_type == 3:
            type_tag = "(合集视频)"
            episode_tag = "(第" + str(now_episode_index) + "集/全" + str(episode_num) + "集)"
        else:
            type_tag = "(unknown)"
            episode_tag = "(unknown)"
        print("\t" + str(i) + "." + type_tag + episode_tag + title)
    print("")
