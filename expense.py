import os
from datetime import datetime
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
def read_date(message):
    while True:
        value = prompt(message).strip()
        try:
            parsed = datetime.strptime(value, "%Y-%m-%d")
            if parsed.strftime("%Y-%m-%d") != value:
                raise ValueError
            return parsed.strftime("%Y-%m-%d")
        except ValueError:
            print("Érvénytelen dátum. Kérjük, az ÉÉÉÉ-HH-NN formátumot használja!")
            #clear_screen()
def read_place(message):
    while True:
        value = prompt(message).strip()
        if value:
            return value
        print("A szolgáltató neve nem lehet üres!")
        clear_screen()
def read_amount(message):
    while True:
        value = prompt(message).strip()
        try:
            amount = float(value)
        except ValueError:
            print("Érvénytelen összeg. Számot kell megadni!")
            clear_screen()
            continue
        if amount <= 0:
            print("Az összegnek 0-nál nagyobbnak kell lennie!")
            clear_screen()
            continue
        return amount
def read_category(message):
    while True:
        value = prompt(message).strip()
        try:
            category = int(value)
        except ValueError:
            print("Érvénytelen kategória. 1-4 közötti számot adjon meg!")
            clear_screen()
            continue
        if category not in (1, 2, 3, 4):
            print("A kategória csak 1, 2, 3 vagy 4 lehet!")
            clear_screen()
            continue
        return category
def sumexp():
    sum = 0
    with open("expenses.csv", "r") as f:
            for line in f:
                if not line.strip():
                    continue
                row = line.strip().split(";")
                sum += float(row[0].strip())
    return sum
def exp_menu():
    print("1. Bevásárlás")
    print("2. Utazás")
    print("3. Szórakozás")
    print("4. Transzfer")

    category = read_category("Választott kategória (1-4): ")
    date = read_date("Dátum (ÉÉÉÉ-HH-NN): ")
    place = read_place("Szolgáltató: ")
    amount = read_amount("Mennyiség (HUF): ")

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
        print(f.read())
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
            list_expenses()
        case "3":
            pass



if __name__ == "__main__":
    main()