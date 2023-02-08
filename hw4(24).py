bush_num = int(input())
berry_num = input()

berry_num = berry_num.split(" ")

work_list = []
for i in berry_num:
    work_list.append(int(i))

res_list = []
index = 0
while True:
    if index == bush_num:
        break
    elif index == bush_num-1:
        r = work_list[index] + work_list[0] + work_list[index-1]
        res_list.append(r)
        index += 1
    elif index == 0:
        r = work_list[index] + work_list[1] + work_list[-1]
        res_list.append(r)
        index += 1
    else:
        r = work_list[index] + work_list[index+1] + work_list[index-1]
        res_list.append(r)
        index += 1

print(max(res_list))





