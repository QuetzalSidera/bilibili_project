# 本文件在用户接口与程序内核之间进行过渡
import re


# #输入 video_config={}
# video_config格式
# BV号: [模式，集数]
# url: [模式，集数]
# 关键词: [模式，default_select?](关键词检索若遇到分集不能爬去所有集数，只能爬取第一集)
# 输出universal_video_url_dict={}
# universal_video_url_dict格式
# key:[mode,episode/default_select?,identity_flag]
# 统一用[-1]索引identity_flag，以避免前面空项默认的情况
# identity_flag 0:BV和url 1:关键词检索
def user_interface(config_dict):
    # 字符串匹配分离
    in_func_dict = {}
    for key in config_dict:

        out_law_input_flag = 0  # url输入时，不含BV或AV号的URL会置1
        identity_flag = 0  # 0:BV和url 1:关键词检索
        http_abv_flag = 0  # 0:http等；1:BV或AV
        in_func_key = ""

        # 1.字符串匹配确定identity_flag
        if len(key) >= 2 and (key[0:2] == "BV" or key[0:2] == "bv" or key[0:2] == "bV" or key[0:2] == "Bv"):
            identity_flag = 0
            http_abv_flag = 1
        elif len(key) >= 2 and (key[0:2] == "AV" or key[0:2] == "av" or key[0:2] == "aV" or key[0:2] == "Av"):
            identity_flag = 0
            http_abv_flag = 1
        elif len(key) >= 4 and key[0:4] == "www." or key[0:3] == "WWW.":
            identity_flag = 0
            http_abv_flag = 0
        elif len(key) >= 7 and key[0:7] == "http://":
            identity_flag = 0
            http_abv_flag = 0
        elif len(key) >= 8 and key[0:8] == "https://":
            identity_flag = 0
            http_abv_flag = 0
        else:  # 关键词检索
            identity_flag = 1

        # 2.从config_dict得到in_func_dict,如果是BV号则换成url
        if identity_flag == 0:  # BV与http
            if http_abv_flag:  # BV或AV
                in_func_key = key  # 标明AV,BV号结束
                config_dict[key].append(identity_flag)
                in_func_dict[in_func_key] = config_dict[key]
            else:  # http
                id = ""
                # 找到AV,BV号，规范化
                try:
                    id = "BV" + re.findall("/(BV|Bv|bV|bv)(([A-Z]|[a-z]|[0-9])+)", key)[0][1]
                except IndexError:
                    try:
                        id = "AV" + re.findall("/(AV|Av|aV|av)(([A-Z]|[a-z]|[0-9])+)", key)[0][1]
                    except IndexError:  # 未发现AV或BV号
                        print("非法的URL(不含AV或BV号):" + key)
                        out_law_input_flag = 1  # 非法URL不会被包含进in_func_dict中

                if out_law_input_flag == 0:
                    in_func_key = id  # 标明AV,BV号结束
                    config_dict[key].append(identity_flag)
                    in_func_dict[in_func_key] = config_dict[key]
        else:  # 关键词检索
            in_func_key = key
            config_dict[key].append(identity_flag)
            in_func_dict[in_func_key] = config_dict[key]
    # print(in_func_dict)
    return in_func_dict
