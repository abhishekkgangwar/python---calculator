a = float(input("Enter a first number:"))
operator = input("Enter a operator(+,-,/,*,%):")
b = float(input("enter a second number:"))

if operator == "+":
    result = a+b
elif operator == "-":
    result = a-b
elif operator == "*":
    result = a*b
elif operator == "%":
    result = a%b
elif operator == "/":
    if b != 0 :
        result == a/b
    else:
       result = "cannot divide by zero"
else :
    result = "inavalid operator"

print("Result:",result)