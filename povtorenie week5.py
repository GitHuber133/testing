# # Decorators
# # Scope
# # Bulit in functions

# # Декораторы - функция высшего порядка (функция которая принимает другую функцию в качестве аргумента)

# # def decorator(func):
# #     def wrapper():
# #         print(f'this function named {func.__name__}')
# #         return func
# #     return wrapper

# # @decorator
# # def hello():
# #     print('Hello')

# # hello()

# def sq(func):
#     def wrapper(num):
#         nums = func(num)
#         return list(map(lambda x: x ** 2, nums))
#     return wrapper

# @sq
# def func(num: int):
#     return list(range(1, num))
# @sq
# def func2(num):
#     return list(range(1, num, 2))

# # print(func(5))
# print(func2(6))

# ------------------------------------------------------------
# map, filter, enemurate, zip
# lambda

# ls = ['hello', 'word', 'min']

# new_list = list(map(len, ls))
# print(new_list)

# new_list = list(filter(lambda x: len(x) > 4, ls))
# print(new_list)

# ls = [1, 2, 3, 4, 5]
# new_ls = list(map(lambda x: x ** 2 if x % 2 == 0 else x, ls))
# print(new_ls)













