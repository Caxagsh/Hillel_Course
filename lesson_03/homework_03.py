
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')

single_quotes = [char for char  in alice_in_wonderland if char == "'" ]
print(single_quotes)

print(alice_in_wonderland)

#     # Задачі 04 -10:
#     # Переведіть задачі з книги "Математика, 5 клас"
#     # на мову пітон і виведіть відповідь, так, щоб було
#     # зрозуміло дитині, що навчається в п'ятому класі
# """
# # task 04
# """
# Площа Чорного моря становить 436 402 км2, а площа Азовського
# моря становить 37 800 км2. Яку площу займають Чорне та Азов-
# ське моря разом?
# """
print("##############################################")
black_sea_square = "436 402 км2"
azov_sea_square = "37 800 км2"
result = int(black_sea_square[0:7].replace(" ", "")) + int(azov_sea_square[0:6].replace(" ", ""))
print(result)
result_to_str = str(result)
result_formated  = result_to_str[:3] + " " + result_to_str[3:] + " км2"

print(result_formated)
#
# # task 05
# """
# Мережа супермаркетів має 3 склади, де всього розміщено
# 375 291 товар. На першому та другому складах перебуває
# 250 449 товарів. На другому та третьому – 222 950 товарів.
# Знайдіть кількість товарів, що розміщені на кожному складі.
# """
#
all_warehouse = "375 291"
first_and_second_warehouse = "250 449"
second_and_third_warehouse = "222 950"
all_warehouse_to_int = int(all_warehouse.replace(" ", ""))
first_and_second_warehouse_to_int = int(first_and_second_warehouse.replace(" ", ""))
second_and_third_warehouse_to_int = int(second_and_third_warehouse.replace(" ", ""))
first_warehouse = all_warehouse_to_int - second_and_third_warehouse_to_int
second_warehouse = all_warehouse_to_int - first_warehouse - first_warehouse
third_warehouse = all_warehouse_to_int - first_and_second_warehouse_to_int
first_warehouse_to_str = str(first_warehouse) + "товар"
second_warehouse_to_str = str(second_and_third_warehouse) + "товар"
third_warehouse_to_str = str(third_warehouse) + "товар"

# # task 06
# """
# Михайло разом з батьками вирішили купити комп’ютер, ско-
# риставшись послугою «Оплата частинами». Відомо, що сплачу-
# вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
# вартість комп’ютера.
# """

one_month_payment = "1179 грн/місяць"
one_month_payment_to_int = int(one_month_payment.replace(" грн/місяць", ""))
all_time_payment = one_month_payment_to_int * 18
all_time_payment_to_str = str(all_time_payment) + "<грн>"
#
# # task 07
# """
# Знайди остачу від діленя чисел:
# a) 8019 : 8     d) 7248 : 6
# b) 9907 : 9     e) 7128 : 5
# c) 2789 : 5     f) 19224 : 9
# """
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
#
# # task 08
# """
# Іринка, готуючись до свого дня народження, склала список того,
# що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
# для даного її замовлення.
# Назва товару    Кількість   Ціна
# Піца велика     4           274 грн
# Піца середня    2           218 грн
# Сік             4           35 грн
# Торт            1           350 грн
# Вода            3           21 грн
# """
#
pizza_xl = 4 * 274
pizza_l = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 + 21
pizza_xl_to_str = str(pizza_xl) + "грн"
pizza_l_to_str = str(pizza_l) + "грн"
juice_to_str = str(juice) + "грн"
cake_to_str = str(cake) + "грн"
water_to_str = str(water) + "грн"
# # task 09
# """
# Ігор займається фотографією. Він вирішив зібрати всі свої 232
# фотографії та вклеїти в альбом. На одній сторінці може бути
# розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
# Ігорю, щоб вклеїти всі фото?
# """
pages_num = 232 / 8

#
# # task 10
# """
# Родина зібралася в автомобільну подорож із Харкова в Буда-
# пешт. Відстань між цими містами становить 1600 км. Відомо,
# що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
# становить 48 літрів.
# 1) Скільки літрів бензину знадобиться для такої подорожі?
# 2) Скільки щонайменше разів родині необхідно заїхати на зап-
# равку під час цієї подорожі, кожного разу заправляючи пов-
# ний бак?
# """

distans_in_liter = 1600 / 100 * 9
number_of_gas_stations = distans_in_liter / 48
