import psycopg2
import json

try:
    from config import my_password, my_user, my_host, my_port, my_database
except ModuleNotFoundError as mail_1:
    print(mail_1)
    print("Проверьте наличие config.py")


def create_con():
    """Функция для подключения к БД Postgres"""
    try:
        con = psycopg2.connect(database=my_database,
                               user=my_user,
                               password=my_password,
                               host=my_host,
                               port=my_port
                               )
    except psycopg2.OperationalError as mail_2:
        print(mail_2)
        print("Проверьте актуальность данных в config.py")
    return con


def create_table_employers_postgres() -> None:
    """
    Функция подключается к БД course_project_5 и создаёт таблицу employers
    :return: None
    """
    con = create_con()
    cur = con.cursor()
    cur.execute('''CREATE TABLE employers
         (id int PRIMARY KEY NOT NULL,
         name TEXT NOT NULL,
         url TEXT,
         count_open_vacancies INT NOT NULL);'''
                )
    con.commit()
    con.close()


def create_table_vacancies_postgres() -> None:
    """
    Функция подключается к БД course_project_5 и создаёт таблицу vacancies
    :return: None"""
    con = create_con()
    cur = con.cursor()
    cur.execute('''CREATE TABLE vacancies
         (id serial PRIMARY KEY NOT NULL,
         employers_id INT REFERENCES employers(id) NOT NULL,
         name TEXT NOT NULL,
         salary_from INT DEFAULT NULL,
         salary_to INT DEFAULT NULL,
         requirement text DEFAULT NULL,
         responsibility text DEFAULT NULL,
         url text);
         '''
                )
    con.commit()
    con.close()


def push_data_in_employers(file_json: str = 'employers_data.json') -> None:
    """
    Функция открывает файл, берёт данные и загружает их в таблицу employers
    :param file_json: Название файла, откуда будут взяты данные. По умолчанию file_json = 'employers_data.json'
    :return: None
    """
    data_list = []

    try:
        with open(file_json) as json_file:
            data = json.load(json_file)
            for row in data["items"]:
                data_tuple = tuple([row["id"], row["name"], row["url"], row["open_vacancies"]])
                data_list.append(data_tuple)

    except FileNotFoundError as mail_3:
        print(mail_3)
        print("Не находит 'employers_data.json' ")

    con = create_con()
    cur = con.cursor()
    for row in data_list:
        cur.execute(
            "INSERT INTO employers (id, name, url,count_open_vacancies) VALUES "
            f"{row}"
        )
    con.commit()
    con.close()


def push_data_in_vacancies(file_json: str = 'vacancies_data.json') -> None:
    """
    Функция открывает файл, берёт данные и загружает их в таблицу vacancies
    :param file_json: Название файла, откуда будут взяты данные. По умолчанию file_json = 'vacancies_data.json'
    :return: None"""
    data_list = []

    try:
        with open(file_json) as json_file:
            data = json.load(json_file)
            for key, value in data.items():

                for line in value["items"]:
                    salary_from = line["salary"]["from"] if line["salary"]["from"] else 0
                    salary_to = line["salary"]["to"] if line["salary"]["to"] else 0
                    requirement = line["snippet"]["requirement"] if line["snippet"]["requirement"] else ''
                    responsibility = line["snippet"]["responsibility"] if line["snippet"]["responsibility"] else ''
                    url = line["alternate_url"] if line["alternate_url"] else ''
                    data_tuple = tuple([line["id"], key, line["name"],
                                        salary_from, salary_to, requirement, responsibility, url])
                    data_list.append(data_tuple)

    except FileNotFoundError as mail_4:
        print(mail_4)
        print("Не находит 'vacancies_data.json' ")

    con = create_con()
    cur = con.cursor()
    for row in data_list:
        cur.execute(
            "INSERT INTO vacancies "
            "(id, employers_id, name, salary_from, salary_to, requirement, responsibility, url) VALUES"
            f"{row}"
        )
    con.commit()
    con.close()


if __name__ == "__main__":
    create_table_employers_postgres()
    create_table_vacancies_postgres()
    push_data_in_employers()
    push_data_in_vacancies()
