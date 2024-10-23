# 利用爬虫爬取bilibili视频

## 概述
### 项目组成
主项目：bilibili视频爬虫 <br>
子项目：利用爬虫爬取网站图片，可以用来爬取bilibili封面<br>
### 项目功能
利用爬虫获取bilibili视频文件与信息，利用爬虫爬取网站图片

### 目前开发状况
bilibili视频爬取已经比较成熟，但是仍然存在一些缺陷，目前尚不清楚有无解决方法
图片爬取仍然还是最开始的样子，基本没有发展
关于程序是怎么执行的，在“项目流程框图.png”里面介绍过，主要介绍的还是bilibili视频爬取的流程，毕竟这个项目主要就是哔哩哔哩视频爬取
在本文档中，介绍的重心也将放在bilibili爬虫项目上

## bilibili爬虫项目

### 一、快速上手
本项目相比于它的前身来讲，最大的优点就是用户友好
#### 1)环境配置
   基本python环境配置好后安装以下库
    
    from json import JSONDecodeError
    from lxml import etree
    import json
    from bs4 import BeautifulSoup
    from moviepy.editor import *
    import re
    import requests
    from time import sleep
项目结构
见“项目结构.png”
在bilibili_project下新建
- audio_file文件夹(用来存储bilibili的音频文件)
- video_file文件夹(用来存储bilibili的画面文件，没有声音)
- video_result文件夹(用来存储bilibili的完整视频文件)
- html_file文件夹(用来存储指定模式下获得的html文件，或者获取视频失败后的html文件)
- picture文件夹(用于存储子项目获取的图片)
<br>
注:在项目中，代码会寻找这些文件夹以存储相关文件，如果没找到会报错
#### 2)运行前的准备
1.配置user_config.py文件<br>
user_config.py文件中，与爬取视频相关的用户变量分为两组<br>
##### 第一组变量
video_config字典，标准格式如下图

    video_config={
    BV号: [模式，集数],
    url: [模式，集数],
    关键词: [模式，select_enable],
    }
    # 模式:mode ==-1:全流程 -2:获取音频 -3:仅获取html -4:仅获取画面
    # 集数:指明该url或者BV号是否为分集视频，不是分集视频填1，是分集视频填集数

    # select_enable 关键词提交给bilibili检索后，会返回许多相关的项目
    # 此时 如果此关键词的select_enable为1的话，程序将进入检索交互界面，将搜索得到的视频标题打印到运行窗口
    # 若 如果此关键词的select_enable为0的话，程序将不会进入检索交互界面，搜索得到的视频，按照bilibili排列的顺序，选择前default_number_of_videos(第二组用户变量中的)个进行爬取
    
    # 合法的输入
    url:以“http://”,“https://”,"www."(w大小写均可)开头且含有视频ID(以AV,BV,ss,ep开头的字母与数字组合) 。程序判定时，若ID中有AV/BV判断是普通视频，若有ss/ep判断是番剧电影
    # 其中 普通视频的网址为”https://www.bilibili.com/video/“+AVxxxxx或BVxxxxxx 番剧电影的网址是“https://www.bilibili.com/bangumi/play/”+ssxxxx或epxxxxx
    # 因此 输入url为“https://www.bilibili.com/video/ss12345”或“https://www.bilibili.com/bangumi/play/BV12345678”虽然不会被判定成非法输入，但最后可能得不到你想要的目标，甚至不能得到目标(ID不存在时会出现)
    ID号:以AV,BV,ss,ep开头的字母与数字组合 (不存在的ID最后不能得到视频，画面或音频文件，程序会告诉你获取失败了，并保存下相应网址请求得到的.html文件)
    关键词:不以“http://”,“https://”,"www."(w大小写均不行)开头且不是“AV,BV,ss,ep+只有数字或字母”

    # 不合法的输入情况处理
    # url中没有bilibili视频ID(一般视频为AV、BV号，番剧电影为ss、ep号),程序自动判断，予以丢弃
    # ID号：不是数字与字母组合，含有特殊字符的，程序自动判断，归类为关键词
