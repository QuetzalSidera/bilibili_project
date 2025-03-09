from bilibili_lib import *
import time

def user_input_interface(config_dict):
    in_func_dict = {}
    keyword_list = []
    ID_list = []
    for key in config_dict:
        # 1.字符串匹配确定identity_flag
        # ID
        ID_head_list = ["BV", "Bv", "bV", "bv", "AV", "Av", "aV", "av", "SS", "Ss", "sS", "ss", "EP", "Ep", "eP", "ep"]
        url_head_list = ["www.", "WWW.", "https://", "http://"]
        if key[0:2] in ID_head_list:
            result = ID_process(key)
            ID = result[0]
            key_type = result[1]
        elif (key[0:4] in url_head_list) or (key[0:7] in url_head_list) or (key[0:8] in url_head_list):
            result = from_url_get_processed_ID(key)
            ID = result[0]
            key_type = result[1]
        else:
            ID = key
            key_type = "keyword"
        in_func_dict[ID] = config_dict[key] + [key_type]
    # 默认处理
    for key in in_func_dict:
        if in_func_dict[key][-1] == "keyword":  # keyword
            if len(in_func_dict[key]) == 1:  # 全默认
                in_func_dict[key] = [default_mode, default_select_enable, in_func_dict[key][-1]]
            elif len(in_func_dict[key]) == 2:  # 半空
                if in_func_dict[key][0] >= 0:  # 指定select_enable默认模式
                    in_func_dict[key] = [default_mode, in_func_dict[key][0], in_func_dict[key][-1]]
                else:  # 默认select_enable指定模式
                    in_func_dict[key] = [in_func_dict[key][0], default_select_enable, in_func_dict[key][-1]]
            elif len(in_func_dict[key]) == 3:  # 全满
                in_func_dict[key] = [in_func_dict[key][0], in_func_dict[key][1],
                                     in_func_dict[key][-1]]
        else:  # ID
            if len(in_func_dict[key]) == 1:  # 全默认
                if default_select_episode_enable == 0 or default_select_episode_enable == 1:  # 默认选集
                    in_func_dict[key] = [default_mode, list(range(1, default_episode_num + 1)), in_func_dict[key][-1]]
                else:
                    in_func_dict[key] = [default_mode, [], in_func_dict[key][-1]]
            elif len(in_func_dict[key]) == 2:  # 半空
                if in_func_dict[key][0] >= 0:  # 指定集数默认模式
                    in_func_dict[key] = [default_mode, list(range(1, in_func_dict[key][0] + 1)), in_func_dict[key][-1]]
                else:  # 指定模式默认集数
                    if default_select_episode_enable == 0 or default_select_episode_enable == 1:  # 默认选集
                        in_func_dict[key] = [in_func_dict[key][0], list(range(1, default_episode_num + 1)),
                                             in_func_dict[key][-1]]
                    else:
                        in_func_dict[key] = [in_func_dict[key][0], [], in_func_dict[key][-1]]
            elif len(in_func_dict[key]) == 3:  # 全满
                in_func_dict[key] = [in_func_dict[key][0], list(range(1, in_func_dict[key][1] + 1)),
                                     in_func_dict[key][-1]]
        # in_func_dict key:[mode,select_enable?/集数列表,key_type]
    for key in in_func_dict:
        if in_func_dict[key][-1] == "keyword":
            keyword_list.append([key, in_func_dict[key][0], in_func_dict[key][1]])
            # [[key,mode,select_enable],...]
        else:
            ID_list.append([key] + in_func_dict[key])
            # [[key,mode,episode],...]

    return [ID_list, keyword_list]


def from_url_get_processed_ID(url):
    in_func_result = re.findall("/(BV|Bv|bV|bv)(([A-Z]|[a-z]|[0-9])+)", url)
    if len(in_func_result):
        ID = "BV" + in_func_result[0][1]  # BV
        id_type = "BVid"
    else:
        in_func_result = re.findall("/(AV|Av|aV|av)(([A-Z]|[a-z]|[0-9])+)", url)
        if len(in_func_result):
            ID = "AV" + in_func_result[0][1]  # AV
            id_type = "AVid"
        else:
            in_func_result = re.findall("/(SS|Ss|sS|ss)(([A-Z]|[a-z]|[0-9])+)", url)
            if len(in_func_result):
                ID = "ss" + in_func_result[0][1]  # ss
                id_type = "ssid"
            else:
                in_func_result = re.findall("/(EP|Ep|eP|ep)(([A-Z]|[a-z]|[0-9])+)", url)
                if len(in_func_result):
                    ID = "ep" + in_func_result[0][1]  # ep
                    id_type = "epid"
                else:
                    ID = "unknown"
                    id_type = "unknown"
    return [ID, id_type]


