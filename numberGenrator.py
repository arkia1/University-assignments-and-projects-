import random

def generate_float_list(size):
    float_list = [round(random.uniform(0, 10), 0) for i in range(size)]  
    return float_list

def check_conditions(float_list, student_number_digits):
    found = False

    repeated_numbers = []
    for i in range(len(float_list) - 1):
        if float_list[i] == float_list[i + 1]:
            found = True
            repeated_numbers.append((float_list[i], i, i + 1))
    
    if repeated_numbers:
        print("\nSuccessive repeated numbers and their positions:")
        for num, pos1, pos2 in repeated_numbers:
            print(f"Number: {num}, Positions: {pos1}, {pos2}")

    matching_numbers = []
    for i, num in enumerate(float_list):
        for digit in student_number_digits:
            if round(num, 0) == digit:  
                found = True
                matching_numbers.append((num, i))

    if matching_numbers:
        print("\nNumbers matching student number digits and their positions:")
        for num, pos in matching_numbers:
            print(f"Number: {num}, Position: {pos}")

    if not found:
        print("\nNo successive repeated numbers or matching digits found.")
    
    return found


def main():
    student_number = 20235443
    last_two_digits = student_number % 100  # Get last two digits
    student_number_digits = [int(digit) for digit in str(student_number)]  # Get individual digits of student number

    # Generate a list of random floats with size equal to last two digits of the student number
    float_list = generate_float_list(last_two_digits)
    
    print(f"Generated list of {last_two_digits} random floats:")
    print(float_list)

    # Check conditions and print the output
    result = check_conditions(float_list, student_number_digits)

    print("\nOutput of the function:", result)

# Run the main function 

main()