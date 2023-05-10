import psycopg2
import json


def create_table_employers_postgres() -> None:
    """
    Функция подключается к БД course_project_5 и создаёт таблицу employers
    :return: None
    """
    con = psycopg2.connect(database="course_project_5", user="postgres",
                           password="qwerty", host="127.0.0.1", port="5432"
                           )
    #    print("Database: course_project_5 opened successfully")

    cur = con.cursor()
    cur.execute('''CREATE TABLE employers
         (id int PRIMARY KEY NOT NULL,
         name TEXT NOT NULL,
         url TEXT,
         count_open_vacancies INT NOT NULL);'''
                )

    # print("Table: employers created successfully")

    con.commit()
    con.close()


def create_table_vacancies_postgres() -> None:
    """"""
    con = psycopg2.connect(database="course_project_5", user="postgres",
                           password="qwerty", host="127.0.0.1", port="5432"
                           )

    #    print("Database: course_project_5 opened successfully")

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

    #    print("Table: employers created successfully")

    con.commit()
    con.close()


def push_data_in_employers(file_json: str) -> None:
    """
    Функция открывает указанный файл, берёт данные и загружает их в таблицу employers
    :param file_json: Название файла, откуда будут взяты данные
    :return: None
    """
    data_list = []

    with open(file_json) as json_file:
        data = json.load(json_file)

        for row in data["items"]:
            data_tuple = tuple([row["id"], row["name"], row["url"], row["open_vacancies"]])

            data_list.append(data_tuple)

        # for row in data_list:
        #     print(row)

    con = psycopg2.connect(
        database="course_project_5",
        user="postgres",
        password="qwerty",
        host="127.0.0.1",
        port="5432"
    )

    #    print("Database: course_project_5 opened successfully")

    cur = con.cursor()

    for row in data_list:
        cur.execute(
            "INSERT INTO employers (id, name, url,count_open_vacancies) VALUES "
            f"{row}"
        )

    con.commit()
    #    print("Record inserted successfully")
    con.close()


def push_data_in_vacancies(file_json: str) -> None:
    """"""
    data_list = []

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

        con = psycopg2.connect(
            database="course_project_5",
            user="postgres",
            password="qwerty",
            host="127.0.0.1",
            port="5432"
        )

#        print("Database: course_project_5 opened successfully")
        cur = con.cursor()

        for row in data_list:
            cur.execute(
                "INSERT INTO vacancies "
                "(id, employers_id, name, salary_from, salary_to, requirement, responsibility, url) VALUES"
                f"{row}"
            )

        con.commit()
#        print("Record inserted successfully")
        con.close()


if __name__ == "__main__":
    """"""
    # create_table_employers_postgres()
    # create_table_vacancies_postgres()
    # push_data_in_employers('employers_data.json')
    push_data_in_vacancies('vacancies_data.json')

    # con = psycopg2.connect(
    #     database="course_project_5",
    #     user="postgres",
    #     password="qwerty",
    #     host="127.0.0.1",
    #     port="5432"
    # )
    #
    # #        print("Database: course_project_5 opened successfully")
    # cur = con.cursor()
    #
    # cur.execute(
    #     "INSERT INTO vacancies "
    #     "(id, employers_id, name, salary_from, salary_to, requirement, responsibility, url) VALUES "
    #     "(100, 36227, 'lalala', 100,101, 'abc', 'def', '')"
    # )
    #
    # con.commit()
    # #        print("Record inserted successfully")
    # con.close()