def ID_process(ID):
    in_func_result = re.findall("(BV|Bv|bV|bv)(([A-Z]|[a-z]|[0-9])+)", ID)
    if len(in_func_result):
        ID = "BV" + in_func_result[0][1]  # BV
        id_type = "BVid"
    else:
        in_func_result = re.findall("(AV|Av|aV|av)(([A-Z]|[a-z]|[0-9])+)", ID)
        if len(in_func_result):
            ID = "AV" + in_func_result[0][1]  # AV
            id_type = "AVid"
        else:
            in_func_result = re.findall("(SS|Ss|sS|ss)(([A-Z]|[a-z]|[0-9])+)", ID)
            if len(in_func_result):
                ID = "ss" + in_func_result[0][1]  # ss
                id_type = "ssid"
            else:
                in_func_result = re.findall("(EP|Ep|eP|ep)(([A-Z]|[a-z]|[0-9])+)", ID)
                if len(in_func_result):
                    ID = "ep" + in_func_result[0][1]  # ep
                    id_type = "epid"
                else:
                    ID = "unknown"
                    id_type = "unknown"
    return [ID, id_type]


# info格式
# 普通视频：[ID号,标题,视频类型标签=ordinary video] atmo
# 分集视频： [ID号,标题，分集id列表[数字]，分集标题列表[]，视频类型标签=episode video] atmo
# 番剧电影合集（ss检索得到）：[ID号,标题，分集id列表[ep号]，分集标题列表[]，视频类型标签=bangumi set]
# 单集番剧电影或贴片（BV或ep号检索得到）：[ID号,标题,视频类型标签=single bangumi]
# 番剧电影贴片（BV或ep号检索得到）：[ID号,标题,视频类型标签=bangumi append]
# 合集视频：[ID号,标题，atmo_list[atmo]，视频类型标签=ordinary set]
# 复杂合集：[ID号，标题,分集列表section_list[section]，视频类型标签=complex set]
# section[]格式： [section_id,标题，atmo_list[atmo]，视频类型标签=ordinary set]
# atmo[]格式： [ID号,标题，分集id列表[]，分集标题列表[]，视频类型标签=ordinary video或episode video] atom原子

