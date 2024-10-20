from json import JSONDecodeError
import requests
from lxml import etree
import json
from bs4 import BeautifulSoup
from moviepy.editor import *
import re
from user_config import *


# alt = "【中日字幕/ED3完整版】不时轻声地以俄语遮羞的邻座艾莉同学 ED3「想い出がいっぱい」/ アーリャ(CV:上坂すみれ)"搜索得到的标题在alt里面
# 关键词转化为视频url函数
def keywords_to_url(keyword_dict, app_type):
    in_func_url_dict = {}  # 添加in_func_前缀以区分
    in_func_title_dict = {}
    if app_type == "bilibili":
        for keyword in keyword_dict:
            # 获取搜索页面html，预处理得到原始list
            search_url = "https://search.bilibili.com/all?keyword=" + keyword  # 转化为搜索页面网址
            response = requests.get(search_url, headers=head)
            url_list_temp = re.findall('href=\"//www.*?\"', response.text)
            title_list_temp = re.findall('alt=\"(.*?)\"', response.text)
            # print(response.text)
            # print(title_list_temp)
            # print(url_list_temp)

            # list处理
            # url_list_temp处理
            url_list_temp.pop(-1)  # 最后一个是'https://www.bilibili.com/v/customer-service'
            for j in range(0, len(url_list_temp)):  # 去除重复项
                if j % 2 == 0:
                    url_list_temp[j] = "https://" + url_list_temp[j][8:-1]
                else:
                    url_list_temp[j] = ""
            for url_item in url_list_temp:
                if url_item == "":
                    url_list_temp.remove(url_item)
            # title_list_temp处理
            for title in title_list_temp:
                if title == "":
                    title_list_temp.remove(title)  # 删除空项
            title_list_temp.pop(0)  # 第一项好像无法通过上面的检查空项的方法删除

            # print(title_list_temp)
            # print(url_list_temp)

            # 截取list中需要的前几项
            if keyword_dict[keyword] == 0:
                url_list_temp = url_list_temp[0:default_number_of_videos]
                title_list_temp = title_list_temp[0:default_number_of_videos]
            else:
                url_list_temp = url_list_temp[0: keyword_dict[keyword]]
                title_list_temp = title_list_temp[0: keyword_dict[keyword]]

            # print(title_list_temp)
            # print(url_list_temp)

            # 将list整理成universal_video_url_list格式
            # 通用video_url_list
            # 格式 url：集数(不分集的默认集数为1)
            for url_item in url_list_temp:
                in_func_url_dict[url_item] = 1
            for title_item in title_list_temp:
                in_func_title_dict[title_item] = 1

    # print(in_func_title_dict)
    # print(in_func_url_dict)
    return in_func_url_dict


def from_set_url_get_epi_url_list(set_url, num_of_episode):
    # 获取BV号
    in_func_list = []
    # 分集总url样例"https://www.bilibili.com/video/BV1ss41117Z8/?spm_id_from=333.337.search-card.all.click&vd_source=61265f50c4aea555795addd1d882df45"
    # 分url样例"https://www.bilibili.com/video/BV1ss41117Z8/?p=3"
    BVID = "BV" + str(re.findall("/BV(.*?)/", set_url)[0])
    for i in range(1, num_of_episode + 1):
        episode_url = "https://www.bilibili.com/video/" + BVID + "/?p=" + str(i)
        in_func_list.append(episode_url)
    print(in_func_list)
    return in_func_list


get_video_debug_setting = 0  # 0:全流程,1:只获取html,2:只获取mp3


def get_video_and_html(target_url):
    response = requests.get(target_url, headers=head)
    res_text = response.text
    with open("get_video.html", "w", encoding="utf-8") as f:
        f.write(res_text)

    soup = BeautifulSoup(res_text, 'lxml')
    title = soup.title.string
    title = str(title)
    title_list = list(title)
    for i in range(len(title_list)):  # 将“/”转换为“｜”防止打开文件时报错
        if title_list[i - 1] == "/":
            title_list[i - 1] = "|"
    title = "".join(title_list)
    print("视频名称：" + title)
    if get_video_debug_setting == 1:
        print("仅获取了html文件")
    if get_video_debug_setting == 0 or get_video_debug_setting == 2:
        # 数据解析

        tree = etree.HTML(res_text)
        try:
            base_info = "".join(tree.xpath("/html/head/script[4]/text()"))[20:]
            # print(base_info)
            info_dict = json.loads(base_info)
            print("html解码方式一(try)")
            video_url = info_dict["data"]["dash"]['video'][0]["baseUrl"]
            audio_url = info_dict["data"]["dash"]['audio'][0]["baseUrl"]
        except JSONDecodeError:
            # try:
            # 目前大会员视频无法获得，但是画质可以获得
            base_info = "".join(tree.xpath("/html/head/script[4]/text()"))
            base_info = str(base_info)
            base_info = re.findall("const\splayurlSSRData\s=\s.*?}}}}", base_info)[0]
            base_info = base_info[23:]
            # print(base_info)
            info_dict = json.loads(base_info)
            # print(info_dict)
            print("html解码方式二(except)")
            video_url = info_dict["result"]["video_info"]["dash"]["video"][0]["baseUrl"]
            audio_url = info_dict["result"]["video_info"]["dash"]['audio'][0]["baseUrl"]

        video_content = requests.get(video_url, headers=head).content
        audio_content = requests.get(audio_url, headers=head).content

        print(video_url)
        print(audio_url)

        # 文件输出
        if len(title) > 100:
            title = title[:100]

        with open("video_split/" + title + "_audio.wav", "wb+") as fp:
            fp.write(audio_content)
            fp.close()
            print("音频获取成功")
        if get_video_debug_setting == 0:
            with open("video_split/" + title + "_video.mp4", "wb") as f:
                f.write(video_content)
                f.close()
                print("画面获取成功")
            # 文件合并
            video_path = "video_split/" + title + "_video.mp4"
            audio_path = "video_split/" + title + "_audio.wav"
            video = VideoFileClip(video_path, audio=False)
            audio = AudioFileClip(audio_path)
            video = video.set_audio(audio)
            video.write_videofile("video_result/" + title + ".mp4")


