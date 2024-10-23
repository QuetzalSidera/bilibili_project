from image import *
from core import *

if __name__ == '__main__':
    # 一、爬取视频(音频)
    if main_debug_setting == 0 or main_debug_setting == 2:
        # 用户输入接口
        separated_list = user_interface(video_config)
        # 分流
        ID_standard_list = standardize_ID_list(separated_list[0])
        keyword_middle_list = separated_list[1]  # keyword_middle_list 目标格式 [[key,select_enable,mode],...]

        # 关键词检索与用户交互界面
        keyword_standard_list = []
        for i in range(len(keyword_middle_list)):
            # print(keyword_middle_list[i])
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
        video_list = merge_list(video_list)
        sleep(1.3)
        # 番剧电影，分集，合集视频选集
        video_list = episode_select_interface(video_list)

        # 展示选择结果
        if len(video_list):
            display_result(video_list)
            print("开始从互联网爬取目标")
        else:
            print("您没有选择任何项目")
        for video in video_list:
            set_unfold_and_commit_to_core(video)

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
