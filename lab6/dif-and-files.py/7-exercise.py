def copier():
    string = str(input("Enter the name of file: "))
    with open(string) as file:
        data = file.read()
    file.close()
    copy_path = ""
    for i in range(len(string)):
        if string[i]=='.':
            copy_path+='_1'
        copy_path+=string[i]
    with open(copy_path, "+w") as file_copy:
        file_copy.write(data)
    file.close()
    
    return 0

copier()