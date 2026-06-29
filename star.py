count = 9

while count >= 1:
    num = 1
    while num <= count:
        print("*", end="")
        num = num + 1
    print()
    count = count - 2
count = 1
while count <= 5:
    num = 1
    while num <= count*2 - 1 :
        print("*", end="")
        num = num + 1
    print()
    count = count + 1



count =1 
while count <= 5 :
    num = 1
    while num <= count:
        print(count , end="")
        num = num + 1
    print()
    count = count + 1

num = int(input("Enter the number of rows: "))
i = 1
while i <= num:
    j = 1
    while j <= num:
        if i== 1 or i == num or j == 1 or j == num:
            print("*", end="")
        else:
            print(" ", end="")
        j += 1
    print("")
    i += 1

name = ["Shiv", "Mohan", "Rohan", "Kavita", "Kamal"]

# index 0,1,2,3,4

# Reverse the given list

# Method 1 :

# index = 0
# while index < len(name)/2 :

#     lastIndex = len(name) - 1 - index
    
#     temp = name[index]

#     name[index] = name[lastIndex]
#     name[lastIndex] = temp

#     index = index + 1

# print(name)


# Methods 2 :

# reverseName = []

# index = len(name) - 1
# while index >= 0:
#     reverseName.append(name[index])
#     index = index - 1

# print(name)
# print(reverseName)

# Que 1. Count how many odd numbers are present.
# nums = [3,6,2,5,8,9,12]


# oddCounts = 0
# i = 0
# while i <= len(nums) - 1:
#     if i % 2 != 0:
#         oddCounts = oddCounts + 1
#     i = i + 1


# print(oddCounts)

# ------------------------

# names = ["Himanshu", "Anjali", "Ayushi", "Shreya", "Anjali", "Shreya" , "Anup", "Shreya"]

# def countPresence(list = [], searchName=""):
#     count = 0
#     i = 0
#     while i <= len(list) - 1:
#         if searchName == list[i]:
#             count = count + 1
#         i = i + 1
#     print(count)

# names = {
#     "Himanshu" : 1,
#     "Anjali":2,
#     "Ayushi" : 1,
#     "Anup" : 1,
#     "shreya" : 3
# }

# countPresence(names, "Himanshu")

# --------------------------

# employees = [
#   { "name": "Aarav Sharma", "yearsOfExperience": 2, "joiningYear": 2024 },
#   { "name": "Priya Singh", "yearsOfExperience": 5, "joiningYear": 2021 },
#   { "name": "Rahul Verma", "yearsOfExperience": 8, "joiningYear": 2018 },
#   { "name": "Sneha Gupta", "yearsOfExperience": 3, "joiningYear": 2023 },
#   { "name": "Vikram Yadav", "yearsOfExperience": 10, "joiningYear": 2016 },
#   { "name": "Ananya Mishra", "yearsOfExperience": 1, "joiningYear": 2025 },
#   { "name": "Rohan Patel", "yearsOfExperience": 6, "joiningYear": 2020 },
#   { "name": "Neha Kapoor", "yearsOfExperience": 4, "joiningYear": 2022 },
#   { "name": "Nikita Sharma", "yearsOfExperience": 3, "joiningYear": 2023 },
#   { "name": "Harsh Vardhan", "yearsOfExperience": 5, "joiningYear": 2021 },
#   { "name": "Tanvi Kulkarni", "yearsOfExperience": 10, "joiningYear": 2016 },
#   { "name": "Deepak Saxena", "yearsOfExperience": 16, "joiningYear": 2010 },
#   { "name": "Riya Bansal", "yearsOfExperience": 2, "joiningYear": 2024 },
#   { "name": "Mohit Arora", "yearsOfExperience": 12, "joiningYear": 2014 },
#   { "name": "Sakshi Choudhary", "yearsOfExperience": 6, "joiningYear": 2020 }
# ];

# i = 0

# while i <= len(employees) - 1:
    
#     if employees[i]["joiningYear"] >= 5:
#         print(employees[i]["name"])

#     i += 1

 # -------------------------
 # print first pair whose sum is zer0 [2,-2]

# nums = [3, 2, 4, 3, 5, -2, 7, 6, -4, 8]

# def sumOfZeroPair(list):
#     i = 0
#     while i <= len(nums) - 1:
#         j = i + 1
#         while j <= len(nums) - 1:
#             # print(nums[i], nums[j])
#             if nums[i] + nums[j] == 0:
#                 print(nums[i], nums[j])
#                 return 
#             j = j  + 1
#         i = i + 1

# sumOfZeroPair(nums)

# Question 1.  Write a function to check the given word is an Anagram or not

# def countEachWordChar(word):
   
#     charCounting = {}

#     for char in word:
#         if charCounting.get(char):
#             charCounting[char] =  charCounting[char] + 1
#         else:
#             charCounting[char] = 1
#     return charCounting


# def checkAnagram():
#     word1 = input("Enter a word : ") # apple
#     word2 = input("Enter a word : ") # apple

#     if len(word1) == len(word2):
#         word1Counting = countEachWordChar(word1)
#         word2Counting = countEachWordChar(word2)

#         isAnagram = True

#         for i in word1Counting:
#             if word1Counting[i] != word2Counting[i]:
#                 isAnagram = False
#                 break

#         if isAnagram:
#             print("Anagram Hai")
#         else : 
#             print("Not Anagram")
#         print(word1Counting)
#         print(word2Counting)
#     else:
#         print("Not Anagram")

# checkAnagram()

# Question 2.  Remove duplicate elements in a list.



# Question 3.  Calculate the sum of all elements. [3,6,8,9,10,34,67]



# Question 4. Find the largest element.

# nums = [3,7,9,23,4,6,8,9,1,6]
# def findMaxNumber():
#     maxNumber = nums[0]
#     for num in nums:
#         if num > maxNumber:
#             maxNumber = num

#     print(maxNumber)

# findMaxNumber()

# Question 5. Find the smallest element.

# def findMinNumber():
#     minNumber = nums[0]
#     for num in nums:
#         if num < minNumber:
#             minNumber = num

#     print(minNumber)
# findMinNumber()

# Question 6. Check whether a given number exists in the list.

# def findElement(list, el):
#     for i in range(len(list)):
#         if list[i] == el:
#             print(i)
#             return True
#         else:
#             return False

# print(findElement([1,6,2,4,6], 4))

# Question 7. Find the second largest number.

# nums = [1,12,6,7,8,9] # 9
nums = [12,6,7,8,9, 12] # 9
# nums = [12, 12] # -1

def findSecondLargestNum(list):
    largestNum = float("-inf")
    secondLargestNum = float("-inf")

    for num in list:
        if num > largestNum:
            secondLargestNum = largestNum
            largestNum = num
        elif num > secondLargestNum and largestNum != num:
            secondLargestNum = num
    
    print(secondLargestNum, largestNum)



findSecondLargestNum(nums)

# Question 8. Find the second smallest number.



# Question 9. Count the frequency of each element.



# Question 10. Move all zeros to the end.

# inp = [4,0,9,6,0,34,0,12]
# out = [4,9,6,34,12, 0,0,0]