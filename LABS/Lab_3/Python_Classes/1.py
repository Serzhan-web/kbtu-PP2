#1:
class OutLine:

    def __init__(self):

        self.line = ""

    def get_str(self):
        self.line = input("Enter a string: ")

    def prin_tstr(self):

        return self.line.upper()

jol = OutLine()

jol.get_str()

print("Upper str:", jol.prin_tstr())
