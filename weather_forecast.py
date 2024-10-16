class InvalidValue(Exception):
    pass

def fconversion(temp):
    # (f-32) * 5 / 9
    try:
        f = float(temp)
        if f < -80 or f > 134:
            raise InvalidValue
        celsius = (f-32) * 5 / 9
    except InvalidValue:
        print(f"{temp} is below or above recorded temperatures")
    except ValueError:
        print(f"{temp} is not a valid temperature.")
    else:
        print(f"{temp} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
    finally:
        print("Thank you for using the weather application.")

# ask for f temp
# else block "100 degree Fahrenheit is 37.78 degrees Celsius"
# finally block to thank user

temp = input("What's the temperature in Fahrenheit?")
fconversion(temp)