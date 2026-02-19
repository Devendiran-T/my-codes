# # list
# a = [1,2,3,4,5,6,7,8,9,0]
# b = [10,20,30,40,50,60,70,80,90,100]
# e = ["app", "web", "apk"]

# # list index
# print(a[1])
# print(b[0])

# # list slice
# print(a[1:4])

# # list concatenation
# c = a + b
# print(c)

# # repetition list
# d = a * 3
# print(d)

# # list length
# print(len(a))

# # list membership

# print(3 in a)
# print(20 in b)

# # list methods
# a.reverse()
# print(a)
# b=a.copy()
# print(a)
# a.append(6)
# print(a)

# a.remove(3)
# print(a)

# a.insert(0, 0)
# print(a)

# a.extend(e)
# print(a)

# a.pop(1)
# print(a)

# # index (before clear)
# print(a.index(5))

# # sort (only numbers part)
# num_list = [1,2,3,4,5]
# num_list.sort()
# print(num_list)

# print(a.count(6))
# print(e.count("app"))

# # list comparison
# print(a == e)

# # list comprehension
# squares = [x**2 for x in num_list]
# print(squares)

# # clear at last
# a.clear()
# print(a)

# #map reduse lamda fun
# num=(1,2,3,4,5)
# def fun(x):
#     return x*2
# result=list(map(fun,num))
# print(result)

# f=list(filter(lambda x:x%2==0,num))
# print(f)   

# #reduce
# from functools import reduce
# num=(1,2,3,4,5,6,7,8,9,10)
# sum=reduce(lambda x,y:x+y,num)
# print(sum)

# from functools import reduce
# num=(1,2,3,4,5,6,7,8,9,10)
# e=list(filter(lambda x:x%2==0,num))
# print("e=",e)
# sum=reduce(lambda x,y:x+y,num)
# print("sum=",sum)
# f=list(filter(lambda x:x%2==0,num))
# print("f=",f)
# sum=reduce(lambda x,y:x+y,f)
# print("sum of even numbers=",sum)

# #palindrome
# a=input("enter a string:")
# if a==a[::-1]:
#     print("palindrome")  
# else:
#     print("not palindrome") 
    
#without using slicing
# a=input("enter a string:")  
# rew=""
# for i in a:
#     rew=i+rew  
# if a==rew:
#     print("palindrome") 
# else:
# #     print("not palindrome")

# def reverse_number(n):
#     rev = 0
#     while n > 0:
#         rev = rev * 10 + n % 10
#         n //= 10
#     return rev

# print(reverse_number(123))

#anagram

# s1 = input("Enter first word: ")
# s2 = input("Enter second word: ")

# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not an anagram")

#climbing stairs
# n = int(input("Enter number of steps: "))

# if n == 1:
#     print(1)
# elif n == 2:
#     print(2)
# else:
#     a = 1   
#     b = 2  

#     for i in range(3, n + 1):
#         c = a + b
#         a = b
#         b = c

#     print(b)

#fizzbuzz
# n = int(input("Enter a number: "))  
# for i in range(1, n + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")      
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
    
#single number
# def singleNumbers(nums):
#     result = []
#     for i in nums:
#         if nums.count(i) == 1:
#             result.append(i)
#     return result

# print(singleNumbers([1,1,1,2,2,3,3,4,5]))

# def singleNumber(nums):
#     for i in nums:
#         if nums.count(i) == 1:
#             return i
#     return None




#sign of the product of an array
# def arraySign(self, nums):
#         sign = 1
        
#         for num in nums:
#             if num == 0:
#                 return 0
#             elif num < 0:
#                 sign = -sign
        
#         return sign

#union

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# union_list = list(set(list1) | set(list2))

# print("Union:", union_list)

# #imtersections
# intersection_list = list(set(list1) & set(list2))   
# print("Intersection:", intersection_list)
#     #union using loops
# union_list = list1.copy()
# for item in list2:
#     if item not in union_list:
#         union_list.append(item)
# print("Union using loops:", union_list)

#adding digits until single digit
# num=23
# print(1+(num-1)%9)