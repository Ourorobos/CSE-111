import math
from datetime import datetime

#this is section is added to exced the requierments

size = input("Enter Tire size in the format of 205/55R16")
w, size = size.split('/')
try:
    r,d = size.split('R')
except:
    try:
        r,d = size.split('r')
    except:
        print('ERROR!!')
        #I know this is not the best way to do this

w = int(w)
r = int(r)
d = int(d)

#w = int(input("Enter width:"))
#r = int(input("Enter Aspect Ratio:"))
#d = int(input("Enter Diameter:"))

a = w*r+2540*d
a *= math.pi*w**2*r
a /= 10000000000
a = round(a,2)

print(f"~{a} Liters in Volume")

time = datetime.now()
data = f'date:{time:%y-%m-%d},width:{w},ratio:{r},diameter:{d},volume{a}'

with open("volumes.txt","a") as file:
    file.write(data)
    file.write('\n')