##### 第二组变量
文件user_config.py中注释“debug_setting_variables_begin”与“debug_setting_variables_end”中间的全局变量
主要负责video_config字典中 每个键对应的“值列表”缺项的默认认定(见下图) <br>
我们从上面也已经知道，模式变量一定小于0，集数变量一定大于0，select_enable只能为0或1，因此，在两项中缺一项时，我们很容易通过留下的项的正负来推断它的实际意义
    
    # 缺项的默认认定
    # url与ID号
    # 1.全空例：ID:[]——模式集数全默认 
    # 2.半空例：ID:[-1]——指定模式为-1，默认集数
    # 3.半空例：ID:[2]——默认模式，指定集数为2
    # 4.全满例：直接认定
    
    # 关键词
    # 1.全空例：关键词:[]——模式与select_enable全默认
    # 2.半空例：关键词:[-1]——指定模式为-1，默认select_enable
    # 3.半空例：关键词:[0]——默认模式，指定select_enable为0
    # 4.全满例：直接认定
    
    当“模式”默认时，mode=default_mode
    当“集数”默认时，集数=default_episode_num 一般为1，但是如果一个视频只有一集本身，按照多集的url配置去访问也不会出现类似数组越界的情况，而只会访问到这一集视频本身
    当“select_enable”默认时，select_enable=default_select_enable (提示一下，这里的select_enable=1时会进入检索交互界面，为0时跳过检索交互界面(见上述))
    
    # 标准格式(想偷懒也可以直接缺项取配置全局的默认变量就行)
    video_config={
        BV号: [模式，集数],
        url: [模式，集数],
        关键词: [模式，select_enable],
    }
    # 示例
    video_config = {
    "https://jw.hitsz.edu.cn": [-1, 3],  # 不合法的输入 非bilibili网站网址
    "https://www.bilibili.com": [-1, 3],  # 不合法的输入，bilibili网站网址但非bilibili视频网址
    "https://www.bilibili.com/video/BV12F411u7my/": [-1, 1],  # 网址检索
    "BV1aj411w7qj": [-1, 1],  # BV号检索
    "https://www.bilibili.com/bangumi/play/ep827835?spm_id_from=333.337.0.0":[-1,]
    "https://www.bilibili.com/video/BV1J84y1a7i1/?spm_id_from=333.999.0.0": [-2],  # 缺项用默认补全
    "想い出がいっぱい": [-1, 0],  # 关键词检索非交互模式
    "感情的摩天楼": [-1, 1],  # 关键词检索交互模式
    "星之梦": [-2, 1] # 关键词检索交互模式
    }
##### 好像少了什么
<p>
通过上述讲解，如果你足够细心，应该可以发现我们在上面的介绍中遗漏了两个变量<br>
一个变量是main_debug_setting，这个变量我不讲你也应该知道，去main.py(原谅我用c语言的方法来命名.py)里面看看就知道了, main_debug_setting=0:只获取视频，1:只获取图片，2:都要，3与其他：debug程序<br></p>
<p>另一个变量是display_num，这个变量在检索交互中有大作用。由于在向bilibili提交关键词，网站返回的检索结果是42个，
如果尽数打印出来，交互界面会显得很庞大。而且交互界面还是在运行窗口里面，这样就给选择造成很大干扰，用户体验也不好，况且排序靠后的检索结果大概率也是相关性很低，我们不想要的。
因此，这个变量限制了交互界面最多打印的项目数(从前往后取display_num个检索结果来展示)。<br></p>
<p>
当然, video_config字典中那么多关键词，也不能一概而论后面的检索结果都是我们不想要的，因此在检索交互界面，我们提供了“all”命令，可以不论display_num为何值而将该关键词的检索结果尽数列出。
</p>

