from functions import get_data_employers_hh, get_data_vacancies_hh
from functions_for_postgres import create_table_vacancies_postgres, create_table_employers_postgres
from functions_for_postgres import push_data_in_vacancies, push_data_in_employers
from classes import DBManager


def main():
    """"""
    # Делаем запросы на НН и создаем файлы json с данными о работодателях и вакансиях.
    get_data_employers_hh()
    get_data_vacancies_hh()

    # Создаем таблицы employers и vacancies в Postgres
    create_table_employers_postgres()
    create_table_vacancies_postgres()

    # Загружаем данные из ранее созданных файлов в созданные таблицы в Postgres
    push_data_in_employers()
    push_data_in_vacancies()

    # Cоздаем экземпляр класса DBManager для получения данных из таблиц Postgres
    db_manager_1 = DBManager()

    # Выполняем методы и записываем результат в переменные
    data_1 = db_manager_1.get_companies_and_vacancies_count()
    data_2 = db_manager_1.get_all_vacancies()
    data_3 = db_manager_1.get_avg_salary()
    data_4 = db_manager_1.get_vacancies_with_higher_salary()
    data_5 = db_manager_1.get_vacancies_with_keyword("Грузчик")

    # Вывод данных
    [print(row) for row in data_1]
    [print(row) for row in data_2]
    [print(row) for row in data_3]
    [print(row) for row in data_4]
    [print(row) for row in data_5]


if __name__ == '__main__':
    main()
