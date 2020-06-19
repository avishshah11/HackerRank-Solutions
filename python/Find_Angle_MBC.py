import math


x = int(input(""))         # x = AB
y = int(input(""))         # y = BC

print(str(int(round(math.degrees(math.atan2(x,y))))) +'°')

