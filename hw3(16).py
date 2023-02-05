list1_len = int(input("Введите длину массива - "))
list1 = []

for i in range(list1_len):
    list1_nums = int(input())
    list1.append(list1_nums)

find_num = int(input("Введите желаемое число - "))

result = 0
print(list1)
for j in list1:
    if j == find_num:
        result += 1

print(f"Число {find_num} встречается в массиве {result} раз(а)")
