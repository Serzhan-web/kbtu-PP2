#4
def is_prime(N):
    if N <= 0 or N == 1: return False
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            return False
    return True

def filter_prime(yournums):
    prime_list = []
    for i in yournums:
        if is_prime(i): prime_list.append(i)
    return prime_list

lst = list(map(int, input("Введите числа через пробел: ").split()))
print(filter_prime(lst))
