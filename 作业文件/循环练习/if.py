x=float(input("Enter your age: "))
if x>=18:
    print("You are eligible to vote.")
elif x<0:
    print("Age cannot be negative.")
elif x<18:
    print("You are not eligible to vote.")
elif x==18:
    print("You are eligible to vote.")
elif x>1000:
    print("Age cannot be greater than 1000.")
else:
    print("Invalid input.")

