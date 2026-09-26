first_list = ['Hay', 'en' , 'que' , 'iteracion' , 'indices' , 'muy']
second_list = ['casos', 'los' , 'la' , 'por' , 'es' , 'util']

new_list = []

for index in range(len(first_list)):
    new_list.append([first_list[index], second_list[index]])

for pair in new_list:
    print(pair[0], pair[1])

for pair in new_list:
    print(pair[0], pair[1], end = ' ')