import os
import csv


class dog:
    def __init__(self, number, FIO, Email, Group):    # конструктор класса
        # self - ссылка на сам только что созданный объект
        self.number = number
        self.FIO = FIO
        self.Email = Email
        self.Group = Group

    def __setattr__(self, attr, value):     # установка атрибутов
        if attr == 'number':
            self.__dict__[attr] = value
        elif attr == 'FIO':
            self.__dict__[attr] = value
        elif attr == 'Email':
            self.__dict__[attr] = value
        elif attr == 'Group':
            self.__dict__[attr] = value
        else:
            raise AttributeError

    def __repr__(self):  # repr позволяет получить описание объекта
        return " Номер: " + self.number.join(("'", "'")) + " Имя: " + self.FIO.join(("'", "'")) + \
               " Маил: " + self.Email.join(("'", "'")) + " Группа: " + \
               self.Group.join(("'", "'"))


class dog_ovch(dog):
    def __init__(self, number, FIO, Email, Group): #init конструктор объектов класса, вызывается при создании объектов
        super().__init__(number, FIO, Email, Group) # self для обращения в переменным и методам объекта

class dog_al(dog):
    def __init__(self, number, FIO, Email, Group):
        super().__init__(number, FIO, Email, Group)

class dog_bul(dog):
    def __init__(self, number, FIO, Email, Group):
        super().__init__(number, FIO, Email, Group)



class WorkWithFile:
    @staticmethod
    def count_file():
        """
        Статический метод выполняет подсчёт файлов в директории
        :return 0 если неверный путь
        """
        # "listdir()" - получение списка файлов в дириктории.
        # "try - except" - для обработки исключений
        # "os.path.isfile()" - сущ ли путь???
        # "os.path.join()" - правильно соединяет компоненты пути файловой системы через "/"
        way = input("Введите путь: ")
        try:
            return len([name for name in os.listdir(way) if os.path.isfile(os.path.join(way, name))])
        except:
            print("Неверный путь")
            return 0

    @staticmethod
    def reader_file():
        """
        Статический метод reader_file считывает строки из файла и записывает данные в словарь
        """
        Dictionary = []
        with open("data.csv", "r") as fl:
            file = csv.DictReader(fl, delimiter=";")
            for row in file:
                elem = dog_ovch(row['#'], row['FIO'], row['Email'], row['Group'])
                Dictionary.append(elem)
            return Dictionary


class DictionaryWorks(WorkWithFile):
    def __init__(self, table):  # init позволяет классу инициализировать атрибуты класса
        self.all_rows = table

    def __getitem__(self, i):  # getitem позволяет задать поведение при обращении к элементу контейнера.
        return self.all_rows[i]

    def print_csv(self):
        """
        Вывод всех данных, содержит иттератор
        """
        obj_dict = iter(self)
        while True:
            try:
                print(next(obj_dict))
            except StopIteration:
                break
        print()

    def sort_csv(self):
        """
        Сортировка
        """
        try:
            self.all_rows = sorted(self.all_rows, key=lambda name: name.number)
            self.print_csv()
        except:
            print("Такого ключа не существует")

    def print_specific_csv(self):
        """
        Вывод данных, где порода = "мышь"
        """
        print("Введите название группы")
        NameGroup = input()
        for elem in self:   # self - поле c породой

            if str(elem.Group) == "IVTAPbd":
                print(elem)
        print()


def read_csv_file(Dictionary):
    """
    Считывает элементы в .csv файле и записывает все данные в лист
    :param Dictionary лист объектов
    """
    with open("data.csv", "r") as cf:
        # csv.DictReader() - читает CSV файл как список словарей.
        file = csv.DictReader(cf, delimiter=";")
        for way in file:
            # append() - вставляет в конец исходного списка значение аргумента.
            Dictionary.append(way)
    print("Данные считаны успешно")
    return Dictionary


def change_csv(Dictionary):
    """
    Изменяет данные в Dictionary и перезаписывает изменения в файл
    :param Dictionary лист
    """
    read_csv_file(Dictionary)
    st = int(input("Строка для редактирования: "))
    k = input("Введите ключ, который надо поменять: ")
    v = input("Поменять на: ")
    if st >= 0:
        Dictionary[st][k] = v
        print("Успешно изменено")
    else:
        print("Строка не может быть отрицательной")

    """
    Перезаписывает файл .csv формата на то, что было сохранено в Dictionary
    """
    names = ['#', 'FIO', 'Email', 'Group']
    with open("data.csv", "w") as csvfile:
        wrt = csv.DictWriter(csvfile, delimiter=";", fieldnames=names, lineterminator="\r")
        wrt.writeheader()
        for st in Dictionary:
            wrt.writerow(st)
        print("Данные успешно записаны в файл")


def main():
    """
    Функция, в которой вызываются все функции
    """
    Dictionary = []
    data = DictionaryWorks.reader_file()
    File_Work = DictionaryWorks(data)

    print("1)Показать количество файлов в директории")
    print("2)Показать словарь")
    print("3)Выборка")
    print("4)Сортировка")
    print("5)Редактировать и записать изменения в файл")

    while True:
        n = input()
        if n == "1":
            # "format()" - форматирует значение переменной для вывода на печать
            print("Найдено файлов: {}".format(DictionaryWorks.count_file()))
        elif n == "2":
            File_Work.print_csv()
        elif n == "3":
            File_Work.print_specific_csv()
        elif n == "4":
            File_Work.sort_csv()
        elif n == "5":
            change_csv(Dictionary)
        else:
            print("Завершение работы")
            break



if __name__ == '__main__':
    main()