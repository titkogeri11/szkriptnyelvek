import os
def read_non_negative_int(message):
    while True:
        try:
            value = int(prompt(message))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Érvénytelen érték. Adjon meg 0 vagy nagyobb számot!")
            clear_screen()
def read_yes_no(message):
    while True:
        value = prompt(message).strip().lower()
        if value in ("y", "n"):
            return value
        print("Érvénytelen válasz. y vagy n kell!")
        clear_screen()
def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")
def prompt(message):
    value = input(message)
    clear_screen()
    return value
def sumexp():
    with open("allexp.csv", "r") as f:
        return f.readline()
def exp_menu():
    print("1. Bevásárlás")
    print("2. Utazás")
    print("3. Szórakozás")
    print("4. Transzfer")
    date = input("Dátum: ").replace(".", "-")
    category = input("Választott kategória: ")
    amount = int(input("Mennyiség (HUF): "))
    clear_screen()

    f = open("expenses.csv", "w")
    writed_category = ""

    match category:
        case 1:
            writed_category = "Bevásárlás"
            f.write("")




def menu():

    print(f"Összes kiadás: {sumexp()} HUF")
    print("1. Új kiadás")
    print("2. Tételek listázása")
    print("3. Kiadás törlése")


def main():
    menu()
    mode = prompt("Mód: ")

    match mode:
        case 1:
            exp_menu():






if __name__ == "__main__":
    main()