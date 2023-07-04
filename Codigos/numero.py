
def read_number(message) -> float:   '''Solicita un número al usuario'''
    is_numeric = False

    while not is_numeric:
        number = input(message)
        is_numeric = number.isnumeric()
    
    return float (number)

min_number = (read_number('Ingresa el número mínimo: '))
max_number = (read_number('Ingresa el número máximo: '))

if max_num < min_num:
    print("Tus datosno son validos")
else:
    iterator = min_num
    result =[]
    while iterator <= max_num:   
     if (iterator % 3) == 0:
        result.append(iterator)
    iterator += 1
print("El resultado es", result)         