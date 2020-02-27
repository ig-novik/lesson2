"""

Домашнее задание №2

Дата и время

* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime

"""

def print_days():
    dt_now = datetime.now() .date()
    delta = [timedelta(days=1), timedelta(days = 31)]
    print(f'Вчера: {dt_now - delta[0]}')
    print(f'Сегодня: {dt_now}')
    print(f'Месяц назад: {dt_now - delta[1]}')
    
    
def str_2_datetime(string):
    return datetime.strptime(string, "%d/%m/%y %H:%M:%S.%f")

if __name__ == "__main__":
    from datetime import datetime, date, timedelta
    print_days()
    print(str_2_datetime("01/01/17 12:10:03.234567"))
