# 本文件在用户接口与程序内核标准格式之间进行过渡
import re
import requests
from time import sleep

from user_config import *


# #输入 video_config={}
# video_config格式
# BV号: [模式，集数]
# url: [模式，集数]
# 关键词: [模式，select_enable?](关键词检索若遇到分集不能爬去所有集数，只能爬取第一集)
# 输出universal_video_url_dict={}
# universal_video_url_dict格式
# key:[mode,episode/default_select?,identity_flag]
# 统一用[-1]索引identity_flag，以避免前面空项默认的情况
# identity_flag 0:BV和url 1:关键词检索

# 输入:config_dit
# 输出:内核通用接口格式
# video_dict = []  # 最终遍历带入get_video_and_html的列表
# {[视频id(BVAV与SSEP),选择集数列表[], 总集数，视频标题，视频类型标签(0: 一般视频，1: 番剧电影),模式]}

# 中间变量
# in_func_dict 用于处理ID号模式和URL模式
# 格式：key:[mode,episode/default_select?,identity_flag,视频类型标签(0: 一般视频，1: 番剧电影)]
# # 统一用[-1]索引identity_flag，以避免前面空项默认的情况
# # identity_flag 0:BV和url 1:关键词检索
def user_interface(config_dict):
    # 字符串匹配分离
    print_flag = 0  # 用于优化执行界面ui如果该函数内部调用了print，最后就调用print("\n")与下一节分开
    in_func_dict = {}
    for key in config_dict:

        out_law_input_flag = 0  # url输入时，不含BV或AV号的URL会置1
        identity_flag = 0  # 0:BV和url 1:关键词检索
        http_id_flag = 0  # 0:http等；1:BV或AV
        in_func_key = ""

        # 1.字符串匹配确定identity_flag
        # ID
        ID = ""
        if len(key) >= 2 and (key[0:2] == "BV" or key[0:2] == "Bv" or key[0:2] == "bV" or key[0:2] == "bv"):
            identity_flag = 0
            http_id_flag = 1
            ID = key.upper()
        elif len(key) >= 2 and (key[0:2] == "AV" or key[0:2] == "Av" or key[0:2] == "aV" or key[0:2] == "av"):
            identity_flag = 0
            http_id_flag = 1
            ID = key.upper()
        elif len(key) >= 2 and (key[0:2] == "SS" or key[0:2] == "Ss" or key[0:2] == "sS" or key[0:2] == "ss"):
            identity_flag = 0
            http_id_flag = 1
            ID = key.lower()
        elif len(key) >= 2 and (key[0:2] == "EP" or key[0:2] == "Ep" or key[0:2] == "sp" or key[0:2] == "sp"):
            identity_flag = 0
            http_id_flag = 1
            ID = key.lower()
        # URL
        elif len(key) >= 4 and key[0:4] == "www." or key[0:3] == "WWW.":
            identity_flag = 0
            http_id_flag = 0
        elif len(key) >= 7 and key[0:7] == "http://":
            identity_flag = 0
            http_id_flag = 0
        elif len(key) >= 8 and key[0:8] == "https://":
            identity_flag = 0
            http_id_flag = 0
        else:  # 关键词检索
            identity_flag = 1

        # 2.从config_dict得到in_func_dict,如果是BV号则换成url
        if identity_flag == 0:  # ID与http
            if http_id_flag:  # ID
                config_dict[key].append(identity_flag)
                in_func_dict[ID] = config_dict[key]
            else:  # http
                ID = from_url_get_ID(key)
                if ID == "none":
                    print("非法的URL(不含视频ID号):" + key)
                    print_flag = 1
                    # 非法URL不会被包含进in_func_dict中
                else:
                    config_dict[key].append(identity_flag)
                    in_func_dict[ID] = config_dict[key]

        else:  # 关键词检索
            if len(key):
                keyword = key
                config_dict[key].append(identity_flag)
                in_func_dict[keyword] = config_dict[key]
    # 1.排除空输入与非法url，BV AV换成大写，ss ep换成消小写
    # 补充默认项
    for key in in_func_dict:
        # 由于补充了identity_flag，因此全空：长度1，半空：长度2，全满：长度3
        if in_func_dict[key][-1] == 0:  # 直接给出URL
            # 以下是处理默认情况的逻辑
            if len(in_func_dict[key]) == 1:  # 全空
                if select_episode_enable == 1:
                    in_func_dict[key] = [default_mode, default_episode_num] + in_func_dict[key]
                else:
                    in_func_dict[key] = [default_mode, "select_episode"] + in_func_dict[key]
            elif len(in_func_dict[key]) == 2:  # 半空
                if in_func_dict[key][0] < 0:  # 指定了模式，默认集数
                    if select_episode_enable == 1:
                        in_func_dict[key].insert(1, default_episode_num)
                    else:
                        in_func_dict[key].insert(1, "select_episode")
                else:  # 指定了集数，默认模式
                    in_func_dict[key].insert(0, default_mode)
            elif len(in_func_dict[key]) == 3:  # 全满
                pass

        else:  # 关键词检索
            # 以下是处理默认情况的逻辑
            if len(in_func_dict[key]) == 1:  # 全空
                in_func_dict[key] = [default_mode, default_select_enable] + in_func_dict[key]  # 默认模式，默认是否交互
            elif len(in_func_dict[key]) == 2:  # 半空
                if in_func_dict[key][0] < 0:  # 指定了模式，默认是否交互
                    in_func_dict[key].insert(1, default_select_enable)
                else:  # 指定了是否交互，默认模式
                    in_func_dict[key].insert(0, default_mode)
            elif len(in_func_dict[key]) == 3:  # 全满
                pass
    if print_flag == 1:
        print("\n")
    # in_func_dict 标准化完成
    # print(in_func_dict)
    # 格式 key:[mode,episode/select_enable?,identity_flag]

    # key 关键词，ID
    # ID_list 目标格式 [[视频id(BV AV与ss ep), 选择集数列表[], 总集数，视频标题，视频类型标签(0: 一般视频，1: 番剧电影,2:分集视频，3:合集视频), 模式],...]
    # keyword_list 目标格式 [[key,select_enable,mode],...]
    ID_list = []
    keyword_list = []
    for key in in_func_dict:
        if in_func_dict[key][-1] == 0:  # ID模式
            if key[0:2] == "ss" or key[0:2] == "ep":  # 番剧电影ID
                if in_func_dict[key][1] != "select_episode":
                    ID_list += [[key, list(range(1, in_func_dict[key][1] + 1)), "unknown", "unknown", 1,
                                 in_func_dict[key][0]]]
                else:  # 暂不选集
                    ID_list += [[key, [], "unknown", "unknown", 1, in_func_dict[key][0]]]
            else:  # 一般视频ID
                if in_func_dict[key][1] != "select_episode":
                    ID_list += [[key, list(range(1, in_func_dict[key][1] + 1)), "unknown", "unknown", "unknown",
                                 in_func_dict[key][0]]]
                else:
                    ID_list += [[key, [], "unknown", "unknown", "unknown", in_func_dict[key][0]]]
        if in_func_dict[key][-1] == 1:  # 关键词模式
            keyword_list += [[key, in_func_dict[key][1], in_func_dict[key][0]]]

    # ID_list与keyword_list格式化完成
    # ID_list 符合内核调用规范，可以直接调用 # ID索引由于不能知晓具体有多少集，因此，按照config里面配置的集数操作，没有交互界面
    # print(ID_list)
    # print(keyword_list)

    return [ID_list, keyword_list]


