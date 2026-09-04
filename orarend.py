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
    print("Hétfő")
    with open("classes.csv", "r") as f:
        for line in f:
            if not line.strip():
                continue
            row = line.strip().split(";")
            if row[2].strip().lower() == "hétfő":
                print("\t" + line.strip())
    print()
    print("Kedd")
    with open("classes.csv", "r") as f:
        for line in f:
            if not line.strip():
                continue
            row = line.strip().split(";")
            if row[2].strip().lower() == "kedd":
                print("\t" + line.strip())
    print()
    print("Szerda")
    with open("classes.csv", "r") as f:
        for line in f:
            if not line.strip():
                continue
            row = line.strip().split(";")
            if row[2].strip().lower() == "szerda":
                print("\t" + line.strip())
    print()
    print("Csütörtök")
    with open("classes.csv", "r") as f:
        for line in f:
            if not line.strip():
                continue
            row = line.strip().split(";")
            if row[2].strip().lower() == "csütörtök":
                print("\t" + line.strip())
    print()
    print("Péntek")
    with open("classes.csv", "r") as f:
        for line in f:
            if not line.strip():
                continue
            row = line.strip().split(";")
            if row[2].strip().lower() == "péntek":
                print("\t" + line.strip())
    print()
def main():
    print("1. Összes óra listázása")
    print("2. Új óra hozzáadása")

    mode = int(input("Mód: "))
    clear_screen()

    match mode:
        case 1:
            list_classes()
        case 2:
            new_class()


if __name__ == "__main__":
    main()