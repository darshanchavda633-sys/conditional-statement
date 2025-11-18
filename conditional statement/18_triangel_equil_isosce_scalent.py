a=int(input("Enter first side = "))
b=int(input("Enter second side ="))
c=int(input ("Enter third side = "))


if a+b >c and a+c >b and b+c>a:
    if a==b==c:
        print("Equilateral") 
    elif a==b or b==c or a==c:
        print("isosceles")
    else:
        print("scalene")
else:
    print("not possible triangle")