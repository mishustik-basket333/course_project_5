from functions import get_data_employers_hh, get_data_vacancies_hh
from functions_for_postgres import create_table_vacancies_postgres, create_table_employers_postgres


def main():
    """"""
    get_data_employers_hh()
    get_data_vacancies_hh()
    create_table_employers_postgres()
    create_table_vacancies_postgres()


if __name__ == '__main__':
    main()
