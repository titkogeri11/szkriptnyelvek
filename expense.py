import os
def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")
def prompt(message):
    value = input(message)
    clear_screen()
    return value
def sumexp():
    with open("allexp.csv", "r") as f:
        return f.readline()

def menu():

    print(f"Összes kiadás: {sumexp()}")
    print("2. Új kiadás")
    print("Tételek listázása")
    print("3. Kiadás törlése")


def main():
    menu()
    mode = prompt("Mód: ")





if __name__ == "__main__":
    main()