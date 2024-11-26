import openai

# Function to get hints using OpenAI API
def get_movie_hints(api_key, question):
    openai.api_key = api_key
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Generate hints for a movie guessing game based on: {question}. Provide 3 hints in a list.",
            max_tokens=100,
            temperature=0.7
        )
        return response["choices"][0]["text"].strip().split("\n")
    except Exception as e:
        print("Error fetching hints:", e)
        return []

# Main game function
def play_movie_guessing_game():
    print("Welcome to the Movie Guess Game!")
    
    # Get OpenAI API key from user
    api_key = input("Enter your OpenAI API Key: ")
    if not api_key:
        print("API Key is required to generate hints!")
        return

    # Input movie-related question
    question = input("Enter a question or movie name to generate hints: ")

    # Fetch hints using ChatGPT
    print("Fetching hints...")
    hints = get_movie_hints(api_key, question)
    if not hints:
        print("Could not generate hints. Try again.")
        return
    
    # Display hints
    print("\nHints for the game:")
    for i, hint in enumerate(hints, 1):
        print(f"Hint {i}: {hint}")

    # Initialize game variables
    points = 0
    guessed_correctly = False

    while not guessed_correctly:
        print("\nMake your guess!")
        print("Options: [1] Guess Full Name, [2] Guess Main Star, [3] Guess Other Info, [4] Pass")
        choice = input("Your choice (1-4): ")

        if choice == "1":
            guess = input("Enter your guess for the movie name: ").strip().lower()
            if "movie_name" in question.lower():  # Replace with the actual movie name
                print("Correct! You guessed the movie name.")
                points += 5
                guessed_correctly = True
            else:
                print("Wrong guess.")
                points -= 2

        elif choice == "2":
            guess = input("Enter your guess for the main star: ").strip().lower()
            if "main_star" in question.lower():  # Replace with the actual main star
                print("Correct! You guessed the main star.")
                points += 4
                guessed_correctly = True
            else:
                print("Wrong guess.")
                points -= 2

        elif choice == "3":
            guess = input("Enter your guess for other info: ").strip().lower()
            if "some_info" in question.lower():  # Replace with actual other info
                print("Correct! You guessed additional info.")
                points += 2
            else:
                print("Wrong guess.")
                points -= 2

        elif choice == "4":
            print("You passed this turn.")
            points += 0

        else:
            print("Invalid choice. Try again.")
        
        print(f"Your current points: {points}")

    # End game
    print("\nGame Over!")
    print(f"Final Score: {points}")
    print("Thank you for playing!")

# Run the game
if __name__ == "__main__":
    play_movie_guessing_game()