def standardize_ID_list(ID_list):
    for i in range(len(ID_list)):
        if ID_list[i][0][0:2] == "ss" or ID_list[i][0][0:2] == "ep":
            video_identity_flag = 1
            target_url = "https://www.bilibili.com/bangumi/play/" + ID_list[i][0]
            video_response = requests.get(target_url, headers=head)

            with open("test" + ".html", "w") as f:
                f.write(video_response.text)
            episode_num = re.findall("全\d*?话", video_response.text)
            episode_num = episode_num[0][1:-1]
            episode_num = eval(episode_num)
            title = re.findall("<meta property=\"og:title\" content=\".*?\"/>", video_response.text)
            title = title[0][35:-3]

        elif ID_list[i][0][0:2] == "BV" or ID_list[i][0][0:2] == "AV":
            target_url = "https://www.bilibili.com/video/" + ID_list[i][0]
            video_response = requests.get(target_url, headers=head)
            if ID_list[i][0][0:2] == "BV":
                video_identity_flag = 0
                # 获取集数并确定video_identity_flag
                video_episode_info_list = re.findall(
                    "<div title=\"视频选集\" class=\"title\" data-v-f4470e68>视频选集</div> <div class=\"amt\" data-v-f4470e68>（\d*?/\d*?）</div>",
                    video_response.text)
                if len(video_episode_info_list) == 0:
                    video_episode_info_list = re.findall("<div class=\"amt\" data-v-f4470e68>（\d*?/\d*?）</div>",
                                                         video_response.text)
                    if len(video_episode_info_list) == 0:
                        video_identity_flag = 0  # 一般不分集不合集视频
                    else:
                        video_identity_flag = 3  # 合集视频
                else:
                    video_identity_flag = 2  # 分集视频

                if video_identity_flag == 2 or video_identity_flag == 3:
                    if len(video_episode_info_list) == 1:
                        episode_num = re.findall("/\d*?）", video_episode_info_list[0])
                        episode_num = episode_num[0][1:-1]
                        episode_num = int(episode_num)
                    else:
                        print(ID_list[i][0] + "集数解析错误")
                        episode_num = 1
                else:  # 一般不分集不合集视频
                    episode_num = 1
                if ID_list[i][2] == 1 or ID_list[i][2] == "unknown":  # BV1wZyHYSEc5 遇到的情况 动画综合，分集但无法得知集数
                    video_identity_flag = 0

                title = re.findall("\"title\":\".*?\"", video_response.text)
                title = title[0][9:-1]
            else:  # AV 号暂未测试
                video_identity_flag = 0  # 视为普通视频
                # episode_num = "unknown" #去掉unknown
                # title = "unknown"
                episode_num = 1
                title = "unknown"
        else:
            print("不合法输入ID")
            episode_num = 1
            title = "unknown"
            video_identity_flag = 0
        ID_list[i][2] = episode_num
        ID_list[i][3] = title
        ID_list[i][4] = video_identity_flag
    for i in range(len(ID_list)):
        if ID_list[i][2] == "unknown":
            print(ID_list[i][0] + "集数解析错误,默认只有一集")
            ID_list[i][2] = 1
    # 删去不符合条件的集数
    for i in range(len(ID_list)):
        for j in range(len(ID_list[i][1])):
            if ID_list[i][1][j] > ID_list[i][2]:
                ID_list[i][1][j] = ID_list[i][2]
        ID_list[i][1] = list(set(ID_list[i][1]))  # 去重
        ID_list[i][1].sort()  # 排序

    return ID_list


