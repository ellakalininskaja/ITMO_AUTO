# 1
def max_number(a: int, b: int):
    if a > b:
        return a
    else:
        return b


print(max_number(0, 6))


# 2
def number135(a: int, b: int):
    if a - b == 135 or b - a == 135:
        return "yes"
    else:
        return "no"


print(number135(-135, 1))


# 3
def season(a: int):
    if a in range(1, 3) or a == 12:
        return "зима"
    if a in range(3, 6):
        return "весна"
    if a in range(6, 9):
        return "лето"
    if a in range(9, 12):
        return "осень"


print(season(12))


# 4
def number3(a: int, b: int, c: int):
    if a > 10 and b > 10 and c > 10:
        return "yes"
    else:
        return "no"


print(number3(12, 2, 15))


# 5
def number5(list_of_number):
    count = 0
    for i in list_of_number:
        if i > 0:
            count = count + 1
    return count


print(number5([1, 2, 3, -2, 5]))


# 6
def day(a: int, b: int):
    return a * b * 29


print(day(2, 5))
