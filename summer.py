
temperature = float(input("Enter the current temperature in °C: "))

if temperature >= 45:
    print(" Extremely Hot! Stay indoors and keep hydrated")
elif 35 <= temperature < 45:
    print(" Very Hot! Avoid going out in the afternoon.")
elif 30 <= temperature < 35:
    print(" Warm and sunny — typical Indian summer day")
elif 25 <= temperature < 30:
    print(" Pleasant for summer, enjoy the breeze!")
else:
    print(" Cooler than usual for summer — might be pre-monsoon showers")