# info_list=[info1,info2]
# 输出为ID_list同类列表 [[key,mode,episode],...]
# keyword_list 格式：[[key,mode,select_enable],...]
# 其中 episode可以为空（自选集），或者直接默认选集
def search_interface(keyword_list):
    # keyword_list 格式： # [[key,mode,select_enable],...]
    # info_dict格式：keyword:info_list
    info_dict = {}
    in_func_list = []
    # 格式：[[key,mode,episode],...]与ID_list一致
    for item in keyword_list:
        keyword = item[0]
        info_dict[keyword] = sort_info_list(search_in_bilibili(keyword))
    for item in keyword_list:
        keyword = item[0]
        mode = item[1]
        select_enable = item[2]
        info_list = info_dict[keyword]
        if select_enable == 1:
            selected_index_list = []
            selected_id_list = []
            if len(info_list) > display_num and display_num != -1:
                display_list = info_list[0:display_num]
                max_index = display_num
                limited_display_flag = 1
            else:
                display_list = info_list
                max_index = len(info_list)
                limited_display_flag = 0
            if limited_display_flag == 1:
                # os.system('clear')
                print("关键词:\"" + keyword + "\"检索结果如下，共" + str(len(info_list)) + "个，仅展示前" + str(
                    len(display_list)) + "个:")
                display_info_list(display_list)
                in_law_index_list = list(range(1, max_index + 1))
                for i in range(len(in_law_index_list)):
                    in_law_index_list[i] = str(in_law_index_list[i])
                input_result = input(
                    "请输入您选择的视频序号,输入exit退出选择,输入delete重新选择，输入display all展示所有结果:")
                while input_result != "exit":
                    if input_result in in_law_index_list:  # 排除特殊字符
                        selected_index_list.append(eval(input_result))
                        selected_id_list.append(display_list[eval(input_result) - 1][0])
                        # os.system('clear')
                        print("关键词:\"" + keyword + "\"检索结果如下，共" + str(len(info_list)) + "个，仅展示前" + str(
                            len(display_list)) + "个:")
                        display_info_list(display_list, selected_id_list)
                        input_result = input("请输入您选择的视频序号:")
                    elif input_result == "display all":
                        print("\n展示所有项目\n")
                        display_list = info_list
                        max_index = len(info_list)
                        limited_display_flag = 0
                        selected_index_list.clear()
                        selected_id_list.clear()
                        time.sleep(0.6)
                        break
                    elif input_result == "delete":  # 输入delete重新选择
                        selected_index_list.clear()
                        selected_id_list.clear()
                        print("重新选择")
                        time.sleep(0.6)
                        # os.system('clear')
                        print("关键词:\"" + keyword + "\"检索结果如下，共" + str(len(info_list)) + "个，仅展示前" + str(
                            len(display_list)) + "个:")
                        display_info_list(display_list, selected_id_list)
                        input_result = input(
                            "请输入您选择的视频序号,输入exit退出选择,输入delete重新选择，输入display all展示所有结果:")
                    else:
                        print("非法输入")
                        time.sleep(0.6)
                        # os.system('clear')
                        print("关键词:\"" + keyword + "\"检索结果如下，共" + str(len(info_list)) + "个，仅展示前" + str(
                            len(display_list)) + "个:")
                        display_info_list(display_list, selected_id_list)
                        input_result = input("请输入您选择的视频序号:")

            if limited_display_flag == 0:
                # os.system('clear')
                print("关键词:\"" + keyword + "\"检索结果如下，共:" + str(len(info_list)) + "个")
                display_info_list(display_list)
                in_law_index_list = list(range(1, max_index + 1))
                for i in range(len(in_law_index_list)):
                    in_law_index_list[i] = str(in_law_index_list[i])
                input_result = input("请输入您选择的视频序号,输入exit退出选择,输入delete重新选择:")
                while input_result != "exit":
                    if input_result in in_law_index_list:  # 排除特殊字符
                        selected_index_list.append(eval(input_result))
                        selected_id_list.append(display_list[eval(input_result) - 1][0])
                        # os.system('clear')
                        print("关键词:\"" + keyword + "\"检索结果如下，共:" + str(len(info_list)) + "个")
                        display_info_list(display_list, selected_id_list)
                        input_result = input("请输入您选择的视频序号:")
                    elif input_result == "delete":
                        selected_index_list.clear()
                        selected_id_list.clear()
                        print("重新选择")
                        time.sleep(0.6)
                        # os.system('clear')
                        print("关键词:\"" + keyword + "\"检索结果如下，共:" + str(len(info_list)) + "个")
                        display_info_list(display_list, selected_id_list)
                        input_result = input("请输入您选择的视频序号,输入exit退出选择,输入delete重新选择:")
                    else:
                        print("非法输入")
                        time.sleep(0.6)
                        # os.system('clear')
                        print("关键词:\"" + keyword + "\"检索结果如下，共:" + str(len(info_list)) + "个")
                        display_info_list(display_list, selected_id_list)
                        input_result = input("请输入您选择的视频序号:")
            print("关键词\"" + keyword + "\"选择结束")
            time.sleep(0.6)
            # os.system('clear')
            for index in selected_index_list:
                in_func_list.append([display_list[index - 1][0], mode, []])
        else:
            selected_list = info_dict[keyword][0:default_number_of_videos]
            for i in range(len(selected_list)):
                in_func_list.append([selected_list[i][0], mode, []])
            print("关键词:\"" + keyword + "\"默认选择前" + str(default_number_of_videos) + "项")
            display_info_list(selected_list)
        # 默认选集
        # 等于0时ID，url与关键词默认取前max{default_episode_num,总集数}集；等于1时ID，url默认选集但关键词进入选集交互界面,等于2时ID与url，关键词均会进入选集交互界面；
        if default_select_episode_enable == 0:
            for i in range(len(in_func_list)):
                in_func_list[i][2] = list(range(1, default_episode_num + 1))
    return in_func_list


# info格式
# 番剧电影合集（ss检索得到）：[ID号,标题，分集id列表[ep号]，分集标题列表[]，视频类型标签=bangumi set]
# 单集番剧电影或贴片（BV或ep号检索得到）：[ID号,标题,视频类型标签=single bangumi]
# 番剧电影贴片（BV或ep号检索得到）：[ID号,标题,视频类型标签=bangumi append]

