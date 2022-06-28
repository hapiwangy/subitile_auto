from opencc import OpenCC
with open("6月28日.srt", "r", encoding = "utf-8") as fp:
    content = fp.readlines()    

c = 1
ac = 0
li = []
cc = OpenCC("s2t")
while True:
    if c == 4 or ac == 2:
        c = 1
        li.append(cc.convert(content[ac]))
    elif c < 4:
        c += 1
        li.append(content[ac])
    if ac <= len(content) - 2:
        ac += 1
    else:
        break
with open ("sub.srt","w", encoding="utf-8") as fp:
    for x in li:
        fp.write(x)
