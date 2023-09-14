def menor(lista, pos):
    pos_min = pos
    while pos < len(lista):
        if lista[pos] <= lista[pos_min]:
            pos_min = pos
        pos = pos + 1
    return pos_min

def selection_sort(lst):
    for i in range (len(lst)):
        p = menor(lst, i)
        #lst[0], lst[p] = lst[p], lst[0]
        aux = lst[p]
        lst[p] = lst[i]
        lst[i] = aux
        
lst = [3.4, 7.8, -0.5, -2.0, 7.2, 6.5]
selection_sort(lst)
print(lst)