# Find the largest and second-largest elements in one pass
arr = [3, 1, 6, 9]

largest = second_largest = float("-inf")

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif largest > num > second_largest:
        second_largest = num

print("Largest:", largest)
print("Second Largest:", second_largest)
