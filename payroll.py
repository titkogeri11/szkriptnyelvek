def taxreturn(gross, young, children, travel):

    tax = 0

    if young == 'N' or young == 'n':
        #gross *= 0.85
        tax += 0.15 #szja
        tax += 0.10 #szocho
        tax += 0.085 #tb
    if children != 0:
        if children == 1:
            gross += 20000
        elif children == 2:
            gross += (children * 20000)
        elif children >= 3:
            gross += (children * 66000)
    if(travel != 0):
        gross += (30.5 * travel)


    return tax, gross

def wage(tax, gross):
    return gross * (1 - tax)

def worker_stats():
    wname = input("Name: ").strip().replace(" ", "_")
    wbdate = input("Date of birth: ")
    wposition = input("Position: ")
    wyoung = input("Younger than 25? (y/n): ").strip().lower()
    wchildren = int(input("Number of children: "))
    whwage = int(input("Hourly wage: "))
    whours = int(input("Hours: "))
    wdate = input("Date: ")

    wgross = whwage * whours
    return wname, wbdate, wposition, wyoung, wchildren, whwage, whours, wdate, wgross

def d_mode_input():
        print("1. Adatbázis kiírása")
        print("2. Keresés az adatbázisban")
        print("3. Mező törlése")
        print("4. Mező szerkesztése")
        action = int(input("Choice: "))

        return action

def main():
    mode = input("(t)est / (w)rite / (d)ocumentation: ")
    if mode in ('t', 'T'):
        while True:
            try:
                hours = int(input("Hours: "))
                if hours < 0:
                    raise ValueError
                break
            except ValueError:
                print("Érvénytelen érték, add meg újra.")

        while True:
            try:
                hwage = int(input("HUF/ hour: "))
                if hwage < 0:
                    raise ValueError
                break
            except ValueError:
                print("Érvénytelen érték, add meg újra.")

        while True:
            young = input("Younger than 25? (y/n): ").strip().lower()
            if young in ("y", "n"):
                break
            print("Érvénytelen válasz, y vagy n kell.")

        while True:
            try:
                children = int(input("Number of children: "))
                if children < 0:
                    raise ValueError
                break
            except ValueError:
                print("Érvénytelen érték, add meg újra.")

        while True:
            try:
                travel = int(input("Distance traveled: "))
                if travel < 0:
                    raise ValueError
                break
            except ValueError:
                print("Érvénytelen érték, add meg újra.")

        gross = hours * hwage

        tax, gross = taxreturn(gross, young, children, travel)
        pc = wage(tax, gross)
        print(f"Your paycheck is: {pc} HUF.")
    elif mode in ("W", "w"):
        wname, wbdate, wposition, wyoung, wchildren, whwage, whours, wdate, wgross = worker_stats()

        while True:
            try:
                travel = int(input("Distance traveled: "))
                if travel < 0:
                    raise ValueError
                break
            except ValueError:
                print("Érvénytelen érték, add meg újra.")

        tax, gross = taxreturn(wgross, wyoung, wchildren, travel)
        net = wage(tax, gross)

        with open("payrolls.csv", "a") as f:
            f.write(f"{wname};{wbdate.replace('.', '-')};{wposition.upper()};{whwage:.2f};{whours:.2f};{wdate};{net:.2f}\n")
        print(f"Net wage: {net:.2f} HUF. Adatok mentve a payrolls.csv-be")
    elif mode in("D", "d"):
        action = d_mode_input()
        if action == 1:
            with open("payrolls.csv", "r") as f:
                print(f.read())
        elif action == 2:

            #f = open("payrolls.csv", "r")

            print("1. Név alapján")
            print("2. Szül. dátum alapján")
            print("3. Pozíció alapján")
            print("4. Órabér alapján")
            print("5. Ledolgozott órák száma alapján")
            print("6. Fizetési tárgyhó alapján")
            print("7. Nettő fizetés alapján")
            choice = int(input(": "))
            #zsófi
            #<3
            match choice:
                case 1:
                    s_name = input("Keresett név: ").strip().replace(" ", "_")
                    found = False
                    with open("payrolls.csv", "r") as f:
                        for line in f:
                            if not line.strip():
                                continue
                            row = line.strip().split(";")
                            if row and row[0] == s_name:
                                print(line.strip())
                                found = True
                    if not found:
                        print("Nincs találat.")
                case 2:
                    s_bdate = input("Keresett szül. dátum: ").strip().replace(".", "-")
                    found = False
                    with open("payrolls.csv", "r") as f:
                        for line in f:
                            if not line.strip():
                                continue
                            row = line.strip().split(";")
                            if row and row[1] == s_bdate:
                                print(line.strip())
                                found = True
                            if not found:
                                print("Nincs találat.")
                case 3:
                    s_position = input("Keresett pozíció: ").strip().replace(".", "-")
                    found = False
                    with open("payrolls.csv", "r") as f:
                        for line in f:
                            if not line.strip():
                                continue
                            row = line.strip().split(";")
                            if row and row[2] == s_position:
                                print(line.strip())
                                found = True
                            if not found:
                                print("Nincs találat.")
                case 4:
                    pass

if __name__ == "__main__":
    main()