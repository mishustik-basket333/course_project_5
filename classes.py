import requests

class HeadHunterAPI:
    """Класс для работы с API Head Hunter"""

    def get_request(self, key_word, page):
        """Метод делает запрос на https://api.hh.ru/vacancies и возвращает результат в формате json по ключу [items]"""
        params = {
            "text": key_word,
            "page": page,
            "per_page": VACANCY_COUNT,
        }
        try:
            return requests.get("https://api.hh.ru/vacancies", params=params).json()["items"]
        except requests.exceptions.ConnectionError as e:
            print(e)
            print("Ошибка при запросе. Ошибка соединения")