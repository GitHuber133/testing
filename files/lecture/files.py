# работа с файлами

# каретка - указатель - курсор

# open(<путь до файла>)

# file = open('D:/makers/files/lecture/files.py') # абсолютный путь
# file = open('files.py') # относительный путь (относительно той директории в которой вы работаете)

# Режимы работы с файлами
# 1. чтения -> r/r+ (read)
# 2. записи -> w/w+ (write)
# 3. добавления -> ф/a+ (append)
# b, x, t

# file = open('text.txt', 'r')
# print(file.read()) 
# file.close()

# file = open('D:\makers\files\lecture\text.txt')
# data = file.read()
# data = data.split('\n')
# print(data)
# file.close()

# контекстный менеджер
# with open('text.txt ') as file: # file = open('text.txt)
#     data = file.readline()
#     print(data)
#     print(file.readline())
#     print(file, 'inside')

# print(file.read(), 'outside')

# file.tell() -> возвращает индекс где находиться каретка(курсор)
# file.seek(index) -> перемещает курсор на индекс который вы передали

# with open('D:/makers/files/lecture/text.txt', 'r') as file:
    # print(file.readline().replace('\n', ''))
    # print(file.tell())
    # file.seek(0)
    # print(file.readline().replace('\n', ''))
    # data = file.read()
    # index = data.index('\n')
    # file.seek(index+1)
    # print(file.readline().replace('\n', ''))
    # print(file.readline())
    # print(file.tell())
    # file.read()
    # print(file.tell())
    # print(file.readline())



# with open('D:/makers/files/lecture/text.txt', 'r') as file:
    # print(file.readline(50))
    # print(file.readlines(8))
    # print(file.read(5))

# with open('D:/makers/files/lecture/text.txt', 'w') as file:
#     file.write('Pervya Strochka!\n')
#     file.write('John Snow is bastard of Ned Stark!\n')
#     file.write('This is lesson abous files!\n')
#     file.seek(0)
#     data = ['Bilal is genius!\n', 'Tima good boy!\n']
#     file.writelines(data)

# with open('D:/makers/files/lecture/text.txt', 'r+') as file:
#     file.write('John Snow')
#     file.seek(0)
#     print(file.read())



# sudo apt update
# sudo apt install tesseract-ocr
# sudo apt install libtesseract-dev


# with open('D:/makers/files/lecture/text.txt', 'r+') as file:
#     file.write('John Snow')
#     file.seek(0)
#     print(file.read())

# try:
#     from PIL import Image
# except ImportError:
#     import Image

# import pytesseract
# import re

# def gen_imei_code(image)
#     string = pytesseract.image_to_string(image)
#     # print(string, type(string))
#     list_of_imei = re.findall(r'IMEI\d.\s\d+', string)

#     with open('imei_codes.txt', 'w') as file:
#         file.writelines(f'{x}\n' for x in list_of_imei)

# Image = 'imei.gpg'
# get_imei_code(Image)