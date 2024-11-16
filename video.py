from interface import *
from core import *


def get_video(config_list):
    # 处理输入，分流
    return_result = user_input_interface(config_list)
    ID_list = return_result[0]
    keyword_list = return_result[1]
    # 搜索
    ID_list += search_interface(keyword_list)
    # result格式
    # [ID号，标题, selected_id_list[],selected_title_list[], mode, 视频类型标签=bangumi set]
    # [ID号，标题, mode, 视频类型标签=single bangumi]
    # [ID号，标题, mode, 视频类型标签=bangumi append]

    # [ID号，标题,  mode, 视频类型标签=ordinary video]
    # [ID号，标题, selected_id_list[数字],selected_title_list[], mode, 视频类型标签=episode video]
    # [ID号，标题, atmo_list[], mode, 视频类型标签=ordinary set]
    # [ID号，标题, atmo_list[], mode, 视频类型标签=complex set]
    # atmo_list[]中atmo格式和ordinary video与episode video的result格式相同
    result_list = episode_select_interface(ID_list)  # 选集
    result_list = merge_result_list(result_list)
    display_result_list(result_list)
    print("即将开始从互联网爬取目标:")
    for result in result_list:
        set_unfold_and_commit_to_core(result)
