# 一、head配置
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "Referer": "https://www.bilibili.com/",
    "Cookie": "CURRENT_FNVAL=4048; buvid3=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc; b_nut=1721567317; _uuid=67165DF10-7B77-BDE8-3C63-732C2FCAF4D520375infoc; enable_web_push=DISABLE; buvid4=0245F01B-6C4B-CD5A-2EC5-BC060EC0777D18433-024072113-zRTpkL0r94scQqxGfSYKhQ%3D%3D; home_feed_column=5; header_theme_version=CLOSE; rpdid=|(Y|RJRR)Y~0J'u~kulY~Rkk; DedeUserID=1611307689; DedeUserID__ckMd5=b0865dba0b3ced5b; buvid_fp_plain=undefined; is-2022-channel=1; b_lsid=D8542F24_191412D93C0; bsource=search_bing; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; browser_resolution=1659-943; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM2MzQ1OTMsImlhdCI6MTcyMzM3NTMzMywicGx0IjotMX0.Ox8rnEpQH5i1H_wQfH2z5CzZC0y8PlqQCy1KVa8XEfQ; bili_ticket_expires=1723634533; SESSDATA=f567fef6%2C1738927393%2C5d207%2A82CjAh2pSUKwDLr1XiI6ncU5B6NXEfWKS7ES6mDC8yGxM6aT3-BTdvK0KAlYpMhCXtEXgSVkl2aTlQWUNacTZOZ0ZNXzJwZ21QT2ozMXFXcWtFc1FpNnBIWlNWbml2Y3BxNV80bUNMZTBVN1dyb3h0STU1ZklDM0MwckJvanRmTmNkeTBFcW5qYl9RIIEC; bili_jct=8d788bcb503d69ba2ded7dfbb53f6e58; sid=71po5kkf; fingerprint=0c7279b7c69b9542a76b8d9df9b7872a; buvid_fp=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc; bp_t_offset_1611307689=964382000909647872"
}

# 二、视频信息配置
# 用户配置接口，支持BV与AV号,ss号与ep号，bilibili视频网址，视频关键词检索
# ID号(AV,BV,ss,ep): [mode，集数]
# url: [mode，集数]
# 关键词: [mode，select_enable]
# mode ==-1:全流程 -2:获取音频 -3:仅获取html -4:仅获取画面 -5:自定义
# select_enable==0自动选择检索结果，select_enable==1自己选择检索结果

video_config = {
    # 输入样例
    "https://www.bilibili.com/video/BV1pM41117Yr": [-1, 1],
    "BV1pM41117Yr": [-1, 1],
    "ss43164": [-1,12],
    "孤独摇滚": [-3, 1],

    # 测试用例，分集视频
    # "BV1gp421X78k": [-1],
    # "BV1jS4y1L7oW": [-1],
    # 测试用例，一般合集视频
    # "BV1mN1jYCEAo": [-1],
    # 测试用例，复杂合集视频
    # "BV19T421k75K": [-1],
    # "BV1ndryYBEav":[-1],
    # "BV1F6PWeBEJC":[-1],
}

# 空项默认情况的认定
# url与ID号(AV,BV,ss,ep)
# 1.全空例："BV1pM41117Yr":[]——全默认
# 2.半空例："BV1pM41117Yr":[-1]——指定模式(-1)，默认集数
# 3.半空例："BV1pM41117Yr":[2]——默认模式，指定集数(2)
# 4.全满例："BV1pM41117Yr":[-1,2]——指定模式(-1)，指定集数(2)

# 关键词
# 1.全空例："孤独摇滚":[]——全默认
# 2.半空例："孤独摇滚":[-1]——指定模式(-1)，默认select_enable=default_select_enable==1
# 3.半空例："孤独摇滚":[0]——默认模式，select_enable==0
# 4.全满例："孤独摇滚":[-1,1]——指定模式(-1)，select_enable==1

# 三、用户设置变量
# bilibili_project_debug_setting_variables_begin
# 模式(mode)默认的情况下
default_mode = -1  # mode == -1:全流程 -2:获取mp3 -3:获取html -4:获取画面 -5

# 关键词select_enable默认的情况下
default_select_enable = 1  # 默认的select_enable

# case select_enable == 0 不进入检索交互界面
default_number_of_videos = 5  # 默认取检索结果的前number_of_videos个视频
# case select_enable == 1 进入检索交互界面
display_num = 10  # 交互模式下，返回的检索结果数，display_num==-1则不限检索结果数，尽数打印(每个关键词检索结果约42个)

# ID选集默认与关键词检索的情况下
default_select_episode_enable = 2  # 等于0时ID，url与关键词默认取前max{default_episode_num,总集数}集；等于1时ID，url默认选集但关键词进入选集交互界面,等于2时ID与url，关键词均会进入选集交互界面；
# case default_select_episode_enable == 0
default_episode_num = 1  # select_episode_enable == 0默认选择max{default_episode_num,总集数}集

# Moviepy 支持的格式
audio_file_type = ".wav"  # 音频文件格式(.mp3,.wav)
video_file_type = ".mp4"  # 完整视频文件或者画面文件格式(.mp4,.avi)

# 通过Cookie模拟登陆
User_Cookie_enable = 0  # 如果要使用自定义Cookie请求bilibili服务器，请将此项置1，程序默认使用非大会员账号登陆获得的Cookie
User_cookie = ""
# bilibili_project_debug_setting_variables_end

# 四、部分实现
# ID与url
# url->统一为ID(BV,AV,ep,不含ss)->(若含有分集，合集视频，番剧电影且集数默认)选集(默认选或者在交互界面选)->爬取
# ID(BV,AV,ep,ss)->统一为ID(BV,AV,ep,不含ss)->(若含有分集，合集视频，番剧电影且集数默认)选集(默认选或者在交互界面选)->爬取
# 关键词流程
# 关键词->检索得到结果->选择检索结果(默认选或在交互界面选)->(若选择了分集，合集视频，番剧电影)选集(默认选或在交互界面选)->爬取
