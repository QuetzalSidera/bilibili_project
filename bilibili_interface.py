# 检索交互界面与选集交互界面
from time import sleep
from bilibili_lib import *


# 检索交互界面
# 传入参数：关键词，是否选择，分区，初始页面
def bilibili_search_select_interface(keyword, select_enable, mode, target_area="all", page_id=1):
    global display_num
    in_func_id_list = []  # 添加in_func_前缀以区分，所有搜索结果id列表
    in_func_title_list = []
    info_list = []
    # 视频类型标签(0:一般视频，1:番剧电影，2：分集视频，3:合集视频，4:合集嵌套视频)
    selected_list=[]
    # 格式：在选择的info后面append一个空表
    # 一、获取检索结果
    print("正在bilibili搜索：\"" + keyword + "\"...")
    id_list = from_search_page_get_id(keyword, target_area, page_id)
    print("得到bilibili响应，正在提取检索结果")
    for id in id_list:
        if id[1] == 0:  # ssep
            info = from_ssepid_get_info(id[0])
            if info != "unknown":
                info_list.append(info)
        if id[1] == 1:  # BVAV
            info = from_BVAVid_get_info(id[0])
            if info != "unknown":
                info_list.append(info)
    print("检索结果提取完毕")
    # 视频类型标签 (0: 一般视频，1: 番剧电影，2:分集视频，3:合集视频，4:合集嵌套合分集视频（BV1wZyHYSEc5，BV17j28YqEv6）) 番剧的附带类型怎么办？
    # 合集视频info格式 [合集标题，atmo_list[atmo]，视频类型标签=3]
    # 一般视频,分集视频与合集atmo的info格式 [ID号,标题，分集id列表[]，分集标题列表[]，视频类型标签]
    # 番剧电影info格式 [ID号,标题，分集id列表[]，分集标题列表[]，视频类型标签]
    # for info in info_list:
    # 三、选择与交互界面
    display_id_list = []
    display_title_list = []
    selected_id_list = []

    if select_enable == 0:  # 不交互，默认截取list中需要的前几项
        display_id_list = in_func_id_list
        display_title_list = in_func_title_list
        selected_id_list = list(range(1, default_number_of_videos + 1))
        print("关键词\"" + keyword + "\"检索,非交互模式,以下是默认选择的检索结果(共" + str(
            len(selected_id_list)) + "个):")
        for i in selected_id_list:
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
                type_tag = "(合集)"
                episode_tag = "(第" + str(now_episode_index) + "集/全" + str(episode_num) + "集)"
            else:
                type_tag = "(unknown)"
                episode_tag = "(unknown)"
            print("\t" + str(i) + "." + type_tag + episode_tag + title)
        print("")

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

            select_result = input(
                "请输入您选择的视频序号,输入exit退出选择,输入delete重新选择，输入display all展示所有结果:")
            while select_result != "exit":
                if select_result in in_law_index_list:  # 排除特殊字符
                    selected_id_list.append(eval(select_result))
                    select_result = input("请输入您选择的视频序号:")
                elif select_result == "display all":
                    print("\n展示所有项目\n")
                    display_all_flag = 1
                    sleep(0.6)
                    break
                elif select_result == "delete":  # 输入delete重新选择
                    selected_id_list.clear()
                    print("重新选择")
                    select_result = input(
                        "请输入您选择的视频序号,输入exit退出选择,输入delete重新选择，输入display all展示所有结果:")
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
