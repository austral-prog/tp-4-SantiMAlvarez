def es_bisiesto(año):
    return (año % 4 == 0) and (año % 100 != 0 or año % 400 == 0)
    año = int(input("Ingrese un año: "))
    if es_bisiesto(año):
    print(f"El año {año} es bisiesto")
    else:
    print(f"El año {año} no es bisiesto")
