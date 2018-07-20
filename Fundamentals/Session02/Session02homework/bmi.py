weight=float(input("your weight"))
heightcm=float(input("your height"))
heightm= float(heightcm/100)
bmi=float(weight/(heightm**2))
if bmi<16 :
    print("severly underweight")
elif bmi<=18.5 :
    print("underweight")
else :
    if bmi<=25:
        print("normal")
    elif bmi<=30:
        print("overweight")
    else :
        print("obese")



