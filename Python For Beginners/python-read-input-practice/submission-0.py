def add_two_numbers() -> int:
    pass
    arr = []
    nums = input()
    two = nums.split(",")

    for i in two:
        arr.append(int(i))
    value = arr[0] + arr[1]
    return value




# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
