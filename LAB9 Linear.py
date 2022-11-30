global Value
Value = [7, 10, 12, 14, 16, 20, 29, 37]

def linear(Value, n, x):
    for i in range(0, n):
        if (Value[i] == x):
            return i
    return -1

print("Value = ",Value)
x = input("Enter Number for Searching Algorithm :")
x = int(x)

n = len(Value)
res = linear(Value, n, x)

if (res == -1):
    print("not found")
else:
    print("found at index: ", res)
