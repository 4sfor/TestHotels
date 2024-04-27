def table(number):
    if number < 0:
        return number
    table = []
    row = []
    count = 1
    for i in range(1, number + 1):
        while count <= number:
            row.append(i * count)
            count += 1
        table.append(row)
        row = []
        count = 1

    for element in table:
        for elem in element:
            print(elem, end='\t')
        print('\n')





