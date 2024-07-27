def input_numbers_to_added(first_number, second_number):
    return first_number + second_number

def input_numbers_to_subtracted(first_number, second_number):
    return first_number - second_number

def main():
    try:
        first_number = float(input("first number (first_number): "))
        second_number = float(input("second number (second_number): "))
    except Error:
        print("Only numerical values needed.")
        return

    add_input_result = input_numbers_to_added(first_number, second_number)
    subtract_input_result = input_numbers_to_subtracted(first_number, second_number)

    print(f"The sum of {first_number} and {second_number} is: {add_input_result}")
    print(f"The difference of {first_number} and {second_number} is: {subtract_input_result}")

if __name__ == "__main__":
    main()
