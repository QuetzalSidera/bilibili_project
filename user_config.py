# 一、head配置
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "Referer": "https://www.bilibili.com/",
    "Cookie": "CURRENT_FNVAL=4048; buvid3=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc; b_nut=1721567317; _uuid=67165DF10-7B77-BDE8-3C63-732C2FCAF4D520375infoc; enable_web_push=DISABLE; buvid4=0245F01B-6C4B-CD5A-2EC5-BC060EC0777D18433-024072113-zRTpkL0r94scQqxGfSYKhQ%3D%3D; home_feed_column=5; header_theme_version=CLOSE; rpdid=|(Y|RJRR)Y~0J'u~kulY~Rkk; DedeUserID=1611307689; DedeUserID__ckMd5=b0865dba0b3ced5b; buvid_fp_plain=undefined; is-2022-channel=1; b_lsid=D8542F24_191412D93C0; bsource=search_bing; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; browser_resolution=1659-943; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM2MzQ1OTMsImlhdCI6MTcyMzM3NTMzMywicGx0IjotMX0.Ox8rnEpQH5i1H_wQfH2z5CzZC0y8PlqQCy1KVa8XEfQ; bili_ticket_expires=1723634533; SESSDATA=f567fef6%2C1738927393%2C5d207%2A82CjAh2pSUKwDLr1XiI6ncU5B6NXEfWKS7ES6mDC8yGxM6aT3-BTdvK0KAlYpMhCXtEXgSVkl2aTlQWUNacTZOZ0ZNXzJwZ21QT2ozMXFXcWtFc1FpNnBIWlNWbml2Y3BxNV80bUNMZTBVN1dyb3h0STU1ZklDM0MwckJvanRmTmNkeTBFcW5qYl9RIIEC; bili_jct=8d788bcb503d69ba2ded7dfbb53f6e58; sid=71po5kkf; fingerprint=0c7279b7c69b9542a76b8d9df9b7872a; buvid_fp=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc; bp_t_offset_1611307689=964382000909647872"
}

# 二、视频url配置(目前只支持bilibili)(悲

# 理论最优方法(支持AV号检索)
# 一个用户接口：通用AV,BV号，url，关键词
# default_number_of_videos = 2  # 默认返回检索结果的前number_of_videos个视频
# default_mode = 0
# mode ==-1:全流程 -2:获取音频 -3:仅获取html
# default_episode=1 #也可以不要这个变量，默认不指定集数则只有一集

# 与关键词检索后打印结果有关的变量
# 1.是否最大长度限制？（防止返回的检索结果过多）
# 2.最大长度限制的情况下，MAX_LEN常量
# input("请输入选择的序号，输入(0)退出选择:")

# (url以www或者http开头，用于字符串匹配，对三种进行区别)
# BV号: [模式，集数]
# url: [模式，集数]
# 关键词: [模式，default_select?](关键词检索若遇到分集不能爬去所有集数，只能爬取第一集)
# 关键词检索后，若default_select==0，单独打印出视频标题，通过输入序号进行选择
# (default_select==0/1)

# 默认情况的认定
# url与BV号
# 1.全空例：BV:[]——全默认
# 2.半空例：BV:[-1]——指定模式(-1)，默认集数
# 3.半空例：BV:[2]——默认模式，指定集数为2
# 4.全满例：直接认定

# 关键词
# 1.全空例：关键词:[]——全默认
# 2.半空例：关键词:[-1]——指定模式(-1)，默认default_select==1
# 3.半空例：关键词:[0]——默认模式，default_select==0
# 4.全满例：直接认定

# 故障排除
# 1.大会员专享
# 2.限免
# 3.分集
# 4.特别项目(如番剧后的附加视频)

# #流程
# 1.用户输入
# 2.url www匹配，分成两类
# 3.转化为universal_video_url_dict
# 4.两次遍历universal_video_url_dict，得到最终url(video_url_list)在此步进行选择
# 5.video_url_list导入get_video_and_html中(此函数需要重构以满足需求)


# 通用用户接口
# BV号: [模式，集数]
# url: [模式，集数]
# 关键词: [模式，select_enable?](关键词检索若遇到分集不能爬去所有集数，只能爬取第一集)select_enable==0不交互，select_enable==1交互
# 模式 mode ==-1:全流程 -2:获取音频 -3:仅获取html -4:仅获取画面
video_config = {
    # url
    # "https://www.bilibili.com/video/BV1ss41117Z8": [],
    # BVID与AVID
    # "BV1ss41117Z1": [],
    # 关键词检索
    "想い出がいっぱい": [-1,1]
}

# debug_setting_variables
# 主程序调试变量
main_debug_setting = 0  # 0:获取视频 1:获取图片 2:都要 3与其他：debug程序

# 关键词检索默认
default_select = 0  # 默认直接取前几位，而非进行交互选择
# case default_select == 0 默认不交互模式
default_number_of_videos = 2  # 默认返回检索结果的前number_of_videos个视频
# case default_select == 1 交互模式
to_select_num = 10  # 交互模式下，返回的检索结果数，to_select_num==-1则不限检索结果数，尽数打印

# 通用默认
default_mode = 0  # mode == -1:全流程(整个完整视频) -2:获取mp3 -3:获取html -4:获取画面
default_episode_num = 1  # 也可以不要这个变量，默认不指定集数则只有一集


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
