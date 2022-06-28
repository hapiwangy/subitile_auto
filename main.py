from copy import deepcopy
from opencc import OpenCC
file = open("draft_content.json", "r", encoding="utf-8")
con = file.readlines()
li = con[0]
cl = deepcopy(li)
sl = len("<size=5.000000>")
cc = OpenCC("s2t")
with open("sub.txt", "w+", encoding="utf-8") as fp:
    while True:
        nums = li.find("<size=5.000000>")
        nume = li.find("</size>")
        fst = cl.find("target_timerange")
        est = cl.find("track_render_index")
        temp = cl[fst:est]
        fcommon = temp.find(",")
        scommon = temp.find("}")
        dur = temp[30:fcommon]
        start = temp[fcommon + 9:scommon]
        cl = cl[est + 1:]
        if nums == -1: break
        fp.write(start +" "+ dur+" "+ cc.convert(li[nums + sl:nume])+"\n")
        li = li[nume + 1:]