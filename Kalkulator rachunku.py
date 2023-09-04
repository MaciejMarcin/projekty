rachunek = input("Jaka jest kwota rachunku? \n" )
liczba_osob = input("Na ile osób podzielić rachunek? \n")
procent = input("Jaki chcesz zostawić % napiwku? \n")

napiwek = (int(procent) / 100) * float(rachunek)

rachunekinapiwek = float(rachunek) + napiwek

ostateczna_cena = rachunekinapiwek / int(liczba_osob)

x = round(ostateczna_cena, 2)


print(f"Twoja opłata wynosi {x}zł")

input()
