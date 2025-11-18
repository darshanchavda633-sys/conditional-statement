num=int(input("Enter a number ="))

original=num
sum=0

while num > 0:
    digit=num%10
    sum=sum+digit*digit*digit
    num//=10
if sum==original:
    print("Number is Armstrong")
else:
    print("Number is Not Armstrong")
    