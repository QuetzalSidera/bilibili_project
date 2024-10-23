<a target="_blank"
                                                                     href="//space.bilibili.com/23052222/channel/collectiondetail?sid=3883158&amp;spm_id_from=333.788.0.0"
                                                                     title="东方Vocal" class="title jumpable"
                                                                     data-v-f4470e68>东方Vocal</a>
"<div title="视频选集" class="title" data-v-f4470e68>视频选集</div>"


最佳接口
video_config = {
    BV号: [模式，集数],
url: [模式，集数],
关键词: [模式，select_enable],
}

1)视频分类
1.普通不分集视频
2.普通分集视频
3.合集视频：本视频不分集，但是包含于一个合集之中，合集之中的视频BV号不相同
4.番剧电影
5.番剧电影附加视频(暂无计划)

后期开发规划：
关于合集视频：
可以找到合集视频的每一集，反馈到控制台打印选集

关于分集视频
读取分集总数，若分集视频集数>选择的集数，则打印错误信息，并选择全集
一般分集视频也加入选集交互窗口中去选择


数据标准格式
内核标准格式
video_dict = []  # 最终遍历带入get_video_and_html的列表
[[视频id(BVAV与SSEP),选择集数列表[], 总集数，视频标题，视频类型标签(0: 一般视频，1: 番剧电影,2:合集视频),模式],....]

 选择集数列表：如果是分集视频或者番剧电影则是数字
如果是合集视频则是对应视频的BV号
视频描述信息
[视频id(BVAV与SSEP),总集数,视频标题,视频类型标签(0: 一般视频,1: 番剧电影,2:合集视频),]