# 普通视频：[ID号,标题,视频类型标签=ordinary video] atmo
# 分集视频： [ID号,标题，分集id列表[数字]，分集标题列表[]，视频类型标签=episode video] atmo
# 合集视频：[ID号,标题，atmo_list[atmo]，视频类型标签=ordinary set]
# 复杂合集：[ID号，标题,分集列表section_list[section]，视频类型标签=complex set]

# section[]格式： [section_id,标题，atmo_list[atmo]，视频类型标签=ordinary set]
# atmo[]格式： [ID号,标题，分集id列表[]，分集标题列表[]，视频类型标签=ordinary video或episode video] atom原子

# selected_list格式：[[key,mode,episode],...]
# 其中，episode可能为空表，也可能是数字列表，并且没有限制最大集数，默认选集已经结束

# result格式
# [ID号，标题, selected_id_list[],selected_title_list[], mode, 视频类型标签=bangumi set]
# [ID号，标题, mode, 视频类型标签=single bangumi]
# [ID号，标题, mode, 视频类型标签=bangumi append]

# [ID号，标题,  mode, 视频类型标签=ordinary video]
# [ID号，标题, selected_id_list[数字],selected_title_list[], mode, 视频类型标签=episode video]
# [ID号，标题, atmo_list[], mode, 视频类型标签=ordinary set]
# [ID号，标题, atmo_list[], mode, 视频类型标签=complex set]
# atmo_list[]中atmo格式和ordinary video与episode video的result格式相同

