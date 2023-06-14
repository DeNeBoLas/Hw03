# # 2/11
# # def invite_to_event(username):
# #     return f"Dear {username}, we have the honour to invite you to our event"

# """3/11
# base_rate = 40
# price_per_km = 10
# total_trip = 0

# def trip_price(path):
#     global total_trip
#     total_trip += 1
#     summ = base_rate + price_per_km * path
#     return summ
# trip_price(4.3)   """


# """4/11
# def discount_price(price, discount):
#     def apply_discount():
#         nonlocal price
#         price = price - (discount * price)
#     apply_discount()
#     return price"""


# """5/11


# def get_fullname(first_name, last_name, middle_name=None):
#     if middle_name is not None:
#         return f'{first_name} {middle_name} {last_name}'
#     else:
#         return f'{first_name} {last_name}'
# """

# """6/11


# def format_string(string, length):
#     if len(string) >= length:
#         return string
#     else:
#         space_number = (length - len(string)) // 2
#         result = (' ' * space_number + string)
#         return result"""


# # """7/11"""
# # def first(size, *args):
# #     return size + len(args)
# # def second(size, **kwargs):
# #     return size + len(kwargs)

# """8/11"""


# # def cost_delivery(quantity, *orders, discount=0):
# #     if quantity == 1:
# #         return 5 + discount * quantity
# #     elif quantity > 1:
# #         summ = 5
# #     return summ + 2 * orders + discount * quantity
# #     print(summ)


# # cost_delivery(3, 3)
# # cost_delivery(2, 1, 2, 3, discount=0.5)

# 9 / 11


# def cost_delivery(quantity, *_, discount=0):
#     """Функція повертає суму за доставлення замовлення.

#     Перший параметр &mdash; кількість товарів в замовленні.
#     Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0.
#     """

#     result = (5 + 2 * (quantity - 1)) * (1 - discount)
#     return result


# print(cost_delivery.__doc__)

# 10 / 11


# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n - 1)


# def number_of_groups(n, k):
#     if k < 2:
#         return 1
#     else:
#         cn = factorial(n) / (factorial(n - k) * factorial(k))
#         print(cn)
#         return int(cn)

#     # 11 / 11


# def fibonacci(n):
#     if n < 0:
#         print("Incorrect input")
#     elif n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
