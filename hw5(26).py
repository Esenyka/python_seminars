# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
# с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def powNums(a, b):
    if b == 1:
        return a
    else:
        return a * powNums(a, b-1)


user_a = int(input('введите цифру '))
user_b = int(input('введите степень '))

print(powNums(user_a, user_b))
