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
        return f.readline().strip()
def exp_menu():
    print("1. Bevásárlás")
    print("2. Utazás")
    print("3. Szórakozás")
    print("4. Transzfer")
    date = input("Dátum: ").replace(".", "-")
    place = input("Szolgáltató: ")
    amount = int(input("Mennyiség (HUF): "))
    try:
            category = int(input("Választott kategória: "))
    except ValueError:
            print("Érvénytelen kategória. Számot adjon meg (1-4).")
            return
    #clear_screen()

    f = open("expenses.csv", "w")
    writed_category = ""

    writed_category = ""

    match category:
            case 1:
                writed_category = "Bevásárlás"
            case 2:
                writed_category = "Utazás"
            case 3:
                writed_category = "Szórakozás"
            case 4:
                writed_category = "Transzfer"
            case _:
                print("Ismeretlen kategória. 1-4 között adja meg.")
                return
    with open("expenses.csv", "a", encoding="utf-8") as f:
        f.write(f"{amount:.2f};{place};{writed_category};{date}\n")
def list_expenses():
    with open("expenses.csv", "r") as f:
        f.read()

def menu():

    print(f"Összes kiadás: {sumexp()} HUF")
    print("1. Új kiadás")
    print("2. Összes kiadás listázása")
    print("3. Tételek szerinti listázás")


def main():
    menu()
    mode = prompt("Mód: ")

    match mode:
        case "1":
            exp_menu()
        case "2":
            pass
        case "3":
            pass






if __name__ == "__main__":
    main()