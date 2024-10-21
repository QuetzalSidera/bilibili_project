from image import *
from video import *
main_debug_setting = 0  # 0:获取视频 1:获取图片 2:都要 3与其他：debug程序
if __name__ == '__main__':
    # 一、爬取视频(音频)
    if main_debug_setting == 0 or main_debug_setting == 2:
        universal_video_url_dict = user_interface(video_config)
        for key in universal_video_url_dict:
            # 由于补充了identity_flag，因此全空：长度1，半空：长度2，全满：长度3
            if universal_video_url_dict[key][-1] == 0:  # 直接给出URL
                # 以下是处理默认情况的逻辑
                if len(universal_video_url_dict[key]) == 1:  # 全空
                    universal_video_url_dict[key] = [default_mode, default_episode_num] + universal_video_url_dict[key]
                elif len(universal_video_url_dict[key]) == 2:  # 半空
                    if universal_video_url_dict[key][0] < 0:  # 指定了模式，默认集数
                        universal_video_url_dict[key].insert(1, default_episode_num)
                    else:  # 指定了集数，默认模式
                        universal_video_url_dict[key].insert(0, default_mode)
                elif len(universal_video_url_dict[key]) == 3:  # 全满
                    pass

            else:  # 关键词检索
                # 以下是处理默认情况的逻辑
                if len(universal_video_url_dict[key]) == 1:  # 全空
                    universal_video_url_dict[key] = [default_mode, default_select] + universal_video_url_dict[
                        key]  # 默认模式，默认是否交互
                elif len(universal_video_url_dict[key]) == 2:  # 半空
                    if universal_video_url_dict[key][0] < 0:  # 指定了模式，默认是否交互
                        universal_video_url_dict[key].insert(1, default_select)
                    else:  # 指定了是否交互，默认模式
                        universal_video_url_dict[key].insert(0, default_mode)
                elif len(universal_video_url_dict[key]) == 3:  # 全满
                    pass
            # universal_video_url_dict 标准化完成

        video_url_dict = {}  # 最终遍历带入get_video_and_html的列表,格式  {url1：模式1,url2：模式2}
        for key in universal_video_url_dict:  # 第一次遍历，完成“URL模式”与“关键词检索非交互模式”的video_url_dict转换
            if universal_video_url_dict[key][-1] == 0:  # URL模式
                # 原视频不分集的情况下，输入p=1依然可以正常访问
                for eposide_id in range(1, universal_video_url_dict[key][1] + 1):
                    eposide_url = "https://www.bilibili.com/video/" + str(key) + "/?p=" + str(eposide_id)
                    video_url_dict[eposide_url] = universal_video_url_dict[key][0]

            if universal_video_url_dict[key][-1] == 1 and universal_video_url_dict[key][1] == 0:  # 关键词检索且不交互
                # 默认只找一集(这个地方可能后面来改)
                selected_list = []
                selected_list += keywords_to_url(key, "bilibili", 0)
                for result_url in selected_list:
                    video_url_dict[result_url] = universal_video_url_dict[key][0]
        for key in universal_video_url_dict:  # 第二次遍历，完成“关键词检索交互模式”的video_url_dict转换
            if universal_video_url_dict[key][-1] == 1 and universal_video_url_dict[key][1] == 1:  # 关键词检索且交互
                selected_list = []
                selected_list += keywords_to_url(key, "bilibili", 1)
                for result_url in selected_list:
                    video_url_dict[result_url] = universal_video_url_dict[key][0]
        for key in video_url_dict:
            get_video_and_html(key, video_url_dict[key])

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
