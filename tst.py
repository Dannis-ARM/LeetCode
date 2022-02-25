def numberTwoArray(num):
    res = []
    while(num / 10 > 1):
        digit = num % 10
        res.insert(0, digit)
        num = int(num/10)
    res.insert(0, num)
    return res


print(numberTwoArray(12312))

print(int(0.6))
