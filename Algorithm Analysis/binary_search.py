from random import randint


def binary_search_iterative(arr: list, target: int):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target: 
            left = mid + 1  
        else: 
            right = mid - 1  
    return -1

def binary_search_recursive(arr: list, target: int, left: int, right: int):
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


array = sorted([randint(1, 1000) for _ in range(500)])
target = int(input("Enter target: "))
position = binary_search_iterative(array, target)

if position == -1:
    print("Target not in list")
else:
    print(f"Target {target} at position {position}")

array = sorted([randint(1, 1000) for _ in range(500)])
position = binary_search_recursive(array, target, 0, len(array) -1)

if position == -1:
    print("Target not in list")
else:
    print(f"Target {target} at position {position}")