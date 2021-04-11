# coding = UTF-8
"""下载器核心组件，包括下载器和本地文件管理等。"""

# 导入歌单构造模块和音乐检查模块
from KuGou.Tools.LocalTools import MusicSheet, CheckMusic

# 导入酷狗音乐必需的下载组件
from KuGou.Tools.KuGouWebTools import MusicList as KuGouMusicList
from KuGou.Tools.KuGouWebTools import MusicInfo as KuGouMusicInfo
from KuGou.Tools.KuGouWebTools import Music

# 导入网易云音乐必需的下载组件
from KuGou.Tools.WangYiYunWebTools import MusicList as WangYiYunMusicList

# 导入聚合管理模块(可聚合并操作多个网站的结果)
from KuGou.Tools.Controller import GetMusicList, GetMusicInfo, SaveMusic
