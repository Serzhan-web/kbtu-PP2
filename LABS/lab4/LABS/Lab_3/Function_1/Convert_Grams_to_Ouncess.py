#1
def convert(grams):
    ounces = grams * 28.3495231
    return f"{grams} grams equals to {ounces} ounces"

grams = int(input("Enter a grams: "))
print(convert(grams), '\n')
