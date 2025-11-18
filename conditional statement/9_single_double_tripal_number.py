num=int(input("Enter a number ="))

if num <= 9:
    print(f"{num} is single-digit ")
elif num < 100:
    print(f"{num} is double-digit")
else:
    print(f"{num} is tripal - digit")