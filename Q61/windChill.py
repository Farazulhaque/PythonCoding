# Requirement 1 -> Calculate and return windchill based on a given
# temperature and wind speed
# here V is wind speed and T is temperature in fahrenheit
def calculateWindChill(V, T):
    windChill = 35.74 + 0.6215 * T - 35.75 * (V ** 0.16) + 0.4275 * T * (V ** 0.16)
    return windChill


# Requirement 2 -> Convert temperature from celsius to fahrenheit
def convertToFahrenheit(temperature):
    T = (temperature * 9/5) + 32
    return T


def main():
    temperature = float(input("What is the temperature? "))
    # Requirement 3 -> get temperature in celsius or fahrenheit
    F_or_C = input("Favrenheit or Celsius (F/C)? ")
    # If celsius (C) then convert to fahrenheit
    if F_or_C.lower() == "c":
        T = convertToFahrenheit(temperature)
    else:
        T = temperature
    # Requirement 4 -> loop through wind speeds from 5 to 60, incrementing by 5
    for windSpeeds in range(5, 61, 5):
        V = windSpeeds
        # Calculate wind chill
        windChill = calculateWindChill(V, T)
        # Requirement 5 -> Display the wind chill value to 2 decimal precision
        print(f"At temperature {T}F, and wind speed {V} mph, the windchill is: {round(windChill,2)}F")


main()
