#  h = quantity of hot dogs, c = quantity of chips, s = quantity of sodas
while True:
    try:
        h = float(input("Enter the number of hot dogs sold: "))
        if h < 0:
            raise ValueError
    except ValueError:
        print("input value must be a positive number")
    else:
        h = h
        break
while True:
    try:
        c = float(input("Enter the number of chips sold: "))
        if c < 0:
            raise ValueError
    except ValueError:
        print("input must be a positive number")
    else:
        c = c
        break
while True:
    try:
        s = float(input("Enter the number of sodas sold: "))
        if s < 0:
            raise ValueError
    except ValueError:
        print("input must be positive number")
    else:
        s = s
        break
# print(h, c, s)
hp = 2.5  # hot dog price
cp = 1.5  # chip price
sp = 1.25  # soda price
ht = h*hp  # hot dog total
print(ht)
ct = c*cp  # chip total
print(ct)
st = s*sp  # soda total
print(st)
saleTotal = float(ht+ct+st)
print(f'The total sale is: ${saleTotal:.2f}')


