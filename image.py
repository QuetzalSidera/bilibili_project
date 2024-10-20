import requests
from interface import *

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
