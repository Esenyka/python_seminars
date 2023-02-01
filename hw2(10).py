coins = int(input())

first_side = 0
second_side = 0
count = 0

while count != coins:
    size = int(input())
    if size > 1:
        print("Стороны всего две")
    elif size == 1:
        first_side += 1
        count += 1
    elif size == 0:
        second_side += 1
        count += 1

print(max(first_side, second_side))


