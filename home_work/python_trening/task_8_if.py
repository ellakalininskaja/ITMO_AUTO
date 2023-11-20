# прграмма проверяет является число положительным или отрицательным и выводит соответствующее сообщение.

num = 0

# также попробуйте др.варианты num
# num = -5
# num = 0

if num >=0:
    print("число больше либо равно 0")
else:
    print("число отрицательное")
# str_2 содержит в себе str_1 ?

str_1 = "test"
str_2 = "test1"
if str_1 in str_2: print("yes")

num_float = -4.5

# num_float = 0
# num_float = -4.5
if num_float > 0:
    print("положительное число")
elif num_float == 0:
    print("0")
else:
    print("число отрицательное")

permit_print = True

if num > 0 and permit_print:
    print("num - положительное число")
elif not permit_print:
    print("печать запрещена")

kurs = 19
if 0 < kurs <= 4:
    print("бакалавр")
elif 5 <= kurs <= 6:
    print("магистр")
elif 7 <= kurs <= 9:
    print("аспирант")
else:
    print("введите корректный год обучения")

num1 = 2
if num1 > 100 or num1 < -100:
    print("-")
else:
    print("+")




