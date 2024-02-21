import re 


with open("row.txt") as f:
    data = f.read()


print("Task 1")
matches = re.findall(r"a.*b", data)
print(matches)