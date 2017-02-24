"""
import  mymoudle
mymoudle.say_hi()
print("Version",mymoudle.__version__)
"""

from mymoudle import say_hi,__version__
say_hi()
print(__version__)



import sys
a=5
del a
print(dir())
