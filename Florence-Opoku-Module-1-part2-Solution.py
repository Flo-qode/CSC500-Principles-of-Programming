
def input_numbers_to_multiply(first_number, second_number):
    return first_number * second_number
def input_numbers_to_divide(first_number, second_number):
    if second_number == 0:
        return "Denomitor should be greater than zero"
    return first_number / second_number
def main():
    try:
        first_number = float(input("Input your first number (first_number): "))
        second_number = float(input("Input your second number (second_number): "))
    except Error:
        print("Only numbers allowed")
        return
    result_for_multiplication = input_numbers_to_multiply(first_number, second_number)
    result_for_division = input_numbers_to_divide(first_number, second_number)
    print(f"Multiplying {first_number} and {second_number} is: {result_for_multiplication}")
    print(f"Dividing {first_number} by {second_number} is: {result_for_division}")
if __name__ == "__main__":
    main()
