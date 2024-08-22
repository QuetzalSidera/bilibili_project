# head配置
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "Referer": "https://www.bilibili.com/",
    "Cookie": "CURRENT_FNVAL=4048; buvid3=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc; b_nut=1721567317; _uuid=67165DF10-7B77-BDE8-3C63-732C2FCAF4D520375infoc; enable_web_push=DISABLE; buvid4=0245F01B-6C4B-CD5A-2EC5-BC060EC0777D18433-024072113-zRTpkL0r94scQqxGfSYKhQ%3D%3D; home_feed_column=5; header_theme_version=CLOSE; rpdid=|(Y|RJRR)Y~0J'u~kulY~Rkk; DedeUserID=1611307689; DedeUserID__ckMd5=b0865dba0b3ced5b; buvid_fp_plain=undefined; is-2022-channel=1; b_lsid=D8542F24_191412D93C0; bsource=search_bing; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; browser_resolution=1659-943; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM2MzQ1OTMsImlhdCI6MTcyMzM3NTMzMywicGx0IjotMX0.Ox8rnEpQH5i1H_wQfH2z5CzZC0y8PlqQCy1KVa8XEfQ; bili_ticket_expires=1723634533; SESSDATA=f567fef6%2C1738927393%2C5d207%2A82CjAh2pSUKwDLr1XiI6ncU5B6NXEfWKS7ES6mDC8yGxM6aT3-BTdvK0KAlYpMhCXtEXgSVkl2aTlQWUNacTZOZ0ZNXzJwZ21QT2ozMXFXcWtFc1FpNnBIWlNWbml2Y3BxNV80bUNMZTBVN1dyb3h0STU1ZklDM0MwckJvanRmTmNkeTBFcW5qYl9RIIEC; bili_jct=8d788bcb503d69ba2ded7dfbb53f6e58; sid=71po5kkf; fingerprint=0c7279b7c69b9542a76b8d9df9b7872a; buvid_fp=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc; bp_t_offset_1611307689=964382000909647872"
}
# url配置
# 1)视频url或关键词(目前只支持bilibili)(悲
video_url_list = [  # 视频所在网址
    # "https://www.bilibili.com/video/BV1Fy411e7Pc/?spm_id_from=333.337.search-card.all.click&vd_source=61265f50c4aea555795addd1d882df45",
    # # 朝鲜《亲切的父亲》
    # "https://www.bilibili.com/video/BV1XW4y137F5/?spm_id_from=333.337.search-card.all.click&vd_source=61265f50c4aea555795addd1d882df45"
    # # 虹夏妈妈洗脑视频
    # "https://www.bilibili.com/video/BV1RR4y1L76K/?spm_id_from=333.337.search-card.all.click&vd_source=61265f50c4aea555795addd1d882df45"
    # 冰雪奇缘《Let it go》

    # # 冰雪奇缘 Do You Wanna Build a Snowman? 钢琴
    # "https://www.bilibili.com/video/BV1pi42127BU/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 香港迪士尼烟花混剪
    # "https://www.bilibili.com/video/BV1vt421p7s2/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 香港迪士尼烟花
    # "https://www.bilibili.com/video/BV19y421v7vA/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",

    # # 艾莉同学第一~七集 （第七集暂时只能获得预览部分）
    # "https://www.bilibili.com/bangumi/play/ep827835?spm_id_from=333.337.0.0&from_spmid=666.25.episode.0",
    # "https://www.bilibili.com/bangumi/play/ep827836?spm_id_from=333.337.0.0&from_spmid=666.25.episode.0",
    # "https://www.bilibili.com/bangumi/play/ep827837?spm_id_from=333.337.0.0&from_spmid=666.25.episode.0",
    # "https://www.bilibili.com/bangumi/play/ep829607?spm_id_from=333.337.0.0&from_spmid=666.25.episode.0",
    # "https://www.bilibili.com/bangumi/play/ep829608?spm_id_from=333.337.0.0&from_spmid=666.25.episode.0",
    # "https://www.bilibili.com/bangumi/play/ep829609?spm_id_from=333.337.0.0&from_spmid=666.25.episode.0",
    # "https://www.bilibili.com/bangumi/play/ep833028?spm_id_from=333.337.0.0&from_spmid=666.25.episode.0"

    # # 艾莉同学 op
    # "https://www.bilibili.com/video/BV17E4m1R7NZ/?spm_id_from=333.788&vd_source=61265f50c4aea555795addd1d882df45",
    # # 艾莉同学 ed (1～8)
    # "https://www.bilibili.com/video/BV1F6421f7e8/?spm_id_from=333.788&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV17E421P7Vj/?spm_id_from=333.788&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV1CM4m127pd/?spm_id_from=333.788&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV1m4421U7XA/?spm_id_from=333.788&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV1mb421E7h7/?spm_id_from=333.788&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV1iS42197qT/?spm_id_from=333.788&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV1wf421i7Vy/?spm_id_from=333.788&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV1RZ421T7qV/?spm_id_from=pageDriver&vd_source=61265f50c4aea555795addd1d882df45",

    # # GBC回忆向
    # "https://www.bilibili.com/video/BV18m421V7nL/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # GBC 呼诶！？
    # "https://www.bilibili.com/video/BV1em411y71w/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    #
    # # 铁臂阿童木op ed
    # "https://www.bilibili.com/video/BV1Fq4y1p7yq?p=1&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV1Fq4y1p7yq?p=3&vd_source=61265f50c4aea555795addd1d882df45",

    # # 中国铁路上演你的名字名场面
    # "https://www.bilibili.com/video/BV1CF4m1F7k7/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 日本电车上动画一般的天空
    # "https://www.bilibili.com/video/BV1n3411C7YD/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 【下北泽特有动画片】野兽新之助之长毛象的尺寸是？
    # "https://www.bilibili.com/video/BV1Xc411q7XV/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # #【鸡蛋狂魔】砸电脑原版
    # "https://www.bilibili.com/video/BV1Z94y1N7Ea/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # #【鸡蛋狂魔】如何做家庭作业
    # "https://www.bilibili.com/video/BV1L441137Fd/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",

    # # 神奇阿呦op ed
    # "https://www.bilibili.com/video/BV1PU4y1W7Kp/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV19V411C76h/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    #
    # # 我推的孩子 官方MV v1 and v2
    # "https://www.bilibili.com/video/BV1Ws4y1A7fS/?spm_id_from=333.337.search-card.all.click&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV1fu4y1S749/?spm_id_from=333.788.recommend_more_video.5&vd_source=61265f50c4aea555795addd1d882df45",

    # # 泰坦尼克号 我心永恒 钢琴独奏 My Heart Will Go On
    # "https://www.bilibili.com/video/BV1RC4y1a7Py/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 大鱼海棠 印象曲 大鱼
    # "https://www.bilibili.com/video/BV1qp4y167hz/?spm_id_from=333.788.recommend_more_video.3&vd_source=61265f50c4aea555795addd1d882df45",
    # # 钢琴｜Can You Feel The Love Tonight 狮子王 The Lion King Elton John
    # "https://www.bilibili.com/video/BV1HB42167VY/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 梦幻联动！《冰雪奇缘》与《魔发奇缘》史诗管弦乐演奏 - 烈日与坚冰 Frostudio Chambersonic作品
    # "https://www.bilibili.com/video/BV1uq4y1j7Wm/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 【冰雪奇缘9周年】Vuelie II - 史诗管弦乐
    # "https://www.bilibili.com/video/BV1mP4y1X7FD/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 【冰雪奇缘】暗海之夜曲 - Queentessence Outtake - 史诗管弦乐
    # "https://www.bilibili.com/video/BV1YN411n7Uv/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # Let It Go重构 -《冰雪奇缘》史诗管弦乐
    # "https://www.bilibili.com/video/BV1eP411J7RD/?spm_id_from=333.788.recommend_more_video.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # All Is Found回忆之河 -《冰雪奇缘2》史诗管弦乐
    # "https://www.bilibili.com/video/BV17T4y1U75s/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",

    # # YOASOBI 海のまにまに(Umi No Manimani) Official Music Video
    # "https://www.bilibili.com/video/BV1DT411z7gc/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 幻想乡の国际歌，超过20种语言接力衔接bad apple
    # "https://www.bilibili.com/video/BV15c41117aN/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",

    # # 【アイドル】味儿太冲!暴躁男高转生少女爱豆！全网最无违和感偶像中文翻唱
    # "https://www.bilibili.com/video/BV1Uc411M7Xd/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 手牵少女机器人成长日记
    # "https://www.bilibili.com/video/BV17Z4y187Jr/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 用交往过的女孩子的名字翻唱了アイドル (Idol)
    # "https://www.bilibili.com/video/BV1Eu41187Xc/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 【俄语翻唱】推しの子 OP——『アイドル 』
    # "https://www.bilibili.com/video/BV1zN411D7Ep/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 【官方英文版】YOASOBI「アイドル (偶像)」MV English Ver.
    # "https://www.bilibili.com/video/BV17k4y1x7k9/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 千万不要得罪动画角色！！！
    # "https://www.bilibili.com/video/BV1GE421w74b/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 用《权力的游戏》片头打开中国四大一线城市
    # "https://www.bilibili.com/video/BV1r4411V7WD/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 【头脑特工队钢琴】 不同情绪的头脑特工队主题曲
    # "https://www.bilibili.com/video/BV1jf421z7tS/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 【魔法满屋】What Else Can I Do?
    # "https://www.bilibili.com/video/BV15u411D7rZ/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # I See The Light -《魔发奇缘》史诗管弦乐改编
    # "https://www.bilibili.com/video/BV1JW4y1B7Uj/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 徐佳莹《湫兮如风》+陈奕迅《在这个世界相遇》+周深《大鱼》《大鱼海棠》片尾曲/主题曲/印象曲
    # "https://www.bilibili.com/video/BV1ms411B7Pa/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 【冰雪奇缘2】戴上耳机艾莎就在你房间里！8D环绕《Show Yourself》等OST
    # "https://www.bilibili.com/video/BV1rJ41167rv/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 【冰雪奇缘】《Let it go》8D版，戴上耳机感受环绕音！
    # "https://www.bilibili.com/video/BV1EJ411n7Tm/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 【4K超高清】千本桜原版MV feat 初音ミク
    # "https://www.bilibili.com/video/BV1sM4y1V7x1/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # ⚡不时洗脑你的艾莉同学⚡
    # "https://www.bilibili.com/video/BV1pz421i7cu/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # ⚡滋 滋 滋 崩 崩 崩⚡
    # "https://www.bilibili.com/video/BV1sE421P7Vv/?spm_id_from=333.337.search-card.all.click&vd_source=61265f50c4aea555795addd1d882df45",
    # # 【上坂堇/H2O/谭咏麟】「想い出がいっぱい/爱的替身」（《不时轻声地以俄语遮羞的邻座艾莉同学》第三集ED及两版原唱MV）
    # "https://www.bilibili.com/video/BV1Yb421E77k/?spm_id_from=333.788.recommend_more_video.2&vd_source=61265f50c4aea555795addd1d882df45",

    # # gbc全集 分集可用p=x代替
    # "https://www.bilibili.com/video/BV16D421M7x2?p=1&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=2&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=3&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=4&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=5&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=6&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=7&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=8&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=9&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=10&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=11&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=12&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=13&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=14&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=15&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=16&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=17&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=18&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=19&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=20&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=21&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=22&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=23&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=24&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=25&vd_source=61265f50c4aea555795addd1d882df45",
    # "https://www.bilibili.com/video/BV16D421M7x2?p=26&vd_source=61265f50c4aea555795addd1d882df45",

    # # 【交响】《达芬奇密码The DaVinci Code》配乐Chevaliers de Sangreal(汉斯季默Hans Zimmer)
    # "https://www.bilibili.com/video/BV1UW41167yP/?spm_id_from=333.337.search-card.all.click&vd_source=61265f50c4aea555795addd1d882df45",
    # # Rusanda Panfili & 圣杯骑士 - 小提琴 电影《达芬奇密码》OST Chevaliers de Sangreal-Violin Cover
    # "https://www.bilibili.com/video/BV1DA41187wM/?spm_id_from=autoNext&vd_source=61265f50c4aea555795addd1d882df45",
    # # 【孤独摇滚×深海少女】“看呐，你也隐藏着美好的颜色”
    # "https://www.bilibili.com/video/BV1EM411y7jX/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45",
    # # 【4K超高清】深海少女原版 feat. 初音ミク
    # "https://www.bilibili.com/video/BV1s44y1b7Tw/?spm_id_from=333.999.0.0&vd_source=61265f50c4aea555795addd1d882df45"
]

video_keyword_list = [
    # "猫meme",
    # "俄罗斯抽象视频"
    # "robomaster机器人大赛"
    # "想い出がいっぱい"
]
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
