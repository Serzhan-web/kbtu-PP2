def writesome(list_of_elements):
    with open("sometext.txt", '+a') as f:
        text = "\n"
        for i in list_of_elements:
            text+=str(i)+' '
        f.write(text)
        f.close()
    
 

writesome([12345, 56789, 90987654, "dfghjkl","efrgf",34,34])