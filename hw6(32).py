def findElementsFromNumToNum(list1, min_el, max_el):
    result = []
    count = 0
    for i in list1:
        if (i >= min_el) and (i <= max_el):
            result.append(count)
        count += 1

    return result


user_list = input('введите список - ')
user_list = user_list.split(',')
user_list = [int(i) for i in user_list]
user_min_el = int(input('введите минимальный элемент диапазона - '))
user_max_el = int(input('введите максимальный элемент диапазона - '))

print(findElementsFromNumToNum(user_list, user_min_el, user_max_el))





