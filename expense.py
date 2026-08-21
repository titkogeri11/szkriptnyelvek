import os
def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")
def prompt(message):
    value = input(message)
    clear_screen()
    return value
def sumexp():
    with open("expenses.csv", "r") as f:
        return f.readline()

def menu():

    #print("1. Összes kiadás")
    print("2. Új kiadás")
    print("3. Kiadás törlése")
    #print("4. ")

def main():
    menu()
    mode = prompt("Mód: ")





if __name__ == "__main__":
    main()