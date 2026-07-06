# Move all zeroes in the array to the end while keeping the
# relative order of the non-zero elements
arr = [1, 0, 3, 4, 0, 6]

j = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1

print(arr)
