import requests
import json


def get_data_employers_hh(count_employers: int = 10) -> None:
    """
    Функция делает запрос на HH и берет данные 10 работодателей.
    После записывает в файл employers_data.json.
    Если файл уже был создан, то он перезаписывается.
    :param count_employers: Кол-во получаемых работодателей. По умолчанию = 10
    :return: None
    """
    params = {
        "only_with_vacancies": True,
        "per_page": count_employers,
    }

    data_employers = requests.get("https://api.hh.ru/employers", params=params).json()

    with open('employers_data.json', 'w', encoding="UTF-8") as file:
        json.dump(data_employers, file, indent=4)


def get_data_vacancies_hh() -> None:
    """
    Функция берет данные по работодателям из файла employers_data.json и делает запрос по вакансиям на HH.
    После записывает в файл vacancies_data.json.
    Если файл уже был создан, то он перезаписывается.
    :return: None
    """
    dict_data = {}

    with open('employers_data.json') as json_file:
        data = json.load(json_file)

    for row in data["items"]:
        data_vacancies = requests.get(row["vacancies_url"]).json()
        dict_data[row["id"]] = data_vacancies

    with open('vacancies_data.json', 'w', encoding="UTF-8") as file:
        json.dump(dict_data, file, indent=4, ensure_ascii=True)


if __name__ == "__main__":
    """"""
    get_data_employers_hh(3)
    get_data_vacancies_hh()
