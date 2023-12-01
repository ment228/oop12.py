"""Смоделировать структуру библиотеки. Построить диаграмму классов.
Классы
Свойства
Библиотека
название (getter, setter)
Отдел (по жанрам)
название жанра (getter, setter)
количество изданий (getter, setter)
Издание
название (getter, setter)
автор (getter, setter)
год издания (getter, setter)
сформировать описание()
Книга
резюме (getter, setter)
сформировать описание()
Журнал
статьи (getter, setter)
сформировать описание()
"""
class Library:#новый класс Library
    def __init__(self, name):#конструктор с параметрами name
        self._name = name
        self._departments = []#инициализируем параметры

    def get_name(self):#метод get_name
        return self._name#возвращаем name

    def set_name(self, name):#метод set_name
        self._name = name

    def add_department(self, department):#метод add_department
        self._departments.append(department)

    def remove_department(self, department):#метод remove_department
        self._departments.remove(department)

class Department:#класс Departament
    def __init__(self, genre):#конструктор с параметрами genre
        self._genre = genre
        self._num_publications = 0#инициализируем параметры

    def get_genre(self):#метод get_genre
        return self._genre#возвращаем _genre

    def set_genre(self, genre):#метод set_genre
        self._genre = genre

    def get_num_publications(self):#метод get_new_publications
        return self._num_publications#возвращаем _num_publications

    def set_num_publications(self, num):#метод set_num_publications
        self._num_publications = num

class Publication:#новый класс Publication
    def __init__(self, title, author, year):#конструктор с параметрами title, author, year
        self._title = title
        self._author = author
        self._year = year#инициализируем параметры

    def get_title(self):#метод get_tittle
        return self._title#возвращаем _tittle

    def set_title(self, title):#метод set_tittle
        self._title = title

    def get_author(self):#метод get_author
        return self._author#возвращаем _author

    def set_author(self, author):#метод set_author
        self._author = author

    def get_year(self):#метьод get_year
        return self._year#возвращаем _year

    def set_year(self, year):#метод set_year
        self._year = year

    def generate_description(self):#метод generate_description
        return f"Издание: {self._title}, Автор: {self._author}, Год издания: {self._year}"#возвращаем сообщение

class Book(Publication):#новый класс Book Наследующий от Publication
    def __init__(self, title, author, year, summary):#конструктор с параметрами title, author, year, summary
        super().__init__(title, author, year)#наследующие параметры
        self._summary = summary#инициализируем параметры

    def get_summary(self):#метод get_summary
        return self._summary#возвращаем _summary

    def set_summary(self, summary):#метод set_summary
        self._summary = summary

    def generate_description(self):#метод generate_description
        return f"Книга: {self._title}, Автор: {self._author}, Год издания: {self._year}\nРезюме: {self._summary}"#возвращаем сообщение

class Magazine(Publication):#новый класс Magazine наследующиц от Publication
    def __init__(self, title, author, year, articles):#конструктор с параметрами title, author, year, articles
        super().__init__(title, author, year)#наследующие параметры
        self._articles = articles#инициализируем параметры

    def get_articles(self):#метод get_articles
        return self._articles#возвращаем _article

    def set_articles(self, articles):#метод set_article
        self._articles = articles

    def generate_description(self):#метод generate_description
        article_list = (self._articles)
        return f"Журнал: {self._title}, Автор: {self._author}, Год издания: {self._year}\nСтатьи:{article_list}"#возвращаем сообщение


#Создание объектов и демонстрация использования
#Создание библиотеки
library = Library("Центральная библиотека")
# Создание отдела и добавление в библиотеку
department = Department("Фантастика")
library.add_department(department)
#Создание книги и добавление в список
book = Book("оно", "стивен кинг", 2017, "ужас детей в городе Дерри")
department.set_num_publications(1)
book_description = book.generate_description()
print(book_description)  # Вывод описания книги
#Создание журнала
magazine = Magazine("терминатор", "Уильям Вишер", 1985, "блабла")
department.set_num_publications(2)
magazine_description = magazine.generate_description()
print(magazine_description)#Вывод описания журнала