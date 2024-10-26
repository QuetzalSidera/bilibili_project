# 一、head配置
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "Referer": "https://www.bilibili.com/",
    "Cookie": "CURRENT_FNVAL=4048; buvid3=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc; b_nut=1721567317; _uuid=67165DF10-7B77-BDE8-3C63-732C2FCAF4D520375infoc; enable_web_push=DISABLE; buvid4=0245F01B-6C4B-CD5A-2EC5-BC060EC0777D18433-024072113-zRTpkL0r94scQqxGfSYKhQ%3D%3D; home_feed_column=5; header_theme_version=CLOSE; rpdid=|(Y|RJRR)Y~0J'u~kulY~Rkk; DedeUserID=1611307689; DedeUserID__ckMd5=b0865dba0b3ced5b; buvid_fp_plain=undefined; is-2022-channel=1; b_lsid=D8542F24_191412D93C0; bsource=search_bing; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; browser_resolution=1659-943; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM2MzQ1OTMsImlhdCI6MTcyMzM3NTMzMywicGx0IjotMX0.Ox8rnEpQH5i1H_wQfH2z5CzZC0y8PlqQCy1KVa8XEfQ; bili_ticket_expires=1723634533; SESSDATA=f567fef6%2C1738927393%2C5d207%2A82CjAh2pSUKwDLr1XiI6ncU5B6NXEfWKS7ES6mDC8yGxM6aT3-BTdvK0KAlYpMhCXtEXgSVkl2aTlQWUNacTZOZ0ZNXzJwZ21QT2ozMXFXcWtFc1FpNnBIWlNWbml2Y3BxNV80bUNMZTBVN1dyb3h0STU1ZklDM0MwckJvanRmTmNkeTBFcW5qYl9RIIEC; bili_jct=8d788bcb503d69ba2ded7dfbb53f6e58; sid=71po5kkf; fingerprint=0c7279b7c69b9542a76b8d9df9b7872a; buvid_fp=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc; bp_t_offset_1611307689=964382000909647872"
}

# 二、视频配置(目前只支持bilibili)(悲
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

# 通用用户接口，支持BV与AV号,ss号与ep号，bilibili视频网址，视频关键词检索
# ID号: [模式，集数]
# url: [模式，集数]
# 关键词: [模式，select_enable] select_enable==0自动选择检索结果交互，select_enable==1自己选择检索结果
# 模式 mode ==-1:全流程 -2:获取音频 -3:仅获取html -4:仅获取画面 -5:自定义
video_config = {
    # "https://jw.hitsz.edu.cn": [-1, 3],  # 不合法的输入 非bilibili网站网址
    # "https://www.bilibili.com": [-1, 3],  # 不合法的输入，bilibili网站网址但非bilibili视频网址
    # "https://www.bilibili.com/video/BV12F411u7my/": [-1, 1],  # 网址检索
    # "BV1aj411w7qj": [-1, 1],  # BV号检索
    # "https://www.bilibili.com/video/BV1J84y1a7i1/?spm_id_from=333.999.0.0": [-2],  # 缺项用默认补全
    # "想い出がいっぱい": [-1, 1],  # 关键词检索非交互模式
    # "感情的摩天楼": [-1, 1],  # 关键词检索交互模式
    # "感情的摩天楼": [-2, 1]
    # "BV1gx4y1G7FL": [-1, 1],
    "ss5045": [-1]
}

# bilibili_project_debug_setting_variables_begin

# ID与url流程
# url->统一为ID(BV,AV,ep,不含ss)->(若含有分集，合集视频，番剧电影且集数默认)选集(默认选或者在交互界面选)->爬取
# ID(BV,AV,ep,ss)->统一为ID(BV,AV,ep,不含ss)->(若含有分集，合集视频，番剧电影且集数默认)选集(默认选或者在交互界面选)->爬取
# 关键词流程
# 关键词->检索得到结果->选择检索结果(默认选或在交互界面选)->(若选择了分集，合集视频，番剧电影)选集(默认选或在交互界面选)->爬取

# 主程序调试变量
main_debug_setting = 0  # 0:获取视频 1:获取图片 2:都要 3与其他：debug程序

# 模式默认的情况下
default_mode = -1  # mode == -1:全流程 -2:获取mp3 -3:获取html -4:获取画面 -5

# 关键词select_enable默认的情况下
default_select_enable = 1  # 默认的select_enable
# case select_enable == 0 不进入检索交互界面
default_number_of_videos = 5  # 默认取检索结果的前number_of_videos个视频
# case select_enable == 1 进入检索交互界面
display_num = 10  # 交互模式下，返回的检索结果数，display_num==-1则不限检索结果数，尽数打印(每个关键词检索结果约42个)

# ID选集默认与关键词检索的情况下
default_select_episode_enable = 1  # 等于0时ID，url与关键词默认取前max{default_episode_num,总集数}集；等于1时ID与url，关键词均会进入选集交互界面；等于2时ID，url默认选集但关键词进入选集交互界面
# case default_select_episode_enable == 0
default_episode_num = 1  # select_episode_enable == 0默认选择max{default_episode_num,总集数}集

# Moviepy 支持的格式
audio_file_type = ".wav"  # 音频文件格式(.mp3,.wav)
video_file_type = ".mp4"  # 完整视频文件或者画面文件格式(.mp4,.avi)

# 通过Cookie模拟登陆
User_Cookie_enable = 0  # 如果要使用自定义Cookie请求bilibili服务器，请将此项置1，程序默认使用非大会员账号登陆获得的Cookie
User_cookie = ""
# bilibili_project_debug_setting_variables_end

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
