# prompt user to enter how much they weigh in pounds
weight = int(input ("How much do you weigh (in pounds)? "))

# prompt user to enter their height in inches
height = int(input ("What is your height (in inches)? "))

# this converts weight to kilograms
weight_in_kg = weight / 2.2

# this converts height to centimeters
height_in_meter = height * 2.54 / 100

# this calculates BMI
bmi = round(weight_in_kg / (height_in_meter ** 2), 1)

if bmi <= 18.5:
    print("Oh no, your BMI is", bmi, "which means you are underwewight. Eat some food!")

elif bmi > 18.5 and bmi < 25:
     print('Congratulations! Your BMI is', bmi, 'which means you are in the normal range. Keep up the good work!')

elif bmi > 25 and bmi < 30:
     print('Uh oh, your BMI is', bmi, 'which means you are overweight. Make healthy choices and exercise!')

elif bmi > 30:
     print('Oh boy, your BMI is', bmi, 'which means you are obese. GO SEE YOUR DOCTOR~')

else:
    print('Uh oh, something went wrong.')


