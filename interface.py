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
# video_id_dict = []  # 最终遍历带入get_video_and_html的列表
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
        if len(key) >= 2 and (key[0:2] == "BV" or key[0:2] == "Bv" or key[0:2] == "bV" or key[0:2] == "bv"):
            identity_flag = 0
            http_id_flag = 1
        elif len(key) >= 2 and (key[0:2] == "AV" or key[0:2] == "Av" or key[0:2] == "aV" or key[0:2] == "av"):
            identity_flag = 0
            http_id_flag = 1
        elif len(key) >= 2 and (key[0:2] == "SS" or key[0:2] == "Ss" or key[0:2] == "sS" or key[0:2] == "ss"):
            identity_flag = 0
            http_id_flag = 1
        elif len(key) >= 2 and (key[0:2] == "EP" or key[0:2] == "Ep" or key[0:2] == "sp" or key[0:2] == "sp"):
            identity_flag = 0
            http_id_flag = 1
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
            ID = ""
            if http_id_flag:  # ID
                ID = key
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
            keyword = key
            config_dict[key].append(identity_flag)
            in_func_dict[keyword] = config_dict[key]

    # 补充默认项
    for key in in_func_dict:
        # 由于补充了identity_flag，因此全空：长度1，半空：长度2，全满：长度3
        if in_func_dict[key][-1] == 0:  # 直接给出URL
            # 以下是处理默认情况的逻辑
            if len(in_func_dict[key]) == 1:  # 全空
                in_func_dict[key] = [default_mode, default_episode_num] + in_func_dict[key]
            elif len(in_func_dict[key]) == 2:  # 半空
                if in_func_dict[key][0] < 0:  # 指定了模式，默认集数
                    in_func_dict[key].insert(1, default_episode_num)
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
    # ID_list 目标格式 [[视频id(BVAV与SSEP)/关键词, 选择集数列表[], 总集数，视频标题，视频类型标签(0: 一般视频，1: 番剧电影), 模式],...]
    # keyword_list 目标格式 [[key,select_enable,mode],...]
    ID_list = []
    keyword_list = []
    for key in in_func_dict:
        if in_func_dict[key][-1] == 0:  # ID模式
            if key[0:2] == "ss" or key[0:2] == "ep":  # 番剧电影ID
                ID_list += [[key, list(range(1, in_func_dict[key][1] + 1)), "unknown", "unknown", 1,
                             in_func_dict[key][0]]]
            else:  # 一般视频ID
                ID_list += [[key, list(range(1, in_func_dict[key][1] + 1)), "unknown", "unknown", 0,
                             in_func_dict[key][0]]]
        if in_func_dict[key][-1] == 1:  # 关键词模式
            keyword_list += [[key, in_func_dict[key][1], in_func_dict[key][0]]]

    # ID_list与keyword_list格式化完成
    # ID_list 符合内核调用规范，可以直接调用 # ID索引由于不能知晓具体有多少集，因此，按照config里面配置的集数操作，没有交互界面
    # print(ID_list)
    # print(keyword_list)

    return [ID_list, keyword_list]


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
    if app_type == "bilibili":
        # 一、普通视频处理
        # 获取搜索页面html，预处理得到原始list
        search_url = "https://search.bilibili.com/all?keyword=" + keyword  # 转化为搜索页面网址
        response = requests.get(search_url, headers=head)
        in_func_id_list = re.findall('href=\"//www.bilibili.com/video/.*?/.*?class=\"bili-video-card__info--tit\"',
                                     response.text)
        in_func_title_list = re.findall(
            'href=\"//www.bilibili.com/video/.*?/.*?class=\"bili-video-card__info--tit\" title=\"(.*?)\"',
            response.text)

        # print(response.text)
        # print(title_list_temp)
        # print(url_list_temp)

        # list处理
        # in_func_id_list处理
        # 二次匹配,并加上"https://"
        for i in range(len(in_func_id_list)):
            in_func_id_list[i] = re.findall("www.bilibili.com/video/.*?/", in_func_id_list[i])[0][23:-1]
        # in_func_title_list处理
        # 将&amp;quot;换为"\""
        for title_id in range(len(in_func_title_list)):
            in_func_title_list[title_id] = in_func_title_list[title_id].replace("&amp;quot;", "\"")

        # print(in_func_id_list)
        # print(in_func_title_list)

        # 二、番剧电影处理
        # 1.分离番剧电影描述信息
        episode_num_list = []
        animation_and_film_id_list = []
        animation_and_film_title_list = []

        animation_and_film_temp_list = re.findall(
            '<a title=\".*?\" class=\"text_ellipsis\" href=\"https://www.bilibili.com/bangumi/play/.*?\" target=\"_blank\"',
            response.text)
        episode_num_list = re.findall('</span></span><span data-v-384b5d39>全(\d*)话</span></div>', response.text)
        # print(animation_and_film_temp_list)

        # 2.再次提取与修整list
        for item in animation_and_film_temp_list:
            animation_and_film_title_list += re.findall("title=\".*?\"", item)
            animation_and_film_id_list += re.findall("href=\"https://www.bilibili.com/bangumi/play/.*?\"", item)
        for i in range(len(animation_and_film_title_list)):
            animation_and_film_title_list[i] = animation_and_film_title_list[i][7:-1]
            animation_and_film_title_list[i] = animation_and_film_title_list[i].replace("&amp;quot;",
                                                                                        "\"")  # 将&amp;quot;换为"\""
        for i in range(len(animation_and_film_id_list)):
            animation_and_film_id_list[i] = animation_and_film_id_list[i][44:-1]
        for i in range(len(episode_num_list)):
            episode_num_list[i] = int(episode_num_list[i])

        # print(episode_num_list)
        # print(animation_and_film_title_list)
        # print(animation_and_film_id_list)
        # 3.合并list并标准化
        animation_and_film_list = []
        # 格式 [ss/ep号,标题，集数]
        # 番剧电影url："https://www.bilibili.com/bangumi/play/"+ss/ep号(第一集)+集数-1
        for i in range(len(animation_and_film_id_list)):
            animation_and_film_list.append(
                [animation_and_film_id_list[i], animation_and_film_title_list[i], episode_num_list[i]])

        # print(animation_and_film_list)

        animation_and_film_list.reverse()
        for video in animation_and_film_list:
            in_func_id_list.insert(0, video[0])
            in_func_title_list.insert(0, video[1])
        animation_and_film_list.reverse()

        selected_video_list = []  # 格式 [[视频id,选择集数列表[],总集数，视频标题，视频类型标签(0:一般视频，1:番剧电影)],...]
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
                    if i > len(animation_and_film_list):
                        title = "(一般视频)" + display_title_list[i - 1]
                        print("\t" + str(i) + "." + title)
                    else:
                        title = "(番剧电影)" + display_title_list[i - 1]
                        print("\t" + str(i) + "." + title)
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
                    if i > len(animation_and_film_list):
                        title = "(一般视频)" + display_title_list[i - 1]
                        print("\t" + str(i) + "." + title)
                    else:
                        title = "(番剧电影)" + display_title_list[i - 1]
                        print("\t" + str(i) + "." + title)
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
            print("退出交互模式")
        # 得到 selected_id_list

        sleep(1)
        for selected_index in selected_id_list:
            if selected_index > len(animation_and_film_id_list):  # 一般视频
                selected_video_list.append(
                    [display_id_list[selected_index - 1], [1], 1, display_title_list[selected_index - 1], 0])
            else:  # 番剧电影
                # animation_and_film_list 格式 [[ss/ep号,标题，集数],...]
                video_id = display_id_list[selected_index - 1]
                temp_index = 0
                for i in range(0, len(animation_and_film_list)):
                    if video_id == animation_and_film_list[i][0]:
                        temp_index = i
                selected_video_list.append(
                    [display_id_list[selected_index - 1], [], animation_and_film_list[temp_index][2],
                     display_title_list[selected_index - 1], 1])
        # 得到番剧电影未选集的 selected_video_list # 目前格式 [[视频id,选择集数列表[],总集数，视频标题，视频类型标签(0:一般视频，1:番剧电影)],...]

        # 番剧电影选集
        if len(selected_video_list) != 0:
            selected_animation_and_film_flag = 0  # 如果选择了番剧电影，则为1
            selected_animation_and_film_title_list = []
            for i in range(len(selected_video_list)):
                if selected_video_list[i][-1] == 1:
                    selected_animation_and_film_flag = 1
                    selected_animation_and_film_title_list.append(selected_video_list[i][3])
            if selected_animation_and_film_flag:
                print("\n您选择的项目中含有" + str(len(selected_animation_and_film_title_list)) + "部番剧电影")

                for i in range(len(selected_video_list)):
                    if selected_video_list[i][-1] == 1:
                        print("标题:" + selected_video_list[i][3])
                        print("总集数:" + str(selected_video_list[i][2]))
                        selected_video_list[i][1].clear()
                        # 合法集数列表
                        in_law_index_list = list(range(1, selected_video_list[i][2] + 1))
                        for j in range(1, len(in_law_index_list) + 1):
                            in_law_index_list[j - 1] = str(in_law_index_list[j - 1])

                        select_result = input(
                            "请输入您选择的集数序号,输入exit退出选择,输入delete重新选择，输入all选择全集:")
                        while select_result != "exit":
                            if select_result in in_law_index_list:  # 排除特殊字符
                                selected_video_list[i][1].append(eval(select_result))
                                select_result = input("请输入您选择的集数序号:")
                            elif select_result == "delete":
                                selected_video_list[i][1].clear()
                                print("重新选择")
                                select_result = input(
                                    "请输入您选择的集数序号,输入exit退出选择,输入delete重新选择，输入all选择全集:")
                            elif select_result == "all":
                                for j in range(1, selected_video_list[i][2] + 1):
                                    selected_video_list[i][1].append(j)
                                print("选择全集")
                                break
                            else:
                                print("非法输入")
                                select_result = input("请输入您选择的集数序号:")
                        if len(selected_video_list[i][1]) == 0:
                            print("您没有选择集,该项目将会被移除")
                        selected_video_list[i][1] = list(set(selected_video_list[i][1]))  # 去重
                        selected_video_list[i][1].sort()  # 排序
                        print("")
        # selected_video_list处理，以满足通用接口标准
        # 删除选集为空的项目
        iter_index_list = list(range(len(selected_video_list)))
        iter_index_list.reverse()  # 从后向前删除，防止数组索引越位
        for i in iter_index_list:
            if len(selected_video_list[i][1]) == 0:
                selected_video_list.pop(i)

        # 加入mode变量
        for i in range(len(selected_video_list)):
            selected_video_list[i].append(mode)
        # print(selected_video_list)
        # 格式(内核接口标准) [[视频id(BV AV与SS EP), 选择集数列表[], 总集数，视频标题，视频类型标签(0: 一般视频，1: 番剧电影), 模式],...]
        # 打印选择结果
        if len(selected_video_list) != 0:
            if select_enable == 0:
                print("关键词\"" + keyword + "\"检索，非交互模式，以下是默认选择的项目:")
            else:
                print("关键词\"" + keyword + "\"检索，交互模式，以下是您选择的项目:")
            cnt = 1
            for i in range(len(selected_video_list)):
                if selected_video_list[i][-2] == 1:
                    select_episode = ""
                    if len(selected_video_list[i][1]) == selected_video_list[i][2]:
                        select_episode = "全集"
                    else:
                        for j in selected_video_list[i][1]:
                            select_episode += "第" + str(j) + "集\s"

                    title = "(番剧电影)" + selected_video_list[i][3]
                    print("\t" + str(cnt) + "." + title + select_episode)
                    cnt += 1
            for i in range(len(selected_video_list)):
                if selected_video_list[i][-2] == 0:
                    title = "(一般视频)" + selected_video_list[i][3]
                    print("\t" + str(cnt) + "." + title)
                    cnt += 1
            print("")
        else:
            print("关键词\"" + keyword + "\"检索，交互模式，您没有选择项目\n")

        return selected_video_list


# 输入: 满足内核标准输入的list
# 输出：不含重复项的满足内核标准的list
# 过程：判断冲突，合并
def merge_list(standard_list):
    pass
