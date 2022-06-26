metr = float(input("Podaj odległość w metrach: "))
try:
    if(metr < 0):
        print("Odległość nie może być ujemna")
    else:
        czas = float(input("Podaj czas w sekundach: "))
        if(czas < 0):
            print("Czas nie może być ujemny")
        else:
            V = float(metr) / float(czas)
            print("Prędkość w m/s:", V)
except ZeroDivisionError:
    print("Nie można dzielić przez zero")
except ValueError:
    print("Błędne dane")
print("Koniec programu")