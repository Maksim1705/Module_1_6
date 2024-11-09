                                          #Словарь
my_dict={'Имя': 'Maksim' ,'Год рождения': 1998}
print(my_dict)
print(my_dict['Имя'])
print(my_dict.get('Город'))
my_dict['Возраст']=25
my_dict['Количество пальцев на руке']=20
del my_dict['Количество пальцев на руке']
print(my_dict['Возраст'])
print(my_dict)
                             #МНОЖЕСТВА
my_set = {1, 2, 3,'Дата свадьбы', 1 , 2 , 3 }
print(my_set)
my_set={1 , 2 , 3 , 'Дата свадьбы', 1 , 2 , 3, 'Дата',(1,2,3,4) }
print(my_set.discard('Дата'))
print(my_set)