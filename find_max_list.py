def find_max(numbers):
    max_num = 0
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(find_max([4, 9, 1, 17, 2]))
print(find_max([-5, -9, -2, -12]))
print(find_max([42]))