import pdfkit
from PyPDF2 import PdfMerger
import os

# pageCounter - количество страниц в книге, замените под свое необходимое значение
pageCounter = 352
merger = PdfMerger()
filenames = []


def process_page(i):
    try:
        print('Печатаю', i, 'страницу')
        x = '{:04}'.format(i)
        # url - ссылка на страницу, я находил ее через веб инспектор
        # пример на скрине - ebooks/2021/03/05/c3530b7d86ec06779b9c43b2cad99de6/OEBPS
        url = f'https://bmstu.press/ebooks/2021/03/05/c3530b7d86ec06779b9c43b2cad99de6/OEBPS/mybook{x}.xhtml'
        filename = f'{i}.pdf'
        pdfkit.from_url(url, filename)
        print('Напечатал', i, 'страницу')

        return filename
    except Exception as e:
        print(f'Ошибка при обработке страницы {i}: {e}')
        return None


# Запускаем функцию process_page для каждой страницы
for i in range(1, pageCounter):
    filename = process_page(i)
    if filename is not None:
        filenames.append(filename)

# После того как все страницы обработаны, добавляем их в объединенный PDF
for filename in filenames:
    merger.append(filename)

# Записываем все в один файл и закрываем merger
bookName = 'Mosyagin'
merger.write(f'{bookName}.pdf')
merger.close()

# После того как все страницы объединены, удаляем временные файлы
for filename in filenames:
    os.remove(filename)
