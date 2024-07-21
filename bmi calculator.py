def get_user_input():
    """Get weight and height from the user and validate the input."""
    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            height = float(input("Enter your height in meters: "))
            if weight <= 0 or height <= 0:
                raise ValueError("Weight and height must be positive numbers.")
            return weight, height
        except ValueError as e:
            print(e)
            print("Please enter valid numbers for weight and height.")

def calculate_bmi(weight, height):
    """Calculate BMI using the formula: BMI = weight / (height ** 2)."""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify the BMI into health categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")
    weight, height = get_user_input()
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)
    
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Health category: {category}")

if __name__ == "__main__":
    main()
