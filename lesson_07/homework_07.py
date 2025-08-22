# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while number * multiplier <= 25:
        result = number * multiplier

        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def plus (number1, number2):
    return number1 + number2
print(plus(3, 4))
# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(numbers):
    return sum(numbers) / len(numbers)

print(average([1, 2, 3, 4, 5]))
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse(string):
    return string[::-1]
print(reverse("hello"))
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def largest_word(words):
    return max(words, key=len)
print(largest_word(["hello", "world", "hi", "commit"]))
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
def find_all_str(string):
    result = []
    for i in string:
        if type(i) == str:
             result.append(i)
    return result
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

print(find_all_str(lst1))
# task 8

def unique_list(lst):

    return len(lst)  == len(set(lst))
print(unique_list([1, 2, 3, 4, 5]))
print(unique_list([1, 2, 3, 4, 4]))
# task 9
def even_sum(numbers):
    result = 0
    for num in numbers:
        if num % 2 == 0:
            result += num
    return result

lst = [1, 2, 3, 4]
print(even_sum(lst))
# task 10
def find_letter_in_word(word, letter):
    return word.find(letter)

print(find_letter_in_word("python", "y"))
print(find_letter_in_word("python", "f"))
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""