nums = [1,2,3,4,5,6,7,8,9]
my_list=[n*n for n in nums]
counter = 0
max_index = len(nums)
my_list2 = []
while counter < max_index:
    num = nums[counter]
    counter = counter + 1
    if num % 2 == 0:
        my_list2.append(num*num)
my_list3 = list(map(lambda n: n*n if x % 2 == 0, nums))
print(my_list3)
print(my_list2 == my_list == my_list3)
