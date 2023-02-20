poem = input().split(' ')
russian_vowels = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']
vowels_list = [list(filter(lambda x: x in russian_vowels, poem[i])) for i in range(len(poem))]
res_list = [len(i) for i in vowels_list]

if len(set(res_list)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')
