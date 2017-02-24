shoplist = ["apple","banana","mango","carrot"]

print("i have",len(shoplist),"items to purchase")

print("These items are:",end=" ")
for itme in shoplist:
    print(itme,end=" ")
print("\n I also have to buy rice")

shoplist.append("rice")
print("My shoping list is now",shoplist)
print(" I will sort my list now")
shoplist.sort()
print("Sorted shoping list is",shoplist)

print("THe first item i will buy is ",shoplist[0])
olditem=shoplist[0]
del shoplist[0]
print("i bought the ",olditem)
print("My shoping list is now",shoplist)
