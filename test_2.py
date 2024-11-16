# # 测试用例程
import requests
from json import JSONDecodeError
from lxml import etree
import json
from bs4 import BeautifulSoup
import re
from bilibili_lib import *
from user_config import video_config

#
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "Referer": "https://www.bilibili.com/",
    "Cookie": "CURRENT_FNVAL=4048; buvid3=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc; b_nut=1721567317; _uuid=67165DF10-7B77-BDE8-3C63-732C2FCAF4D520375infoc; enable_web_push=DISABLE; buvid4=0245F01B-6C4B-CD5A-2EC5-BC060EC0777D18433-024072113-zRTpkL0r94scQqxGfSYKhQ%3D%3D; home_feed_column=5; header_theme_version=CLOSE; rpdid=|(Y|RJRR)Y~0J'u~kulY~Rkk; DedeUserID=1611307689; DedeUserID__ckMd5=b0865dba0b3ced5b; buvid_fp_plain=undefined; is-2022-channel=1; b_lsid=D8542F24_191412D93C0; bsource=search_bing; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; browser_resolution=1659-943; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM2MzQ1OTMsImlhdCI6MTcyMzM3NTMzMywicGx0IjotMX0.Ox8rnEpQH5i1H_wQfH2z5CzZC0y8PlqQCy1KVa8XEfQ; bili_ticket_expires=1723634533; SESSDATA=f567fef6%2C1738927393%2C5d207%2A82CjAh2pSUKwDLr1XiI6ncU5B6NXEfWKS7ES6mDC8yGxM6aT3-BTdvK0KAlYpMhCXtEXgSVkl2aTlQWUNacTZOZ0ZNXzJwZ21QT2ozMXFXcWtFc1FpNnBIWlNWbml2Y3BxNV80bUNMZTBVN1dyb3h0STU1ZklDM0MwckJvanRmTmNkeTBFcW5qYl9RIIEC; bili_jct=8d788bcb503d69ba2ded7dfbb53f6e58; sid=71po5kkf; fingerprint=0c7279b7c69b9542a76b8d9df9b7872a; buvid_fp=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc; bp_t_offset_1611307689=964382000909647872"
}


epid_list = ["ep1113346"]
for id_item in epid_list:
    target_url = "https://www.bilibili.com/bangumi/play/" + id_item
    response = requests.get(target_url, headers=head)
    with open("ep番剧电影" + '.html', 'w') as f:
        f.write(response.text)
        f.close()
    # tree = etree.HTML(response.text)
    # id = (tree.xpath('/html/head/meta[@property="og:url" and @content]/@content')[0]).split("/")[-1]
    # print(id)
    # sitemap_url = tree.xpath('/html/head/link[@rel="sitemap" and @title="Sitemap" and @href]/@href')[0]
    # print(sitemap_url)
    # print(id)
