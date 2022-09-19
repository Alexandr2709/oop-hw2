import pprint

pp = pprint.PrettyPrinter()


def cook_dict():
    with open('book cooks.txt', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            data = line.strip().split(' | ')

            if len(data) > 1:
                ingrident = {'ingridient_name': data[0],
                             'quantity': float(data[1]),
                             'measure': data[2]}
                cook_book[recept].append(ingrident)
            else:
                if data[0] == '' or data[0].isdigit():
                    continue
                else:
                    recept = data[0]
                    cook_book[recept] = []
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    '''рассчитываем блюдо на количество персон'''
    result = {}

    for dish in dishes:
        if dish in cook_dict().keys():
            for ingrident in cook_dict()[dish]:
                if ingrident['ingridient_name'] in result.keys():
                    result[ingrident['ingridient_name']]['quantity'] += ingrident['quantity'] * person_count
                else:
                    result[ingrident['ingridient_name']] = {'measure': ingrident['measure'],
                                                            'quantity': ingrident['quantity'] * person_count}
    pp.pprint(result)


def changes():
    print("название блюда: "
          "Омлет,"
          "Утка по-пекински,"
          "Запеченный картофель,"
          "Фахитос")
    dishes = input("Введите название блюда через пробел: ").split()
    person_count = int(input("Введите количество персон: "))
    get_shop_list_by_dishes(dishes, person_count)


changes()
