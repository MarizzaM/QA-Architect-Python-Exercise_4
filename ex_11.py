def min_number(a, b, c):
    if a != b and a != c and b != c:
        if a < b and a < c:
            return a
        elif b < c:
            return b
        else:
            return c
    else:
        return 'Similar numbers'


num = min_number(-1, -9, -15)
print(num)
