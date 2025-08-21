def main():
    weight = float(input("Enter your weight(lbs): "))
    height = float(input("Enter your height(in): "))
    bmi = ((weight * 703) / (height**2))
    formatted = "{:.1f}".format(bmi)

    print(f"Your BMI is {formatted}.")
    if bmi < 18.5:
        print("Your BMI indicates that you are underweight.")
    elif bmi > 25: 
        print("Your BMI indicates that you are overweight.")
    else:
        print("Your BMI indicates that you are at an optimal weight.")


main()