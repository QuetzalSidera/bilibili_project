from image import *
from video import *

if __name__ == '__main__':
    # 一、爬取视频(音频)
    if main_debug_setting == 0 or main_debug_setting == 2:
        get_video(video_config)
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
