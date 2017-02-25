"""
with open("poem.txt") as f:
    for line in f:
        print(line,end="")

def get_error_details():
    return (2,"details")

errnum,errstr = get_error_details()
print(errnum)
print(errstr)

points = [
    {"x":2,"y":3},
    {"x":4,"y":1}]
print(points)
points.sort(key=lambda i:i["y"])
print(points)

listone = [2,3,4]
listone = [2*i for i in listone if i >2]
print(listone)

def powersum(power,*args):
    total = 0
    for i in args:
        total += pow(i,power)
    return total

print(powersum(2,3,4))

mylist = ["item"]
assert len(mylist) >=1
print(assert len(mylist) >=1)
"""
from time import sleep
from  functools import wraps
import logging
logging.basicConfig()
log = logging.getLogger("retry")

def retry(f):
    @wraps(f)
    def wrapped_f(*args,**kwargs):
        MAX_ATTEMPTS = 5
        for attempt in range(1,MAX_ATTEMPTS+1):
            try:
                return f(*args,**kwargs)
            except:
                log.exception("Attempt %s/%s failed :%s",attempt,MAX_ATTEMPTS,(args,kwargs))
                sleep(10 * attempt)
        log.critical("All %s attempts failed : %s",MAX_ATTEMPTS,(args,kwargs))
    return wrapped_f
counter = 0
@retry
def save_to_database(arg):
    print("装饰器还没学懂")
    print("下一步重点学习Python装饰器")
    global counter
    counter += 1
    if counter < 2:
        raise  ValueError(arg)
if __name__ == "__main__":
    save_to_database("我也不清楚我写的是什么，但是今天有点累了")
