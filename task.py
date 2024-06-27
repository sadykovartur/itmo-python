import csv

LOW_RISE = 5
MID_RISE = 16


def read_file(filename: str) -> list[dict]:
    """Читает данные из CSV файла и преобразует их в список словарей.

    :param filename: Название файла, содержащего данные.
    :return: Список словарей с данными о домах.
    """
    with open(filename) as file:
        # прочитаем с помощью модуля CSV https://docs.python.org/3/library/csv.html
        reader = csv.DictReader(file)
        return list(reader)  # какая-то короткая запись (работает)


def classify_house(floor_count: int) -> str:
    """Классифицирует дом на основе количества этажей.

    Проверяет, является ли количество этажей целым числом и положительным значением.
    Возвращает категорию дома в зависимости от количества этажей.

    :param floor_count: Количество этажей в доме.
    :return: Категория дома в виде строки: "Малоэтажный", "Среднеэтажный" или "Многоэтажный".
    """
    # проверка типа данных
    type_error_msg = "Количество этажей должно быть целым числом."
    value_error_msg = "Количество этажей должно быть больше нуля"

    if not isinstance(floor_count, int):
        raise TypeError(type_error_msg)

    # проверка на ноль и отрицательное значение
    if floor_count <= 0:
        raise ValueError(value_error_msg)

    # условия
    if floor_count <= LOW_RISE:
        return "Малоэтажный"
    if floor_count <= MID_RISE:
        return "Среднеэтажный"
    return "Многоэтажный"


def get_classify_houses(houses: list[dict]) -> list[str]:
    """Классифицирует дома на основе количества этажей.

    :param houses: Список словарей с данными о домах.
    :return: Список категорий домов.
    """
    categories = []
    for house in houses:
        floor_count = int(house["floor_count"])
        # вызовем уже реализованную функцию
        category = classify_house(floor_count)
        # добавим в список
        categories.append(category)
    return categories


def get_count_house_categories(categories: list[str]) -> dict[str, int]:
    """
    Подсчитывает количество домов в каждой категории.

    :param categories: Список категорий домов.
    :return: Словарь с количеством домов в каждой категории.
    """
    category_count = {}
    # пройдем по всем категориям
    for cat in categories:
        if cat in category_count:  # короткая проверка на вхождение (можно еще count)
            category_count[cat] += 1
        else:
            category_count[cat] = 1
    return category_count


def min_area_residential(houses: list[dict]) -> str:
    """Находит адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца.

    :param houses: Список словарей с данными о домах.
    :return: Адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца.
    """
    min_area_person = 100000000
    min_area_addr = ""
    type_error_msg = "Должно быть целое число"

    for house in houses:
        area_residential = house["area_residential"]
        population = house["population"]
        if not isinstance(population, int):
            raise TypeError(type_error_msg)
        if population > 0:  # на ноль не делим
            area_person = area_residential / population
            if area_person < min_area_person:
                min_area_person = area_person
                min_area_addr = house["house_address"]
    return min_area_addr


# file_path = 'housing_data.csv'
# data = read_file(file_path)
# print(data)
# print("---")
# #print(classify_house(-1))
# print(classify_house(3))
# print("---")
# print(get_classify_houses(data))
# print("---")
# categories = get_classify_houses(data)
# print(get_count_house_categories(categories))
# print("---")
# print(min_area_residential(data))
