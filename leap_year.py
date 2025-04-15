def leap_year():
    text=input("Ingrese un año: ")
    year=int(text)
    A=year%4
    B=year%100
    C=year%400
    if A==0:
        if B==0:
            if C==0:
                print(f"El año {year) es bisiesto"?
            else:
                print(f"'El año {year) no es bisiesto")
        else:
            print(f"'El año {year} es bisiesto")
    else:
        print(f"'El año {year} no es bisiesto")
leap_year()
