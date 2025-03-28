# Классы позволяют объединять данные и функции в единый объект,
# что способствует структурированию кода и повторному использованию.
# Пример использования:
# class Dog: def __init__(self, name, age):
# Конструктор класса self.name = name self.

import json, string # Импортируем библиотеки json (для работы с JSON) и string (для работы со строками)


class TextAnalyzer: # Объявление класса TextAnalyzer
    def __init__(self): # Конструктор класса. Выполняется при создании объекта класса.
        self.text = None # Инициализируем атрибут text значением None (текст пока не загружен).
        self.result = {} # Создаем пустой словарь result для хранения результатов анализа.


    def read_text_from_file(self, path): # Метод для чтения текста из файла. Принимает путь к файлу (path).
        try: # Блок try...except для обработки исключений.
            with open(path, 'r', encoding='utf-8') as file: # Открываем файл в режиме чтения ('r') с кодировкой UTF-8.
                self.text = file.read() # Читаем весь текст из файла и сохраняем в атрибут self.text.
        except FileNotFoundError: # Если файл не найден, перехватываем исключение FileNotFoundError.
            print(f"Ошибка: Файл {path} не найден.") # Выводим сообщение об ошибке.
            self.text = "" # Присваиваем пустую строку атрибуту self.text, чтобы избежать ошибок в дальнейшем.


    def analyze(self): # Метод для анализа текста.
        if not self.text: # Проверяем, есть ли текст. Если нет (файл не найден или пустой), выходим из метода.
            return

        words = self.text.split() # Разбиваем текст на слова по пробелам.
        word_counts = {} # Создаем пустой словарь для подсчета количества каждого слова.

        for word in words: # Цикл по всем словам.
            word_lower = word.lower() # Приводим слово к нижнему регистру.
            word_counts[word_lower] = word_counts.get(word_lower, 0) + 1 # Увеличиваем счетчик для слова. Если слова нет в словаре, создаем запись с начальным значением 0.

        letter_counts = {} # Создаем пустой словарь для подсчета частоты букв.

        for char in self.text.lower(): # Цикл по всем символам текста, приведенного к нижнему регистру.
            if char.isalpha(): # Проверяем, является ли символ буквой.
                letter_counts[char] = letter_counts.get(char, 0) + 1 # Увеличиваем счетчик для буквы.

        punctuation_counts = {} # Создаем пустой словарь для подсчета других символов (знаки препинания и т.д.).

        for char in self.text: # Цикл по всем символам текста.
            if not char.isalnum() and not char.isspace(): # Проверяем, не является ли символ буквой, цифрой или пробелом.
                punctuation_counts[char] = punctuation_counts.get(char, 0) + 1 # Увеличиваем счетчик.

        lines = self.text.splitlines() # Разбиваем текст на строки.


        self.result = { # Заполняем словарь result результатами анализа.
            "Всего символов": len(self.text), # Общее количество символов.
            "Всего букв": sum(c.isalpha() for c in self.text), # Количество букв.
            "Всего строк": len(lines), # Количество строк.
            "Непустых строк": sum(bool(line.strip()) for line in lines), # Количество непустых строк (strip() удаляет пробелы в начале и конце строки).
            "Всего слов": len(words), # Количество слов.
            "Слов в каждой строке": {i + 1: len(line.split()) for i, line in enumerate(lines)}, # Количество слов в каждой строке. enumerate() возвращает номер строки и саму строку.
            "Символов в каждой строке": {i + 1: len(line) for i, line in enumerate(lines)}, # Количество символов в каждой строке.
            "Повторяющиеся слова": {w: c for w, c in word_counts.items() if c > 1}, # Слова, встречающиеся более одного раза.
            "Частота букв": letter_counts, # Частота каждой буквы.
            "Другие символы": punctuation_counts, # Количество других символов.
        }


    def write_result_to_txt(self, path='analyz.txt'): # Метод для записи результатов в текстовый файл.
        with open(path, 'w', encoding='utf-8') as file: # Открываем файл для записи с кодировкой UTF-8.
            for key, value in self.result.items(): # Цикл по парам ключ-значение в словаре result.
                file.write(f"{key}: " if not isinstance(value, dict) else f"{key}:\n") # Записываем ключ и двоеточие. Если значение - словарь, добавляем перевод строки.
                if isinstance(value, dict): # Если значение - словарь,
                    for sub_key, sub_value in value.items(): # перебираем его элементы.
                        file.write(f"    {sub_key}: {sub_value}\n") # Записываем под-ключ и под-значение с отступом.
                else: # Если значение не словарь,
                    file.write(f"{value}\n") # записываем значение и перевод строки.

    def write_result_to_json(self, path='analyz.json'): # Метод для записи результатов в JSON-файл.
        with open(path, 'w', encoding='utf-8') as file: # Открываем файл для записи с кодировкой UTF-8.
            json.dump(self.result, file, ensure_ascii=False, indent=4) # Записываем словарь result в JSON-формат. ensure_ascii=False для корректного отображения кириллицы. indent=4 для форматирования.


# Использование класса:
analyzer = TextAnalyzer() # Создаем объект класса TextAnalyzer.
analyzer.read_text_from_file('poem.txt') # Читаем текст из файла.
analyzer.analyze() # Анализируем текст.
analyzer.write_result_to_txt() # Записываем результаты в текстовый файл.
analyzer.write_result_to_json() # Записываем результаты в JSON-файл.