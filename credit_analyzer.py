from datetime import datetime

# Classify the credit score based on FICO ranges
def check_credit(score):
    match score:
        case s if 300 <= s <= 579:
            return "Poor"
        case s if 580 <= s <= 669:
            return "Fair"
        case s if 670 <= s <= 739:
            return "Good"
        case s if 740 <= s <= 799:
            return "Very Good"
        case s if 800 <= s <= 850:
            return "Excellent"
        case _:
            return "Invalid score"

def main():
    # Prompt user for credit score input
    credit = input("Credit score:\n")

    # Attempt to convert input to an integer
    try:
        score = int(credit)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Get credit score category
    category = check_credit(score)
    print(f"Your credit is {score}, in the category {category}")

    # Log the result to a file with timestamp
    with open("log.txt", "a") as log:
        log.write(
            f"User input: {score} – Result: {category} – Time: {datetime.now().strftime('%Y-%m-%d %I:%M %p')}\n"
        )

if __name__ == "__main__":
    main()