#### 3)关于交互界面
目前的交互界面有两个，检索交互界面和选集交互界面
##### 检索交互界面
<p>
当全局变量display_num>=0时，交互界面默认为不完全打印窗口(检索交互界面，不完全打印.png)<br>
此时，可以输入属于区间[1，展示出的最大序号]的数字，表示你想选择哪个结果<br>
也可以输入exit退出选择<br>
也可以输入delete，删除之前选择的结果，重新选择<br>
也可以输入all，程序将重新开始此次选择，打印所有检索结果，并且删除输入all之前的选择结果<br>
除此之外，任何输入，包括不属于属于区间[1，展示出的最大序号]的数字，将被视为非法字符，输入非法字符程序会给出提示，并且程序会忽略所有非法字符，不会对选择造成任何影响<br>
</p>
<p>
若全局变量display_num=-1时，或者在不完全打印状态下输入all命令，将进入完全打印窗口
此时，可以输入属于区间[1，展示出的最大序号]的数字，表示你想选择哪个结果<br>
也可以输入exit退出选择<br>
也可以输入delete，删除之前选择的结果，重新选择<br>
除此之外，任何输入，包括不属于属于区间[1，展示出的最大序号]的数字，将被视为非法字符，输入非法字符程序会给出提示，并且程序会忽略所有非法字符，不会对选择造成任何影响<br>
</p>

##### 选集交互界面
<p>
我们知道，bilibili的检索结果不仅仅包含普通视频，也包含官方番剧和电影(还有广告)<br>
好在广告的问题在程序里面已经解决了<br>
</p>
<p>
与直接输入官方番剧和电影的ID进行请求不同，通过关键词检索返回的结果能够看见剧集的总集数以及第一集的地址<br>
因此，这就为我们进行选集提供了便利之处<br>
</p>
<p>
这里介绍一个小知识<br>
对于普通分集视频 第i集的网址为 “https://www.bilibili.com/video/BVxxxxxxxx/?p=i”
对于番剧电影，这里要麻烦一点，一般的番剧电影，ep码是连续的
比如《不时用俄语说真心话的邻桌艾莉同学》每连续三集都是连续的

    [ep827835,ep827836,ep827837,
    ep829607,ep829608,ep829609,
    ep833028,ep833029,ep833030,
    ep835998,ep835999,ep836000]
    (中间有断点推测是送审方式为三集一个周期导致)
因此，理论上我们可以通过“第一集地址+偏移地址”的方式找到所有剧集（这种方法对于普通视频都是成立的，但有些番剧电影的ep码老是从中间断开(估计又是万恶的送审机制搞的)）
其中 ss码是番剧编号，ep编号指向的是番剧的具体某一集，因此，若想获取番剧的每一集，建议使用ep号+集数-1的方法
除此之外，还有md码，对应的是番剧电影的介绍页面(例如“https://www.bilibili.com/bangumi/media/md28234980”)
</p>

无论select_enable是何值，都不会影响进入选集交互界面，select_enable决定的是进入检索交互界面<br>
进入选集交互界面的唯一条件就是从检索结果中选择了：分集视频，合集视频或番剧电影

在选集交互界面，可以输入属于区间[1，番剧电影最大集数]的数字，表示你想选择哪一集<br>
也可以输入exit退出选择<br>
也可以输入delete，删除之前选择的结果，重新选择<br>
也可以输入all，表示选择全集，并退出选集交互界面<br>
除此之外，任何输入，包括不属于属于区间[1，番剧电影最大集数]的数字，将被视为非法字符，输入非法字符程序会给出提示，并且程序会忽略所有非法字符，不会对选择造成任何影响<br>

### 二、bilibili介绍
#### 1)bilibili api介绍
##### 1. search
target_url = "https://search.bilibili.com/all?keyword="+keyword+"&page="+page_num


加入简介
读取普通视频集数
将bilibili的html中所有有效信息提取，构建一个库
后期工作：梳理所有视频输入方式的情况