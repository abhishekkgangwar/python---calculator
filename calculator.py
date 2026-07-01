a = float(input("Enter the first number: "))
operator = input("choose an operator(+, -, /, *, %): ")
b = float(input("Enter the second number: "))

if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "%":
    if b != 0:
        result = a % b
    else:
        result = "Cannot take modulo by zero"
elif operator == "/":
    if b != 0 :
        result = a / b
    else:
       result = "cannot divide by zero"
else :
    result = "Invalid operator"

print("Result:",result)
