def organiza(lista, pos):
    aux = lista[pos]
    while pos > 0 and lista[pos - 1] > aux:
        lista[pos] = lista[pos-1]
        pos = pos - 1
    lista[pos] = aux

def insertion_sort(lista):
    for i in range (1, len(lista)):
        organiza(lista,i)













































                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      