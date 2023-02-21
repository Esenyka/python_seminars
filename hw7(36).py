def print_operation_table(operation, num_rows=6, num_columns=6):
    res = []
    for i in range(1, num_rows+1):
        rows = []
        res.append(rows)
        for g in range(1, num_columns+1):
            rows.append(i * g)
    c = 1
    while c != num_rows:
        g = 1
        while g != num_columns:
            res[c][g] = operation(res[c][0], res[0][g])
            g += 1
        c += 1

    for i in res:
        print(i)


print_operation_table(lambda x, y: x + y)

