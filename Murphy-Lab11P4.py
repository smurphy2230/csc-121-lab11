# h = quantity of hot dogs, c = quantity of chips, s = quantity of sodas
h = float(input("Enter the number of hot dogs sold :"))
c = float(input("Enter the number of chips sold :"))
s = float(input("Enter the number of sodas sold :"))
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

