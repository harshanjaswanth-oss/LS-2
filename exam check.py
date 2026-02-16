
medicalcause=(input("do you have a medical cause?"))

if medicalcause=="Y":
    print("you are eligible for the exam")
else:                                  
    attendance=int(input("enter your attendance"))
    if attendance>=75:
       print("you are eligible for the exam")
    else:
        print("you are not eligible for the exam")