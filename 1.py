import sys
import json

list_shop = []
spisok_new = []


def table():
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 6,
        '-' * 20,
        '-' * 30,
        '-' * 20
    )
    return line


def table_name():
    post = '| {:^6} | {:^20} | {:^30} | {:^20} | '.format(
        "№",
        "Название магазина",
        "Название товара",
        "Стоимость"
    )
    return post


def table_name_fil(names):
    post = []
    for idx_new, spisok_new_new in enumerate(names, 1):
        post.append(
            '| {:>6} | {:<20} | {:<30} | {:<20} | '.format(
                idx_new,
                spisok_new_new.get('name_shop', ''),
                spisok_new_new.get('name_prodyckt', ''),
                spisok_new_new.get('prise', '')
            )
        )
    return post


while True:
    command = input('>>> ').lower()

    if command == 'exit':
        break

    elif command == 'add':
        name_shop = input('Название магазина: ')
        name_prodyckt = input('Название товара: ')
        prise = input('Стоимость товара: ')

        list_shop_new = {
            'name_shop': name_shop,
            'name_prodyckt': name_prodyckt,
            'prise': prise
        }

        list_shop.append(list_shop_new)

        if len(list_shop) > 1:
            list_shop.sort(key=lambda item: item.get('name_shop', ''))

    elif command == 'list':
        print(table())
        print(table_name())
        print(table())
        for item_n in table_name_fil(list_shop):
            print(item_n)
        print(table())


    elif command.startswith('prodyckt'):
        shop_sear = input('Введите название товара: ')
        search_shop = []
        for shop_sear_itme in list_shop:
            if shop_sear == shop_sear_itme['name_prodyckt']:
                search_shop.append(shop_sear_itme)

        if len(search_shop) > 0:
            print(table())
            print(table_name())
            print(table())
            for item_f in table_name_fil(search_shop):
                print(item_f)
            print(table())
        else:
            print('Такого товара не найдено', file=sys.stderr)

    elif command.startswith('load '):
        parts = command.split(' ', maxsplit=1)

        with open(parts[1], 'r', encoding="utf-8") as f:
            list_shop = json.load(f)
            validate(instance=list_shop, schema=schema)


    elif command.startswith('save '):
        parts = command.split(' ', maxsplit=1)

        with open(parts[1], 'w', encoding="utf-8") as f:
            json.dump(list_shop, f)


    elif command == 'help':
        print('Список команд:\n')
        print('add - добавить магазин.')
        print('list - вывести список магазинов.')
        print('prodyckt <Название> - запросить информацию о товаре.')
        print("load <имя файла> - загрузить данные из файла;")
        print("save <имя файла> - сохранить данные в файл;")
        print('help - Справочник.')
        print('exit - Завершить пработу программы.')
    else:
        print(f'Команда <{command}> не существует.', file=sys.stderr)
        print('Введите <help> для просмотра доступных команд')
