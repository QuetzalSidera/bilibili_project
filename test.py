# 测试用例程

import requests
import re
from video import *
import jieba

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "Referer": "https://www.bilibili.com/",
    "Cookie": "CURRENT_FNVAL=4048; buvid3=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc; b_nut=1721567317; _uuid=67165DF10-7B77-BDE8-3C63-732C2FCAF4D520375infoc; enable_web_push=DISABLE; buvid4=0245F01B-6C4B-CD5A-2EC5-BC060EC0777D18433-024072113-zRTpkL0r94scQqxGfSYKhQ%3D%3D; home_feed_column=5; header_theme_version=CLOSE; rpdid=|(Y|RJRR)Y~0J'u~kulY~Rkk; DedeUserID=1611307689; DedeUserID__ckMd5=b0865dba0b3ced5b; buvid_fp_plain=undefined; is-2022-channel=1; b_lsid=D8542F24_191412D93C0; bsource=search_bing; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; browser_resolution=1659-943; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM2MzQ1OTMsImlhdCI6MTcyMzM3NTMzMywicGx0IjotMX0.Ox8rnEpQH5i1H_wQfH2z5CzZC0y8PlqQCy1KVa8XEfQ; bili_ticket_expires=1723634533; SESSDATA=f567fef6%2C1738927393%2C5d207%2A82CjAh2pSUKwDLr1XiI6ncU5B6NXEfWKS7ES6mDC8yGxM6aT3-BTdvK0KAlYpMhCXtEXgSVkl2aTlQWUNacTZOZ0ZNXzJwZ21QT2ozMXFXcWtFc1FpNnBIWlNWbml2Y3BxNV80bUNMZTBVN1dyb3h0STU1ZklDM0MwckJvanRmTmNkeTBFcW5qYl9RIIEC; bili_jct=8d788bcb503d69ba2ded7dfbb53f6e58; sid=71po5kkf; fingerprint=0c7279b7c69b9542a76b8d9df9b7872a; buvid_fp=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc; bp_t_offset_1611307689=964382000909647872"
}

target_url = "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/14/16/892361614/892361614-1-416.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1729838821&gen=playurlv2&os=cosbv&oi=0&trid=80ee169a6742411db463a61e1cc9184bp&mid=0&platform=pc&og=cos&upsig=554c787609a1581f353ceab50b04535c&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=0,3&buvid=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc&build=0&f=p_0_0&agrr=0&bw=90993&logo=80000000"
response = requests.get(target_url, headers=head)
with open("anime.mp4", "wb") as f:
    f.write(response.content)
    f.close()

