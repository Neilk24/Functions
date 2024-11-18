def add(P, Q):
    return P+Q
def subtract(P, Q):
    return P-Q
def multiply(P, Q):
    return P*Q
def divide(P,Q):
    return P/Q

print("Please choose which operation you would like to do: ")
print("a. addition")
print("b. subtraction")
print("c. multiplication")
print("d. division")
print("a/b/c/d")

choice=input("")
num_1=int(input("Please enter your first number: "))
num_2=int(input("Please enter your second number: "))

if choice=='a':
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice=='b':
    print(num_1, "-", num_2, "=", subtract(num_1, num_2))
elif choice=='c':
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))
elif choice=='d':
    print(num_1, "/", num_2, "=", divide(num_1, num_2))
else:
    print("This is not a valid input. PLease try again")