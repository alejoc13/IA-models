"""Procedimiento para escribir un archivo de texrto, tenga en cuenta uqe si el nombre asigando al .txt no ecxiste python 
procedera automaticamente a crfar un aechivo con el nombre dado"""
with open("seguidores.txt", mode="w") as seguidores: #crear un .txt con la inforamcion que se desea
    seguidores.write("@charlidamelio D’Amelio 108.1\n@addisonre Addison 76.4\n@zachking Zach 56.6\n@bellapoarch Bella 56.3")


"""Procedimiento para leer un archiv de texto"""
with open("seguidores.txt", mode='r') as seguidores:
    print(f'{"Handle":<20}{"Nombre":<10}{"num-seg":>10}')
    for record in seguidores:
        Handle,Nombre,numseg = record.split()
        print(f'{Handle:<20}{Nombre:<10}{numseg:>10}')

"""Procedimiento para cambiar el contenido de un archivo de texto(feo feo feo)"""
seguidores = open("seguidores.txt","r")
temporal = open("temporal.txt",'w')
with seguidores,temporal:
    for record in seguidores:
        Handle,Nombre,numseg = record.split()
        if Handle!='@charlidamelio':
            temporal.write(record)
        else:
            nuevo_nombre = " ".join([Handle ,"Charlie ",numseg])
            temporal.write(nuevo_nombre+"\n")