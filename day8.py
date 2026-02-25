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


#srack-LIFO OR FILO
#operations
#1)push--> insert
#2)pop--> delete
#3)peek--> top element

#isEmpty-check stack empty
#SIZE-number of items

#PUSH-add an item at top
#1)create empty stack
#2)input value
#3)add value to stack
#4)print stack

#pseudocode
# push(data)
# if(stack is full)
#     print("Stack overflow")
# else
#     top=top+1
#     stack[top]=data

#pop(data)
# if(stack is empty)
#     print("Stack underflow")
# else
#     data=stack[top]
#     top=top-1
#     return data

# stack = []

# while True:
#     print("1.Push 2.Pop 3.Peek 4.Display 5.Exit")
#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         value = int(input("Enter data to push: "))
#         stack.append(value)
#         print("Pushed:", value)

#     elif choice == 2:
#         if not stack:
#             print("Stack empty")
#         else:
#             value = stack.pop()
#             print("Popped value:", value)

#     elif choice == 3:
#         if not stack:
#             print("Stack empty")
#         else:
#             print("Top element:", stack[-1])

#     elif choice == 4:
#         print("Stack:", stack)

#     elif choice == 5:
#         print("Exiting...")
#         break

#     else:
#         print("Invalid choice. Please try again.")
    


# operations
# 1)enqueue--> insert an item at rear
# 2)dequeue--> delete an item from front


# queue = []

# while True:
#     print("1.Enqueue 2.Dequeue 3.Display 4.Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         value = int(input("Enter data to enqueue: "))
#         queue.append(value)
#         print("Enqueued:", value)

#     elif choice == 2:
#         if not queue:
#             print("Queue empty")
#         else:
#             value = queue.pop(0)
#             print("Dequeued value:", value)

#     elif choice == 3:
#         print("Queue:", queue)

#     elif choice == 4:
#         print("Exiting...")
#         break

#     else:
#         print("Invalid choice. Please try again.")


#circular queue

size = 5
# queue = [None] * size
# front = -1
# rear = -1

# def enqueue(value):
#     global front, rear
    
#     if (rear + 1) % size == front:
#         print("Queue Full")
#         return
    
#     if front == -1:
#         front = 0
    
#     rear = (rear + 1) % size
#     queue[rear] = value
#     print(value, "inserted")

# def dequeue():
#     global front, rear
    
#     if front == -1:
#         print("Queue Empty")
#         return
    
#     removed = queue[front]
    
#     if front == rear:
#         front = rear = -1
#     else:
#         front = (front + 1) % size
    
#     print(removed, "removed")

# def display():
#     if front == -1:
#         print("Queue Empty")
#         return
    
#     i = front
#     print("Queue elements:")
    
#     while True:
#         print(queue[i], end=" ")
#         if i == rear:
#             break
#         i = (i + 1) % size
#     print()

# while True:
#     print("\n1.Enqueue")
#     print("2.Dequeue")
#     print("3.Display")
#     print("4.Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         value = int(input("Enter value: "))
#         enqueue(value)

#     elif choice == 2:
#         dequeue()

#     elif choice == 3:
#         display()

#     elif choice == 4:
#         break

#     else:
#         print("Invalid choice")

