import csv
import os

a = []
p = []
def add_expense():
    name = input("Name: ")
    food = int(input("Food expense: "))
    travel = int(input("Travel expense: "))
    a.append({"name": name, "food": food, "travel": travel})
    p.append(food+travel)

def save():
    file_exists = os.path.exists("expenses.csv")
    with open("expenses.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "food", "travel"])
        if not file_exists:
            writer.writeheader()
        writer.writerows(a)
    print("Saved!")

def view():
    print(a)



def total():
    print(f"this is your sum of expenses {p}")

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
