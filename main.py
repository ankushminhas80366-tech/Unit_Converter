def convert_length():

    print("----Length Converter----")
    print("1: For Km to Miles")
    print("2: For Miles to Km")
    input_=input("Select option from above 2: ")

    if input_=="1":
        km=float(input("Enter Kilometers: "))
        miles=km * 0.621371
        print(f"{km} km = {miles} miles")

    elif input_=="2":
        miles=float(input("Enter Miles: "))
        km=miles/0.621371
        print(f"{miles} Miles = {km} Km")

    else:
        print("Invalid Input:")


def convert_weight():

    print("----Weight Converter----")
    print("1: For Kilograms to Pounds:")
    print("2: For Pounds to Kilograms:")
    input_=input("Select options from above 2: ")

    if input_=="1":
        Kilo=float(input("Enter Kilograms: "))
        Pounds=Kilo *  2.20462
        print(f"{Kilo} Kilograms = {Pounds} Pounds")

    elif input_=="3":
        pounds=float(input("Enter Pounds: "))
        kilo=pounds/2.20462
        print(f"{pounds} Pounds = {kilo} Kilograms")

    else:
        print("Invalid Input:")

def convert_temprature():

    print("----Temprature Converter----")
    print("1: For Celsius to Fahrenhiet")
    print("2: For Fahrenheit to Celsius")
    input_=float(input("select options from above 2: "))

    if input_=="1":
        C=int(input("Enter Celsius: "))
        F=(C * 9/5) + 32
        print(f"{C} Celsius = {F:.2f} Fahrenheit")

    elif input_=="2":
        F=int(input("Enter Fahrenheit: "))
        C=(F-32)*5/9
        print(f"{F} Fahrenheit = {C:.2f} Celsius")

    else:
        print("Invalid Input:")
   
    
def main():
    print("----Welcome in Unit Converter----")
    print("1 : For Convert Length:")
    print("2 : For Convert Weight:")
    print("3 : For Convert Temprature:")
    choice=input("Select options from above 3: ")
    if choice=="1":
        convert_length()
    elif choice=="2":
        convert_weight()
    elif choice=="3":
        convert_temprature()
    else:
        print("Invalid Input:")


if __name__=="__main__":
    main()