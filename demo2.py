# type_student=(input("enter the student type (MGSH/MGSDS)="))
# tuition_fee=float(input("enter the tuition fee="))
# bus_fee=float(input("enter the bus fee="))
# hostel_fee=float(input("enter the hostel fee="))
# if type_student=="MGSDS":
#     total_fee=(tuition_fee*1.5) + bus_fee
#     print('total amount of MGSDS fee',total_fee)
# elif type_student=="MGSH":
#     total_fee=(tuition_fee*1.5) + hostel_fee
#     print('total amount of MGSH fee',total_fee)
# else:
#     print("invalid type of student:please enter the student type")

# store_balance = float(input("Enter the store balance: "))
# store_withdraw = float(input("Enter the amount to withdraw: "))

# if store_withdraw > 10000:
#     print("The withdrawal amount exceeds the limit. You can't withdraw $", store_withdraw)

# elif store_withdraw < 0:
#     print("Invalid input. Please enter a valid withdrawal amount")

# elif store_withdraw > store_balance:
#     print("Insufficient balance. You cannot withdraw $", store_withdraw)

# elif store_withdraw == store_balance:
#     print("You have withdrawn all your money. Your new balance is $0")

# else:
#     new_balance = store_balance - store_withdraw
#     print("The new balance is $", new_balance)

# account_balance = float(input("Enter the account balance: "))
# account_pin = int(input("Enter the account PIN: "))
# if account_pin == 9696:
#     print("Correct PIN. Transaction is processing...")
#     withdraw_amount = float(input("Enter the amount to withdraw: "))
#     if withdraw_amount > account_balance:
#         print("Insufficient balance.")
#     elif withdraw_amount <= 0:
#         print("Invalid amount.")
#     else:
#         account_balance -= withdraw_amount
#         print("Withdrawal successful.")
#         print("Remaining balance:", account_balance)
# else:
#     print("Wrong PIN. Access declined.")
 
# age=int(input("entr ur age: "))
# child=149
# adult=249
# senior=199
# if age< 18:
#     print("the ticket price is $", child)
# elif age >=18 and age <60:
#     print("the ticket price is $", adult)
# elif age >60:
#      print("the ticket price is $", senior)   
# else:
#     print("error")

age = int(input("Enter your age: "))
time = input("Enter show time (morning/evening): ")
baby = 0
child = 149


adult = 249
senior = 199
if age < 5:
    price = baby
elif age >= 5 and age < 18:
    price = child
elif age >= 18 and age < 60:
    price = adult
elif age >= 60:
    price = senior
else:
    print("Invalid age")
if time == "morning":
    discount = price * 0.20
    price = price - discount
    print("Morning show discount applied (20%)")
elif time == "evening":
    pass
else:
    print("Invalid show time")
print("Final ticket price is $", price)
