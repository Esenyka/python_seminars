file_info = []

with open('input.txt', 'r') as file:
    for line in file:
        file_info.append(line.rstrip())

len_list = file_info[0]
list1 = file_info[1].split(' ')
list1 = [int(i) for i in list1]

positive = [i for i in list1 if i > 0]
sum_positive = 0
for i in positive:
    sum_positive += i

list1_max_index = list1.index(max(list1))
list1_min_index = list1.index(min(list1))

c = 0
times_from_max_min = 1
if list1_min_index < list1_max_index:
    while list1_min_index < list1_max_index-1:
        times_from_max_min = times_from_max_min * list1[list1_min_index + 1]
        list1_min_index += 1
elif list1_max_index < list1_min_index:
    while list1_max_index < list1_min_index-1:
        times_from_max_min = times_from_max_min * list1[list1_max_index + 1]
        list1_max_index += 1


with open('output.txt', 'w') as out_file:
    out_file.write(f"{sum_positive, times_from_max_min}")
