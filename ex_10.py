def getInRange(min_value, max_value):

    while True:
        num = int(input('Please enter number: '))
        if max_value > num > min_value:
            return num


number = getInRange(10, 100)
print(number)
