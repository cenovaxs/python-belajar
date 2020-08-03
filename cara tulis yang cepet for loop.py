nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list = [n*n for n in nums if n % 2 == 0]
counter = 0
max_index = len(nums)
my_list2 = []
while counter < max_index:
    num = nums[counter]
    counter = counter + 1
    if num % 2 == 0:
        my_list2.append(num*num)

print(my_list2)
print(my_list == my_list2)
