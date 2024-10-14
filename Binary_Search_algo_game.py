

def get_user_number():
    while True:
        try:
            number = int(input("What is the number I'm thinking of? "))
            if 0 <= number <= 100:
                return number
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

def simple_search(number):
    print("I'll guess the number using simple search.")
    for i in range(101):
        print(f"Is the number {i}?")
        if i == number:
            print("Yay! I guessed it!")
            break

def binary_search(number):
    print("I'll guess the number using binary search.")
    low = 0
    high = 100
    for _ in range(5):
        mid = (low + high) // 2
        print(f"Is the number {mid}?")
        user_input = input("Is the number higher (h) or lower (l)? \nclick any other button if the guess is correct. ")
        if user_input == "h":
            low = mid + 1
        elif user_input == "l":
            high = mid - 1
        else:
            print("Invalid input. Please try again.")
        if mid == number:
            print("Yay! I guessed it!")
            break
    else:
        print("I didn't guess it. Better luck next time!")


number = get_user_number()
print("I'm thinking of a number between 0 and 100. You have 5 chances to guess it.")

while True:
    choice = input("Do you want to use simple search or binary search? (simple/binary): ")
    if choice == "simple":
        simple_search(number)
        break
    elif choice == "binary":
        binary_search(number)
        break
    else:
        print("Invalid choice. Please try again.")

