koders = [
    "Luis",
    "Benjamin",
    "Juan",
    "Julio",
    "Irving",
    "Miren",
    "Martin",
    "Miguel",
    "Enrique",
    "Francisco",
    "Rodrigo",
    "Francisco2",
    "Jose",
    "Jesus",
]

ages = [
  22,
  23,
  24,
  25,
  26,
  27,
  28,
  29,
  30,
  31,
  32,
  33,
  34,
  35,
]


koders_ages = []
koders_range = range(len(koders))
for i in koders_range:
    koders_ages.append((koders[i], ages[i]))
    
message= "Hola Koders\nLa lista completa es:\n"

for pair in koders_ages:
    message += f"{pair[0]} - {pair[1]}\n"
    
    print(message)    


message=f"Hola Koders, los saludo por su nombre y edad: {union}"
print(message)