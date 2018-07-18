def calc(x, y, ran_op):
# argument
    if ran_op == "+":
        res = x + y
    elif ran_op == "-":
        res = x - y
    elif ran_op == "*":
        res = x * y
    elif ran_op == "/":
        res = x / y
    
    return res

# call function
result = calc(8,9,"+")
print(result)

