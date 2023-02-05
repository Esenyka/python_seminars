dict_points_english = {1: 'A, E, I, O, U, L, N, S, T, R', 2: 'D, G', 3: 'B, C, M, P',
                       4: 'F, H, V, W, Y', 5: 'K', 8: 'J, X', 10: 'Q, Z'}

word = input("Ввелите слово на английском - ")
word = word.upper()
result = 0
c = 0

while c != len(word):
    i = 0
    for i in dict_points_english:
        if c == len(word):
            break
        if word[c] in dict_points_english[i]:
            result += i
            c += 1


print(result)

