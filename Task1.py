def pc_case(number):
    if number < 0:
        return number
    dict_case = {'a': ['2', '3', '4'], 'ов': ['0', '5', '6', '7', '8', '9']}
    word = 'компьютер'
    number = str(number)
    for i in dict_case:
        if number[-1] in dict_case[i]:
            result = word+i
            return result
    return word





