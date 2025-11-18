salary=int(input("Enter salary = "))

if salary>=50000:
    bonus=salary*10/100
    print("bonus is =", bonus)
    print("salary plus bonus =", salary+bonus)
elif salary >30000:
    bonus=salary*5/100
    print("bonus is =",bonus)
    print("salary plus bonus =",salary+bonus)
elif salary >= 10000 and salary <= 30000:
    bonus=salary*3/100
    print("bonus is =",bonus)
    print("salary plus bonus =",salary+bonus)
else:
    print("no bonus add in salary")
    
