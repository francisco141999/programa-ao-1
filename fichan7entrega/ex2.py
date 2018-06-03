file = open ("fichan7entrega\ex1.txt", "r")

def crescente (my_list):
    if len(my_list) > 1:
        mid = int(len(my_list)/2)
        left = my_list[:mid]
        right = my_list[mid:]
        # Split
        crescente(left)
        crescente(right)
        # sort
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                my_list[k] = left[i]
                i += 1
            else:
                my_list[k] = right[j]
                j += 1
            k += 1
        # left leftovers
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1
        # right leftovers
        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1

def decrescente (my_list):
    if len(my_list) > 1:
        mid = int(len(my_list)/2)
        left = my_list[:mid]
        right = my_list[mid:]
        # Split
        decrescente(left)
        decrescente(right)
        # sort
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                my_list[k] = left[i]
                i += 1
            else:
                my_list[k] = right[j]
                j += 1
            k += 1
        # left leftovers
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1
        # right leftovers
        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1


lista=[]
linha=file.readline()
for i in linha:
    i=int(i.split("\n")[0])
    lista.append(0)

crescente(lista)
print(lista)