def episode_select_interface(selected_list):
    result_list = []
    # 格式：[ID号，标题，选择集数列表[]，分集标题列表[],mode，视频类型标签=bangumi set/episode video]
    # [ID号，标题，mode，视频类型标签=single bangumi/bangumi append/ordinary video]
    for i in range(len(selected_list)):
        result = []
        id = selected_list[i][0]
        id_type = ID_process(id)[1]
        info = []
        # print(id)
        # print(id_type)
        # print(selected_list)
        if id_type == "BVid" or id_type == "AVid":
            info = from_BVAVid_get_info(id)
        elif id_type == "ssid" or id_type == "epid":
            info = from_ssepid_get_info(id, id_type)
        else:
            print("\033[91mid type error in function\"episode_select_interface\":\033[0m" + id + ",", selected_list)
            return
        video_type = info[-1]
        if video_type == "bangumi set":
            if len(selected_list[i][2]) == 0:  # 未默认选集
                select_return = select_interface(info, "bangumi set")
                result = [info[0], info[1], select_return[0],
                          select_return[1], selected_list[i][1], info[-1]]
            else:
                episode_id_list = []
                episode_title_list = []
                for index in selected_list[i][2]:
                    if index <= len(info[2]):
                        episode_id_list.append(info[2][index - 1])
                        episode_title_list.append(info[3][index - 1])
                episode_id_list = list(set(episode_id_list))
                episode_title_list = list(set(episode_title_list))
                episode_id_list.sort()
                result = [info[0], info[1], episode_id_list, episode_title_list, selected_list[i][1], info[-1]]
        elif video_type == "single bangumi":
            result = [info[0], info[1], selected_list[i][1], info[-1]]
        elif video_type == "bangumi append":
            result = [info[0], info[1], selected_list[i][1], info[-1]]
        elif video_type == "ordinary video":
            result = [info[0], info[1], selected_list[i][1], info[-1]]
        elif video_type == "episode video":
            if len(selected_list[i][2]) == 0:  # 未默认选集
                # 分集视频： [ID号,标题，分集id列表[数字]，分集标题列表[]，视频类型标签=episode video] atmo
                select_return = select_interface(info, "episode video")
                result = [info[0], info[1], select_return[0], select_return[1], selected_list[i][1], info[-1]]
            else:
                episode_id_list = []
                episode_title_list = []
                for index in selected_list[i][2]:
                    if index <= len(info[2]):
                        episode_id_list.append(info[2][index - 1])
                        episode_title_list.append(info[3][index - 1])
                episode_id_list = list(set(episode_id_list))
                episode_title_list = list(set(episode_title_list))
                episode_id_list.sort()
                result = [info[0], info[1], episode_id_list, episode_title_list, selected_list[i][1], info[-1]]
        elif video_type == "ordinary set":
            set_preselected_obj = "none"
            # 查找在video_config中指定的合集项目，作为提前选择的项目
            atmo_list = info[2]
            for atmo in atmo_list:
                atmo_id = atmo[0]
                if atmo_id == id:
                    set_preselected_obj = atmo
                    break
            if len(selected_list[i][2]) == 0:  # 未默认选集
                selected_atmo_list = select_interface(info, "ordinary set", set_preselected_obj)
            else:
                # 合集视频：[ID号,标题，atmo_list[atmo]，视频类型标签=ordinary set]
                atmo_list = info[2]
                selected_atmo_list = []
                for index in selected_list[i][2]:
                    if index <= len(atmo_list):
                        selected_atmo_list.append(atmo_list[index - 1])
            if set_preselected_obj != "none":
                selected_atmo_list.append(set_preselected_obj)
            else:
                print(info[
                          0] + "\033[93mset preselected obj\"" + id + "\"not found warning in function\"episode_select_interface\",\"ordinary set\"\033[0m")
                # [ID号，标题,  mode, 视频类型标签=ordinary video]
                # [ID号，标题, selected_id_list[数字],selected_title_list[], mode, 视频类型标签=episode video]
                # [ID号，标题, atmo_list[], mode, 视频类型标签=ordinary set]
                # [ID号，标题, atmo_list[], mode, 视频类型标签=complex set]
                # atmo_list[]中atmo格式和ordinary video与episode video的result格式相同
            new_atmo_list = []
            for j in range(len(selected_atmo_list)):  # 再选分集视频
                atmo = selected_atmo_list[j]
                if atmo[-1] == "ordinary video":
                    new_atmo_list.append([atmo[0], atmo[1], selected_list[i][1], atmo[-1]])
                    # [ID号，标题,  mode, 视频类型标签=ordinary video]
                elif atmo[-1] == "episode video":
                    select_return = select_interface(atmo, "episode video")
                    new_atmo_list.append(
                        [atmo[0], atmo[1], select_return[0], select_return[1], selected_list[i][1], atmo[-1]])
                    # print("合集《"+info[1]+"》中选择的视频"+atmo[1]+"为分集视频,共"+str(len(atmo[2]))+"集")
                else:
                    print(
                        "\033[91mtype of atmo in set error in function\"episode_select_interface\",\"ordinary set\":\033[0m",
                        atmo)
                    return
            result = [info[0], info[1], new_atmo_list, selected_list[i][1], info[-1]]
        elif video_type == "complex set":
            # 普通视频：[ID号,标题,视频类型标签=ordinary video] atmo
            # 分集视频： [ID号,标题，分集id列表[数字]，分集标题列表[]，视频类型标签=episode video] atmo
            # 复杂合集：[ID号，标题,分集列表section_list[section]，视频类型标签=complex set]
            # 查找在video_config中指定的合集项目，作为提前选择的项目
            set_preselected_obj = "none"
            unfolded_info = complex_set_unfold(info)
            atmo_list = unfolded_info[2]
            for atmo in atmo_list:
                atmo_id = atmo[0]
                if atmo_id == id:
                    set_preselected_obj = atmo
                    break
            if len(selected_list[i][2]) == 0:  # 未默认选集
                selected_atmo_list = select_interface(info, "complex set", set_preselected_obj)
            else:
                atmo_list = unfolded_info[2]
                selected_atmo_list = []
                for index in selected_list[i][2]:
                    if index <= len(atmo_list):
                        selected_atmo_list.append(atmo_list[index - 1])
            if set_preselected_obj != "none":
                selected_atmo_list.append(set_preselected_obj)
            else:
                print(info[
                          0] + "\033[93mset preselected obj\"" + id + "\"not found warning in function\"episode_select_interface\",\"complex set\"\033[0m")
                # [ID号，标题,  mode, 视频类型标签=ordinary video]
                # [ID号，标题, selected_id_list[数字],selected_title_list[], mode, 视频类型标签=episode video]
                # [ID号，标题, atmo_list[], mode, 视频类型标签=ordinary set]
                # [ID号，标题, atmo_list[], mode, 视频类型标签=complex set]
                # atmo_list[]中atmo格式和ordinary video与episode video的result格式相同
            new_atmo_list = []
            for j in range(len(selected_atmo_list)):  # 再选分集视频
                atmo = selected_atmo_list[j]
                if atmo[-1] == "ordinary video":
                    new_atmo_list.append([atmo[0], atmo[1], selected_list[i][1], atmo[-1]])
                    # [ID号，标题,  mode, 视频类型标签=ordinary video]
                elif atmo[-1] == "episode video":
                    select_return = select_interface(atmo, "episode video")
                    new_atmo_list.append(
                        [atmo[0], atmo[1], select_return[0], select_return[1], selected_list[i][1], atmo[-1]])
                    # print("合集《"+info[1]+"》中选择的视频"+atmo[1]+"为分集视频,共"+str(len(atmo[2]))+"集")
                else:
                    print(
                        "\033[91mtype of atmo in set error in function\"episode_select_interface\",\"complex set\"\033[0m",
                        atmo)
                    return
            result = [info[0], info[1], new_atmo_list, selected_list[i][1], info[-1]]
        else:
            print("\033[91mtype of video error in function\"episode_select_interface\"\033[0m", info)
            return
        result_list.append(result)
    return result_list


