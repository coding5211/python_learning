import pickle
import io

shoplistfile = "shoplist.data"

shoplist = ["apple","banana","mango"]
ff = open(shoplistfile,"wb")
pickle.dump(shoplist,ff)
ff.close()

del shoplist
f1 = open(shoplistfile,"rb")
storedlist = pickle.load(f1)
print(storedlist)

f = io.open("abc.txt","wt",encoding="utf-8")
f.write(u"这不是英语语言")
f.close()

text = io.open("abc.txt",encoding="utf-8").read()
print(text)
