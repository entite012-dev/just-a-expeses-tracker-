import csv
import os
#creating empty list
a = []
p = []
#adding function and taking input 
def add_expense():
    name = input("Name: ")
    food = int(input("Food expense: "))
    travel = int(input("Travel expense: "))
    a.append({"name": name, "food": food, "travel": travel})
    p.append(food+travel)

#save function
def save():
    file_exists = os.path.exists("expenses.csv")
    with open("expenses.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "food", "travel"])
        if not file_exists:
            writer.writeheader()
        writer.writerows(a)
    print("Saved!")
#view function 
def view():
    print(a)

#total function 

def total():
    print(f"this is your sum of expenses {p}")
# asking loop
while True:
    print("1. Add  2. View  3. Exit 4. sum")
    x = input("Choice: ")
    if x == "1":
        add_expense()
        save()
    elif x == "2":
        view()
    elif x == "3":
        break
    elif x=="4":
        total()