# 输入 URL
# 输出 BV AV SS EP等(字符串)
# 若没找到则返回"none"
def from_url_get_ID(url):
    in_func_result = re.findall("/(BV|Bv|bV|bv)(([A-Z]|[a-z]|[0-9])+)", url)
    if len(in_func_result):
        return "BV" + in_func_result[0][1]  # BV
    else:
        in_func_result = re.findall("/(AV|Av|aV|av)(([A-Z]|[a-z]|[0-9])+)", url)
        if len(in_func_result):
            return "AV" + in_func_result[0][1]  # AV
        else:
            in_func_result = re.findall("/(SS|Ss|sS|ss)(([A-Z]|[a-z]|[0-9])+)", url)
            if len(in_func_result):
                return "ss" + in_func_result[0][1]  # ss
            else:
                in_func_result = re.findall("/(EP|Ep|eP|ep)(([A-Z]|[a-z]|[0-9])+)", url)
                if len(in_func_result):
                    return "ep" + in_func_result[0][1]  # ep
                else:
                    return "none"


def from_set_url_get_epi_url_list(set_url, num_of_episode):
    # 获取BV号
    in_func_list = []
    # 分集总url样例"https://www.bilibili.com/video/BV1ss41117Z8/?spm_id_from=333.337.search-card.all.click&vd_source=61265f50c4aea555795addd1d882df45"
    # 分url样例"https://www.bilibili.com/video/BV1ss41117Z8/?p=3"
    BVID = "BV" + str(re.findall("/BV(.*?)/", set_url)[0])
    for i in range(1, num_of_episode + 1):
        episode_url = "https://www.bilibili.com/video/" + BVID + "/?p=" + str(i)
        in_func_list.append(episode_url)
    # print(in_func_list)
    return in_func_list


