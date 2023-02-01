# 1.	Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def divis_args(arg1, arg2) -> object:
    try:
        div_result = round(arg1 / arg2, 2)
    except ZeroDivisionError:
        return 'делить на ноль нельзя'
    div_result = round(arg1 / arg2, 2)
    return div_result


print(divis_args(8, 3))
