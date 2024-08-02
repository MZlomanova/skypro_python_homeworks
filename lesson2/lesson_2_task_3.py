import math

def square(side):
    if side.find('.') != -1 :
        sideInt = math.ceil(float(side))
        return sideInt * sideInt
    return int(side) * int(side)

inp = input("Введите сторону квадрата ")

s = square(inp)
print(s)
