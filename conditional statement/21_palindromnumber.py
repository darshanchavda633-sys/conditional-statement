num=int(input("Enter number ="))

original=num
rev=0
if num > 0:
    while num > 0:
        digit=num%10
        rev=rev*10+digit
        num//=10
if rev == original:
    print("number is palindrom")
else:
    print("number is not palindrom")