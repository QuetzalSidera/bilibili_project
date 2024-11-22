from qqmusic_lib import *
from user_config import *


def get_music(music_config):
    for key in music_config:
        music_id = key
        detail_list = music_config[key]
        if len(detail_list) == 0:
            app_type = default_app
        else:
            app_type = detail_list[0]
        if app_type == 'qq_music':
            from_music_id_get_music(music_id)
        else:
            pass