def keywords_to_selected_list(keyword, app_type, select_enable, mode):
    global display_num
    in_func_id_list = []  # 添加in_func_前缀以区分，所有搜索结果id列表
    in_func_title_list = []
    info_list = []
    # info_list格式 [[ID号,标题，集数，这是第..集，视频类型标签],[ID号,标题，集数，这是第..集，视频类型标签],[ID号,标题，集数，这是第..集，视频类型标签].....]
    # 视频类型标签(0:一般视频，1:番剧电影，2：分集视频，3:合集视频)
    if app_type == "bilibili":
        # 一、获取搜索页面html
        search_url = "https://search.bilibili.com/all?keyword=" + keyword  # 转化为搜索页面网址
        response = requests.get(search_url, headers=head)
        # 得到response

        # print(response.text)
        # with open(keyword + ".html", "w", encoding="utf-8") as f:
        #     f.write(response.text)

        # 二、从response中提取普通视频，番剧电影检索结果
        # 1)普通视频信息提取
        # 1.分离普通视频描述信息
        video_id_list = []  # 视频id(BV) (str)
        video_title_list = []  # 视频标题 (str)
        video_episode_num_list = []  # 如果是合集视频则为集数(int)，不是合集视频则为1
        video_episode_index_list = []  # 该id的视频是合集视频中的第几集
        video_type_list = []  # 视频类型标签列表(0:一般不分集不合集视频，2：分集视频，3:合集视频)
        video_id_list = re.findall('href=\"//www.bilibili.com/video/.*?/.*?class=\"bili-video-card__info--tit\"',
                                   response.text)
        video_title_list = re.findall(
            'href=\"//www.bilibili.com/video/.*?/.*?class=\"bili-video-card__info--tit\" title=\"(.*?)\"',
            response.text)
        # 得到未处理的video_title_list,video_id_list

        # print(video_title_list)
        # print(video_id_list)

        # 2.处理list 得到video_title_list(截取标题,替换特殊字符),video_id_list(BVid)
        for i in range(len(video_id_list)):
            video_id_list[i] = re.findall("www.bilibili.com/video/.*?/", video_id_list[i])[0][23:-1]
        # 将&amp;quot;换为"\""
        for title_id in range(len(video_title_list)):
            video_title_list[title_id] = video_title_list[title_id].replace("&amp;quot;", "\"")
        # 得到处理后的的video_title_list与video_id_list

        # print(video_title_list)
        # print(video_id_list)
        # 获取每一个普通视频合集信息，集数，位于第几集（后面可能添加合集标题）
        for i in range(len(video_id_list)):
            video_identity_flag = 0  # 视频类型标签(0:一般不分集不合集视频，2：分集视频，3:合集视频)
            index = 1
            episode_num = 1
            target_url = "https://www.bilibili.com/video/" + video_id_list[i]
            video_response = requests.get(target_url, headers=head)

            video_episode_info_list = re.findall(
                "<div title=\"视频选集\" class=\"title\" data-v-f4470e68>视频选集</div> <div class=\"amt\" data-v-f4470e68>（\d*?/\d*?）</div>",
                video_response.text)
            if len(video_episode_info_list) == 0:
                video_episode_info_list = re.findall("<div class=\"amt\" data-v-f4470e68>（\d*?/\d*?）</div>",
                                                     video_response.text)
                if len(video_episode_info_list) == 0:
                    video_identity_flag = 0  # 一般不分集不合集视频
                else:
                    video_identity_flag = 3  # 合集视频
            else:
                video_identity_flag = 2  # 分集视频

            if video_identity_flag == 2 or video_identity_flag == 3:
                if len(video_episode_info_list) == 1:
                    temp_episode_index = re.findall("（\d*?/", video_episode_info_list[0])
                    index = temp_episode_index[0][1:-1]
                    index = int(index)
                    temp_episode_num = re.findall("/\d*?）", video_episode_info_list[0])
                    episode_num = temp_episode_num[0][1:-1]
                    episode_num = int(episode_num)
                    if video_identity_flag == 2:  # 分集视频
                        # print(video_id_list[i] + "为分集视频，该系列共" + str(episode_num) + "集")
                        video_episode_index_list.append(index)
                        video_episode_num_list.append(episode_num)
                    if video_identity_flag == 3:  # 合集视频
                        if episode_num > 1:
                            # print(video_id_list[i] + "为合集视频，这一集为该合集中的第" + str(index) + "集，该系列共" + str(episode_num) + "集")
                            pass
                        else:
                            # BV1wZyHYSEc5 遇到的情况
                            # print(video_id_list[i] + "为动画综合，目前暂不支持这样的集数检索，因此作为普通视频处理，只取第一集")
                            pass
                            video_identity_flag = 0

                        video_episode_index_list.append(index)
                        video_episode_num_list.append(episode_num)
                else:  # 一般不分集不合集视频
                    print("集数解析错误")
            else:  # 一般不分集不合集视频
                # print(video_id_list[i] + "为不分集视频")
                video_episode_index_list.append(1)
                video_episode_num_list.append(1)
            video_type_list.append(video_identity_flag)  # 视频类型标签(0:一般不分集不合集视频，2：分集视频，3:合集视频)
        # 得到 video_episode_num_list 如果是合集视频则为集数(int)，不是合集视频则为1
        # video_episode_index_list 该id的视频是合集视频中的第几集
        # video_type_list 视频类型标签列表(0:一般不分集不合集视频，2：分集视频，3:合集视频)

        # print(video_type_list)
        # print(video_episode_num_list)
        # print(video_episode_index_list)

        # 3.合并上述list为video_list(无需特殊处理)
        video_list = []
        # 格式 [[id号(BV),标题,集数,这是第..集，视频类型标签],[id号(BV),标题，集数,这是第..集，视频类型标签],[id号(BV),标题，集数,这是第..集，视频类型标签].....] 问题:检索界面无法得知分集普通视频的总集数，因此没有加入集数列表成员
        # 视频类型标签(0:一般不分集不合集视频，2：分集视频，3:合集视频)
        # 普通视频url："https://www.bilibili.com/video/"+BV号(第一集)+"/？p="+集数
        for i in range(len(video_id_list)):
            video_list.append(
                [video_id_list[i], video_title_list[i], video_episode_num_list[i], video_episode_index_list[i],
                 video_type_list[i]])
        # 得到 video_list(无需特殊处理)

        # print(video_list)

        # 5.将video_list插入in_func_title_list与in_func_id_list中
        video_list.reverse()  # 倒序插入
        for video in video_list:
            in_func_id_list.insert(0, video[0])
            in_func_title_list.insert(0, video[1])
        video_list.reverse()
        # 得到含普通视频的in_func_title_list与in_func_id_list
        # print(in_func_title_list)
        # print(in_func_id_list)

        # 2)番剧电影信息提取
        # 1.分离番剧电影描述信息
        episode_num_list = []  # 番剧电影总集数 (int)
        animation_and_film_ssid_list = []  # 番剧电影ssid (str)
        animation_and_film_epid_list = []  # 番剧电影epid(第一集epid) (str)
        animation_and_film_title_list = []  # 番剧标题 (str)

        animation_and_film_temp_list = re.findall(
            '<a title=\".*?\" class=\"text_ellipsis\" href=\"https://www.bilibili.com/bangumi/play/.*?\" target=\"_blank\"',
            response.text)
        for item in animation_and_film_temp_list:
            animation_and_film_title_list += re.findall("title=\".*?\"", item)
            animation_and_film_ssid_list += re.findall("href=\"https://www.bilibili.com/bangumi/play/.*?\"", item)
        episode_num_list = re.findall('</span></span><span data-v-384b5d39>全(\d*)话</span></div>', response.text)
        # 得到 未处理的episode_num_list(str),animation_and_film_title_list和animation_and_film_ssid_list

        # print(animation_and_film_temp_list) #临时list
        # print(animation_and_film_title_list)
        # print(animation_and_film_ssid_list)
        # print(episode_num_list)

        # 2.处理list 得到animation_and_film_title_list(截取标题,替换特殊字符),animation_and_film_ssid_list(截取ssid)与episode_num_list(str->int)
        for i in range(len(animation_and_film_title_list)):
            animation_and_film_title_list[i] = animation_and_film_title_list[i][7:-1]
            animation_and_film_title_list[i] = animation_and_film_title_list[i].replace("&amp;quot;",
                                                                                        "\"")  # 将&amp;quot;换为"\""
        for i in range(len(animation_and_film_ssid_list)):
            animation_and_film_ssid_list[i] = animation_and_film_ssid_list[i][44:-1]
        for i in range(len(episode_num_list)):
            episode_num_list[i] = int(episode_num_list[i])
        # 得到标准的 animation_and_film_title_list,animation_and_film_ssid_list与episode_num_list

        # print(animation_and_film_title_list)
        # print(animation_and_film_ssid_list)
        # print(episode_num_list)

        # 3.搜索结果返回的为番剧ss号，因此为了便于选集，更换为第一集的ep号(ssid->epid)
        for ssid in animation_and_film_ssid_list:
            target_url = "https://www.bilibili.com/bangumi/play/" + ssid
            response = requests.get(target_url, headers=head)
            animation_and_film_epid_list += re.findall(
                "<link rel=\"canonical\" href=\"//www.bilibili.com/bangumi/play/ep(\d*)\"/>", response.text)
        for i in range(len(animation_and_film_epid_list)):
            animation_and_film_epid_list[i] = "ep" + animation_and_film_epid_list[i]

        # print(animation_and_film_title_list)
        # print(animation_and_film_epid_list)
        # print(animation_and_film_ssid_list)
        # print(episode_num_list)

        # 4.合并上述list为animation_and_film_list(无需特殊处理)
        animation_and_film_list = []
        # 格式 [[ep号,标题，集数],[ep号,标题，集数],[ep号,标题，集数].....]
        # 番剧电影url："https://www.bilibili.com/bangumi/play/"+ep号(第一集)+集数-1
        for i in range(len(animation_and_film_epid_list)):
            animation_and_film_list.append(
                [animation_and_film_epid_list[i], animation_and_film_title_list[i], episode_num_list[i]])
        # 得到 animation_and_film_list(无需特殊处理)
        # print(animation_and_film_list)

        # 5.将animation_and_film_list插入in_func_title_list与in_func_id_list中
        animation_and_film_list.reverse()  # 倒序插入
        for video in animation_and_film_list:
            in_func_id_list.insert(0, video[0])
            in_func_title_list.insert(0, video[1])
        animation_and_film_list.reverse()
        # 得到含番剧电影的in_func_title_list与in_func_id_list
        # print(in_func_title_list)
        # print(in_func_id_list)

        # 3)合并番剧电影与视频描述信息
        # video_list格式 [[id号(BV),标题,集数,这是第..集，视频类型标签],[id号(BV),标题，集数,这是第..集，视频类型标签],[id号(BV),标题，集数,这是第..集，视频类型标签].....]
        # animation_and_film_list格式 [[ep号,标题，集数],[ep号,标题，集数],[ep号,标题，集数].....]
        # info_list格式 [[ID号,标题，集数，这是第..集，视频类型标签],[ID号,标题，集数，这是第..集，视频类型标签],[ID号,标题，集数，这是第..集，视频类型标签].....]
        # 视频类型标签(0:一般视频，1:番剧电影，2：分集视频，3:合集视频)
        for animation_and_film in animation_and_film_list:
            info_list.append([animation_and_film[0], animation_and_film[1], animation_and_film[2], 1, 1])
        info_list += video_list

        # 提取检索信息完毕
        # print(in_func_title_list)
        # print(in_func_id_list)
        # print(info_list)

        # 三、选择与交互界面
        display_id_list = []
        display_title_list = []
        selected_id_list = []

        if select_enable == 0:  # 不交互，默认截取list中需要的前几项
            display_id_list = in_func_id_list
            display_title_list = in_func_title_list
            selected_id_list = list(range(1, default_number_of_videos + 1))

        else:  # 交互模式
            display_all_flag = 0  # to_select_num==-1时起作用
            if display_num != -1:
                display_all_flag = 0
                # 交互界面
                display_id_list = in_func_id_list[0:display_num]
                display_title_list = in_func_title_list[0:display_num]

                in_law_index_list = list(range(1, len(display_title_list) + 1))
                for i in range(1, len(in_law_index_list) + 1):
                    in_law_index_list[i - 1] = str(in_law_index_list[i - 1])

                print("关键词检索，交互模式，" + "目前仅展示检索结果前" + str(
                    display_num) + "个视频,以下是可供选择的项目:")
                for i in range(1, len(display_title_list) + 1):
                    # info_list格式 [[ID号,标题，集数，这是第..集，视频类型标签],[ID号,标题，集数，这是第..集，视频类型标签],[ID号,标题，集数，这是第..集，视频类型标签].....]
                    # 视频类型标签(0:一般视频，1:番剧电影，2：分集视频，3:合集视频)
                    info_index = i - 1
                    title = info_list[info_index][1]
                    episode_num = info_list[info_index][2]
                    now_episode_index = info_list[info_index][3]
                    video_type = info_list[info_index][-1]
                    if video_type == 0:
                        type_tag = "(一般视频)"
                        episode_tag = ""
                    elif video_type == 1:
                        type_tag = "(番剧电影)"
                        episode_tag = "(全" + str(episode_num) + "话)"
                    elif video_type == 2:
                        type_tag = "(分集视频)"
                        episode_tag = "(全" + str(episode_num) + "话)"
                    elif video_type == 3:
                        type_tag = "(合集视频)"
                        episode_tag = "(第" + str(now_episode_index) + "集/全" + str(episode_num) + "集)"
                    else:
                        type_tag = "(unknown)"
                        episode_tag = "(unknown)"
                    print("\t" + str(i) + "." + type_tag + episode_tag + title)
                print("")

                select_result = input("请输入您选择的视频序号,输入exit退出选择,输入delete重新选择，输入all展示所有结果:")
                while select_result != "exit":
                    if select_result in in_law_index_list:  # 排除特殊字符
                        selected_id_list.append(eval(select_result))
                        select_result = input("请输入您选择的视频序号:")
                    elif select_result == "all":
                        print("\n展示所有项目\n")
                        display_all_flag = 1
                        sleep(0.6)
                        break
                    elif select_result == "delete":  # 输入delete重新选择
                        selected_id_list.clear()
                        print("重新选择")
                        select_result = input(
                            "请输入您选择的视频序号,输入exit退出选择,输入delete重新选择，输入all展示所有结果:")
                    else:
                        print("非法输入")
                        select_result = input("请输入您选择的视频序号:")

            if display_num == -1 or display_all_flag == 1:  # 别用else 上文里面all要用这个地方
                selected_id_list.clear()
                display_id_list = in_func_id_list
                display_title_list = in_func_title_list

                in_law_index_list = list(range(1, len(display_title_list) + 1))
                for i in range(1, len(in_law_index_list) + 1):
                    in_law_index_list[i - 1] = str(in_law_index_list[i - 1])

                print("关键词检索，交互模式，" + "目前展示所有检索结果，共" + str(
                    len(display_title_list)) + "个视频,以下是可供选择的项目:")
                for i in range(1, len(display_title_list) + 1):
                    # info_list格式 [[ID号,标题，集数，这是第..集，视频类型标签],[ID号,标题，集数，这是第..集，视频类型标签],[ID号,标题，集数，这是第..集，视频类型标签].....]
                    # 视频类型标签(0:一般视频，1:番剧电影，2：分集视频，3:合集视频)
                    info_index = i - 1
                    title = info_list[info_index][1]
                    episode_num = info_list[info_index][2]
                    now_episode_index = info_list[info_index][3]
                    video_type = info_list[info_index][-1]
                    if video_type == 0:
                        type_tag = "(一般视频)"
                        episode_tag = ""
                    elif video_type == 1:
                        type_tag = "(番剧电影)"
                        episode_tag = "(全" + str(episode_num) + "话)"
                    elif video_type == 2:
                        type_tag = "(分集视频)"
                        episode_tag = "(全" + str(episode_num) + "话)"
                    elif video_type == 3:
                        type_tag = "(合集视频)"
                        episode_tag = "(第" + str(now_episode_index) + "集/全" + str(episode_num) + "集)"
                    else:
                        type_tag = "(unknown)"
                        episode_tag = "(unknown)"
                    print("\t" + str(i) + "." + type_tag + episode_tag + title)
                print("")

                select_result = input("请输入您选择的视频序号,输入exit退出选择,输入delete重新选择:")
                while select_result != "exit":
                    if select_result in in_law_index_list:  # 排除特殊字符
                        selected_id_list.append(eval(select_result))
                        select_result = input("请输入您选择的视频序号:")
                    elif select_result == "delete":
                        selected_id_list.clear()
                        print("重新选择")
                        select_result = input("请输入您选择的视频序号,输入exit退出选择,输入delete重新选择:")
                    else:
                        print("非法输入")
                        select_result = input("请输入您选择的视频序号:")
            print("退出交互模式\n")
        # 得到 selected_id_list

        # info_list格式 [[ID号,标题，集数，这是第..集，视频类型标签],[ID号,标题，集数，这是第..集，视频类型标签],[ID号,标题，集数，这是第..集，视频类型标签].....]
        # 视频类型标签(0:一般视频，1:番剧电影，2：分集视频，3:合集视频)
        # 根据selected_id_list建立未选集的内核标准格式selected_video_list
        selected_video_list = []
        # selected_video_list目前格式 [[视频id(BV AV与EP),选择集数列表[], 总集数，视频标题，视频类型标签(0: 一般视频，1: 番剧电影,2:分集视频，3:合集视频),模式],...]
        for selected_index in selected_id_list:
            video_id = display_id_list[selected_index - 1]
            info_list_index = 0
            for i in range(len(info_list)):
                if video_id == info_list[i][0]:
                    info_list_index = i  # 在info_list中索引到对应视频描述信息
            selected_video_list.append([info_list[info_list_index][0],
                                        [], info_list[info_list_index][2],
                                        info_list[info_list_index][1],
                                        info_list[info_list_index][4], mode])
        # 得到番剧电影未选集的 selected_video_list # 目前格式 [[视频id(BV AV与EP),选择集数列表[], 总集数，视频标题，视频类型标签(0: 一般视频，1: 番剧电影,2:分集视频，3:合集视频),模式],...]
        return selected_video_list


