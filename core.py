from json import JSONDecodeError
from lxml import etree
import json
from bs4 import BeautifulSoup
from moviepy.editor import *

from interface import *
from user_config import *


# mode == -1:全流程(整个完整视频) -2:获取音频 -3:获取html -4:获取画面
# video:内核标准格式
# [[视频id(BV AV与SS EP),选择集数列表[], 总集数，视频标题，视频类型标签(0: 一般视频，1: 番剧电影),模式],...]

# 函数输入:video格式变量(列表类型):[视频id(BV AV与SS EP),选择集数列表[], 总集数，视频标题，视频类型标签(0: 一般视频，1: 番剧电影,2:分集视频，3:合集视频),模式]
# 函数输出:无
def set_unfold_and_commit_to_core(video):
    id = video[0]
    info = video[1:]
    # print(video)
    if info[-2] == 0 or info[-2] == 2:  # 一般视频与分集视频
        target_url = "https://www.bilibili.com/video/" + id
        mode = info[-1]
        for episode in info[0]:
            episode_url = "https://www.bilibili.com/video/" + id + "?p=" + str(episode)
            core_function(episode_url, mode)
    elif info[-2] == 1:  # 番剧电影
        target_url = "https://www.bilibili.com/bangumi/play/" + id
        mode = info[-1]
        for episode in info[0]:
            base_episode_id = id[2:]
            # 问题:万一是 ep0003以零开头没办法处理？
            episode_id = id[0:2] + str(eval(base_episode_id) + episode - 1)
            episode_url = "https://www.bilibili.com/bangumi/play/" + episode_id
            core_function(episode_url, mode)
    else:  # 合集视频 collection
        for collection_item_id in info[0]:
            target_url = "https://www.bilibili.com/video/" + collection_item_id
            episode_url = target_url
            mode = info[-1]
            core_function(episode_url, mode)


def core_function(url, mode):
    fail_flag = 0
    # 一、请求返回html的txt
    response = requests.get(url, headers=head)
    res_text = response.text
    soup = BeautifulSoup(res_text, 'lxml')

    # 二、解析html文件
    # 1.获取标题(修正标题以避免误识别成文件路径，防止标题过长导致文件输出出错)
    title = soup.title.string
    title = str(title)
    # 从html中获取的视频名称示例：【东方编曲集】感情的摩天楼　～ Cosmic Mind_哔哩哔哩_bilibili
    title_list = list(title)
    for i in range(len(title_list)):  # 将“/”转换为“｜”防止打开文件时报错
        if title_list[i] == "/":
            title_list[i] = "|"
    title_list = title_list[0:-14]  # 删去最后的"_哔哩哔哩_bilibili"
    title = "".join(title_list)
    print("视频名称：" + title)
    if len(title) > 100:
        title = title[:100]

    # 2.需要获取html,画面或音频文件时,解析html中的资源URL
    if mode == -3:
        print("获取html文件")
        with open("html_file/" + title + ".html", "w", encoding="utf-8") as f:
            f.write(res_text)

    if mode == -1 or mode == -2 or mode == -4:  # 全视频，音频，画面
        # 数据解析
        tree = etree.HTML(res_text)
        try:
            base_info = "".join(tree.xpath("/html/head/script[4]/text()"))[20:]
            # print(base_info)
            info_dict = json.loads(base_info)
            # print("html解码方式一(try)")
            print("该视频为普通视频")
            video_url = info_dict["data"]["dash"]['video'][0]["baseUrl"]
            audio_url = info_dict["data"]["dash"]['audio'][0]["baseUrl"]
        except (JSONDecodeError, IndexError, KeyError):
            try:
                # 目前大会员视频无法获得，但是画质可以获得(?)
                base_info = "".join(tree.xpath("/html/head/script[4]/text()"))
                base_info = str(base_info)
                base_info = re.findall("const\splayurlSSRData\s=\s.*?}}}}", base_info)[0]
                base_info = base_info[23:]
                # print(base_info)
                info_dict = json.loads(base_info)
                # print(info_dict)
                # print("html解码方式二(except)")
                print("该视频为番剧电影")
                video_url = info_dict["result"]["video_info"]["dash"]["video"][0]["baseUrl"]
                audio_url = info_dict["result"]["video_info"]["dash"]['audio'][0]["baseUrl"]
            except (JSONDecodeError, IndexError, KeyError):
                print("该视频返回的html暂时无法解析，已保存\"" + title + ".html\"文件")
                with open("html_file/"+"html_decode_error_" + title + ".html", "w", encoding="utf-8") as f:
                    f.write(res_text)
                video_url = ""
                audio_url = ""
                fail_flag = 1
                print("造成此结果的原因可能是 1.视频需要大会员或充电 2.网络问题 3.访问的视频不存在")
        if fail_flag == 0:
            if mode == -1 or mode == -4:  # 全视频或画面
                video_content = requests.get(video_url, headers=head).content
                # print(video_url)
                with open("video_file/" + title + video_file_type, "wb") as f:
                    f.write(video_content)
                    f.close()
                    if mode == -1:
                        print("获取整个视频，画面已获取成功")
                    else:
                        print("仅获取画面，画面获取成功")

            if mode == -1 or mode == -2:  # 全视频或音频
                audio_content = requests.get(audio_url, headers=head).content
                # print(audio_url)
                with open("audio_file/" + title + audio_file_type, "wb+") as fp:
                    fp.write(audio_content)
                    fp.close()
                    if mode == -1:
                        print("获取整个视频，音频已获取成功")
                    else:
                        print("仅获取音频，音频获取成功")

            if mode == -1:
                print("音频与画面获取结束，音画合并中\n")
                video_path = "video_file/" + title + video_file_type
                audio_path = "audio_file/" + title + audio_file_type
                video = VideoFileClip(video_path, audio=False)
                audio = AudioFileClip(audio_path)
                video = video.set_audio(audio)
                video.write_videofile("video_result/" + title + ".mp4")
    if mode == -5:
        pass  # 自定义程序
    print("\n")
# end_of_get_video
