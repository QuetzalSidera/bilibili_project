from json import JSONDecodeError

import requests
from lxml import etree
import json
from bs4 import BeautifulSoup
from moviepy.editor import *
import re
from ref import *

number_of_videos = 2  # 返回检索结果的前number_of_videos个视频


# def data_analyse(res_text):
#     video_url_list=
#     return video_url, audio_url


# alt = "【中日字幕/ED3完整版】不时轻声地以俄语遮羞的邻座艾莉同学 ED3「想い出がいっぱい」/ アーリャ(CV:上坂すみれ)"搜索得到的标题在alt里面
# 关键词转化为视频url函数
def keywords_to_url(keyword_list, app_type):
    url_list = []
    title_list = []
    if app_type == "bilibili":
        for i in range(len(keyword_list)):
            keyword_list[i - 1] = "https://search.bilibili.com/all?keyword=" + keyword_list[i - 1]  # 转化为搜索页面网址
            response = requests.get(keyword_list[i - 1], headers=head)
            url_list_temp = re.findall('href=\"//www.*?\"', response.text)
            title_list_temp = re.findall('alt=\"(.*?)\"', response.text)
            for j in range(len(url_list_temp)):
                url_list_temp[j - 1] = "https://" + url_list_temp[j - 1][8:-1]
            for j in range(len(title_list_temp)):
                title_list_temp[j - 1] = url_list_temp[j - 1][5:-1]
            # print(url_list_temp)
            url_list += url_list_temp[0:2 * number_of_videos:2]  # 此处可以配置视频选择方法
            title_list += title_list_temp[0:2 * number_of_videos:2]
            # print(url_list)
    # print(title_list)
    return url_list


get_video_debug_setting = 1  # 0:只获取html，1:全流程


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
    if get_video_debug_setting == 0:
        print("仅获取了html文件")
    if get_video_debug_setting == 1:
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
        # except JSONDecodeError:
        #     base_info = "".join(tree.xpath("/html/head/script[4]/text()"))
        #     base_info = str(base_info)
        #     base_info = re.findall("const\splayurlSSRData\s=\s.*?}}}}}", base_info)[0]
        #     base_info = base_info[23:]
        #     print(base_info)
        #     info_dict = json.loads(base_info)
        #     print(info_dict)
        #     print("except")
        #     video_url = info_dict["result"]["video_info"]["durl"][0]["url"]
        #     audio_url = info_dict["result"]["video_info"]["dash"]['audio'][0]["baseUrl"]
        video_content = requests.get(video_url, headers=head).content
        audio_content = requests.get(audio_url, headers=head).content

        print(video_url)
        print(audio_url)

        # 文件输出
        if len(title) > 100:
            title = title[:100]

        with open("video_split/" + title + "_video.mp4", "wb") as f:
            f.write(video_content)
            f.close()
            print("画面获取成功")
        with open("video_split/" + title + "_audio.mp3", "wb+") as fp:
            fp.write(audio_content)
            fp.close()
            print("音频获取成功")
        # 文件合并
        video_path = "video_split/" + title + "_video.mp4"
        audio_path = "video_split/" + title + "_audio.mp3"
        video = VideoFileClip(video_path, audio=False)
        audio = AudioFileClip(audio_path)
        video = video.set_audio(audio)
        video = video.set_audio(audio)
        video.write_videofile("video_result/" + title + ".mp4")


# end_of_get_video


get_image_debug_setting = 2  # 0:打印获取的html文本 1:打印获取的图片url 2:正常执行全流程
relative_index = 3  # 相关链接一次递归调用的最大数目，只调用排在0～relative_index区间的相关链接
max_depth = 6  # 递归调用最大次数
depth = 0  # 全局变量，用于记录当前递归调用次数


def get_image(target_url, recursive=0):  # 输入网址获取图片
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
    # 一、url配置
    video_url_list += keywords_to_url(keyword_list=video_keyword_list, app_type="bilibili")

    if len(picture_key_word_list) != 0:
        for key_word in picture_key_word_list:
            picture_url_list += [
                "https://baike.baidu.com/item/" + key_word
            ]

    # 二、条件判断与获取
    if main_debug_setting == 0 or main_debug_setting == 2:
        for url in video_url_list:
            get_video_and_html(url)
            print("\n")
        print("视频获取结束")
        print("\n\n")

    if main_debug_setting == 1 or main_debug_setting == 2:
        for url in picture_url_list:
            get_image(url, 0)
            print("\n")
        print("图像获取结束")
    else:
        pass
# end_of_main
