n = int(input())
count = 0
for i in range(n):
    if 2 ** count == i:
        print(i, end=' ')
        count += 1
