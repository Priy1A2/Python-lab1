# string = input("Enter the string: ")
# dict = {}
 
# for i in string:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1
 
# print("Count of all characters in GeeksforGeeks is :\n "
#       + str(dict))



# 3
# import math
# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# ans = math.gcd(a, b)
# print("Gcd of", a , "&", b , "=", ans)

# ans2 = math.lcm(a,b)
# print("lcm of",a,"&",b,"=", ans2)





# 2

# birthdays = {
#     'Rama': 'January 15',
#     'Shyam': 'March 20'
# }

# print(f"Rama is born on {birthdays['Rama']} and Shyam is born on {birthdays['Shyam']}.")

# rama_birthdate = birthdays['Rama']
# shyam_birthdate = birthdays['Shyam']

# rama_year = 2007
# shyam_year = 2010


# current_year = 2024
# rama_age = current_year - int(rama_year)
# shyam_age = current_year - int(shyam_year)

# print(f"Rama turns {rama_age} years on date {rama_birthdate} and Shyam turns {shyam_age} years on date {shyam_birthdate}.")



# 4

# import math
# x1 = int(input("Enter x coordinate of ball 1: "))
# y1 = int(input("Enter y coordinates of ball 1: "))
# x2 = int(input("Enter x coordinate of ball 2: "))
# y2 = int(input("Enter y coordinate of ball 2: "))
# r1 = int(input("Enter radius of ball1: "))
# r2 = int(input("Enter radius of ball2: "))

# d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
# r = r1 + r2

# if d < r:   print("Balls are colliding")
# else: print("Balls are not colliding")




# 5

# import statistics

# n = [1, 2, 3, 4, 5, 2, 6, 1, 5, 2]
# n.sort()
# mean = 0
# median = 0
# mode = 0

# for i in n:
#     mean = mean + i

# print("Mean: ", mean)

# length = len(n)
# if length%2==0: median = n[length//2 ]
# else: median = n[length//2 - 1]
# print("Median: ", median)


# print("Mode:",statistics.mode(n))








# 6




nums = list(map(int, input("Enter list: ").split()))
print("0 : bubble sort, 1 :merge sort, 2 : selection sort, 3 :insertion sort")
which_sort = int(input("Enter suitable number: "))
def bubble_sort(nums :list[int]) -> list[int]:
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
     
    return nums

def insertion_sort(nums: list[int]) -> list[int]:
    n = len(nums)
    if n <= 1:
        return nums
    
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    
    return nums

def selection_sort(nums :list[int]) -> list[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] < nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
    return nums

def merge(nums: list[int], l :int, m :int, r :int):
    n1 = m - l + 1
    n2 = r - m
    
    left = [0] * n1
    right = [0] * n2
    
    for i in range(0, n1):
        left[i] = nums[l + i]
        
    for j in range(0, n2):
        right[j] = nums[m + 1 + j]
        
    i = 0
    j = 0
    k = l
    
    while i < n1 and j < n2:
        if left[i] <= right[i]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1        
        k += 1
    
    while i < n1:
        nums[k] = left[i]
        i += 1
        k += 1
    
    while j < n2:
        nums[k] = right[j]
        j += 1
        k += 1
            
            
def merge_sort(nums: list[int], l :int, r :int):
    if l < r:
        m = l + (r - 1) // 2
        
        merge_sort(nums, l, m)
        merge_sort(nums, m + 1, r)
        merge(nums, l, m, r)




match  which_sort:
    case 0:
        print(bubble_sort(nums))
    case 1:
        merge_sort(nums, 0, len(nums) - 1)
        print(nums)
    case 2:
        print(selection_sort(nums))
    case 3:
        print(insertion_sort(nums)) 
    case default:
        print("Invalid option")