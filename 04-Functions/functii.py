# print("Mesaj")
# format()
# a = input("Input dat de utilizator")
# def functia_mea(param_1):
#     pass

def  suma(a: int, b: int = 1, c: int = 0) -> (int, int):
    """

    :param a: first param
    :param b: second param
    :param c: third param
    :return: sum of params, dif of params
    """
    return a + b + c, a - b - c


variablia_1 = 1
variablia_2 = 2
suma(variablia_1, variablia_2)
sum, dif = suma(a=variablia_1, c=0, b=variablia_2)
print(sum, type(sum))
print(dif, type(dif))
