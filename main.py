from groq_service import generate_message
from prompts import MESSAGE_TYPES, TONES


def choose_from_menu(title, options):
    """Display a numbered menu and return the selected option."""
    while True:
        print(f"\n{title}")
        for number, option in enumerate(options, start=1):
            print(f"{number}. {option}")
        choice = input("Enter your choice: ").strip()

        if choice.isdigit():
            number = int(choice)
            if 1 <= number <= len(options):
                return options[number - 1]

        print(f"Please enter a number from 1 to {len(options)}.")


def get_message():
    while True:
        message = input("\nEnter the main points/details of your message: ").strip()
        if message:
            return message
        print("Your message cannot be empty. Please try again.")


def main():
    print("=" * 55)
    print("       AI EMAIL & MESSAGE ASSISTANT")
    print("=" * 55)

    while True:
        message_type = choose_from_menu("Select message type:", MESSAGE_TYPES)
        tone = choose_from_menu("Select writing tone:", TONES)
        user_message = get_message()

        while True:
            print("\nGenerating your message. Please wait...")
            try:
                result = generate_message(user_message, message_type, tone)
                print("\n" + "=" * 55)
                print("GENERATED MESSAGE")
                print("=" * 55)
                print(result)
                print("=" * 55)
            except Exception as error:
                print(f"\nCould not generate the message: {error}")
                print("Check your internet connection and Groq API settings.")
                break

            action = choose_from_menu(
                "What would you like to do?",
                ["Regenerate message", "Create another message", "Exit"]
            )

            if action == "Regenerate message":
                continue
            if action == "Create another message":
                break
            print("\nThank you for using AI Email & Message Assistant!")
            return


if __name__ == "__main__":
    main()
