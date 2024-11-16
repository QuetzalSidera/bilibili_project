# 测试用例程
import requests
from bilibili_lib import *
from interface import ID_process

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "Referer": "https://www.bilibili.com/",
    "Cookie": "CURRENT_FNVAL=4048; buvid3=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc; b_nut=1721567317; _uuid=67165DF10-7B77-BDE8-3C63-732C2FCAF4D520375infoc; enable_web_push=DISABLE; buvid4=0245F01B-6C4B-CD5A-2EC5-BC060EC0777D18433-024072113-zRTpkL0r94scQqxGfSYKhQ%3D%3D; home_feed_column=5; header_theme_version=CLOSE; rpdid=|(Y|RJRR)Y~0J'u~kulY~Rkk; DedeUserID=1611307689; DedeUserID__ckMd5=b0865dba0b3ced5b; buvid_fp_plain=undefined; is-2022-channel=1; b_lsid=D8542F24_191412D93C0; bsource=search_bing; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; browser_resolution=1659-943; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM2MzQ1OTMsImlhdCI6MTcyMzM3NTMzMywicGx0IjotMX0.Ox8rnEpQH5i1H_wQfH2z5CzZC0y8PlqQCy1KVa8XEfQ; bili_ticket_expires=1723634533; SESSDATA=f567fef6%2C1738927393%2C5d207%2A82CjAh2pSUKwDLr1XiI6ncU5B6NXEfWKS7ES6mDC8yGxM6aT3-BTdvK0KAlYpMhCXtEXgSVkl2aTlQWUNacTZOZ0ZNXzJwZ21QT2ozMXFXcWtFc1FpNnBIWlNWbml2Y3BxNV80bUNMZTBVN1dyb3h0STU1ZklDM0MwckJvanRmTmNkeTBFcW5qYl9RIIEC; bili_jct=8d788bcb503d69ba2ded7dfbb53f6e58; sid=71po5kkf; fingerprint=0c7279b7c69b9542a76b8d9df9b7872a; buvid_fp=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc; bp_t_offset_1611307689=964382000909647872"
}
# target_url = "https://www.bilibili.com/video/BV17j28YqEv6"
# response = requests.get(target_url, headers=head)
# with open("合集.html", "w") as f:
#     f.write(response.text)
#     f.close()
# # print(from_search_page_get_id("孤独摇滚"))
# # id_list = ["BV1wZyHYSEc5", "BV17j28YqEv6", "BV1Wb421E7Yj"]
# for id in id_list:
#     print(from_BVAVid_get_info(id))
#     print("\n")
# #
# a = ['https://space.bilibili.com/476857955/channel/collectiondetail?sid=4065768', '东方project系列', [
#     ['BV1wZyHYSEc5', '【4K超清修复版】东方幻想万华镜 全集', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
#      ['幻想万华镜第1集 春雪异变之章(上)', '幻想万华镜第1集 春雪异变之章(中)', '幻想万华镜第1集 春雪异变之章(下)',
#       '幻想万华镜第2-4集 红雾异变之章(上)', '幻想万华镜第2-4集 红雾异变之章(中)', '幻想万华镜第2-4集 红雾异变之章(下)',
#       '幻想万华镜第5-6集 花之异变之章', '幻想万华镜第7集 巨大妖怪传说之章', '幻想万华镜8-11集 永夜异变之章',
#       '幻想万华镜12-13集 试胆大会之章', '幻想万华镜14-17集 妖怪之山决战之章', '幻想万华镜第18集 灵梦暗杀计划'],
#      'episode video'], ['BV1mN1jYCEAo', '琪露诺八嘎一小时', 'ordinary video']], 'ordinary set']
#
print(ID_process("BV17j28YqEv6"))
b = ['https://space.bilibili.com/8826988/channel/collectiondetail?sid=118272', 'DNA打结系列', [
    ['https://space.bilibili.com/8826988/channel/collectiondetail?sid=118272', '大少女乐团时代',
     [['BV17j28YqEv6', '迷星叫 (Faded ver.)', 'ordinary video'],
      ['BV1i34FeSEtE', '稻香 (MyGO!!!!! ver.)', 'ordinary video'],
      ['BV1fPskeqEX9', '【MyGO】下雨天 (feat. 端程山)', 'ordinary video'],
      ['BV1zeteedE9W', '【GBC】吹き消した灯火听起来就像...心做し', 'ordinary video'],
      ['BV1UDpYe4Ehr', '【GBC】蝶に結いた赤い糸听起来就像...glow', 'ordinary video'],
      ['BV1ZUHvekErF', '影 色 偽 物 / Silhouette phony', 'ordinary video'],
      ['BV1FaWreiEcD', '【完整版】端程山听起来就像...', 'ordinary video'],
      ['BV1QTYge9ETr', '端程山听起来就像... #3', 'ordinary video'],
      ['BV1y9iwewEHg', '端程山听起来就像... #2', 'ordinary video'],
      ['BV19T421k75K', '端程山听起来就像...', 'ordinary video'],
      ['BV1ur421M7mT', '闇に溶けてく听起来就像...', 'ordinary video'],
      ['BV1GB421z7iR', '影 色 发 财（影色舞×恭喜发财）', 'ordinary video'],
      ['BV1xh4y1A7do', '当AveMujica遇上核爆神曲aLIEz', 'ordinary video'],
      ['BV1ZF411S71A', '吉他与孤独与蓝色迷星[MyGO/孤独摇滚]', 'ordinary video'],
      ['BV1yN4y1Q77m', '迷星の塔——最适合花之塔的一曲[MyGO/Lycoris Recoil]', 'ordinary video']], 'ordinary set'],
    ['https://space.bilibili.com/8826988/channel/collectiondetail?sid=118272', '米哈游',
     [['BV1ah4y1a7n8', '⚡原神生日会，启动！⚡', 'ordinary video'],
      ['BV1Ep4y1u7Nw', '【原神】你呀你呀，让风告诉你', 'ordinary video'],
      ['BV1k44y1f7p9', '【原神】如果突然想起我，那就让风告诉你', 'ordinary video'],
      ['BV17a4y1579o', '星间旅行 X 梦的光点【星穹铁道】', 'ordinary video']], 'ordinary set'],
    ['https://space.bilibili.com/8826988/channel/collectiondetail?sid=118272', '绊爱',
     [['BV1D34y1C73t', '你不要走，绊爱 / いかないで、Kizuna AI 【future base X いかないで】', 'ordinary video'],
      ['BV1AZ4y1d7Kc', '绊爱，别走／いかないで、Kizuna AI', 'ordinary video']], 'ordinary set'],
    ['https://space.bilibili.com/8826988/channel/collectiondetail?sid=118272', '主播女孩重度依赖',
     [['BV1744y1H7cM', '✝Rage Your Dream✝', 'ordinary video'],
      ['BV1Wq4y18742', '✝向阿P奔去／Pちゃんに駆ける✝', 'ordinary video']], 'ordinary set'],
    ['https://space.bilibili.com/8826988/channel/collectiondetail?sid=118272', '你的名字',
     [['BV1ds411b7a7', 'Faded X なんでもないや', 'ordinary video'],
      ['BV1VQ4y1M7EY', 'なんでもないや X Faded（重制版）', 'ordinary video'],
      ['BV1SJ411h7GQ', '夢灯籠 × グランドエスケープ', 'ordinary video']], 'ordinary set'],
    ['https://space.bilibili.com/8826988/channel/collectiondetail?sid=118272', '试作',
     [['BV1f3411e7FB', '擅长诈骗的高木同学 第三季 OP', 'ordinary video'],
      ['BV1kz4y1W7tk', '所有奇迹的始发点 Clear Morning X (Re) Aoharu【蔚蓝档案】', 'ordinary video'],
      ['BV1nu4m1P7t2', '灰 姑 娘 发 财', 'ordinary video'],
      ['BV1YtYeetEzc', '【补档】らくらく乐意效劳', 'ordinary video']], 'ordinary set']], 'complex set']

