a=int(input("Enter a fist number = "))
b=int(input("Enter a second number = "))
c=int(input("Enter a third number = "))
d=int (input("Enter a forth number = "))

smallest=a

if b < smallest:
    smallest=b
if c < smallest:
    smallest=c
if d < smallest:
    smallest=d
print("smllest number is = ",smallest)