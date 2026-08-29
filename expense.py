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
    print("4. Keresés")
def src_menu():
    print("1. Szolgáltató szerint")
    print("2. Összeg szerint")
    print("3. Dátum szerint")
    print("4. Kategória szerint")
    mode = input("Mód: ")
    clear_screen()
    match mode:
        case "1":
            sdata = input("Szolgáltató: ")
            with open("expenses.csv", "r") as f:
                for line in f:
                    if not line.strip():
                        continue
                    row = line.strip().split(";")
                    if row[1] == sdata:
                        print(line)
        case "2":
            sdata = input("Összeg: ")
            with open("expenses.csv", "r") as f:
                for line in f:
                    if not line.strip():
                        continue
                    row = line.strip().split(";")
                    if row[0] == sdata:
                        print(line)
        case "3":
            sdata = input("Dátum: ")
            with open("expenses.csv", "r") as f:
                for line in f:
                    if not line.strip():
                        continue
                    row = line.strip().split(";")
                    if row[3] == sdata:
                        print(line)
        case "4":
            sdata = input("Kategória: ")
            with open("expenses.csv", "r") as f:
                for line in f:
                    if not line.strip():
                        continue
                    row = line.strip().split(";")
                    if row[2] == sdata:
                        print(line)    
def list_categories():
    bevasarlas = []
    bev_sum = 0.0
    utazas = []
    ut_sum = 0.0
    #niga8)
    szorakozas = []
    szor_sum = 0.0
    transzfer = []
    tr_sum = 0.0

    with open("expenses.csv", "r") as f:
            for line in f:
                if not line.strip():
                    continue
                row = line.strip().split(";")
                if row[2] == "Bevásárlás":
                    bevasarlas.append(line)
                    bev_sum += float(row[0].strip())
                elif row[2] == "Utazás":
                    utazas.append(line)
                    ut_sum += float(row[0].strip())
                elif row[2] == "Szórakozás":
                    szorakozas.append(line)
                    szor_sum += float(row[0].strip())
                elif row[2] == "Transzfer":
                    transzfer.append(line)
                    tr_sum += float(row[0].strip())

            if bev_sum != 0.0:
                print(f"BEVÁSÁRLÁS:{bev_sum}\n")                    
                for line in bevasarlas:
                    print("\t" + line)
            else:
                pass

            if ut_sum != 0.0:
                print(f"UTAZÁS: {ut_sum}\n")
                for line in utazas:
                    print("\t" + line)
            else:
                pass

            if szor_sum != 0.0:
                print(f"SZÓRAKOZÁS:{szor_sum} \n")
                for line in szorakozas:                
                    print("\t" + line)
            else:
                pass

            if tr_sum != 0.0:
                print(f"TRANSZFER: {tr_sum}\n")
                for line in transzfer:
                    print("\t" + line)
            else:
                pass

def main():
    menu()
    mode = prompt("Mód: ")

    match mode:
        case "1":
            exp_menu()
        case "2":
            list_expenses()
        case "3":
            list_categories()
        case "4":
            src_menu()



if __name__ == "__main__":
    main()