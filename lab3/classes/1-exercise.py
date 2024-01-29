class String:
    def __init__(self):
        self.input_string = ""

    def getstring(self):
        self.input_string = input("soz: ")

    def string_uppercase(self):
        print("Uppercase string:", self.input_string.upper())


mystring = String()


mystring.getstring()
mystring.string_uppercase()