# id = "BV18nbceJE3z"
# target_url = "https://space.bilibili.com/327475434"#无默认主页#dynamic动态#video投稿 #favlist #合集channel/series #bangumi追番追剧
# response = requests.get(target_url, headers=head)
# with open("主页" + '.html', 'w') as f:
#     f.write(response.text)
#     f.close()
# tree = etree.HTML(response.text)
# id = (tree.xpath('/html/head/meta[@property="og:url" and @content]/@content')[0]).split("/")[-1]
# print(id)
# sitemap_url = tree.xpath('/html/head/link[@rel="sitemap" and @title="Sitemap" and @href]/@href')[0]
# print(sitemap_url)
# target_url = sitemap_url
# response = requests.get(target_url, headers=head)
# # with open("xml_file.xml", "w") as f:
# #     f.write(response.text)
# #     f.close()
# xml_tree = etree.XML(response.text.encode('utf-8'))
# id_list = xml_tree.xpath('/season/episodeList/episode/playUrl/text()')
# for i in range(len(id_list)):
#     id_list[i]=id_list[i].split("/")[-1]
# print(id_list)
#
# title_list = xml_tree.xpath('/season/episodeList/episode/longTitle/text()')
# print(title_list)
# title=xml_tree.xpath('/season/seasonTitle/text()')[0]
# print(title)
# set_id=sitemap_url.split("/")[-1][0:-4]
# print(set_id)
# id="BV1jx4y1s7u5"
# url->ID->BVAV/SSEP
# 关键词->keyword_list
# ID号: [模式，集数]
# url: [模式，集数]
# 关键词: [模式，select_enable] select_enable==0自动选择检索结果交互，select_enable==1自己选择检索结果
# def user_input_interface(config_dict):
#     in_func_dict = {}
#     keyword_list = []
#     ID_list = []
#     for key in config_dict:
#         # 1.字符串匹配确定identity_flag
#         # ID
#         ID_head_list = ["BV", "Bv", "bV", "bv", "AV", "Av", "aV", "av", "SS", "Ss", "sS", "ss", "EP", "Ep", "eP", "ep"]
#         url_head_list = ["www.", "WWW.", "https://", "http://"]
#         if key[0:2] in ID_head_list:
#             result = ID_standardize(key)
#             ID = result[0]
#             key_type = result[1]
#         elif (key[0:4] in url_head_list) or (key[0:7] in url_head_list) or (key[0:8] in url_head_list):
#             result = from_url_get_ID(key)
#             ID = result[0]
#             key_type = result[1]
#         else:
#             ID = key
#             key_type = "keyword"
#         in_func_dict[ID] = config_dict[key] + key_type
#     # 默认处理
#     for key in in_func_dict:
#         if in_func_dict[key][-1] == "keyword":  # keyword
#             if len(in_func_dict[key]) == 1:  # 全默认
#                 in_func_dict[key] = [default_mode, default_select_enable, in_func_dict[key][-1]]
#             elif len(in_func_dict[key]) == 2:  # 半空
#                 if in_func_dict[key][0] >= 0:  # 指定select_enable默认模式
#                     in_func_dict[key] = [default_mode, in_func_dict[key][0], in_func_dict[key][-1]]
#                 else:  # 默认select_enable指定模式
#                     in_func_dict[key] = [in_func_dict[key][0], default_select_enable, in_func_dict[key][-1]]
#             elif len(in_func_dict[key]) == 3:  # 全满
#                 in_func_dict[key] = [in_func_dict[key][0], in_func_dict[key][1], in_func_dict[key][-1]]
#         else:  # ID
#             if len(in_func_dict[key]) == 1:  # 全默认
#                 if default_select_episode_enable == 0 or default_select_episode_enable == 1:  # 默认选集
#                     in_func_dict[key] = [default_mode, list(range(1, default_episode_num + 1)), in_func_dict[key][-1]]
#                 else:
#                     in_func_dict[key] = [default_mode, [], in_func_dict[key][-1]]
#             elif len(in_func_dict[key]) == 2:  # 半空
#                 if in_func_dict[key][0] >= 0:  # 指定集数默认模式
#                     in_func_dict[key] = [default_mode, list(range(1, in_func_dict[key][0] + 1)), in_func_dict[key][-1]]
#                 else:  # 指定模式默认集数
#                     if default_select_episode_enable == 0 or default_select_episode_enable == 1:  # 默认选集
#                         in_func_dict[key] = [in_func_dict[key][0], list(range(1, default_episode_num + 1)),
#                                              in_func_dict[key][-1]]
#                     else:
#                         in_func_dict[key] = [in_func_dict[key][0], [], in_func_dict[key][-1]]
#             elif len(in_func_dict[key]) == 3:  # 全满
#                 in_func_dict[key] = [in_func_dict[key][0], in_func_dict[key][1], in_func_dict[key][-1]]
#         # in_func_dict key:[mode,select_enable?/集数列表,key_type]
#     for key in in_func_dict:
#         if in_func_dict[key][-1] == "keyword":
#             keyword_list += [key,in_func_dict[key][0], in_func_dict[key][1]]
#         else:
#             ID_list += key+in_func_dict[key]
#     return [ID_list,keyword_list]
#
#
# def from_url_get_ID(url):
#     in_func_result = re.findall("/(BV|Bv|bV|bv)(([A-Z]|[a-z]|[0-9])+)", url)
#     if len(in_func_result):
#         ID = "BV" + in_func_result[0][1]  # BV
#         id_type = "BVAVid"
#     else:
#         in_func_result = re.findall("/(AV|Av|aV|av)(([A-Z]|[a-z]|[0-9])+)", url)
#         if len(in_func_result):
#             ID = "AV" + in_func_result[0][1]  # AV
#             id_type = "BVAVid"
#         else:
#             in_func_result = re.findall("/(SS|Ss|sS|ss)(([A-Z]|[a-z]|[0-9])+)", url)
#             if len(in_func_result):
#                 ID = "ss" + in_func_result[0][1]  # ss
#                 id_type = "ssid"
#             else:
#                 in_func_result = re.findall("/(EP|Ep|eP|ep)(([A-Z]|[a-z]|[0-9])+)", url)
#                 if len(in_func_result):
#                     ID = "ep" + in_func_result[0][1]  # ep
#                     id_type = "epid"
#                 else:
#                     ID = "unknown"
#                     id_type = "unknown"
#     return [ID, id_type]
#
#
# def ID_standardize(ID):
#     in_func_result = re.findall("(BV|Bv|bV|bv)(([A-Z]|[a-z]|[0-9])+)", ID)
#     if len(in_func_result):
#         ID = "BV" + in_func_result[0][1]  # BV
#         id_type = "BVAVid"
#     else:
#         in_func_result = re.findall("(AV|Av|aV|av)(([A-Z]|[a-z]|[0-9])+)", ID)
#         if len(in_func_result):
#             ID = "AV" + in_func_result[0][1]  # AV
#             id_type = "BVAVid"
#         else:
#             in_func_result = re.findall("(SS|Ss|sS|ss)(([A-Z]|[a-z]|[0-9])+)", ID)
#             if len(in_func_result):
#                 ID = "ss" + in_func_result[0][1]  # ss
#                 id_type = "ssid"
#             else:
#                 in_func_result = re.findall("(EP|Ep|eP|ep)(([A-Z]|[a-z]|[0-9])+)", ID)
#                 if len(in_func_result):
#                     ID = "ep" + in_func_result[0][1]  # ep
#                     id_type = "epid"
#                 else:
#                     ID = "unknown"
#                     id_type = "unknown"
#     return [ID, id_type]