# result = "".join(re.findall(r'[\u4e00-\u9fa5]', response.text))
# result = result[150:]
# keyword_list = jieba.lcut(result)
# print(keyword_list)
# print(result)
#
# # # with open('result.html','w') as f:
# #     f.write(response.text)
#
# for keyword in keyword_list[6:]:
#     keywords_to_selected_list(keyword, "bilibili", 0, -1)
# #
# #
#
# # test="gggggg<ggGGGg>ggg<ggggG>GggG>GGGGGGGGGgg"
# # text=re.findall("<.*?>",test)
# # print(text)
# def debug(info_list):
#     display_title_list = []
#     for info in info_list:
#         display_title_list.append(info[1])
#     print(len(display_title_list))
#     in_law_index_list = list(range(1, len(display_title_list) + 1))
#     for i in range(1, len(in_law_index_list) + 1):
#         in_law_index_list[i - 1] = str(in_law_index_list[i - 1])
#
#     print("关键词检索，交互模式，" + "目前展示所有检索结果，共" + str(
#         len(display_title_list)) + "个视频,以下是可供选择的项目:")
#     for i in range(1, len(display_title_list) + 1):
#         # info_list格式 [[ID号,标题，集数，这是第..集，视频类型标签],[ID号,标题，集数，这是第..集，视频类型标签],[ID号,标题，集数，这是第..集，视频类型标签].....]
#         # 视频类型标签(0:一般视频，1:番剧电影，2：分集视频，3:合集视频)
#         info_index = i - 1
#         title = info_list[info_index][1]
#         episode_num = info_list[info_index][2]
#         now_episode_index = info_list[info_index][3]
#         video_type = info_list[info_index][-1]
#         if video_type == 0:
#             type_tag = "(一般视频)"
#             episode_tag = ""
#         elif video_type == 1:
#             type_tag = "(番剧电影)"
#             episode_tag = "(全" + str(episode_num) + "话)"
#         elif video_type == 2:
#             type_tag = "(分集视频)"
#             episode_tag = "(全" + str(episode_num) + "话)"
#         elif video_type == 3:
#             type_tag = "(合集视频)"
#             episode_tag = "(第" + str(now_episode_index) + "集/全" + str(episode_num) + "集)"
#         else:
#             type_tag = "(unknown)"
#             episode_tag = "(unknown)"
#         print("\t" + str(i) + "." + type_tag + episode_tag + title)
#     print("")
false = 0
true = 1
test = {"code": 0, "message": "success",
        "result": {"play_check": {"limit_play_reason": "PAY", "play_detail": "PLAY_PREVIEW"},
                   "play_view_business_info": {
                       "episode_info": {"aid": 562117657, "bvid": "BV1Vv4y1D7HP", "cid": 949870270,
                                        "delivery_business_fragment_video": false, "delivery_fragment_video": false,
                                        "ep_id": 693248, "ep_status": 13, "interaction": {"interaction": false},
                                        "long_title": "明天见", "title": "2"},
                       "season_info": {"season_id": 43164, "season_type": 1},
                       "user_status": {"follow_info": {"follow": 0, "follow_status": 2}, "is_login": 0,
                                       "pay_info": {"pay_check": 0, "pay_pack_paid": 0, "sponsor": 0},
                                       "vip_info": {"real_vip": false},
                                       "watch_progress": {"current_watch_progress": 0, "last_ep_id": 0,
                                                          "last_time": 0}}},
                   "video_info": {"accept_format": "mp4,mp4,mp4,mp4,mp4", "code": 0, "seek_param": "start",
                                  "is_preview": 1, "fnval": 12240, "video_project": true, "fnver": 0, "type": "MP4",
                                  "bp": 0, "result": "suee", "seek_type": "second", "from": "local", "video_codecid": 7,
                                  "record_info": {"record_icon": "", "record": ""}, "durl": [
                           {"size": 19250141, "ahead": "", "length": 180137, "vhead": "", "backup_url": [
                               "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/70/02/949870270/949870270-1-416.mp4?e=ig8euxZM2rNcNbRV7bdVhwdlhWdjhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1729840773&gen=playurlv2&os=cosbv&oi=0&trid=239cb377a0394db6bcca4a8d9e2129c3p&mid=0&platform=pc&og=cos&upsig=38bfbe19fc4540d7e5c3074375f92514&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=1,3&buvid=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc&build=0&f=p_0_0&agrr=0&bw=106945&logo=40000000",
                               "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/70/02/949870270/949870270-1-416.mp4?e=ig8euxZM2rNcNbRV7bdVhwdlhWdjhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1729840773&gen=playurlv2&os=cosbv&oi=0&trid=239cb377a0394db6bcca4a8d9e2129c3p&mid=0&platform=pc&og=cos&upsig=38bfbe19fc4540d7e5c3074375f92514&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=2,3&buvid=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc&build=0&f=p_0_0&agrr=0&bw=106945&logo=40000000"],
                            "url": "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/70/02/949870270/949870270-1-416.mp4?e=ig8euxZM2rNcNbRV7bdVhwdlhWdjhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1729840773&gen=playurlv2&os=cosbv&oi=0&trid=239cb377a0394db6bcca4a8d9e2129c3p&mid=0&platform=pc&og=cos&upsig=38bfbe19fc4540d7e5c3074375f92514&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=0,3&buvid=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc&build=0&f=p_0_0&agrr=0&bw=106945&logo=80000000",
                            "order": 1, "md5": ""}], "is_drm": false, "no_rexcode": 0, "format": "mp4",
                                  "support_formats": [
                                      {"display_desc": "1080P", "has_preview": true, "sub_description": "",
                                       "superscript": "高码率", "need_login": true, "codecs": [], "format": "hdflv2",
                                       "description": "高清 1080P+", "need_vip": true, "quality": 112,
                                       "new_description": "1080P 高码率"},
                                      {"display_desc": "1080P", "has_preview": true, "sub_description": "",
                                       "superscript": "", "need_login": true, "codecs": [], "format": "flv",
                                       "description": "高清 1080P", "quality": 80, "new_description": "1080P 高清"},
                                      {"display_desc": "720P", "has_preview": true, "sub_description": "",
                                       "superscript": "", "need_login": true, "codecs": [], "format": "flv720",
                                       "description": "高清 720P", "quality": 64, "new_description": "720P 高清"},
                                      {"display_desc": "480P", "has_preview": true, "sub_description": "",
                                       "superscript": "", "codecs": [], "format": "flv480", "description": "清晰 480P",
                                       "quality": 32, "new_description": "480P 清晰"},
                                      {"display_desc": "360P", "has_preview": true, "sub_description": "",
                                       "superscript": "", "codecs": [], "format": "mp4", "description": "流畅 360P",
                                       "quality": 16, "new_description": "360P 流畅"}], "message": "",
                                  "accept_quality": [112, 80, 64, 32, 16], "quality": 32, "timelength": 1425214,
                                  "durls": [{"durl": [{"size": 41984887, "ahead": "", "length": 180137, "vhead": "",
                                                       "backup_url": [
                                                           "https://upos-sz-estghw.bilivideo.com/upgcxcode/70/02/949870270/949870270-1-464.mp4?e=ig8euxZM2rNcNbNzhzdVhwdlhbhzhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1729840773&gen=playurlv2&os=upos&oi=0&trid=239cb377a0394db6bcca4a8d9e2129c3p&mid=0&platform=pc&og=hw&upsig=f5c75d8ea5f4045e373c295e8a234d68&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=1,3&buvid=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc&build=0&f=p_0_0&agrr=0&bw=233249&logo=40000000",
                                                           "https://upos-sz-estghw.bilivideo.com/upgcxcode/70/02/949870270/949870270-1-464.mp4?e=ig8euxZM2rNcNbNzhzdVhwdlhbhzhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1729840773&gen=playurlv2&os=upos&oi=0&trid=239cb377a0394db6bcca4a8d9e2129c3p&mid=0&platform=pc&og=hw&upsig=f5c75d8ea5f4045e373c295e8a234d68&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=2,3&buvid=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc&build=0&f=p_0_0&agrr=0&bw=233249&logo=40000000"],
                                                       "url": "https://upos-sz-estghw.bilivideo.com/upgcxcode/70/02/949870270/949870270-1-464.mp4?e=ig8euxZM2rNcNbNzhzdVhwdlhbhzhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1729840773&gen=playurlv2&os=upos&oi=0&trid=239cb377a0394db6bcca4a8d9e2129c3p&mid=0&platform=pc&og=hw&upsig=f5c75d8ea5f4045e373c295e8a234d68&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=0,3&buvid=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc&build=0&f=p_0_0&agrr=0&bw=233249&logo=80000000",
                                                       "order": 1, "md5": ""}], "quality": 80}, {"durl": [
                                      {"size": 23293963, "ahead": "", "length": 180137, "vhead": "", "backup_url": [
                                          "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/70/02/949870270/949870270-1-448.mp4?e=ig8euxZM2rNcNbRgnWdVhwdlhWNHhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1729840773&gen=playurlv2&os=cosbv&oi=0&trid=239cb377a0394db6bcca4a8d9e2129c3p&mid=0&platform=pc&og=cos&upsig=5b9959e935ed782d32963f4632ca5035&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=1,3&buvid=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc&build=0&f=p_0_0&agrr=0&bw=129410&logo=40000000",
                                          "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/70/02/949870270/949870270-1-448.mp4?e=ig8euxZM2rNcNbRgnWdVhwdlhWNHhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1729840773&gen=playurlv2&os=cosbv&oi=0&trid=239cb377a0394db6bcca4a8d9e2129c3p&mid=0&platform=pc&og=cos&upsig=5b9959e935ed782d32963f4632ca5035&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=2,3&buvid=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc&build=0&f=p_0_0&agrr=0&bw=129410&logo=40000000"],
                                       "url": "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/70/02/949870270/949870270-1-448.mp4?e=ig8euxZM2rNcNbRgnWdVhwdlhWNHhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1729840773&gen=playurlv2&os=cosbv&oi=0&trid=239cb377a0394db6bcca4a8d9e2129c3p&mid=0&platform=pc&og=cos&upsig=5b9959e935ed782d32963f4632ca5035&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=0,3&buvid=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc&build=0&f=p_0_0&agrr=0&bw=129410&logo=80000000",
                                       "order": 1, "md5": ""}], "quality": 64}, {"durl": [
                                      {"size": 19250141, "ahead": "", "length": 180137, "vhead": "", "backup_url": [
                                          "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/70/02/949870270/949870270-1-416.mp4?e=ig8euxZM2rNcNbRV7bdVhwdlhWdjhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1729840773&gen=playurlv2&os=cosbv&oi=0&trid=239cb377a0394db6bcca4a8d9e2129c3p&mid=0&platform=pc&og=cos&upsig=38bfbe19fc4540d7e5c3074375f92514&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=1,3&buvid=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc&build=0&f=p_0_0&agrr=0&bw=106945&logo=40000000",
                                          "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/70/02/949870270/949870270-1-416.mp4?e=ig8euxZM2rNcNbRV7bdVhwdlhWdjhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1729840773&gen=playurlv2&os=cosbv&oi=0&trid=239cb377a0394db6bcca4a8d9e2129c3p&mid=0&platform=pc&og=cos&upsig=38bfbe19fc4540d7e5c3074375f92514&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=2,3&buvid=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc&build=0&f=p_0_0&agrr=0&bw=106945&logo=40000000"],
                                       "url": "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/70/02/949870270/949870270-1-416.mp4?e=ig8euxZM2rNcNbRV7bdVhwdlhWdjhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1729840773&gen=playurlv2&os=cosbv&oi=0&trid=239cb377a0394db6bcca4a8d9e2129c3p&mid=0&platform=pc&og=cos&upsig=38bfbe19fc4540d7e5c3074375f92514&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=0,3&buvid=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc&build=0&f=p_0_0&agrr=0&bw=106945&logo=80000000",
                                       "order": 1, "md5": ""}], "quality": 32}, {"durl": [
                                      {"size": 10833493, "ahead": "", "length": 180137, "vhead": "", "backup_url": [
                                          "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/70/02/949870270/949870270-1-400.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1729840773&gen=playurlv2&os=cosbv&oi=0&trid=239cb377a0394db6bcca4a8d9e2129c3p&mid=0&platform=pc&og=cos&upsig=ba5962e74b8ac0c71ac16732c3a05f8e&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=1,3&buvid=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc&build=0&f=p_0_0&agrr=0&bw=60186&logo=40000000",
                                          "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/70/02/949870270/949870270-1-400.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1729840773&gen=playurlv2&os=cosbv&oi=0&trid=239cb377a0394db6bcca4a8d9e2129c3p&mid=0&platform=pc&og=cos&upsig=ba5962e74b8ac0c71ac16732c3a05f8e&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=2,3&buvid=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc&build=0&f=p_0_0&agrr=0&bw=60186&logo=40000000"],
                                       "url": "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/70/02/949870270/949870270-1-400.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1729840773&gen=playurlv2&os=cosbv&oi=0&trid=239cb377a0394db6bcca4a8d9e2129c3p&mid=0&platform=pc&og=cos&upsig=ba5962e74b8ac0c71ac16732c3a05f8e&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=0,3&buvid=BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc&build=0&f=p_0_0&agrr=0&bw=60186&logo=80000000",
                                       "order": 1, "md5": ""}], "quality": 16}], "has_paid": false, "clip_info_list": [
                           {"materialNo": 0, "start": 39, "end": 125, "toastText": "即将跳过片头",
                            "clipType": "CLIP_TYPE_OP"},
                           {"materialNo": 0, "start": 1331, "end": 1420, "toastText": "即将跳过片尾",
                            "clipType": "CLIP_TYPE_ED"}],
                                  "accept_description": ["高清 1080P+", "高清 1080P", "高清 720P", "清晰 480P",
                                                         "流畅 360P"], "status": 13},
                   "view_info": {"ai_repair_qn_trial_info": {"trial_able": false}, "end_page": {"dialog": {
                       "bottom_display": [
                           {"icon": "http://i0.hdslb.com/bfs/vip/5268554bf700180e3503a6e81b48873150df3086.png",
                            "title": {"text": "会员免费看", "text_color": "#FFFFFF", "text_color_night": ""}},
                           {"icon": "http://i0.hdslb.com/bfs/vip/527a4f4e6b9d5c327d0d57ad6b433c29e5a61a4a.png",
                            "title": {"text": "会员抢先看", "text_color": "#FFFFFF", "text_color_night": ""}},
                           {"icon": "http://i0.hdslb.com/bfs/vip/36a0b9f6e9ee071350c1b640052c6d8bb436ffcd.png",
                            "title": {"text": "会员超清看", "text_color": "#FFFFFF", "text_color_night": ""}},
                           {"icon": "http://i0.hdslb.com/bfs/vip/41fbfb848a46d429e11911e14bcbba3cba832aad.png",
                            "title": {"text": "杜比全景声", "text_color": "#FFFFFF", "text_color_night": ""}}],
                       "button": [{"action_type": "vip", "badge_info": {"bg_color": "", "bg_color_night": "",
                                                                        "bg_gradient_color": {"end_color": "#FFC65D",
                                                                                              "start_color": "#FFEEC9"},
                                                                        "text": "低至0.4元/天",
                                                                        "text_color": "#5B2E00"}, "bg_color": "",
                                   "bg_color_night": "",
                                   "bg_gradient_color": {"end_color": "#E84B85", "start_color": "#FF6699"},
                                   "jump_type": "vip", "left_strikethrough_text": "",
                                   "link": "bilibili://user_center/vip/buy/1?appSubId=layerPay&order_report_params=%7B%22exp_group_tag%22%3A%22def%22%2C%22exp_tag%22%3A%22def%22%2C%22material_type%22%3A%223%22%2C%22position_id%22%3A%2223%22%2C%22request_id%22%3A%2222d1622eaf476739083a82d84d671b2a%22%2C%22tips_id%22%3A%2217880%22%2C%22tips_repeat_key%22%3A%2217880%3A23%3A1729833573%3ABE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc%22%2C%22unit_id%22%3A%226988%22%2C%22vip_status%22%3A%220%22%2C%22vip_type%22%3A%220%22%7D",
                                   "order_report_params": {
                                       "tips_repeat_key": "17880:23:1729833573:BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc",
                                       "ep_status": "13", "exp_tag": "def", "season_id": "43164", "season_status": "13",
                                       "ep_id": "693248", "material_type": "3", "season_type": "1", "vip_type": "0",
                                       "vip_status": "0", "request_id": "22d1622eaf476739083a82d84d671b2a",
                                       "unit_id": "6988", "tips_id": "17880", "exp_group_tag": "def",
                                       "position_id": "23"},
                                   "pc_link": "https://big.bilibili.com/mobile/publicPay?appId=170&appSubId=layerPay&order_report_params=%7B%22exp_group_tag%22%3A%22def%22%2C%22exp_tag%22%3A%22def%22%2C%22material_type%22%3A%223%22%2C%22position_id%22%3A%2223%22%2C%22request_id%22%3A%2222d1622eaf476739083a82d84d671b2a%22%2C%22tips_id%22%3A%2217880%22%2C%22tips_repeat_key%22%3A%2217880%3A23%3A1729833573%3ABE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc%22%2C%22unit_id%22%3A%226988%22%2C%22vip_status%22%3A%220%22%2C%22vip_type%22%3A%220%22%7D",
                                   "report": {"clickEventId": "layer-pay-button",
                                              "extend": "{\"ep_status\":\"13\",\"exp_tag\":\"def\",\"season_status\":\"13\",\"button\":\"vip\",\"material_type\":\"3\",\"season_type\":\"1\",\"vip_type\":\"0\",\"try_status\":\"1\",\"vip_due_date\":\"\",\"unit_id\":\"6988\",\"tips_id\":\"17880\",\"exp_group_tag\":\"def\",\"corner_tip\":\"1\",\"watch_together\":\"0\",\"tips_repeat_key\":\"17880:23:1729833573:BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc\",\"epid\":\"693248\",\"season_id\":\"43164\",\"was_he_inline\":\"0\",\"layer_from\":\"pay\",\"vip_status\":\"0\",\"request_id\":\"22d1622eaf476739083a82d84d671b2a\",\"position_id\":\"23\"}",
                                              "showEventId": "layer-pay-button"}, "simple_bg_color": "",
                                   "simple_bg_color_night": "",
                                   "simple_text_info": {"text": "", "text_color": "", "text_color_night": ""},
                                   "task_param": {"activity_id": 0, "task_type": "", "tips_id": 17880},
                                   "text": "成为大会员免费看", "text_color": "#FFFFFF", "text_color_night": ""}],
                       "code": 6002105,
                       "config": {"is_background_translucent_enable": false, "is_force_halfscreen_enable": false,
                                  "is_nested_scroll_enable": false, "is_orientation_enable": false,
                                  "is_show_cover": true}, "count_down_sec": 0, "image": {
                           "url": "https://i0.hdslb.com/bfs/bangumi/image/d9d6284e0919ecfda41981c1f9119f993db62935.jpg"},
                       "link": "https://big.bilibili.com/mobile/publicPay?appId=170&appSubId=layerQRCode",
                       "link_desc": "打开哔哩哔哩App\n扫一扫开通大会员", "msg": "开通大会员观看",
                       "pay_desc": "打开哔哩哔哩App\n扫一扫开通大会员",
                       "pay_url": "https://big.bilibili.com/mobile/publicPay?appId=170&appSubId=layerQRCode",
                       "report": {"clickEventId": "",
                                  "extend": "{\"ep_status\":\"13\",\"exp_tag\":\"def\",\"season_status\":\"13\",\"material_type\":\"3\",\"season_type\":\"1\",\"vip_type\":\"0\",\"try_status\":\"1\",\"vip_due_date\":\"\",\"unit_id\":\"6988\",\"tips_id\":\"17880\",\"exp_group_tag\":\"def\",\"watch_together\":\"0\",\"tips_repeat_key\":\"17880:23:1729833573:BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc\",\"epid\":\"693248\",\"season_id\":\"43164\",\"vip_frozen\":\"0\",\"was_he_inline\":\"0\",\"layer_from\":\"pay\",\"vip_status\":\"0\",\"request_id\":\"22d1622eaf476739083a82d84d671b2a\",\"position_id\":\"23\"}",
                                  "showEventId": "layer-pay.0"}, "style_type": "vertical_text",
                       "subtitle": {"text": "", "text_color": "#CCCCCC", "text_color_night": ""},
                       "title": {"text": "试看已结束，本片是大会员专享内容", "text_color": "#FFFFFF",
                                 "text_color_night": ""}, "type": "pay"}, "hide": false}, "ext_toast": {}, "pop_win": {
                       "bottom_desc": {"action_type": "", "badge_info": {"bg_color": "", "bg_color_night": "",
                                                                         "bg_gradient_color": {"end_color": "",
                                                                                               "start_color": ""},
                                                                         "text": "", "text_color": ""}, "bg_color": "",
                                       "bg_color_night": "", "bg_gradient_color": {"end_color": "", "start_color": ""},
                                       "jump_type": "link", "left_strikethrough_text": "", "link": "",
                                       "order_report_params": {}, "pc_link": "",
                                       "report": {"clickEventId": "", "extend": "", "showEventId": ""},
                                       "simple_bg_color": "", "simple_bg_color_night": "",
                                       "simple_text_info": {"text": "", "text_color": "", "text_color_night": ""},
                                       "task_param": {"activity_id": 0, "task_type": "", "tips_id": 0}, "text": "",
                                       "text_color": "", "text_color_night": ""}, "bottom_text": "", "button": [
                           {"action_type": "vip", "badge_info": {"bg_color": "", "bg_color_night": "",
                                                                 "bg_gradient_color": {"end_color": "",
                                                                                       "start_color": ""}, "text": "",
                                                                 "text_color": ""}, "bg_color": "",
                            "bg_color_night": "",
                            "bg_gradient_color": {"end_color": "#E84B85", "start_color": "#FF6699"},
                            "jump_type": "link", "left_strikethrough_text": "",
                            "link": "bilibili://user_center/vip/buy/1?appSubId=layerPay&order_report_params=%7B%22exp_group_tag%22%3A%22def%22%2C%22exp_tag%22%3A%22def%22%2C%22material_type%22%3A%223%22%2C%22position_id%22%3A%2223%22%2C%22request_id%22%3A%2222d1622eaf476739083a82d84d671b2a%22%2C%22tips_id%22%3A%2217880%22%2C%22tips_repeat_key%22%3A%2217880%3A23%3A1729833573%3ABE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc%22%2C%22unit_id%22%3A%226988%22%2C%22vip_status%22%3A%220%22%2C%22vip_type%22%3A%220%22%7D",
                            "order_report_params": {
                                "tips_repeat_key": "17880:23:1729833573:BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc",
                                "ep_status": "13", "exp_tag": "def", "season_id": "43164", "season_status": "13",
                                "ep_id": "693248", "material_type": "3", "season_type": "1", "vip_type": "0",
                                "vip_status": "0", "request_id": "22d1622eaf476739083a82d84d671b2a", "unit_id": "6988",
                                "tips_id": "17880", "exp_group_tag": "def", "position_id": "23"}, "pc_link": "",
                            "report": {"clickEventId": "pgc.pgc-video-detail.content-purchase-btn.0.click",
                                       "extend": "{\"ep_status\":\"13\",\"exp_tag\":\"def\",\"season_status\":\"13\",\"button\":\"vip\",\"material_type\":\"3\",\"season_type\":\"1\",\"vip_type\":\"0\",\"try_status\":\"1\",\"vip_due_date\":\"\",\"unit_id\":\"6988\",\"tips_id\":\"17880\",\"exp_group_tag\":\"def\",\"corner_tip\":\"1\",\"watch_together\":\"0\",\"tips_repeat_key\":\"17880:23:1729833573:BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc\",\"epid\":\"693248\",\"season_id\":\"43164\",\"was_he_inline\":\"0\",\"layer_from\":\"pay\",\"vip_status\":\"0\",\"request_id\":\"22d1622eaf476739083a82d84d671b2a\",\"position_id\":\"23\"}",
                                       "showEventId": "pgc.pgc-video-detail.content-purchase-btn.0.show"},
                            "simple_bg_color": "", "simple_bg_color_night": "",
                            "simple_text_info": {"text": "", "text_color": "", "text_color_night": ""},
                            "task_param": {"activity_id": 0, "task_type": "", "tips_id": 0}, "text": "成为大会员免费看",
                            "text_color": "#FFFFFF", "text_color_night": ""}], "cover": "",
                       "pop_title": {"text": "试看已结束，本片是大会员专享内容", "text_color": "#FFFFFF",
                                     "text_color_night": ""}, "pop_type": "common",
                       "subtitle": {"text": "", "text_color": "#000000", "text_color_night": ""}, "title": ""},
                                 "qn_trial_info": {"trial_able": false},
                                 "report": {"ep_id": "693248", "ep_status": "13", "season_id": "43164",
                                            "season_status": "13", "season_type": "1", "vip_status": "0",
                                            "vip_type": "0"}, "try_prompt_bar": {"benefit_infos": [],
                                                                                 "bg_gradient_color": {
                                                                                     "end_color": "#1B1920",
                                                                                     "start_color": "#171518"},
                                                                                 "bg_image": "http://i0.hdslb.com/bfs/vip/7f7beb19ddfe03f6bdab338582ee79c5528711b4.png",
                                                                                 "button": [{"action_type": "vip",
                                                                                             "badge_info": {
                                                                                                 "bg_color": "",
                                                                                                 "bg_color_night": "",
                                                                                                 "bg_gradient_color": {
                                                                                                     "end_color": "#FFC65D",
                                                                                                     "start_color": "#FFEEC9"},
                                                                                                 "text": "低至0.4元/天",
                                                                                                 "text_color": "#5B2E00"},
                                                                                             "bg_color": "",
                                                                                             "bg_color_night": "",
                                                                                             "bg_gradient_color": {
                                                                                                 "end_color": "#E84B85",
                                                                                                 "start_color": "#FF6699"},
                                                                                             "jump_type": "vip",
                                                                                             "left_strikethrough_text": "",
                                                                                             "link": "bilibili://user_center/vip/buy/1?appSubId=tryBanner",
                                                                                             "order_report_params": {
                                                                                                 "tips_repeat_key": "17881:14:1729833573:BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc",
                                                                                                 "ep_status": "13",
                                                                                                 "exp_tag": "def",
                                                                                                 "season_id": "43164",
                                                                                                 "season_status": "13",
                                                                                                 "ep_id": "693248",
                                                                                                 "material_type": "3",
                                                                                                 "season_type": "1",
                                                                                                 "vip_type": "0",
                                                                                                 "vip_status": "0",
                                                                                                 "tips_id": "17881",
                                                                                                 "unit_id": "6989",
                                                                                                 "request_id": "22d1622eaf476739083a82d84d671b2a",
                                                                                                 "exp_group_tag": "def",
                                                                                                 "position_id": "14"},
                                                                                             "pc_link": "https://big.bilibili.com/mobile/publicPay?appId=170&appSubId=tryTipsPay",
                                                                                             "report": {
                                                                                                 "clickEventId": "try-tips-button",
                                                                                                 "extend": "{\"ep_status\":\"13\",\"exp_tag\":\"def\",\"season_status\":\"13\",\"button\":\"vip\",\"material_type\":\"3\",\"season_type\":\"1\",\"vip_type\":\"0\",\"tips_id\":\"17881\",\"unit_id\":\"6989\",\"exp_group_tag\":\"def\",\"corner_tip\":\"1\",\"tips_repeat_key\":\"17881:14:1729833573:BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc\",\"epid\":\"693248\",\"season_id\":\"43164\",\"vip_status\":\"0\",\"request_id\":\"22d1622eaf476739083a82d84d671b2a\",\"position_id\":\"14\"}",
                                                                                                 "showEventId": "try-tips-button"},
                                                                                             "simple_bg_color": "",
                                                                                             "simple_bg_color_night": "",
                                                                                             "simple_text_info": {
                                                                                                 "text": "",
                                                                                                 "text_color": "",
                                                                                                 "text_color_night": ""},
                                                                                             "task_param": {
                                                                                                 "activity_id": 0,
                                                                                                 "task_type": "",
                                                                                                 "tips_id": 0},
                                                                                             "text": "成为大会员",
                                                                                             "text_color": "#FFFFFF",
                                                                                             "text_color_night": ""}],
                                                                                 "end_time": 0,
                                                                                 "full_screen_bg_gradient_color": {
                                                                                     "end_color": "#18191C",
                                                                                     "start_color": "#2F3238"},
                                                                                 "full_screen_ip_icon": "https://i0.hdslb.com/bfs/vip/29d5348b1f2f730c2b44abb115a507c465b05744.png",
                                                                                 "prompt_bar_style": "TEXT",
                                                                                 "report": {"clickEventId": "",
                                                                                            "extend": "{\"ep_status\":\"13\",\"exp_tag\":\"def\",\"season_status\":\"13\",\"material_type\":\"3\",\"season_type\":\"1\",\"vip_type\":\"0\",\"tips_id\":\"17881\",\"unit_id\":\"6989\",\"exp_group_tag\":\"def\",\"corner_tip\":\"0\",\"tips_repeat_key\":\"17881:14:1729833573:BE2D386A-BBCB-E06E-8C2B-F5223B4C8BC517591infoc\",\"epid\":\"693248\",\"season_id\":\"43164\",\"vip_status\":\"0\",\"request_id\":\"22d1622eaf476739083a82d84d671b2a\",\"position_id\":\"14\"}",
                                                                                            "showEventId": "try-tips.0"},
                                                                                 "subTitle": {
                                                                                     "text": "试看中 · 成为大会员 免费看本片",
                                                                                     "text_color": "#99FFFFFF",
                                                                                     "text_color_night": ""},
                                                                                 "sub_title_icon": "http://i0.hdslb.com/bfs/vip/1560eab73c311673f590f19df0a0953db445b503.png",
                                                                                 "title": {
                                                                                     "text": "本片是大会员专享内容",
                                                                                     "text_color": "#FFFFFF",
                                                                                     "text_color_night": ""}}}}}
