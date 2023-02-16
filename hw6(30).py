def arithmeticProgression(el1, step, num_elements):
    count = 0
    while count != num_elements:
        print(el1)
        el1 += step
        count += 1


arithmeticProgression(int(input('Введите первый элемент - ')), int(input('Введите шаг - ')), int(input('Введите кол-во элементов - ')))
