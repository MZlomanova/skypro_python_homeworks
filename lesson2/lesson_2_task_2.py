def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

inp = input("Введите год: ")
res = is_year_leap(int(inp))
print('год ' + inp + ': ' + str(res))