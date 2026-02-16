units=int(input("input num of units"))

if units<50:
    bill=units*2.60+25
elif units<100:
     bill=units*3.25+35
elif units<200:
     bill=units*5.26+45
else:
     bill=units*8.45+75
    
print("electricity bill",bill)