# 输入: 满足内核标准输入的list
# 输出：不含重复项的满足内核标准的list
# 过程：判断冲突，合并
def merge_list(standard_list):
    pass
    return standard_list


# 问题:这个函数还要debug
# standard_list [[视频id(BV AV与EP),选择集数列表[], 总集数，视频标题，视频类型标签(0: 一般视频(动画综合也包含在其中)，1: 番剧电影,2:分集视频，3:合集视频),模式],...]
# 输入选择集数列表[]为空表
# 输出列表为可提交给内核的列表
def episode_select_interface(standard_list):
    to_pop_list = []  # 选集为空将要删除的列表
    if len(standard_list):
        print("以下是您选择的项目:")
        for i in range(len(standard_list)):  # 打印视频选择情况
            if standard_list[i][-2] == 1:
                tag = "(番剧电影)"
                print(tag + standard_list[i][3])
        for i in range(len(standard_list)):
            if standard_list[i][-2] == 2:
                tag = "(分集视频)"
                print(tag + standard_list[i][3])
        for i in range(len(standard_list)):
            if standard_list[i][-2] == 3:
                tag = "(合集视频)"
                print(tag + standard_list[i][3])
        for i in range(len(standard_list)):
            if standard_list[i][-2] == 0:
                standard_list[i][1] = [1]  # 普通视频只取第一集
                tag = "(一般视频)"
                print(tag + standard_list[i][3])
        print("")
        sleep(1)
        if select_episode_enable == 1:  # 交互界面选集
            for i in range(len(standard_list)):
                if standard_list[i][1] == []:  # 未选集
                    if standard_list[i][-2] == 1 or standard_list[i][-2] == 2:  # 番剧电影/分集视频
                        print("标题:" + standard_list[i][3])
                        print("总集数:" + str(standard_list[i][2]))
                        standard_list[i][1].clear()
                        # 合法集数列表
                        in_law_index_list = list(range(1, standard_list[i][2] + 1))
                        for j in range(1, len(in_law_index_list) + 1):
                            in_law_index_list[j - 1] = str(in_law_index_list[j - 1])

                        select_result = input(
                            "请输入您选择的集数序号,输入exit退出选择,输入delete重新选择，输入all选择全集:")
                        while select_result != "exit":
                            if select_result in in_law_index_list:  # 排除特殊字符
                                standard_list[i][1].append(eval(select_result))
                                select_result = input("请输入您选择的集数序号:")
                            elif select_result == "delete":
                                standard_list[i][1].clear()
                                print("重新选择")
                                select_result = input(
                                    "请输入您选择的集数序号,输入exit退出选择,输入delete重新选择，输入all选择全集:")
                            elif select_result == "all":
                                for j in range(1, standard_list[i][2] + 1):
                                    standard_list[i][1].append(j)
                                print("选择全集")
                                break
                            else:
                                print("非法输入")
                                select_result = input("请输入您选择的集数序号:")
                        if len(standard_list[i][1]) == 0:
                            print("您没有选择集,该项目将会被移除")
                        standard_list[i][1] = list(set(standard_list[i][1]))  # 去重
                        standard_list[i][1].sort()  # 排序
                        print("")

            sleep(1)
            for i in range(len(standard_list)):
                if standard_list[i][1] == []:  # 未选集
                    if standard_list[i][-2] == 3:  # 合集视频
                        target_url = "https://www.bilibili.com/video/" + standard_list[i][0]
                        video_response = requests.get(target_url, headers=head)
                        collection_id_list = re.findall("data-key=\".*?\"", video_response.text)
                        collection_title_list = re.findall(
                            "<div class=\"simple-base-item normal\"><div title=\".*?\" class=\"title\">",
                            video_response.text)
                        collection_name = re.findall("spm_id_from=.*?\" title=\".*?\" class=\"title jumpable\"",
                                                     video_response.text)
                        collection_name = re.findall("title=\".*?\"", collection_name[0])

                        for j in range(len(collection_id_list)):
                            collection_id_list[j] = collection_id_list[j][10:-1]
                        for j in range(len(collection_title_list)):
                            collection_title_list[j] = collection_title_list[j][49:-16]
                        collection_name = collection_name[0][7:-1]

                        # print(collection_title_list)
                        # print(collection_id_list)
                        # print(collection_name)
                        collection_info_dict = {}
                        for i in range(len(collection_id_list)):
                            collection_info_dict[collection_id_list[i]] = collection_title_list[i]
                        # print(collection_info_dict)
                        # 找到已选定的项目标题，否则打印ID
                        pre_selected = standard_list[i][0]
                        try:
                            pre_selected = collection_info_dict[pre_selected]
                        except KeyError:
                            pre_selected = standard_list[i][0]
                        limit_display = 0  # 集数过多，限制打印项目时为1
                        if len(collection_title_list) > 20:
                            max_index = 20
                            limit_display = 1
                        else:
                            max_index = len(collection_title_list)
                            limit_display = 0
                        print("检测到" + pre_selected + "在合集\"" + collection_name + "\"中,该合集共" + str(
                            standard_list[i][2]) + "集,如下,默认已选择\"" + pre_selected + "\":")

                        if limit_display == 1:
                            for j in range(max_index):
                                print(str(j + 1) + "." + collection_title_list[j])
                            in_law_index_list = list(range(1, max_index + 1))
                            for j in range(len(in_law_index_list)):
                                in_law_index_list[j] = str(in_law_index_list[j])
                            select_result = input(
                                "请输入您选择的集数序号,输入exit退出选择,输入delete重新选择,输入display_all展示全集,输入select all选择展示出的全集:")
                            while select_result != "exit":
                                if select_result in in_law_index_list:  # 排除特殊字符
                                    standard_list[i][1].append(collection_id_list[eval(select_result)])
                                    select_result = input("请输入您选择的集数序号:")
                                elif select_result == "delete":
                                    standard_list[i][1].clear()
                                    print("重新选择")
                                    select_result = input(
                                        "请输入您选择的集数序号,输入exit退出选择,输入delete重新选择，输入all选择全集:")
                                elif select_result == "select all":
                                    standard_list[i][1] = collection_id_list[0:max_index + 1]
                                    print("选择全集")
                                    break
                                elif select_result == "display all":
                                    standard_list[i][1].clear()
                                    print("\n展示所有项目\n")
                                    max_index = len(collection_title_list)
                                    limit_display = 0
                                    break
                                else:
                                    print("非法输入")
                                    select_result = input("请输入您选择的集数序号:")
                        if limit_display == 0:
                            for j in range(max_index):
                                print(str(j + 1) + "." + collection_title_list[j])
                            in_law_index_list = list(range(1, max_index + 1))
                            for j in range(len(in_law_index_list)):
                                in_law_index_list[j] = str(in_law_index_list[j])
                            select_result = input(
                                "请输入您选择的集数序号,输入exit退出选择,输入delete重新选择,输入select all选择全集:")
                            while select_result != "exit":
                                if select_result in in_law_index_list:  # 排除特殊字符
                                    standard_list[i][1].append(collection_id_list[eval(select_result)])
                                    select_result = input("请输入您选择的集数序号:")
                                elif select_result == "delete":
                                    standard_list[i][1].clear()
                                    print("重新选择")
                                    select_result = input(
                                        "请输入您选择的集数序号,输入exit退出选择,输入delete重新选择，输入all选择全集:")
                                elif select_result == "select all":
                                    standard_list[i][1] = collection_id_list[0:max_index + 1]
                                    print("选择全集")
                                    break
                                else:
                                    print("非法输入")
                                    select_result = input("请输入您选择的集数序号:")
                        standard_list[i][1].append(standard_list[i][0])  # 默认选择
                        standard_list[i][1] = list(set(standard_list[i][1]))  # 去重
                        print('选择结果:')
                        for j in range(len(standard_list[i][1])):
                            try:
                                print(str(j + 1) + "." + collection_info_dict[standard_list[i][1][j]])
                            except KeyError:
                                print(str(j + 1) + "." + standard_list[i][1][j])
                        print("")
            sleep(1)
            print("退出选集交互界面\n")
            for i in range(len(standard_list)):
                if len(standard_list[i][1]) == 0:
                    to_pop_list.append(i)
            to_pop_list.reverse()
            for i in to_pop_list:
                standard_list.pop(i)
        else:  # 默认选集
            for i in range(len(standard_list)):
                episode_num = max(default_episode_num, standard_list[i][2])
                if standard_list[i][-2] == 1 or standard_list[i][-2] == 2:  # 番剧电影/分集视频
                    standard_list[i][1] = list(range(1, episode_num + 1))
                elif standard_list[i][-2] == 3:  # 合集视频
                    target_url = "https://www.bilibili.com/video/" + standard_list[i][0]
                    video_response = requests.get(target_url, headers=head)
                    collection_id_list = re.findall("data-key=\".*?\"", video_response.text)
                    collection_title_list = re.findall(
                        "<div class=\"simple-base-item normal\"><div title=\".*?\" class=\"title\">",
                        video_response.text)
                    collection_name = re.findall("spm_id_from=.*?\" title=\".*?\" class=\"title jumpable\"",
                                                 video_response.text)
                    collection_name = re.findall("title=\".*?\"", collection_name[0])

                    for j in range(len(collection_id_list)):
                        collection_id_list[j] = collection_id_list[j][10:-1]
                    for j in range(len(collection_title_list)):
                        collection_title_list[j] = collection_title_list[j][49:-16]
                    collection_name = collection_name[0][7:-1]

                    # print(collection_title_list)
                    # print(collection_id_list)
                    # print(collection_name)
                    collection_info_dict = {}
                    for i in range(len(collection_id_list)):
                        collection_info_dict[collection_id_list[i]] = collection_title_list[i]
                    standard_list[i][1] = collection_id_list[0:episode_num]

    return merge_list(standard_list)


