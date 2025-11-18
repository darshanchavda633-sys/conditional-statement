num=int(input("Enter a number ="))

if num%5 == 0 and num%11 == 0:
    print(f"{num} is divisible 5 and 11")
else:
    print(f"{num} is not divisible 5 and 11")