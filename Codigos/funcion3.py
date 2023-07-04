def mi_funcion(value: str)-> str:
    if isinstance(value, int) or isinstance(value, float):
        return str(value)
    return value
fruits = [
    "banana",
    "orange",
    "Kiwi",
    "melon",
    1,
    20,
    8.7,
    "Cherry",
    "mango",
    "apple"]


print(fruits)
fruits.sort(key=mi_funcion)
print(fruits)


def mi_funcion(value)-> str:
    value = str(value)
    return value.lower()


def mi_funcion(value)-> str:
    returnsrt(value).lower()