'''
Вашей программе будет доступна функция foo, которая может бросать исключения.

Вам необходимо написать код, который запускает эту функцию, затем ловит исключения ArithmeticError, AssertionError, ZeroDivisionError и выводит имя пойманного исключения.

Пример решения, которое вы должны отправить на проверку.

try:
    foo()
except Exception:
    print("Exception")
except BaseException:
    print("BaseException")
'''


# только 3/5

# try:
#     foo()
# except BaseException as e:
#     print(type(e).__name__)

# Топорно пишет ошибку

try:
    foo()
except ZeroDivisionError:
    print('ZeroDivisionError')
except AssertionError:
    print('AssertionError')
except ArithmeticError:
    print('ArithmeticError')