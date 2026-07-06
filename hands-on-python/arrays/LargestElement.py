# Find the largest element in an array
arr = [3, 15, 2, 1, 9]

largest = arr[0]
for num in arr:
    if largest < num:
        largest = num

print(largest)
