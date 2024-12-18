# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: Celsius = (Fahrenheit - 32) * 5/9
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

if __name__ == "__main__":
    try:

        fahrenheit = float(input("Fahrenheit: "))


        celsius = fahrenheit_to_celsius(fahrenheit)

        # gay lol
        print(f"{fahrenheit}°F is  {celsius:.2f} in °C.")
    except ValueError:
        print("not valid number ):")
        # ):
