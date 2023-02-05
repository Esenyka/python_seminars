dict_points = {1: 'A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т', 2: 'D, G, Д, К, Л, М, П, У',
                       3: 'B, C, M, P, Б, Г, Ё, Ь, Я', 4: 'F, H, V, W, Y, Й, Ы', 5: 'K, Ж, З, Х, Ц, Ч',
                       8: 'J, X, Ш, Э, Ю', 10: 'Q, Z, Ф, Щ, Ъ'}

word = input("Ввелите слово на - ")
word = word.upper()
result = 0
c = 0

while c != len(word):
    i = 0
    for i in dict_points:
        if c == len(word):
            break
        if word[c] in dict_points[i]:
            result += i
            c += 1

print(result)

