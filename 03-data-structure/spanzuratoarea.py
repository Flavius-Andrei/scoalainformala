# Reguli
# daca primul character si ultimul se repetau in cauvant, caracterul trebuia afisat
# restul caracterelor erau ascune
# 7 sanse de a chici cuvantul
# work = o _ o _ _ _ o _ e e
word = 'onomataopee'
# litera_cuvant = input("Alege o litera")
# print(litera_cuvant)
lista_cuvant = []
for iterator in word:
    lista_cuvant.append('_')
    if iterator == word[0] or iterator == word[-1]:
        lista_cuvant[-1] = iterator
print(' '.join(lista_cuvant))
numar_incercari = 1
lista_litere_incercate = set()
while numar_incercari <= 7:
    litera = input("Alege o litera: ").lower()
    if litera.lower() in word.lower():
        for index, valoare in enumerate(word):
            if valoare.lower() == litera:
                lista_cuvant[index] = litera
    else:
        if litera.lower() not in list(lista_litere_incercate):
            numar_incercari += 1
        lista_litere_incercate.add(litera.lower())
        print(f'Litera nu exista deja ai '
              f'ai incercat deja urmatoarele litere {",".join(lista_litere_incercate)}')
        print(f"Mai ai {7 - numar_incercari} incercari ")
    if 9 - int(numar_incercari) == 0:
        print(f"Ai pierdut! Cuvantul era {word}")
    elif ''.join(lista_cuvant) == word:
        print("Ai castigat!")
        break
    else:
        print(' '.join(lista_cuvant))


