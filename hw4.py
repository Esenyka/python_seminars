#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается
# сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input())
m = int(input())
k = int(input())

if k < m * n and (k % m == 0 or k % n == 0):
    print("yes")
else:
    print("no")