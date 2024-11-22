from image import *
from video import *
from music import *
if __name__ == '__main__':
    # 一、爬取视频(音频)(bilibili)
    if main_debug_setting == 0 or main_debug_setting == 3:
        if User_Cookie_enable == 1:
            head["Cookie"] = User_cookie
        get_video(video_config)
    # 二、爬取音乐(qq音乐)
    if main_debug_setting == 1 or main_debug_setting == 3:
        get_music(music_config)
    # 三、爬取图片
    if main_debug_setting == 2 or main_debug_setting == 3:
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
    # 四、其他debug程序
    else:
        pass
# end_of_main
