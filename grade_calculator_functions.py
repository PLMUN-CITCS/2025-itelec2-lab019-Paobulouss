def get_student_score():
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a number.")

def calculate_grade(score):
    return 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F'

def main():
    print(f"Your Grade is: {calculate_grade(get_student_score())}")

if __name__ == "__main__":
    main()
