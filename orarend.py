import os
def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")
def new_class():
    name = input("Tárgy: ").replace(" ", "_")
    type = input("(E)lmélet / (G)yakorlat: ")
    day = input("Nap: ")
    hr = input("Óra: ")
    prof = input("Oktató: ")
    room = input("Terem: ")

    if type in("e", "E", "g", "G"):
        if type in("e", "E"):
            type = "Elmélet"
        elif type in("g", "G"):
            type = "Gyakorlat"

    with open("classes.csv", "a") as f:
        f.write(f"{name};{type};{day};{hr};{room};{prof}\n")
    clear_screen()
def list_classes():
    days = [
        ("Hétfő", "hétfő"),
        ("Kedd", "kedd"),
        ("Szerda", "szerda"),
        ("Csütörtök", "csütörtök"),
        ("Péntek", "péntek"),
    ]

    for day_display, day_value in days:
        counter = 0
        day_lines = []
        with open("classes.csv", "r") as f:
            for line in f:
                if not line.strip():
                    continue
                row = line.strip().split(";")
                # védelem rövidebb sorok ellen
                if len(row) < 3:
                    continue
                if row[2].strip().lower() == day_value:
                    counter += 1
                    day_lines.append(line.strip())

        # fejléc: nap + összegzés
        if counter == 0:
            print(f"{day_display}: ---")
        else:
            print(f"{day_display}: {counter} óra")
            for l in day_lines:
                print("\t" + l)
        print()
def missed_classes():
    

def main():
    print("1. Összes óra listázása")
    print("2. Új óra hozzáadása")
    print("3. Hiányzások")

    mode = int(input("Mód: "))
    clear_screen()

    match mode:
        case 1:
            list_classes()
        case 2:
            new_class()


if __name__ == "__main__":
    main()