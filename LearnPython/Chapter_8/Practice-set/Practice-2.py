def CelToFar(tempC): 
    tempF = (tempC * 1.8) + 32
    return float(tempF)

far = CelToFar(float(input("Enter the temperature in celcius. ")))
print(f"The tempearture in fahrenheit is : {far}")