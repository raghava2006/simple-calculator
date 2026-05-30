print("Welcome to My Calculator")
print("Addition:")
print("Subtraction:")
print("Multiplication:")
print("Division:")
choice=input("choose operation: ")
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second number:"))
result = 0
if choice == "1":
    result=num1+num2
elif choice == "2":
    result=num1-num2
elif choice =="3":
    result=num1*num2
elif choice == "4":
    result=num1/num2
else:
    print("Invalid Choice!")
print("result=",result)