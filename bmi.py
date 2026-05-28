height=float(input('enter your height in m'))
weight=float(input('enter your weight in kg'))
bmi=weight/height**2
if bmi <= 18.4:
    print ('you are under weight')
elif bmi <= 24.9:
    print('you are healthy')
elif bmi <=29.9:
    print('you are overweight')
elif bmi <= 34.9:
    print('you are severely overweight')
else:
    print('you are obese')