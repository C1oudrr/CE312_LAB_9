global Value
Value = [7, 10, 12, 14, 16, 20, 29, 37]

def binary(Value, lo, hi, x):
    if hi >= lo:
        mid = (hi + lo) // 2
        if Value[mid] == x:
            return mid

        elif Value[mid] > x:
            return binary(Value, lo, mid - 1, x)

        else:
            return binary(Value, mid + 1, hi, x)

    else:
        return -1

print("Value = ",Value)
x = input("Enter Number for Searching Algorithm :")
x = int(x)

res = binary(Value, 0, len(Value) - 1, x)

if res != -1:
    print("found at index: ",(res))
else:
    print("not found")