num = int(input("Enter a number = "))

i = 1
sum = 0

while i < num:
    if num % i == 0:
        sum += i
    i += 1

if sum == num:
    print("It is a Perfect number")
else:
    print("It is not a Perfect number")