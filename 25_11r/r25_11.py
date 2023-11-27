''' Создать класс date для работы с датами в формате "год.месяц.день". Дата представляется структурой с тремя полями
типа unsigned int. Класс должен включать не менее 3 функций инициализации: числами, строкой вида "год.месяц.день" и
датой. Обязательными операциями являются: вычисление даты через заданное количество дней, вычитание заданного количества
 дней из даты, определение високосности года, сравнение дат, вычисления количества дней между датами. '''
class Date:
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    def from_numbers(self, year, month, day):
        return Date(year, month, day)

    def from_string(self, date_str):
            year, month, day = map(int, date_str.split('.'))
            return Date(year, month, day)


    def from_date(self, other_date):
        return Date(other_date.year, other_date.month, other_date.day)

    @staticmethod
    def input_date():
            date_str = input("Введите дату в формате 'год.месяц.день': ")
            year, month, day = map(int, date_str.split('.'))
            return Date(year, month, day)


    def __str__(self):
        return f"{self.year}.{self.month}.{self.day}"

    '''
    def calculate_date(self, days):
        # вычисление новой даты после заданного количества дней

    def minus_date(self):
        # вычитание заданного количества дней из даты
    '''

    def leap_year(self):
        # Проверка на високосный года
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            return True
        else:
            return False

    '''
    def comparison_date(self):
        # сравнение дат

    def days_between(self,user_date, other_date):
        # Вычисление количества дней между двумя датами
    '''
# Пример использования класса
if __name__ == "__main__":
        # Инициализация через числа
        date1 = Date(2023, 11, 26)
        print(f"Дата числами: {date1}")

        # Инициализация через строку
        date_str = "2023.11.27"
        date2 = date1.from_string(date_str)
        print(f"Дата строкой: {date2}")

        print('Выберите функцию:\n'
              '1 - Проверка на високосность\n'
              '2 - Вычисление количества дней между двумя датами\n'
              '3 - Сравнение двух дат \n')
        check = int(input('введите номер: '))

        # Ввод даты вручную
        user_date = Date.input_date()

        if check == 1:
            print(f"Високосность: {user_date.leap_year()}")
        elif check == 2:
            #не реализовано
            other_date = Date.input_date()
            #print(f"Разница: {user_date.days_between()}")