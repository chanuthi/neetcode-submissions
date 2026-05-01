def divide_numbers(a: str, b: str) -> None:
    pass    
    try:
        num1 = int(a)
        num2 = int(b)
        value = num1 / num2
        print(value)
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except ValueError:
        print("Error: Invalid value!")


    


# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
