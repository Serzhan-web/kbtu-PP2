def count_letters(letter):
    upper=0
    lower=0
    for i in letter:
        if i>="A" and i<="Z":
            upper+=1
        else:
            lower+=1
    print("sum upper case:", upper)
    print("sum lower case:", lower)
            
        

soilem=str(input("enter sentence:"))
count_letters(soilem)