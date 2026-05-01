from typing import List

def read_integers() -> List[int]:
    pass
    nums = []
    number_string = input()
    string_list = number_string.split(",")

    for i in string_list:
        nums.append(int(i))
    return nums


    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
