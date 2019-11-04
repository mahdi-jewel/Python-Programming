print('Enter the coefficient of a: ')
a=float(input())
print('Enter the coefficient of b: ')
b=float(input())
print('Enter the coefficient of c: ')
c=float(input())

if b*b>=(4*a*c):
    root = (((b * b) - (4 * a * c)) ** (1 / 2))
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)
    print('Root X1=',x1)
    print('Root X2=',x2)
else:
    print('invalid input')