# Reverse an array without using the built-in reverse()/[::-1]
arr = [100, 200, 300, 400, 500]
rev_arr = []

print("BEFORE REVERSE:", arr)

for i in reversed(range(len(arr))):
    rev_arr.append(arr[i])

print("AFTER REVERSE:", rev_arr)
