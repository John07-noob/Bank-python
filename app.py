# This Bank project created by John07-noob
# Sep/24/2020

from os import system, name
from time import sleep

data = "balance"

def inputNumber(number):
    while True:
        try:
            userInput = int(input(number))
        except ValueError:
            print("Just Enter The Number Please.")
            continue
        else:
            return userInput
            break

def clear_screen():
    x = system('clear')

def shutdown():
    x = 0
    clear_screen()
    for i in range(4):
        print(f"Shutdown in {x}")
        sleep(1)
        clear_screen()
        x = x + 1


def check():
    with open(f"{data}.txt", "r") as file:
        print(f"Your Balance: {file.read()}")

def deposit():
    bank_in = inputNumber("Enter Deposit Amount: ")
    with open(f"{data}.txt", "r") as file:
        balance = int(file.read())
        balance_now = balance + bank_in
        print(f"You just deposit {bank_in}")
    with open(f"{data}.txt", "w") as file:
        file.write(str(balance_now))

def withdraw():
    bank_out = inputNumber("Enter Withdraw Amount: ")
    with open(f"{data}.txt", "r") as file:
        balance = int(file.read())
        print(f"Your Balance Now: {balance - bank_out}")
        balance_now = balance - bank_out
    with open(f"{data}.txt", "w") as file:
        file.write(str(balance_now))
    
#Main Code
while True:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. EXIT")
    user = input("Enter your choice: ")
    if user == "1":
        clear_screen()
        check()
        while True:
            x = input("Type main To Go The Menu or exit: ")
            if x == "main":
                print("")
                clear_screen()
                break
            elif x == "exit":
                clear_screen()
                exit()
            else:
                clear_screen()
                print("Please Type main or exit")
    elif user == "2":
        clear_screen()
        deposit()
    elif user == "3":
        clear_screen()
        withdraw()
    elif user == "4":
        shutdown()
        exit()
    else:
        clear_screen()
        print("Please Enter the Option given!")
