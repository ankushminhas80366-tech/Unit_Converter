"""
Simple command-line unit converter.
Supports length (km <-> miles), weight (kg <-> pounds), and temperature (C <-> F).
"""

def convert_length():
    """Prompt the user and convert between kilometers and miles."""

    print("----Length Converter----")
    print("1: For Km to Miles")
    print("2: For Miles to Km")
    # Menu choice for which length conversion to run
    input_=input("Select option from above 2: ")

    if input_=="1":
        # Convert kilometers to miles using the standard factor
        km=float(input("Enter Kilometers: "))
        miles=km * 0.621371
        print(f"{km} km = {miles} miles")

    elif input_=="2":
        # Convert miles to kilometers (inverse of the factor above)
        miles=float(input("Enter Miles: "))
        km=miles/0.621371
        print(f"{miles} Miles = {km} Km")

    else:
        print("Invalid Input:")


def convert_weight():
    """Prompt the user and convert between kilograms and pounds."""

    print("----Weight Converter----")
    print("1: For Kilograms to Pounds:")
    print("2: For Pounds to Kilograms:")
    # Menu choice for which weight conversion to run
    input_=input("Select options from above 2: ")

    if input_=="1":
        # Convert kilograms to pounds
        Kilo=float(input("Enter Kilograms: "))
        Pounds=Kilo *  2.20462
        print(f"{Kilo} Kilograms = {Pounds} Pounds")

    elif input_=="3":
        # Convert pounds to kilograms
        pounds=float(input("Enter Pounds: "))
        kilo=pounds/2.20462
        print(f"{pounds} Pounds = {kilo} Kilograms")

    else:
        print("Invalid Input:")

def convert_temprature():
    """Prompt the user and convert between Celsius and Fahrenheit."""

    print("----Temprature Converter----")
    print("1: For Celsius to Fahrenhiet")
    print("2: For Fahrenheit to Celsius")
    # Menu choice for which temperature conversion to run
    input_=float(input("select options from above 2: "))

    if input_=="1":
        # Convert Celsius to Fahrenheit: F = C * 9/5 + 32
        C=int(input("Enter Celsius: "))
        F=(C * 9/5) + 32
        print(f"{C} Celsius = {F:.2f} Fahrenheit")

    elif input_=="2":
        # Convert Fahrenheit to Celsius: C = (F - 32) * 5/9
        F=int(input("Enter Fahrenheit: "))
        C=(F-32)*5/9
        print(f"{F} Fahrenheit = {C:.2f} Celsius")

    else:
        print("Invalid Input:")
   
    
def main():
    """Show the main menu and dispatch to the selected converter."""
    print("----Welcome in Unit Converter----")
    print("1 : For Convert Length:")
    print("2 : For Convert Weight:")
    print("3 : For Convert Temprature:")
    # Top-level menu: length, weight, or temperature
    choice=input("Select options from above 3: ")
    if choice=="1":
        convert_length()
    elif choice=="2":
        convert_weight()
    elif choice=="3":
        convert_temprature()
    else:
        print("Invalid Input:")


# Run the program only when this file is executed directly
if __name__=="__main__":
    main()
