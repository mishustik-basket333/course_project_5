from functions import get_data_employers_hh, get_data_vacancies_hh
from functions_for_postgres import create_table_vacancies_postgres, create_table_employers_postgres
from functions_for_postgres import push_data_in_vacancies, push_data_in_employers


def main():
    get_data_employers_hh()
    get_data_vacancies_hh()
    create_table_employers_postgres()
    create_table_vacancies_postgres()
    push_data_in_employers('employers_data.json')
    push_data_in_vacancies('vacancies_data.json')


if __name__ == '__main__':
    main()
