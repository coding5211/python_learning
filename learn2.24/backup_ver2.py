import os
import time

source = ["/Users/yanwenchao/notes"]
target_dir = "/Users/yanwenchao/backup"
today = target_dir + os.sep + time.strftime("%Y%m%d")
now = time.strftime("%H%M%S")
target = today + os.sep +now + ".zip"
if not os.path.exists(today):
    os.mkdir(today)
    print("SUccessfully cerated directory",today)

zip_command ="zip -r {0} {1}".format(target," ".join(source))

print("zip command is")
print(zip_command)
print("running:")
if os.system(zip_command) == 0:
    print("successful backup to ",target)
else:
    print("back failed")
