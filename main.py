from video import *
if __name__ == '__main__':
    # 一、爬取视频(音频)(bilibili)
    if User_Cookie_enable == 1:
        head["Cookie"] = User_cookie
    get_video(video_config)
# end_of_main