# standard_list [[视频id(BV AV与EP),选择集数列表[], 总集数，视频标题，视频类型标签(0: 一般视频(动画综合也包含在其中)，1: 番剧电影,2:分集视频，3:合集视频),模式],...]

def display_result(standard_list):
    if len(standard_list):
        cnt = 0
        print("以下是您选择的项目:")
        for i in range(len(standard_list)):  # 打印视频选择情况
            if standard_list[i][-2] == 1:  # 番剧电影
                tag = "(番剧电影)"
                episode = ""
                if len(standard_list[i][1]) == standard_list[i][2]:
                    episode = "\t全集"
                else:
                    for index in standard_list[i][1]:
                        episode += "\t第" + str(index) + "集"
                print("\t" + str(cnt) + "." + tag + standard_list[i][3] + episode)
                cnt += 1
        for i in range(len(standard_list)):  # 打印视频选择情况
            if standard_list[i][-2] == 2:  # 分集视频
                tag = "(分集视频)"
                episode = ""
                if len(standard_list[i][1]) == standard_list[i][2]:
                    episode = "\t全集"
                else:
                    for index in standard_list[i][1]:
                        episode += "\t第" + str(index) + "集"
                print("\t" + str(cnt) + "." + tag + standard_list[i][3] + episode)
                cnt += 1
        for i in range(len(standard_list)):  # 打印视频选择情况
            if standard_list[i][-2] == 3:  # 合集视频
                tag = "(合集视频)"
                print("\t" + str(cnt) + "." + tag + standard_list[i][3] + "\t共选择" + str(
                    len(standard_list[i][1])) + "集")
                cnt += 1
        for i in range(len(standard_list)):  # 打印视频选择情况
            if standard_list[i][-2] == 0:  # 一般视频
                standard_list[i][1] = [1]  # 普通视频只取第一集
                tag = "(一般视频)"
                print("\t" + str(cnt) + "." + tag + standard_list[i][3])
                cnt += 1


def select(max_index):
    pass
    return max_index
