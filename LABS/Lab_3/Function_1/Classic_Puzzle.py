#3
def solution(heads, legs):
    rabbits = (legs - 2 * heads) //2
    chikens = heads - rabbits
    return f"Rabbits: {rabbits}  and Chikens: {chikens} "

print(solution(35,94))
