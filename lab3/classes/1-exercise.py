class String():
    def getstring(self):
        self.sentence=input("Sentense:")
    def printstring(self):
        print("Wizh upper case:"+self.sentence.upper())
        
mystring=String()
mystring.getstring()
mystring.printstring()