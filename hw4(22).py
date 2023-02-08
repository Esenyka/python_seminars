n = int(input("len n - "))
m = int(input("len m - "))

s_n = input().split(' ')
s_m = input().split(' ')

s_n = set(s_n)
s_m = set(s_m)
result = []

for i in s_n:
    for j in s_m:
        if i == ' ':
            pass
        elif i == j:
            result.append(int(i))

result.sort()
print(result)



