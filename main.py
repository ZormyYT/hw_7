# result = []
# def divider(a, b):
#  if a < b:
#  raise ValueError
#  if b > 100:
#  raise IndexError
#  return a/b
# data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
# for key in data:
#  res = divider(key, data[kem])
#  result.append(res)
#
# print(result)





# try:
#     try:
#         print("Start code")
#         print(10 / 0)
#         print("No errors")
#     except (NameError, ZeroDivisionError) as error:
#         print(error)
# except BaseException:
#     print('Base exception error')
# else:
#     print("No errors")
# finally:
#     print('finally')
#
#
# print("Code after capsule")
#
#
# def checker(var_1):
#     if type(var_1) != str:
#         raise TypeError(f"Sorry, we can`t work with {type(var_1)}, we need class str")
#     else:
#         return var_1
#
#
# first_var = 123
# checker(first_var)






result = []

def divider(a, b):
    if a < b:
        raise ValueError("a менше за b")
    if b > 100:
        raise IndexError("b більше 100")
    return a / b


data = {
    10: 2,
    2: 5,
    "123": 4,
    18: 0,
    8: 4
}

for key in data:
    try:
        if not isinstance(key, (int, float)) or not isinstance(data[key], (int, float)):
            raise TypeError("Невірні дані")

        res = divider(key, data[key])
        result.append(res)

    except ZeroDivisionError as error:
        print(f"ZeroDivisionError: {error}")

    except ValueError as error:
        print(f"ValueError: {error}")

    except IndexError as error:
        print(f"IndexError: {error}")

    except TypeError as error:
        print(f"TypeError: {error}")

    except Exception as error:
        print(f"Інша помилка: {error}")

print("Результат:", result)
