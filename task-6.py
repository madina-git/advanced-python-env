a = int(input())
op = input()
b =  int(input())
if op == "+":
    result = a + b
elif op == "-":
    result = a - b 
elif op == "*":
    result = a * b 
elif op == "/":
  if b != 0:
     result = a / b
  else:
     print("Error!!")
     exit()
else:
    print("Unknown op")
    exit()
print(a, op, b, "=", result)
     

