import psycopg2


class DBManager:
    """Класс для подключения и работы с DB postgres"""

    def __init__(self, database="course_project_5", user="postgres", password="qwerty", host="127.0.0.1", port="5432"):
        self.__database = database
        self.__user = user
        self.__password = password
        self.__host = host
        self.__port = port

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании"""
        con = psycopg2.connect(database=self.__database, user=self.__user,
                               password=self.__password, host=self.__host, port=self.__port
                               )

        cur = con.cursor()
        cur.execute(
            '''SELECT name, count_open_vacancies FROM employers;'''
        )
        data = cur.fetchall()
        cur.close()
        con.close()
        return data

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию
        """
        con = psycopg2.connect(database=self.__database, user=self.__user,
                               password=self.__password, host=self.__host, port=self.__port
                               )

        cur = con.cursor()
        cur.execute(
            '''SELECT vacancies.name,employers.name, salary_from, salary_to, vacancies.url  
            FROM vacancies, employers ;'''
        )
        data = cur.fetchall()
        cur.close()
        con.close()
        return data

    def get_avg_salary(self):
        """ Получает среднюю зарплату по вакансиям"""
        con = psycopg2.connect(database=self.__database, user=self.__user,
                               password=self.__password, host=self.__host, port=self.__port
                               )

        cur = con.cursor()
        cur.execute(
            '''SELECT AVG (salary_from) FROM vacancies;'''
        )
        data = cur.fetchall()
        cur.close()
        con.close()
        return data

    def get_vacancies_with_higher_salary(self):
        """ Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        con = psycopg2.connect(database=self.__database, user=self.__user,
                               password=self.__password, host=self.__host, port=self.__port
                               )

        cur = con.cursor()
        cur.execute(
            '''SELECT * FROM vacancies
            WHERE salary_from > (SELECT AVG (salary_from) FROM vacancies)'''
        )
        data = cur.fetchall()
        cur.close()
        con.close()
        return data

    def get_vacancies_with_keyword(self, word):
        """ Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например 'python'"""
        con = psycopg2.connect(database=self.__database, user=self.__user,
                               password=self.__password, host=self.__host, port=self.__port
                               )

        cur = con.cursor()
        cur.execute(
            f"SELECT * FROM vacancies WHERE name LIKE '%{word}%'"
        )
        data = cur.fetchall()
        cur.close()
        con.close()
        return data


if __name__ == "__main__":
    aaa = DBManager(database="course_project_5", user="postgres", password="qwerty")
    data_1 = aaa.get_companies_and_vacancies_count()
    data_2 = aaa.get_all_vacancies()
    data_3 = aaa.get_avg_salary()
    data_4 = aaa.get_vacancies_with_higher_salary()
    data_5 = aaa.get_vacancies_with_keyword("Грузчик")

    for row in data_5:
        print(row)
    print(len(data_5))
