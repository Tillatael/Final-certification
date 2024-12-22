'''
Задание 1. Логирование с использованием нескольких файлов
Напишите скрипт, который логирует разные типы сообщений в разные файлы.
Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
WARNING и выше — в warnings_errors.log.
'''

import logging

debug_info_logger = logging.getLogger('debug_info_logger')
debug_info_logger.setLevel(logging.DEBUG)
debug_info_handler = logging.FileHandler('debug_info.log')
debug_info_handler.setLevel(logging.DEBUG)
debug_info_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
debug_info_handler.setFormatter(debug_info_formatter)
debug_info_logger.addHandler(debug_info_handler)

warnings_errors_logger = logging.getLogger('warnings_errors_logger')
warnings_errors_logger.setLevel(logging.WARNING)
warnings_errors_handler = logging.FileHandler('warnings_errors.log')
warnings_errors_handler.setLevel(logging.WARNING)
warnings_errors_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
warnings_errors_handler.setFormatter(warnings_errors_formatter)
warnings_errors_logger.addHandler(warnings_errors_handler)

debug_info_logger.debug('Это сообщение DEBUG')
debug_info_logger.info('Это сообщение INFO')
warnings_errors_logger.warning('Это сообщение WARNING')
warnings_errors_logger.error('Это сообщение ERROR')
warnings_errors_logger.critical('Это сообщение CRITICAL')


'''
Задача 2. Работа с текущим временем и датой
Напишите скрипт, который получает текущее время и дату, а затем выводит их в
формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
недели в году.
'''

from datetime import datetime
import calendar

time_now = datetime.now()
formatted_time = time_now.strftime('%Y-%m-%d %H:%M:%S')
day_of_week = calendar.day_name[time_now.weekday()]
week_number = time_now.strftime('%U')

print(formatted_time)
print(day_of_week)
print(week_number)


'''
Задача 3. Планирование задач
Напишите функцию, которая принимает количество дней от текущей даты и
возвращает дату, которая наступит через указанное количество дней. Дополнительно,
выведите эту дату в формате YYYY-MM-DD.
'''

from datetime import datetime, timedelta

def get_future_date(days):
    future_date = datetime.now() + timedelta(days=days)
    return future_date.strftime('%Y-%m-%d')

print(get_future_date(5))

'''Задача 4. Опции и флаги
Напишите скрипт, который принимает два аргумента командной строки: число и
строку. Добавьте следующие опции:
● --verbose, если этот флаг установлен, скрипт должен выводить
дополнительную информацию о процессе.
● --repeat, если этот параметр установлен, он должен указывать,
сколько раз повторить строку в выводе.'''

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('number', type=int)
parser.add_argument('text', type=str)
parser.add_argument('--verbose', action='store_true')
parser.add_argument('--repeat', type=int, default=1)
args = parser.parse_args()

if args.verbose:
    print(f'Number: {args.number}')
    print(f'Text: {args.text}')
    print(f'Repeat: {args.repeat}')

for _ in range(args.repeat):
    print(args.text)

'''Задача 5. Запуск из командной строки
Напишите код, который запускается из командной строки и получает на вход путь
до директории на ПК. Соберите информацию о содержимом в виде объектов
namedtuple. Каждый объект хранит: имя файла без расширения или название
каталога, расширение, если это файл, флаг каталога, название родительского
каталога. В процессе сбора сохраните данные в текстовый файл используя
логирование.
'''

import argparse
import os
import logging
from collections import namedtuple

parser = argparse.ArgumentParser()
parser.add_argument('directory', type=str)
args = parser.parse_args()

logging.basicConfig(filename='directory_info.log', level=logging.INFO, format='%(message)s')

Entry = namedtuple('Entry', ['name', 'extension', 'is_dir', 'parent'])

def collect_directory_info(directory):
    entries = []
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        name, extension = os.path.splitext(item) if os.path.isfile(path) else (item, '')
        is_dir = os.path.isdir(path)
        parent = os.path.basename(directory)
        entry = Entry(name=name, extension=extension, is_dir=is_dir, parent=parent)
        entries.append(entry)
        logging.info(entry)
    return entries

collect_directory_info(args.directory)
