def convert_temperature():
    print("Welcome to the Temperature Converter!")
    
    try:
        temp = float(input("Enter the temperature value: "))
        unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()

        if unit == "C":
            converted = (temp * 9/5) + 32
            print(f"{temp}°C is equal to {converted:.2f}°F")
        elif unit == "F":
            converted = (temp - 32) * 5/9
            print(f"{temp}°F is equal to {converted:.2f}°C")
        else:
            print("Invalid unit! Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        print("Invalid input! Please enter a numeric temperature value.")

convert_temperature()