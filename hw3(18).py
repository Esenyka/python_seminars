list1_len = int(input("Введите длину массива - "))
list1 = []

for i in range(list1_len):
    list1_nums = int(input())
    list1.append(list1_nums)

find_num = int(input("Введите желаемое число - "))

result = 0
l = []
for j in list1:
    if find_num == j:
        result = j
    else:
        l.append(abs(find_num - j))
        i = l.index(min(l))
        result = list1[i]

print(result)

