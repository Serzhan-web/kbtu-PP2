def uqsas(nums, nums1):
    result = []
    for num in nums1:
        if num in nums:
            result.append(num)
    return result

numbers_str = input("enter list numbers: ")
numbers_list = list(map(int, numbers_str.split()))

numbers_str1 = input("enter list numbers1: ")
numbers_list1 = list(map(int, numbers_str1.split()))

res = uqsas(numbers_list, numbers_list1)
print(res)
