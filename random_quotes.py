import requests  # pip install requests
import pyperclip  # pip install pyperclip


# Function to fetch a random quote from the API
def fetch_random_quote():
    try:
        response = requests.get('https://dummyjson.com/quotes/random')
        if response.status_code == 200:
            data = response.json()
            # Fixed key name from 'quotes' to 'quote'
            return {"quote": data["quote"], "author": data["author"]}
        else:
            print("Error fetching quote. Try again later.")
            return None
    except requests.exceptions.RequestException as e:  # Fixed typo in exception name
        print(f"An error occurred: {e}")
        return None


# Function to display the menu (Moved outside of fetch_random_quote)
def display_menu():
    print("\nWelcome to the quote generator written in Python")
    print("1. Generate a new random quote")
    print("2. Copy the quote to clipboard")
    print("3. Exit")


# Main application function (Moved outside of fetch_random_quote)
def run_quote_generator():
    current_quote = None

    while True:
        display_menu()
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            current_quote = fetch_random_quote()
            if current_quote:
                print(f"Quote: {current_quote['quote']}")
                print(f"Author: {current_quote['author']}")
        elif choice == "2":
            if current_quote:
                quote_text = (
                    f"{current_quote['quote']} - {current_quote['author']}"
                )
                pyperclip.copy(quote_text)
                print("Your quote has been copied to the clipboard!")
            else:
                print("Generate a quote first.")
        elif choice == "3":
            print("Thank you for your time. Goodbye.")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 3.")


# Run the application (Called at the root level of the script)
if __name__ == "__main__":
    run_quote_generator()