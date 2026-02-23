# def fun(a,b):
#     return a+b
# print(fun(2,3))       

# def fun(a,b):
#     return a+b
# print(fun(2,3))       

# class Student:
#     def __init__(self, name, age, mark):
#         self.name = name
#         self.age = age
#         self.mark = mark
        
#         if mark >= 60:
#             self.result = "pass"
#         else:
#             self.result = "fail"

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Mark:", self.mark)
#         print("Result:", self.result)
#         print("-------------------")

# s1 = Student("deva", 20, 75)
# s2 = Student("naveen", 21, 45)

# s1.display()
# s2.display()

#   #syntax
#    class class_name:
#     def method_name(self,parameters):
#         print(result)

#celsies to fahrenheit
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = celsius_to_fahrenheit(celsius)

# print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")


# #oops
# def func(a,b)
#     return a+b
# result=func(2,3)
# print(result)

#00ps
# class student:
#     def details(self,name,mark):
        
#         if mark>=60:
#             result="pass"
#             print(result)
#         else:
#             result="fail"
# s1=student()
# s2=student()
# s1.details("john",70)                                    
# s2.details("jane",45)

#syntax
# class classname:
#     def methodname(self): 
#         print("message")    

#with constructor
# class student:
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
#     def methodname(self):
#         if self.mark>=60:
#             result="pass"
#             print(result)
#         else:
#             result="fail"
#         print("student name:",self.name)
#         print()
#         print()
# name=input("enter student name: ")
# mark=int(input("enter student mark: "))
# s1=student(name,mark)
# s1.methodname()

#celcius to fahrenheit
# array=[10,20,30,40,50]
# for c in array:
#     f=(c*9/5)+32
#     print(f"{c} degrees Celsius is equal to {f} degrees Fahrenheit.")

#BANK ACCOUNT
# class BankAccount:
#     def __init__(self, name, pin, balance=0):
#         self.name = name
#         self.__pin = pin
#         self.__balance = balance

#     def deposit(self, amt):
#         self.__balance += amt
#         print("Deposited!")

#     def withdraw(self, amt, pin):
#         if pin != self.__pin:
#             print("Invalid PIN!")
#         elif amt > self.__balance:
#             print("Insufficient Balance!")
#         else:
#             self.__balance -= amt
#             print("Withdrawn!")

#     def balance(self, pin):
#         if pin == self.__pin:
#             print("Balance:", self.__balance)
#         else:
#             print("Wrong PIN!")

# # Create Account
# name = input("Name: ")
# pin = input("Set PIN: ")
# acc = BankAccount(name, pin)

# while True:
#     print("\n1.Deposit  2.Withdraw  3.Balance  4.Exit")
#     ch = input("Choose: ")

#     if ch == "1,Deposit":
#         acc.deposit(float(input("Amount: ")))
#     elif ch == "2,Withdraw":
#         acc.withdraw(float(input("Amount: ")), input("PIN: "))
#     elif ch == "3,Balance":
#         acc.balance(input("PIN: "))
#     elif ch == "4,Exit":
#         break
    
# POLYMORPHISM

# print(len("hello"))              
# print(len([1,2,3,4,5]))          

# print(5 + 3)                   
# print("5" + "3")               

# def add(a, b):
#     return a + b

# print(add(5, 3))                
# print(add("5", "3"))            

# class animal:
#     def speak(self):
#         return "Animal speaks"
# class dog(animal):
#     def speak(self):
#         return "Woof!"
# class cat(animal):
#     def speak(self):
#         return "Meow!"
# animals = [dog(), cat()]
# for a in animals:
#     print(a.speak())
    
    
    
    

#abstaction


from abc import ABC, abstractmethod

# Step 2: Abstract Vehicle class
class Vehicle(ABC):
    def __init__(self, number, total_seats):
        self.number = number
        self.total_seats = total_seats

    @abstractmethod
    def calculate_fare(self):
        pass

    def show_details(self):
        print(f"Bus Number: {self.number}")
        print(f"Total Seats: {self.total_seats}")

# Step 5: LuxuryBus
class LuxuryBus(Vehicle):
    def calculate_fare(self):
        return 500

# Step 7: OrdinaryBus
class OrdinaryBus(Vehicle):
    def calculate_fare(self):
        return 200

# Step 9: SeatManager
class SeatManager:
    def __init__(self, total_seats):
        self.__total_seats = total_seats
        self.__booked = []

    def book_seat(self):
        if len(self.__booked) < self.__total_seats:
            seat_no = len(self.__booked) + 1
            self.__booked.append(seat_no)
            return seat_no
        else:
            return None

    def cancel_seat(self, seat_no):
        if seat_no in self.__booked:
            self.__booked.remove(seat_no)
            print(f"Seat {seat_no} cancelled successfully.")
        else:
            print("Invalid seat number!")

    def available_seats(self):
        return self.__total_seats - len(self.__booked)

# Step 13: Passenger class
class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Step 14: Ticket class
class Ticket:
    def __init__(self, passenger, bus, seat_no, fare):
        self.passenger = passenger
        self.bus = bus
        self.seat_no = seat_no
        self.fare = fare

    def show_ticket(self):
        print("----- Ticket -----")
        self.passenger.show()
        print(f"Bus Number: {self.bus.number}")
        print(f"Seat Number: {self.seat_no}")
        print(f"Fare: {self.fare}")
        print("------------------")

# Step 16: Choose bus type
print("Select Bus Type:")
print("1 → Luxury Bus")
print("2 → Ordinary Bus")
choice = input("Enter choice (1/2): ")

bus_number = input("Enter Bus Number: ")

if choice == "1":
    bus = LuxuryBus(bus_number, 5)
elif choice == "2":
    bus = OrdinaryBus(bus_number, 5)
else:
    print("Invalid choice, defaulting to Ordinary Bus")
    bus = OrdinaryBus(bus_number, 5)

# Step 18: Create SeatManager
seat_manager = SeatManager(bus.total_seats)

# Step 19: Ticket list
tickets = []

# Step 20: Menu loop
while True:
    print("\n--- Menu ---")
    print("1 → Available Seats")
    print("2 → Book Seat")
    print("3 → Cancel Seat")
    print("4 → Show Tickets")
    print("5 → Exit")

    menu_choice = input("Enter choice: ")

    if menu_choice == "1":
        print(f"Available Seats: {seat_manager.available_seats()}")

    elif menu_choice == "2":
        name = input("Enter passenger name: ")
        age = input("Enter passenger age: ")
        seat_no = seat_manager.book_seat()
        if seat_no is None:
            print("Bus Full! Cannot book seat.")
        else:
            passenger = Passenger(name, age)
            fare = bus.calculate_fare()
            ticket = Ticket(passenger, bus, seat_no, fare)
            tickets.append(ticket)
            print("Seat booked successfully!")
            ticket.show_ticket()

    elif menu_choice == "3":
        try:
            seat_no = int(input("Enter seat number to cancel: "))
            seat_manager.cancel_seat(seat_no)
            # Optional: remove ticket from tickets list
            tickets = [t for t in tickets if t.seat_no != seat_no]
        except ValueError:
            print("Invalid input!")

    elif menu_choice == "4":
        if not tickets:
            print("No tickets booked yet.")
        else:
            for t in tickets:
                t.show_ticket()

    elif menu_choice == "5":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")