# info格式
# 番剧电影合集（ss检索得到）：[ID号,标题，分集id列表[ep号]，分集标题列表[]，视频类型标签=bangumi set]
# 单集番剧电影或贴片（BV或ep号检索得到）：[ID号,标题,视频类型标签=single bangumi]
# 番剧电影贴片（BV或ep号检索得到）：[ID号,标题,视频类型标签=bangumi append]

# 普通视频：[ID号,标题,视频类型标签=ordinary video] atmo
# 分集视频： [ID号,标题，分集id列表[数字]，分集标题列表[]，视频类型标签=episode video] atmo
# 合集视频：[ID号,标题，atmo_list[atmo]，视频类型标签=ordinary set]
# 复杂合集：[ID号，标题,分集列表section_list[section]，视频类型标签=complex set]
# section[]格式： [section_id,标题，atmo_list[atmo]，视频类型标签=ordinary set]
# atmo[]格式： [ID号,标题，分集id列表[]，分集标题列表[]，视频类型标签=ordinary video或episode video] atom原子
def select_interface(info, video_type, preselected_obj="none"):
    if video_type == "bangumi set" or video_type == "episode video":
        if video_type == "bangumi set":
            type_tag = "番剧"
        elif video_type == "episode video":
            type_tag = "分集视频"
        else:
            print("\033[91mtype of video error in function\"select_interface\"\033[0m")
            return
        title = info[1]
        episode_id_info_list = info[2]
        episode_title_info_list = info[3]
        selected_index_list = []
        episode_id_list = []
        episode_title_list = []
        print(type_tag + "《" + title + "》共" + str(len(episode_id_info_list)) + "集:")
        index = 1
        for j in range(len(episode_title_info_list)):
            print("\t" + str(index) + "." + episode_title_info_list[j])
            index += 1
        in_law_index_list = list(range(1, len(episode_id_info_list) + 1))
        for j in range(len(in_law_index_list)):
            in_law_index_list[j] = str(in_law_index_list[j])
        input_result = input("请输入您选择的序号,输入exit退出选择,输入select all选择全集,输入delete重新选择:")
        while input_result != "exit":
            if input_result in in_law_index_list:  # 排除特殊字符
                selected_index_list.append(eval(input_result))
                input_result = input("请输入您选择的视频序号:")
            elif input_result == "delete":
                selected_index_list.clear()
                print("重新选择")
                input_result = input("请输入您选择的视频序号,输入exit退出选择,输入delete重新选择:")
            elif input_result == "select all":
                selected_index_list = list(range(1, len(episode_id_info_list) + 1))
                print("选择全集")
                break
            else:
                print("非法输入")
                input_result = input("请输入您选择的视频序号:")
        for index in selected_index_list:
            episode_id_list.append(episode_id_info_list[index - 1])
            episode_title_list.append(episode_title_info_list[index - 1])
        episode_id_list = list(set(episode_id_list))
        episode_title_list = list(set(episode_title_list))
        episode_id_list.sort()
        return [episode_id_list, episode_title_list]
    elif video_type == "ordinary set":
        # 合集视频：[ID号,标题，atmo_list[atmo]，视频类型标签=ordinary set]
        title = info[1]
        atmo_list = info[2]
        selected_index_list = []
        selected_atmo_list = []
        # preselected_obj
        # 普通视频：[ID号,标题,视频类型标签=ordinary video] atmo
        # 分集视频： [ID号,标题，分集id列表[数字]，分集标题列表[]，视频类型标签=episode video] atmo
        if preselected_obj == "none":
            print("合集《" + title + "》" + "共" + str(len(atmo_list)) + "集:")
        else:
            if preselected_obj[-1] == "episode video":
                video_type_tag = "(分集视频)"
            elif preselected_obj[-1] == "ordinary video":
                video_type_tag = "(一般视频)"
            else:
                video_type_tag = ""
                print("\033[91mtype of preselected_obj error in function\"select_interface\",\"ordinary set\":\033[0m",
                      preselected_obj)
            print("合集《" + title + "》" + "共" + str(len(atmo_list)) + "集,默认已经选择" + video_type_tag + "\"" +
                  preselected_obj[1] + "\":")
        for j in range(len(atmo_list)):
            atmo = atmo_list[j]
            # atmo格式
            # [ID号,标题，分集id列表[]，分集标题列表[]，视频类型标签=episode video]
            # [ID号,标题，视频类型标签=ordinary video]
            if atmo[-1] == "episode video":
                type_tag = "(分集视频)"
                episode_tag = "(共" + str(len(atmo[2])) + "集)"
            elif atmo[-1] == "ordinary video":
                type_tag = "(一般视频)"
                episode_tag = ""
            else:
                print("\033[91mtype of atmo in set error in function\"select_interface\",\"ordinary set\"\033[0m", atmo)
                return
            print("\t" + str(j + 1) + "." + type_tag + episode_tag + atmo[1])
        in_law_index_list = list(range(1, len(atmo_list) + 1))
        for j in range(len(in_law_index_list)):
            in_law_index_list[j] = str(in_law_index_list[j])
        input_result = input("请输入您选择的序号,输入exit退出选择,输入select all选择全集,输入delete重新选择:")
        while input_result != "exit":
            if input_result in in_law_index_list:  # 排除特殊字符
                selected_index_list.append(eval(input_result))
                input_result = input("请输入您选择的视频序号:")
            elif input_result == "delete":
                selected_index_list.clear()
                print("重新选择")
                input_result = input("请输入您选择的视频序号,输入exit退出选择,输入delete重新选择:")
            elif input_result == "select all":
                selected_index_list = list(range(1, len(atmo_list) + 1))
                print("选择全集")
                break
            else:
                print("非法输入")
                input_result = input("请输入您选择的视频序号:")
        for index in selected_index_list:
            selected_atmo_list.append(atmo_list[index - 1])
        return selected_atmo_list
    elif video_type == "complex set":
        # 复杂合集：[ID号，标题,分集列表section_list[section]，视频类型标签=complex set]
        # section[]格式： [section_id,标题，atmo_list[atmo]，视频类型标签=ordinary set]
        # atmo[]格式： [ID号,标题，分集id列表[]，分集标题列表[]，视频类型标签=ordinary video或episode video] atom原子
        selected_index_list = []
        selected_atmo_list = []
        title = info[1]
        section_list = info[2]
        index = 1
        if preselected_obj == "none":
            print("含分区合集《" + title + "》" + "共" + str(len(section_list)) + "个分区:")
        else:
            if preselected_obj[-1] == "episode video":
                video_type_tag = "(分集视频)"
            elif preselected_obj[-1] == "ordinary video":
                video_type_tag = "(一般视频)"
            else:
                video_type_tag = ""
                print("\033[91mtype of preselected_obj error in function\"select_interface\",\"complex set\":\033[0m",
                      preselected_obj)
            print("多合集《" + title + "》" + "共" + str(
                len(section_list)) + "个分区,默认已经选择" + video_type_tag + "\"" +
                  preselected_obj[1] + "\":")
        for i in range(len(section_list)):
            section = section_list[i]
            print("\t分区标题:" + section[1])
            for j in range(len(section[2])):
                atmo = section[2][j]
                atmo_title = atmo[1]
                if atmo[-1] == "ordinary video":
                    type_tag = "(一般视频)"
                    episode_tag = ""
                elif atmo[-1] == "episode video":
                    type_tag = "(分集视频)"
                    episode_tag = "(共" + str(len(atmo[2])) + "集)"
                else:
                    print("\033[91mtype of atmo in set error in function\"select_interface\",\"complex set\":\033[0m",
                          atmo)
                    return
                print("\t\t" + str(index) + "." + type_tag + atmo_title + episode_tag)
                index += 1
        new_info = complex_set_unfold(info)
        # 合集视频：[ID号,标题，atmo_list[atmo]，视频类型标签=ordinary set]
        atmo_list = new_info[2]
        in_law_index_list = list(range(1, len(atmo_list) + 1))
        for j in range(len(in_law_index_list)):
            in_law_index_list[j] = str(in_law_index_list[j])
        input_result = input("请输入您选择的序号,输入exit退出选择,输入select all选择全集,输入delete重新选择:")
        while input_result != "exit":
            if input_result in in_law_index_list:  # 排除特殊字符
                selected_index_list.append(eval(input_result))
                input_result = input("请输入您选择的视频序号:")
            elif input_result == "delete":
                selected_index_list.clear()
                print("重新选择")
                input_result = input("请输入您选择的视频序号,输入exit退出选择,输入delete重新选择:")
            elif input_result == "select all":
                selected_index_list = list(range(1, len(atmo_list) + 1))
                print("选择全集")
                break
            else:
                print("非法输入")
                input_result = input("请输入您选择的视频序号:")
        for index in selected_index_list:
            selected_atmo_list.append(atmo_list[index - 1])
        return selected_atmo_list


