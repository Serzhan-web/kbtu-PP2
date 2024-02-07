def _reverse(strings):
    strings=list(strings.split())
    strings.reverse()
    for i in strings:
        print(i, end=" ")

k=str(input("soz:"))
_reverse(k)