
pair_numbers = [(2,3), (4,5),(5,6), (6,7),(9,4), (1,1), (5,2)]

def get_segund_value(tupla):
    return tupla[1]

pair_numbers.sort(key=get_segund_value)
print("ordena ascendente", pair_numbers)

pair_numbers.sort(key=get_segund_value, reverse=True)
print("Ordena desendente", pair_numbers)