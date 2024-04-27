def common_divisor(args):
    if len(args) == 0:
        return 0
    result = []
    count = 0
    div = 2
    while div <= min(args):
        for element in args:
            if element % div != 0:
                break
            count += 1
        if count == len(args):
            result.append(div)
        div += 1
        count = 0

    return result

