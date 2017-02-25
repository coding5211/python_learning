import sys
import time

f = None
try:
    f = open("poem.txt")
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line,end="")
        sys.stdout.flush()
        print("Press now")
        time.sleep(2)
except IOError:
    print("no")
except KeyboardInterrupt:
    print("yes")
finally:
    if f:
        f.close()
    print("cleaning")