# result格式
# [ID号，标题, selected_id_list[],selected_title_list[], mode, 视频类型标签=bangumi set]
# [ID号，标题, mode, 视频类型标签=single bangumi]
# [ID号，标题, mode, 视频类型标签=bangumi append]

# [ID号，标题,  mode, 视频类型标签=ordinary video]
# [ID号，标题, selected_id_list[数字],selected_title_list[], mode, 视频类型标签=episode video]
# [ID号，标题, atmo_list[], mode, 视频类型标签=ordinary set]
# [ID号，标题, atmo_list[], mode, 视频类型标签=complex set]
# atmo_list[]中atmo格式和ordinary video与episode video的result格式相同
def display_result_list(result_list):
    if len(result_list):
        print_flag = 0
        index = 1
        print("以下是你的选择结果:")
        for result in result_list:
            if result[-1] == "bangumi set":
                if result[-2] != -6:  # 不是被删去的重复项目
                    type_tag = "(番剧电影)"
                    episode_tag = "(共" + str(len(result[2])) + "集)"
                    print("\t" + str(index) + "." + type_tag + result[1] + episode_tag)
                    index += 1
                    print_flag = 1
        for result in result_list:
            if result[-1] == "single bangumi":
                if result[-2] != -6:  # 不是被删去的重复项目
                    type_tag = "(单集番剧)"
                    print("\t" + str(index) + "." + type_tag + result[1])
                    index += 1
                    print_flag = 1
        for result in result_list:
            if result[-1] == "bangumi append":
                if result[-2] != -6:  # 不是被删去的重复项目
                    type_tag = "(番剧电影PV)"
                    print("\t" + str(index) + "." + type_tag + result[1])
                    index += 1
                    print_flag = 1
        for result in result_list:
            if result[-1] == "ordinary video":
                if result[-2] != -6:
                    type_tag = "(一般视频)"
                    print("\t" + str(index) + "." + type_tag + result[1])
                    index += 1
                    print_flag = 1
        for result in result_list:
            if result[-1] == "episode video":
                if result[-2] != -6:  # 不是被删去的重复项目
                    type_tag = "(分集视频)"
                    episode_tag = "(共" + str(len(result[2])) + "集)"
                    print("\t" + str(index) + "." + type_tag + result[1] + episode_tag)
                    index += 1
                    print_flag = 1
        index = 1
        if print_flag == 1:
            print("")
            print_flag = 0
        for result in result_list:
            if result[-1] == "ordinary set" or result[-1] == "complex set":
                if result[-1] == "ordinary set":
                    type_tag = "(合集)"
                else:
                    type_tag = "(含分区合集)"
                print("\t" + type_tag + "《" + result[1] + "》:")
                for i in range(len(result[2])):
                    atmo = result[2][i]
                    if atmo[-1] == "episode video":
                        if atmo[-2] != -6:  # 不是被删去的重复项目
                            atmo_title = atmo[1]
                            atmo_type_tag = "(分集视频)"
                            atmo_episode_tag = "(共" + str(len(atmo[2])) + "集)"
                            print("\t\t" + str(index) + "." + atmo_type_tag + atmo_title + atmo_episode_tag)
                            index += 1
                            print_flag = 1
                for i in range(len(result[2])):
                    atmo = result[2][i]
                    if atmo[-2] != -6:  # 不是被删去的重复项目
                        if atmo[-1] == "ordinary video":
                            atmo_title = atmo[1]
                            atmo_type_tag = "(一般视频)"
                            print("\t\t" + str(index) + "." + atmo_type_tag + atmo_title)
                            index += 1
                            print_flag = 1
            index = 1
        if print_flag == 1:
            print("")
            print_flag = 0
    else:
        print("你没有选择任何项目")


