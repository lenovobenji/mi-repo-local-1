min_num = int(input("Ingrese el número mínimo del rango: "))
max_num = int(input("Ingrese el número máximo del rango: "))

print("Números divisibles entre 3 en el rango de", min_num, "a", max_num, ":")

for num in range(min_num, max_num + 1):
    if num % 3 == 0:
        print(num)
        
        
        
    def read_number(message) -> float:   '''Solicita un número al usuario'''
    is_numeric = False

    while not is_numeric:
        number = input(message)
        is_numeric = number.isnumeric()
    
    return number

min = int(read_number('Ingresa el número mínimo: '))
max = int(read_number('Ingresa el número máximo: '))

if max_num < min_num:
    print("Tus datosno son validos")
else:
    iterator = min_num
    result =[]
    while iterator <= max_num:   
    if iterator % 3 == 0:
        result.append(iterator)
    iterator += 1
print("El resultado es", result)         