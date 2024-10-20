# 一、head配置
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "Referer": "https://www.bilibili.com/",
    "Cookie": "CURRENT_FNVAL=4048; buvid3=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc; b_nut=1721567317; _uuid=67165DF10-7B77-BDE8-3C63-732C2FCAF4D520375infoc; enable_web_push=DISABLE; buvid4=0245F01B-6C4B-CD5A-2EC5-BC060EC0777D18433-024072113-zRTpkL0r94scQqxGfSYKhQ%3D%3D; home_feed_column=5; header_theme_version=CLOSE; rpdid=|(Y|RJRR)Y~0J'u~kulY~Rkk; DedeUserID=1611307689; DedeUserID__ckMd5=b0865dba0b3ced5b; buvid_fp_plain=undefined; is-2022-channel=1; b_lsid=D8542F24_191412D93C0; bsource=search_bing; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; browser_resolution=1659-943; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM2MzQ1OTMsImlhdCI6MTcyMzM3NTMzMywicGx0IjotMX0.Ox8rnEpQH5i1H_wQfH2z5CzZC0y8PlqQCy1KVa8XEfQ; bili_ticket_expires=1723634533; SESSDATA=f567fef6%2C1738927393%2C5d207%2A82CjAh2pSUKwDLr1XiI6ncU5B6NXEfWKS7ES6mDC8yGxM6aT3-BTdvK0KAlYpMhCXtEXgSVkl2aTlQWUNacTZOZ0ZNXzJwZ21QT2ozMXFXcWtFc1FpNnBIWlNWbml2Y3BxNV80bUNMZTBVN1dyb3h0STU1ZklDM0MwckJvanRmTmNkeTBFcW5qYl9RIIEC; bili_jct=8d788bcb503d69ba2ded7dfbb53f6e58; sid=71po5kkf; fingerprint=0c7279b7c69b9542a76b8d9df9b7872a; buvid_fp=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc; bp_t_offset_1611307689=964382000909647872"
}

# 二、视频url配置(目前只支持bilibili)(悲
# 1)视频url或BV号
video_config = [  # 视频所在网址或BV号
    # "https://www.bilibili.com/video/BV1ss41117Z8",
    # "BV1ss41117Z8"

]

# 2)关键词检索 如果遇到分集的就可能有bug
default_number_of_videos = 2  # 默认返回检索结果的前number_of_videos个视频
video_keyword_config = {
    # "猫meme": 2,  # 0 代表按照默认值
    # "俄罗斯抽象视频": 1,
    # "robomaster机器人大赛": 2,
    #  "想い出がいっぱい": 3
}

# 3)分集视频url或BV号 (BV号采取字符串匹配，因此，url前两个字符不能是"BV")
video_with_episode_config = {
    # 格式 url/BV号：总集数
    "BV1ss41117Z8": 13,

}

# 三、图片关键词与url配置
# 图片网址或其关键词
picture_url_list = [  # 图片所在网址
    # "https://search.bilibili.com/all?keyword=想い出がいっぱい"
    # "https://baike.baidu.com/item/郑钦文/7679103?fromModule=lemma_search-box"

    # "https://baike.baidu.com/item/孤独摇滚！/56105018?fr=ge_ala",
    # "https://baike.baidu.com/item/后藤独/57098885?lemmaFrom=lemma_starMap&fromModule=lemma_starMap&starNodeId=095968e1cfeab1b823d6aa8d&lemmaIdFrom=56105018",
    # "https://baike.baidu.com/item/后藤偶/63033640?lemmaFrom=lemma_relation_starMap&fromModule=lemma_relation-starMap&lemmaIdFrom=57098885",
    # "https://baike.baidu.com/item/伊地知虹夏/57098884?lemmaFrom=lemma_starMap&fromModule=lemma_starMap&starNodeId=095968e1cfeab1b823d6aa8d&lemmaIdFrom=56105018",
    # "https://baike.baidu.com/item/山田凉/57098882?lemmaFrom=lemma_starMap&fromModule=lemma_starMap&starNodeId=095968e1cfeab1b823d6aa8d&lemmaIdFrom=56105018",
    # "https://baike.baidu.com/item/喜多郁代/57098895?lemmaFrom=lemma_starMap&fromModule=lemma_starMap&starNodeId=095968e1cfeab1b823d6aa8d&lemmaIdFrom=57098882",
]
picture_key_word_list = [  # 搜索关键词(有些多义词百度百科搜索可能需要二次跳转，在代码里面暂时还不太稳定)
    # "GIRLS BAND CRY",
    # "不时轻声地以俄语遮羞的邻座艾莉同学"
    # "鹿乃子乃子乃子虎视眈眈"
    # "郑钦文"
]

# 四、调试设置
# 仅获取html文件
html_url_list = [

]