# c = ['https://space.bilibili.com/398500087/channel/collectiondetail?sid=3337992', 'Latchezar Dimitrov',
#      [['BV1VH4y1A79A', '【東方】灵异任你选/Occult A La Carte [Latchezar Dimitrov]', 'ordinary video'],
#       ['BV1Wb421E7Yj', '【东方幕华祭春雪篇】看不破的人偶剧 [Latchezar Dimitrov]', 'ordinary video'],
#       ['BV146421f7ky', '【东方幕华祭春雪篇】狂樱之舞 [Latchezar Dimitrov]', 'ordinary video'],
#       ['BV1DM4m127a7', '【东方幕华祭】黑暗少女 ～ Dark girl [Latchezar Dimitrov]', 'ordinary video'],
#       ['BV1bb421E7Hn', '【東方】永远的巫女 [Latchezar Dimitrov]', 'ordinary video'],
#       ['BV1AT421k7hS', '【東方】少女密室 [Latchezar Dimitrov]', 'ordinary video'],
#       ['BV1eb421E7cS', '【東方】成对的神兽 [Latchezar Dimitrov]', 'ordinary video'],
#       ['BV1sT421k74X', '【東方】平安时代的外星人 [Latchezar Dimitrov]', 'ordinary video'],
#       ['BV154421U7FG', '【東方】绯想天（标题曲） [Latchezar Dimitrov]', 'ordinary video'],
#       ['BV1eS411c7u8', '【東方】恋色Master Spark [Latchezar Dimitrov]', 'ordinary video'],
#       ['BV1YZ421T7Cv', '【東方】哈德曼的妖怪少女 [Latchezar Dimitrov]', 'ordinary video'],
#       ['BV1FM4m1m7Mg', '【東方】红楼 [Latchezar Dimitrov]', 'ordinary video'],
#       ['BV1Nb421J7My', '【東方】幽梦 ～ Inanimate Dream [Latchezar Dimitrov]', 'ordinary video']], 'ordinary set']
