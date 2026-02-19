# sum= 0
# for i in range(1, 100,2):
#         print(i)
#         sum =i+sum
# print("Total odd numbers:", sum)

# sum = 0
# for i in range(2, 101, 2):
#     print(i)
#     sum = sum + i
# print("Total even numbers:", sum)

# numbers = [1,2,3,4,50]
# total = 0
# for num in numbers :
#     total += num
# print("Average:",total/len(numbers))
 
# for i in range(1,11):
#  sum=i*5
#  print(i,"x5=",sum)

# n = 5
# for i in range(1, n+1):
#     print("1" * i)

# n = 100
# for i in range(n,0, -1 ):
#     print("*" * i)

#while

# sum = 0
# i = 1
# while i < 100:
#     print(i)
#     sum = sum + i
#     i = i + 2
# print("Total odd numbers:", sum)

# sum = 0
# i = 2
# while i <= 100:
#     print(i)
#     sum = sum + i
#     i = i + 2
# print("Total even numbers:", sum)

#i = 1
# while i <= 10:
#     result = i * 5
#     print(i, "x 5 =",result)
#     i += 1

# n = 5
# i = 1
# while i <= n:
#     print("@" * i)
#     i += 1

# n = 100
# i = n
# while i > 0:
#     print("*" * i)
#     i -= 1

# numbers = [1, 2, 3, 4, 50]
# total = 0
# i = 0
# while i < len(numbers):
#     total += numbers[i]
#     i += 1
# print("Average:", total / len(numbers))

# total_seats = 50    
# seat_number = 1     
# while seat_number <= total_seats:   
#     name = input("Enter passenger name: ")   
#     print("Seat", seat_number, "booked for", name) 
#     seat_number += 1   
# print("All seats are booked!")

# n = int(input("Enter number of terms: "))
# t1 = 0
# t2 = 1
# for i in range(n):
#     print(t1)
#     t3 = t1 + t2
#     t1 = t2
#     t2 = t3

t1 = 0
t2 = 1

n=int(input("enter the number: "))
for i in range(n):
    next = t1 + t2
    print(next)
    t1 = t2
    t2 = next  
