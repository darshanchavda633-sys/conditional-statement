ch=input("Enter a character =")

if ch >= 'A' and ch <= 'Z':
    print(f"{ch} Uppercase")
elif ch >='a' and ch <= 'z':
    print(f"{ch} Lowercase")
elif ch >='0' and ch<='9':
    print(f"{ch} Digit")
else:
    print(f"{ch} Symbol")
