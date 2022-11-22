import json
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
a =  json.dumps(tester,indent=4)
print(a)
compri = [data['name'] for data in tester['info']]
print(compri)

### Ejemplo utilizando nombres de juego de tronos, separar los primeros nombres de cada personaje

people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]

first_names =[names[-1] for names in people]
print(first_names)


### verificar qeu estudiantes pasan

students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]

passed = list([pasa[0] for pasa in students if pasa[-1]>=70])
print(passed)
##### usar comprension de listas, y zip conbinados

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
opposites  = list(filter(lambda x: len(x[0])>3 and len(x[1])>3,zip(l1,l2) ))

print(opposites)


####Uso de zipp para juntar lsita y luego fitlrarlas con comprencion de listas
species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']
population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]
pop_info = zip(species,population)
endangered = list([x[0] for(x) in zip(species,population) if x[1]<2500  ])
print(endangered)
