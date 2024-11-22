import json

import requests
import pymediainfo

music_head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
}


def from_music_id_get_music(mid):
    music_url = "https://dl.stream.qqmusic.qq.com/"
    purl = get_purl(mid)
    music = requests.get(music_url + purl).content
    with open("music_result/" + mid + '.wav', 'wb') as f:
        f.write(music)
        print(mid + '下载完成')
    return


def get_purl(mid):
    url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?'
    mid_data = 'data={"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":1248959521,"g_tk_new_20200303":1832066374,"g_tk":1832066374},"req_1":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"6846657260","songmid":["%s"],"songtype":[0],"uin":"1248959521","loginflag":1,"platform":"20"}}}' % (
        mid)
    try:
        r = requests.get(url + mid_data, headers=music_head)
        r.encoding = 'utf-8'
        purl_json = json.loads(r.text).get('req_1').get('data').get('midurlinfo')[0].get('purl')
        return purl_json
    except:
        print('获取purl失败')
