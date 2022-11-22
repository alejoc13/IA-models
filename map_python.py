def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_list = map(triple,a_list)
    return list(new_list)
def  quadrupleStuff(a_list):
    new_list = map(lambda value:  4*value, a_list)
    return list(new_list)

things  = [2,5,9]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)
print(things4)

### funcion
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
map_testing =list( map(lambda value: 'Fruit: '+ value,lst_check))
print(map_testing)
