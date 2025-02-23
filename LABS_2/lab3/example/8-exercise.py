def averages(numbers):
    running_sum = 0
    k=0
    running_averages = []

    for num in numbers:
        running_sum+=num
        k+=1
        s=running_sum/k
        running_averages.append(s)
    return running_averages
        

numbers_str = input("Enter numbers: ")
numbers_list = list(map(float, numbers_str.split()))
averages = averages(numbers_list)
print("Running Averages:", averages)
