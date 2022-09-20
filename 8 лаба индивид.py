import sys

# Название  начального пункта маршрута
# Название конечного пункта
# Номер маршрута (фильтр)

list_route = []
spisok_new = []
list_route = []


def table():
	line = '+-{}-+-{}-+-{}-+-{}-+'.format(
			'-' * 4,
			'-' * 15,
			'-' * 30,
			'-' * 20
		)
	return line

def table_name():
	line = '| {:^4} | {:^15} | {:^30} | {:^20} | '.format(
			"№",
			"Начало маршрута",
			"Конец маршрута",
			"№ Маршрута"
			)
	return line

def table_znach(list_routee):
	post = []
	for idx, spisok_new in enumerate(list_routee, 1):
		post.append('| {:>4} | {:<15} | {:<30} | {:<20} | '.format(
				idx,
				spisok_new.get('name_start', ''),
				spisok_new.get('name_finish', ''),
				spisok_new.get('num_route', 0)
			)
		)
	return post


while True:
	command = input('>>> ').lower()

	if command == 'exit':
		break 

	elif command == 'add':
		name_start = input('Начало маршрута: ')
		name_finish = input('Конец маршрута: ')
		num_route_get = input('Номер маршрута: ')

		num_route = int(num_route_get)

		if type(num_route) != int:
			print("Введенные данные не верны!")

		list_route_new = {
		'name_start': name_start,
		'name_finish': name_finish,
		'num_route': num_route
		}

		list_route.append(list_route_new)

		if len(list_route) > 1:
			list_route.sort(key=lambda item: item.get('num_route', ''))

	elif command == 'list':
		print(table())
		print(table_name())
		print(table())
		for item_x in table_znach(list_route):
			print(item_x)
		print(table())


	elif command == 'route':
		route_sear = input('Введите пункт маршртуа: ')
		search_route = []
		for route_sear_itme in list_route:
			if route_sear == route_sear_itme['name_start']:
				search_route.append(route_sear_itme)
			if route_sear == route_sear_itme['name_finish']:
				search_route.append(route_sear_itme)

		if len(search_route) > 0:
			print(table())
			print(table_name())
			print(table())
			for item_k in table_znach(search_route):
				print(item_k)
			print(table())
		else:
			print('Таких маршрутов не найдено', file=sys.stderr)


	elif command == 'help':
		print('Список команд:\n')
		print('add - добавить маршрут.')
		print('list - вывести список маршрутов.')
		print('route <Пункуты маршрутов> - запросить Начало или конечные пункты маршрутов.')
		print('help - Справочник.')
		print('exit - Завершить пработу программы.')
	else:
		print(f'Команда <{command}> не существует.', file=sys.stderr)
		print('Введите <help> для просмотра доступных команд')