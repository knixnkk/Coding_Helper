def findLonely(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    lonely = []
    for num in nums:
        if (count[num] == 1 and 
            (num + 1) not in count and 
            (num - 1) not in count):
            lonely.append(num)
    
    return lonely

print("Test Case 1: Original example")
print(findLonely([10,6,5,8]))  
