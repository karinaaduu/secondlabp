import math

print("Введите координаты точки (x;y)")
x, y =map(float, input().split())
if y>=0 and y<=1 and x>=-1 and x<=1: 
    if (y-math.fabs(x))>=0:
        print("Данная точка принадлежит заштрихованной части")
    else:
        print("Данная точка не принадлежит заштрихованной части")
else:
    print("Данная точка не принадлежит заштрихованной части")
    
