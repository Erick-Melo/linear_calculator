print("Integer Number Calculator")
a=int(input("Enter the first number: "))
b=int(input("Enter de second number: "))
print("Choose an option:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division ")
c=int(input(": "))
if c == 1:
    print(a+b)
elif c == 2:
    print(a-b)
elif c == 3:
    print(a*b)
elif c == 4:
    print(a/b)
else:
    print("Invaid Option!")
