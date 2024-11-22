# # 测试用例程
import os
import curses
import time
import subprocess
import curses
import requests

#
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    # "Referer": "https://y.qq.com/",
    # "Cookie": "pgv_pvid=2017414210; fqm_pvqid=355e0187-7c45-4a6b-a396-636d4f4b31a7; fqm_sessionid=4a1dcc9e-18c2-4b69-8f30-11e46c278e70; pgv_info=ssid=s4112326145; ts_last=y.qq.com/; ts_uid=4844999248; wxunionid=oqFLxslTSD_y0rw6KEA-L-dzTRKM; wxopenid=opCFJw2iNWYQT9nb7y31QBmiagGA; qm_keyst=W_X_63B0aXb1mSNORk0K7Zm0-mwZKPFUZSCaCYgwf35tgH4hDP1JppW6PZatOhCFw7nOUFfjuU4GvUHWrdZVirFljS17s1mw; euin=oK6kowEAoK4z7K-q7e-AoeoPNv**; qm_keyst=W_X_63B0aXb1mSNORk0K7Zm0-mwZKPFUZSCaCYgwf35tgH4hDP1JppW6PZatOhCFw7nOUFfjuU4GvUHWrdZVirFljS17s1mw; psrf_qqaccess_token=; wxuin=1152921505294220349; wxuin=1152921505294220349; qqmusic_key=W_X_63B0aXb1mSNORk0K7Zm0-mwZKPFUZSCaCYgwf35tgH4hDP1JppW6PZatOhCFw7nOUFfjuU4GvUHWrdZVirFljS17s1mw; wxrefresh_token=86_5JVHpr6kfWesIlF029W7kkChbUZiWIXjcqbLRBMAC70eL6OMOPTqJCxeODCz1QYQQhE-gM8RUef2xTg6BYy2aPQXAdQ0-V98_8DILfwMUrU; psrf_qqopenid=; psrf_qqrefresh_token=; psrf_qqunionid=; tmeLoginType=1; login_type=2"
}

# epid_list = ["ep1113346","1"]
# print("aaaa",epid_list)
# def clear_screen():
#     screen = curses.initscr()
#     curses.noecho()
#     curses.cbreak()
#     screen.keypad(1)
#     screen.clear()
#     curses.curs_set(0)
#     screen.nodelay(True)
#     curses.endwin()
# target_url = "https://y.qq.com/n/ryqq/songDetail/002g4W7v2WpCcK"
# target_url="https://y.qq.com/n/ryqq/player"
# target_url="https://dl.stream.qqmusic.qq.com/C400002jTxMx1BmKZB.m4a?guid=459685824&vkey=0793DB5839D4605D9484B1D388CF05357389917336AEF718D3301E1FDE6D50652B9556E01388F0401A7E1ADE8839FF7014E35A04DE5C2438&uin=1152921505294220349&fromtag=120032&src=C400000ovSAv3AZBiL.m4a"
# response = requests.get(target_url, headers=head)
# with open("qq音乐result" + '.mp3', 'wb') as f:
#     f.write(response.content)
#     f.close()
target_url = "https://y.qq.com/n/ryqq/songDetail/002y49tF4TGHCC"
response = requests.get(target_url, headers=head)
with open("qq音乐song_detail_html" + '.html', 'w') as f:
    f.write(response.text)
    f.close()
# import requests
# import json
# from bs4 import BeautifulSoup
# import urllib.request
#
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
# }
#
#
# def get_purl(mid):
#     url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?'
#     middata = 'data={"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":1248959521,"g_tk_new_20200303":1832066374,"g_tk":1832066374},"req_1":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"6846657260","songmid":["%s"],"songtype":[0],"uin":"1248959521","loginflag":1,"platform":"20"}}}' % (
#         mid)
#     try:
#         r = requests.get(url + middata, headers=head)
#         r.encoding = 'utf-8'
#         purl_json = json.loads(r.text).get('req_1').get('data').get('midurlinfo')[0].get('purl')
#         return purl_json
#     except:
#         print('获取purl失败')
#
#
# def get_mid(w):
#     url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.top&searchid=58540219608212637&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%s&_=1626671326366&cv=4747474&ct=24&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&uin=1248959763&g_tk_new_20200303=1832066374&g_tk=1832066374&hostUin=0&loginUin=0" % (
#         urllib.request.quote(w))
#     r = requests.get(url, headers=header)
#     r.encoding = 'utf-8'
#     mid_json = json.loads(r.text).get('data').get('song').get('list')[0].get('mid')
#     return mid_json
#
#
# if __name__ == '__main__':
#     music_url = "https://dl.stream.qqmusic.qq.com/"
#     purl = get_purl("002g4W7v2WpCcK")
#     print(purl)
#     music = requests.get(music_url + purl).content
#     with open('music.mp3', 'wb') as f:
#         f.write(music)
#         print(f'下载完成')

# target_url = "https://www.bilibili.com/video/BV1m34y1F7fD/"
# response = requests.get(target_url, headers=head)
# with open("空白标题" + '.html', 'w') as f:
#     f.write(response.text)
#     f.close()
# is_term = 0
# for key,value in os.environ.items():
#     if key == "TERM":
#         is_term = 1
# if is_term == 0:
#     os.environ['TERM'] = 'xterm-256color'
# print(is_term)
import sys
import time

a = ['ss46498', '百变校巴之超学先锋4',
     ['ep786589', 'ep786590', 'ep786591', 'ep786592', 'ep786593', 'ep786594', 'ep786595', 'ep786596', 'ep786597',
      'ep786598', 'ep786599', 'ep786600', 'ep786601', 'ep786602', 'ep786603', 'ep786604', 'ep786605', 'ep786606',
      'ep786607', 'ep786608', 'ep786609', 'ep786610', 'ep786611', 'ep786612', 'ep786613', 'ep786614'],
     ['百变校巴之超学先锋4'], 'bangumi set']

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
