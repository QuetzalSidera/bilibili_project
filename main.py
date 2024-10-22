from image import *
from core import *

if __name__ == '__main__':
    # 一、爬取视频(音频)
    if main_debug_setting == 0 or main_debug_setting == 2:
        # 用户输入接口
        separated_list = user_interface(video_config)
        # 分流
        ID_standard_list = separated_list[0]
        keyword_middle_list = separated_list[1]  # keyword_middle_list 目标格式 [[key,select_enable,mode],...]

        # 关键词检索与用户交互界面
        keyword_standard_list = []
        for i in range(len(keyword_middle_list)):
            print(keyword_middle_list[i])
            if keyword_middle_list[i][1] == 0:
                keyword_standard_list += keywords_to_selected_list(keyword_middle_list[i][0], "bilibili",
                                                                   keyword_middle_list[i][1], keyword_middle_list[i][2])

        for i in range(len(keyword_middle_list)):
            if keyword_middle_list[i][1] == 1:
                keyword_standard_list += keywords_to_selected_list(keyword_middle_list[i][0], "bilibili",
                                                                   keyword_middle_list[i][1], keyword_middle_list[i][2])

        # 合并keyword和ID
        video_list = ID_standard_list + keyword_standard_list
        # 判断冲突项与合并
        merge_list(video_list)
        for video in video_list:
            set_unfold_and_commit_to_core(video)

        # video_id_dict = []  # 最终遍历带入get_video_and_html的列表
        # # {[视频id(BV AV与SS EP),选择集数列表[], 总集数，视频标题，视频类型标签(0: 一般视频，1: 番剧电影),模式]}
        # for key in universal_video_url_dict:  # 第一次遍历，完成“URL模式”与“关键词检索非交互模式”的video_url_dict转换
        #     if universal_video_url_dict[key][-1] == 0:  # URL模式#后面加入判断是番剧电影还是普通视频的函数
        #         episode_list = list(range(1, universal_video_url_dict[key][1] + 1))
        #         video_id_dict.append([key, episode_list, universal_video_url_dict[1], "unknown", 0,
        #                               universal_video_url_dict[key][0]])  # 默认一般视频
        #     if universal_video_url_dict[key][-1] == 1 and universal_video_url_dict[key][1] == 0:  # 关键词检索且不交互
        #         # 默认只找一集(这个地方可能后面来改)
        #         video_id_dict += keywords_to_selected_list(key, "bilibili", 0, universal_video_url_dict[key][0])
        # for key in universal_video_url_dict:  # 第二次遍历，完成“关键词检索交互模式”的video_url_dict转换
        #     if universal_video_url_dict[key][-1] == 1 and universal_video_url_dict[key][1] == 1:  # 关键词检索且交互
        #         video_id_dict += keywords_to_selected_list(key, "bilibili", 1, universal_video_url_dict[key][0])
        # for video in video_id_dict:
        #     get_video_and_html(video)

    # 二、爬取图片
    if main_debug_setting == 1 or main_debug_setting == 2:
        # 1.图片url配置
        if len(picture_key_word_list) != 0:
            for key_word in picture_key_word_list:
                picture_url_list += [
                    "https://baike.baidu.com/item/" + key_word
                ]
        # 2.获取图片
        for url in picture_url_list:
            get_image(url, 0)
            print("\n")
        print("图像获取结束")

    # 三、其他debug程序
    else:
        pass
# end_of_main
