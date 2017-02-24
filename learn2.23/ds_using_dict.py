ab={
    "Rose":"rose@rose.com",
    "Jack":"jack@jack.com",
    "Tom":"tom@tom.ocm"
}
print("rose's address is",ab["Rose"])
del ab["Tom"]
print("\nThere are {} contacts in the address-book\n".format(len(ab)))
for name,address in ab.items():
    print("Contact {} at {}".format(name,address))
ab["Guido"]="guido@qq.com"
if "Guido" in ab:
    print("Guido's address is",ab["Guido"])
