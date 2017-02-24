"""
shoplist=["apple","banana","mango","sai"]
str="jackrose"
print("itme 0 is",shoplist[0])
print("item 1 is",shoplist[1])
print("item 2 is",shoplist[2])
print("str 0 is",str[0])

print("itme 1 to 3 is",shoplist[1:2])
print("item 1 end is",shoplist[1:] )
print("item 1 to -1 is",shoplist[1:-1])
print("item start to end is",shoplist[:])

print("str 1 to 3 is",str[1:3])
print("str 1 to end is",str[1:])
print("str 1 to -1 is",str[1:-1])
print("str stard to end is",str[:])
"""
bri = set(["rose","jack","tome"])
if "rose" in bri:
    print("True!")
bric = bri.copy()
bric.add("china")
if bric.issuperset(bri):
    print("True!")
bri.remove("rose")
print(bri&bric)
