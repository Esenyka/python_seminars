sum_nums = int(input())
times_nums = int(input())

D = (sum_nums**2) - (4 * times_nums * 1)

x = ((D ** 0.5) - sum_nums) / (2 * -1)
y = (-(D ** 0.5) - sum_nums) / (2 * -1)

print(f"{x} {y}")
