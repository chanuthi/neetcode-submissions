def remove_fourth_character(word: str) -> str:
    pass
    b = word[0:3]
    a = word[4:len(word)]
    return b+a

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
