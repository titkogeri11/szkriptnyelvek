import os

def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")

def prompt(message):
    value = input(message)
    clear_screen()
    return value

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
    wname = prompt("Name: ").strip().replace(" ", "_")
    wbdate = prompt("Date of birth: ")
    wposition = prompt("Position: ")
    wyoung = prompt("Younger than 25? (y/n): ").strip().lower()
    wchildren = int(prompt("Number of children: "))
    whwage = int(prompt("Hourly wage: "))
    whours = int(prompt("Hours: "))
    wdate = prompt("Date: ")

    wgross = whwage * whours
    return wname, wbdate, wposition, wyoung, wchildren, whwage, whours, wdate, wgross

def d_mode_input():
        print("1. Adatbázis kiírása")
        print("2. Keresés az adatbázisban")
        print("3. Mező törlése")
        print("4. Mező szerkesztése")
        action = int(prompt("Choice: "))
        return action

def almost_matching(query, field_index):
    """
    Egyszerű, könnyen érthető keresés egy megadott mezőre.
    - `query`: a felhasználói keresőszöveg
    - `field_index`: melyik mezőt nézzük (0..6)
    Visszatérési érték: a találatok listája (sorok stringként).
    """
    talalat = []
    q = query.strip().lower()
    try:
        with open("payrolls.csv", "r") as f:
            for line in f:
                if not line.strip():
                    continue
                row = line.strip().split(";")
                # Ha a mező nincs meg a sorban, kihagyjuk
                if field_index >= len(row):
                    continue
                field = row[field_index].strip().lower()
                # Kis egyszerűsítés: ha a mező _ karaktert tartalmaz, cseréljük szóközre
                field = field.replace("_", " ")
                # exact vagy részleges egyezés
                if q == field or q in field or field in q:
                    talalat.append(line.strip())
    except FileNotFoundError:
        return talalat

    return talalat

def main():
    mode = prompt("(t)est / (w)rite / (d)ocumentation: ")
    if mode in ('t', 'T'):
        while True:
            try:
                hours = int(prompt("Hours: "))
                if hours < 0:
                    raise ValueError
                break
            except ValueError:
                print("Érvénytelen érték, add meg újra.")
                clear_screen()

        while True:
            try:
                hwage = int(prompt("HUF/ hour: "))
                if hwage < 0:
                    raise ValueError
                break
            except ValueError:
                print("Érvénytelen érték, add meg újra.")
                clear_screen()

        while True:
            young = prompt("Younger than 25? (y/n): ").strip().lower()
            if young in ("y", "n"):
                break
            print("Érvénytelen válasz, y vagy n kell.")
            clear_screen()

        while True:
            try:
                children = int(prompt("Number of children: "))
                if children < 0:
                    raise ValueError
                break
            except ValueError:
                print("Érvénytelen érték, add meg újra.")
                clear_screen()

        while True:
            try:
                travel = int(prompt("Distance traveled: "))
                if travel < 0:
                    raise ValueError
                break
            except ValueError:
                print("Érvénytelen érték, add meg újra.")
                clear_screen()

        gross = hours * hwage

        tax, gross = taxreturn(gross, young, children, travel)
        pc = wage(tax, gross)
        print(f"Your paycheck is: {pc} HUF.")
    elif mode in ("W", "w"):
        wname, wbdate, wposition, wyoung, wchildren, whwage, whours, wdate, wgross = worker_stats()

        while True:
            try:
                travel = int(prompt("Distance traveled: "))
                if travel < 0:
                    raise ValueError
                break
            except ValueError:
                print("Érvénytelen érték, add meg újra.")
                clear_screen()

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
            choice = int(prompt(": "))
            #zsófi
            #<3
            match choice:
                case 1:
                    s_name = prompt("Keresett név: ").strip()
                    results = almost_matching(s_name, 0)
                    if results:
                        for r in results:
                            print(r)
                    else:
                        print("Nincs találat.")
                case 2:
                    s_bdate = prompt("Keresett szül. dátum: ").strip().replace(".", "-")
                    results = almost_matching(s_bdate, 1)
                    if results:
                        for r in results:
                            print(r)
                    else:
                        print("Nincs találat.")
                case 3:
                    s_position = prompt("Keresett pozíció: ").strip()
                    results = almost_matching(s_position, 2)
                    if results:
                        for r in results:
                            print(r)
                    else:
                        print("Nincs találat.")
                case 4:
                    s_hwage = prompt("Keresett órabér: ").strip()
                    results = almost_matching(s_hwage, 3)
                    if results:
                        for r in results:
                            print(r)
                    else:
                        print("Nincs találat.")
                case 5:
                    s_hours = prompt("Keresett óraszám: ").strip()
                    results = almost_matching(s_hours, 4)
                    if results:
                        for r in results:
                            print(r)
                    else:
                        print("Nincs találat.")
                case 6:
                    s_pmonth = prompt("Keresett fizetési tárgyhó: ").strip()
                    results = almost_matching(s_pmonth, 5)
                    if results:
                        for r in results:
                            print(r)
                    else:
                        print("Nincs találat.")
                case 7:
                    s_net = prompt("Keresett nettó fizetés: ").strip()
                    results = almost_matching(s_net, 6)
                    if results:
                        for r in results:
                            print(r)
                    else:
                        print("Nincs találat.")

if __name__ == "__main__":
    main()