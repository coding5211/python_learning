# coding=UTF-8
class Robot:
    """表示一个带有名字的机器人"""

    # 一个类变量，用以计数机器人的数量
    population = 0

    def __init__(self,name):
        """初始化数据"""
        self.name = name
        print("(Initializing {})".format(self.name))
        #当有人被创建时机器人将增加人口的数量
        Robot.population += 1
    def die(self):
        """我挂了"""
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} is last one".format(self.name))
        else:
            print("there are skill {:d} robots working".format(Robot.population))
    def say_hi(self):
        """来自机器人的诚挚问候"""
        print("Greetings,my masters call me {}".format(self.name))
    @classmethod
    def how_many(cls):
        """打印当前人口数量"""
        print("we have {:d} robots.".format(Robot.population))

droid1 = Robot("jack")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("rose")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")
print("Robots have finished wheir work,So let's destory them")

droid2.die()
droid1.die()

Robot.how_many()
