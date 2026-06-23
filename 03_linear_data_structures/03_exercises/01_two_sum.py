
# Solution one 
def two_sum(nums, target):
    element_count = len(nums)
    for i in range(element_count - 1):
        for j in range(i + 1, element_count):
            if nums[i] + nums[j] == target:
                return [i, j]


result = two_sum([2, 7, 11, 15], 9)  # [0, 1]
print(result)


# Solution two
def two_sum_2(nums, target):
    # First, we store the each number along with its index numbers in a dictionary. 
    numbers_map = {}
    for i in range(len(nums)):  
        key = nums[i]
        numbers_map[key] = i

    # Then, we check against the dictionary to find the pair
    for i in range(len(nums)):  
        needed_num = target - nums[i]
        if needed_num in numbers_map and numbers_map[needed_num] != i:
            return [i, numbers_map[needed_num]]


result_2 = two_sum_2([2, 7, 11, 15], 14)
print(result_2)
