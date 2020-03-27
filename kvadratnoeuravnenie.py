print('a is not equal to 0')
a = float(input())
b = float(input())
c = float(input())

D = b ** 2 - 4 * a * c
print("D = %.2f" % D)

if D>0:
    x1 = (-b + D**0.5) / (2 * a)
    x2 = (-b - D**0.5) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1,x2))
elif D == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("no roots")
    

