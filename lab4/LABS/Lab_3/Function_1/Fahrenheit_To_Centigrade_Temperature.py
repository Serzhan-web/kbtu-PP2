#2
def Fahrenheit_To_Centigrade(Fahrenheit):
    c =  (5 / 9) * (Fahrenheit - 32)
    return f"{Fahrenheit} Fahrenheit = {c} Celsius."

Fahrenheit = int(input("Input a Fahrenheit degree to convert: "))
print(Fahrenheit_To_Centigrade(Fahrenheit), '\n')
