# coding = UTF-8


import KuGou

KuGou.Download(input("Music name : "), FilePath="./Music", LrcFile=True, DebugFlag=True,
               Selector=KuGou.Tools.LocalTools.MusicSelector)
# KuGou.ReDownload(FilePath="./Music", LrcFile=True, DebugFlag=True)
Check = KuGou.CheckMusic()
Check.DeleteVIPMusic(DebugFlag=True)
Check.DeleteTooShortMusic(DebugFlag=True)

input("Finish .")
