"""

Домашнее задание №2

Работа с файлами


* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
* Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
* Подсчитайте количество слов в тексте
* Замените точки в тексте на восклицательные знаки
* Сохраните результат в файл referat2.txt
"""

def main():

    with open('referat.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    with open('referat2.txt', 'w', encoding='utf-8') as f:
        f.write(content.replace('.', '!'))
    content = content.replace('\n', ' ')
    print(f'Длина текста (количество символов) - {len(content)}')
    print (f'Количество слов в тексте - {len(content.split())}')


if __name__ == "__main__":
    main()