# end_of_get_video


get_image_debug_setting = 2  # 0:打印获取的html文本 1:打印获取的图片url 2:正常执行全流程
relative_index = 3  # 相关链接一次递归调用的最大数目，只调用排在0～relative_index区间的相关链接
max_depth = 6  # 递归调用最大次数
depth = 0  # 全局变量，用于记录当前递归调用次数


def get_image(target_url, recursive=0):  # 输入网址获取图片
    global max_depth
    response = requests.get(target_url, headers=head)
    response.encoding = response.apparent_encoding
    global depth  # 递归总深度
    depth += 1
    url_list1 = re.findall('(\"url\":\"http.*?\")', response.text)  # 以url：开头的链接
    url_list2 = re.findall('(src=\"http.*?\")', response.text)  # 以src=开头的链接
    for i in range(len(url_list1)):
        url_list1[i - 1] = url_list1[i - 1][7:-1]
        if url_list1[i - 1][-3:] == ".js":  # 排除.js文件
            url_list1[i - 1] = ""
    for i in range(len(url_list2)):
        url_list2[i - 1] = url_list2[i - 1][5:-1]
        if url_list2[i - 1][-3:] == ".js":  # 排除.js文件
            url_list2[i - 1] = ""
    url_list3 = re.findall('(href=\"/item/.*?\")', response.text)  # 相关其他链接
    for i in range(len(url_list3)):
        url_list3[i - 1] = url_list3[i - 1][6:-1]
        url_list3[i - 1] = "https://baike.baidu.com" + url_list3[i - 1]

    if get_image_debug_setting == 0:
        # image_soup = BeautifulSoup(response.text, 'html.parser')
        with open("image_debug" + ".html", "w") as text_file:
            text_file.write(response.text)
            text_file.close()

    if get_image_debug_setting == 1:
        for url_each in url_list1:
            if url_each != '':
                print(url_each)
        print("\n")

        for url_each in url_list2:
            if url_each != '':
                print(url_each)
        print("\n")

        for url_each in url_list3:
            if url_each != '':
                print(url_each)
        print("\n")

    if get_image_debug_setting == 2:
        for url_each in url_list1 + url_list2:
            if url_each != '':
                res = requests.get(url_each, head)
                res.encoding = res.apparent_encoding
                file_name = hash(url_each)
                with open('picture/result_of_{}.png'.format(file_name), 'wb') as img:
                    img.write(res.content)
                    img.close()

        if recursive == 1:
            if len(url_list3) < relative_index:
                max_index = len(url_list3)
            else:
                max_index = relative_index
            for url_each in url_list3[0:max_index - 1]:
                if url_each != '' and depth < max_depth:
                    get_image(url_each, recursive=0)


# end_of_get_image

main_debug_setting = 0  # 0:获取视频 1:获取图片 2:都要 3与其他：debug程序
if __name__ == '__main__':
    # 一、视频url配置
    # 通用video_url_dict
    # 格式 url：集数(不分集的默认集数为1)
    universal_video_url_dict = {}
    # 1)不分集视频
    for item in video_config:
        if item[0:2] == "BV":
            item = "https://www.bilibili.com/video/" + item
            universal_video_url_dict[item] = 1
        else:
            universal_video_url_dict[item] = 1
    # print(universal_video_url_dict)

    # 2)视频关键词检索
    universal_video_url_dict.update(keywords_to_url(keyword_dict=video_keyword_config, app_type="bilibili"))  # 检索url与合并
    # print(universal_video_url_dict)

    # 3)分集
    for key in video_with_episode_config:
        if key[0:2] == "BV":  # 给出BV号
            cplt_key = "https://www.bilibili.com/video/" + key + "/"  # 用"/"标明BV号结束
            universal_video_url_dict[cplt_key] = video_with_episode_config[key]
        else:  # 给出url号
            universal_video_url_dict[key] = video_with_episode_config[key]
    # print(universal_video_url_dict)

    # 二、图片url配置
    if len(picture_key_word_list) != 0:
        for key_word in picture_key_word_list:
            picture_url_list += [
                "https://baike.baidu.com/item/" + key_word
            ]

    # 二、条件判断与获取
    # 视频
    if main_debug_setting == 0 or main_debug_setting == 2:
        for url in universal_video_url_dict:
            # 一般情况
            if universal_video_url_dict[url] == 1:
                get_video_and_html(url)
            # 分集情况
            elif universal_video_url_dict[url] > 1:
                temp_url_list = from_set_url_get_epi_url_list(url, universal_video_url_dict[url])
                for item in temp_url_list:
                    get_video_and_html(item)
            # 不合法输入
            else:
                print("不合法的集数\n")
        print("视频获取结束")
        print("\n\n")

# 图片
if main_debug_setting == 1 or main_debug_setting == 2:
    for url in picture_url_list:
        get_image(url, 0)
        print("\n")
    print("图像获取结束")

# 其他debug程序
else:
    pass
# end_of_main
