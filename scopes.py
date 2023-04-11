# Область видимости и пространство имён (scopes)
# технология которая определяет контекст имени(переменные), в рамках которого мы можем ее использовать

# built-ins(Встроенная область видимости) -> print, len, max, min,
# global(Глобальная) -> область одного файла
# enclosed(не локальная(замкнутая), nonlocal)
# local(локальная) -> область внутри одной функции


# x = 200

# def myFunc():
#     print(x)
#     a = 300
#     print(a)

# myFunc()
# # print(a)
# print(x)


# a = 10 # global
# print # built-in

# def hello(): # global 
#     a = 'Hello world' # local
#     print(a, 'local inside in func!')

# hello()
# print(a, 'global')

# LEGB - local enclosed global built-in
        #  --------->>>>>>>>>>>>>


# max = 5
# Enclosed
# замкнутое пространство имен - локальное пространство, у которого есть внутренее(вложенное) локальное пространство


# x = 'global'
# print(x)

# def enclosed(): # global
#     x = 'enclosed'
#     def local(): # enclosed
#         x = 'local'
#         print(x, '3') # local
#     print(x, '2') # enclosed
#     local()
#     print(x, '4') # enclosed

# enclosed()
# print(x, '5')


# a = 5

# def func():
#     print(a) # 5
#     a = a + 1

# func()

# global -> позволяет изменять значение глобальной переменной находясь внутри локальной области

# nonlocal -> позволяет изменять значение не локальной (замкнутой) переменной находясь внутри локальной области

# var = 100

# def increment(): # LEGB
#     global var
#     var += 1 # var = var + 1

# print(var) # 100
# increment()
# print(var) # 101
# increment()
# increment()
# increment()
# increment()
# increment()
# print(var) # 106


# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# c_wash = counter()
# c_ask = counter()
# c = counter() # <function counter.<locals>.increment at 0x0000022D16DE9760>
# print(c()) # 1
# print(c()) # 2
# print(c()) # 3
# print(c()) # 4
# print(c()) # 5




# print(dir(__builtins__))
# print(len(dir(__builtins__)))





# globals - func которая возвращает все имена внутри глобальной области видимости

# locals - функция которая возвращает все имена внутри глобальной области видимости и локальной

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# def showStats(heroes, mobs):
#     print()
#     print(f'John Snow ты убил:\n\tгероев: {heroes} \n\tмобов: {mobs}')
#     print()


# counter_heroes = counter()
# counter_mobs = counter()
# heroes = 0
# mobs = 0

# print('Приветствую ваш, Король Севера John Snow В Вестеросе!')
# while True:
#     print('Тебе доступны следующие действия: ')
#     print('1-убить героя, 2-убить моба, 3-статистика, 4-выйти из игры')
#     choice = input('Введите что хотите сделать: ').strip()
#     if choice == '1':
#        heroes = counter_heroes()
#        print('Вы обезглавили Ланистера!')
#     elif choice == '2':
#         mobs = counter_mobs()
#         print('Вы убили белого ходока!')
#     elif choice == '3':
#         showStats(heroes, mobs)
#     elif choice == '4':
#         print('Пока-пока! Ждём ещё раз!')
#         break
    

