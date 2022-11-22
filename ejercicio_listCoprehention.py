L = [12, 34, 21, 4, 6, 9, 42]
lst = []
#este es el metodo esandar con for
for x in L:
    if x > 10:
        lst.append(x)
print(lst)

#este es el metodo por comprensión de listas
lst2 = [num for num in L if num>10]
print(lst2)
