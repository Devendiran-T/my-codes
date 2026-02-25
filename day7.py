
#pascle triangle
# def pascal_triangle(n):
#     triangle = []
#     for i in range(n):
#         row = [1] * (i + 1)
#         for j in range(1, i):
#             row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
#         triangle.append(row)
#     return triangle
# n = int(input("Enter the number of rows for Pascal's Triangle: "))
# result = pascal_triangle(n)
# for row in result:
#     print(row)
        

# climbing stairs
# def climb_stairs(n):
#     if n <= 2:
#         return n
#     return climb_stairs(n-1) + climb_stairs(n-2)

# n = int(input("Enter number of steps: "))
# print("Number of ways:", climb_stairs(n))   

#fizz buzz
# def fizz_buzz(n):
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)
# n = int(input("Enter a number: "))
# fizz_buzz(n)

#majarity element
# nums = list(map(int, input("Enter numbers: ").split()))

# for num in nums:
#     if nums.count(num) > len(nums) // 2:
#         print("Majority Element:", num)

#         break

#Detect Capital
# class Solution:
#     def detectCapitalUse(self, word: str) -> bool:
        
#         if word == word.upper():
#             return True
        
#         if word == word.lower():
#             return True
#         if word[0].isupper() and word[1:] == word[1:].lower():
#             return True
        
#         return False

# Pizza Bill Generator

print("Welcome to the Pizza Bill Shop!")
print("Pizza Category")
print("1. Delux")
print("2. Normal")

category = int(input("Enter the category of pizza (1/2): "))

print("\nPizza Type")
print("1. Veg")
print("2. Non-Veg")

pizza_type = int(input("Enter the type of pizza (1/2): "))

# Base Price Calculation
if category == 1 and pizza_type == 1:
    base_price = 300
    print("You selected Delux Veg Pizza. Price: Rs.", base_price)

elif category == 1 and pizza_type == 2:
    base_price = 500
    print("You selected Delux Non-Veg Pizza. Price: Rs.", base_price)

elif category == 2 and pizza_type == 1:
    base_price = 200
    print("You selected Normal Veg Pizza. Price: Rs.", base_price)

elif category == 2 and pizza_type == 2:
    base_price = 400
    print("You selected Normal Non-Veg Pizza. Price: Rs.", base_price)

else:
    print("Invalid input.")
    exit()

# # Extra Cheese
# extra_cheese_charge = 0
# extra_cheese = input("Do you want extra cheese? (yes/no): ").lower()
# if extra_cheese == "yes":
#     extra_cheese_charge = 100

# # Extra Toppings
# extra_toppings_charge = 0
# extra_toppings = input("Do you want extra toppings? (yes/no): ").lower()
# if extra_toppings == "yes":
#     extra_toppings_charge = 100

# # Water Bottle
# water_total = 0
# water_bottle = input("Do you want water bottle? (yes/no): ").lower()
# if water_bottle == "yes":
#     count = int(input("Enter number of bottles: "))
#     water_total = 20 * count

# # Takeaway
# takeaway_charge = 0
# takeaway = input("Do you want takeaway? (yes/no): ").lower()
# if takeaway == "yes":
#     takeaway_charge = 20

# # Total calculation
# total_cost = base_price + extra_cheese_charge + extra_toppings_charge + water_total + takeaway_charge

# # GST calculation (18%)
# gst = total_cost * 0.18
# net_amount = total_cost + gst

# # Bill Format
# print("\n--------------------------------")
# print("       ** Pizza Bill **")
# print("--------------------------------")
# print("Base Price           =", base_price)
# print("Extra Cheese         =", extra_cheese_charge)
# print("Extra Toppings       =", extra_toppings_charge)
# print("Water Bottle         =", water_total)
# print("Take Away Charges    =", takeaway_charge)
# print("--------------------------------")
# print("Total Cost           =", total_cost)
# print("GST (18%)            =", round(gst, 2))
# print("--------------------------------")
# print("Net Amount Payable   =", round(net_amount, 2))
# print("--------------------------------")