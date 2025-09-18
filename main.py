import random

# Вывести на экран таблицу умножения от 1 до 9 с помощью вложенных циклов
print('Таблица умножения')
print(140 * '-')
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{j} x {i} = {i*j:2}', end='\t')
    print()

# Посчитать сумму всех нечётных чисел от 1 до 100
result = 0
for i in range(1, 100, 2):
    result += i

print(f'Сумма всех нечётных чисел от 1 до 100: {result}')

# Запросить у пользователя число n и вывести все его делители
num = int(input('Введите целое число: '))
divisors = []
for i in range(1, num + 1):
    if num % i == 0:
        divisors.append(str(i))

print(f'Делители числа {num}:')
print(", ".join(divisors))

# Найти факториал числа, введённого пользователем, с помощью цикла
n = int(input('Введите число для нахождения факториала: '))
if n < 0:
    print('Некорректное значение!')
else:
    result = 1
    for i in range(1, n + 1):
        result *= i

    print(f'{n}! =', result)

# Сгенерировать последовательность Фибоначчи длиной n и вывести её
n = int(input("Введите длину последовательности: "))
fibonacci = [0, 1]

for i in range(2, n):
    next_number = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(next_number)

print(f"Последовательность Фибоначчи ({n} чисел):")
print(fibonacci[:n])  # на случай если n=0 или n=1

# Создать список из 10 чисел и вывести только чётные элементы
numbers = [random.randint(-50, 50) for _ in range(10)]
print(numbers)
even_numbers = [str(x) for x in numbers if x % 2 == 0]
print('Четные элементы списка:', ', '.join(even_numbers))

# Найти максимальное и минимальное число в списке
print(numbers)
print(f'max число в списке:{max(numbers)}')
print(f'min число в списке:{min(numbers)}')

# Запросить у пользователя 5 чисел, сохранить в список, отсортировать его и вывести
list_num = []
for i in range(1, 6):
    number = int(input(f'Введите {i} число: '))
    list_num.append(number)

list_num.sort()
print(list_num)

# Удалить из списка все дубликаты (без использования множеств)
print(numbers)
unique_list = []
for item in numbers:
    if item not in unique_list:
        unique_list.append(item)

print("Список без дубликатов:", unique_list)

# Поменять местами первый и последний элемент списка
print(numbers)
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print("Список после замены первого и последнего элемента:", numbers)

# Создать словарь с именами студентов и их оценками, вывести средний балл
students = {
    "Иван": 5,
    "Мария": 4,
    "Петр": 3,
    "Анна": 5,
    "Дмитрий": 4
}
print(students)
average_score = sum(students.values()) / len(students)
print("Средний балл:", average_score)

# Подсчитать количество каждой буквы в строке (словарь: буква → количество)
text = input("Введите строку: ")
letter_count = {}

for letter in text:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

print("Количество каждой буквы:", letter_count)

# Создать словарь, где ключи – это числа от 1 до 10, а значения – их квадраты
squares = {i: i**2 for i in range(1, 11)}
print("Словарь чисел и их квадратов:", squares)

# Составить словарь из двух списков: список ключей и список значений
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
dictionary = dict(zip(keys, values))
print(dictionary)

# Создать два множества и вывести их пересечение и объединение
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

intersection = set1 & set2  # пересечение
union = set1 | set2         # объединение

print("Пересечение:", intersection)
print("Объединение:", union)

# Найти все уникальные слова в тексте, введённом пользователем
text = input("Введите текст: ")
words = text.split()
unique_words = set(words)

print("Уникальные слова:", unique_words)

# Даны два списка. Найти общие элементы с помощью множеств
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

set1 = set(list1)
set2 = set(list2)

common_elements = set1 & set2
print("Общие элементы:", common_elements)

# Проверить, является ли одно множество подмножеством другого
setA = {1, 2}
setB = {1, 2, 3, 4}

is_subset = setA.issubset(setB)
print(f"Является ли множество A {setA} подмножеством множества B {setB}?", is_subset)

# Удалить из множества все элементы, которые меньше заданного числа
s = {1, 3, 5, 7, 9}
threshold = 50
print(s)

s = {x for x in s if x >= threshold}
print("Множество после удаления элементов меньше", threshold, ":", s)

# Сгенерировать список из 20 случайных чисел и вывести только уникальные значения
print(numbers)
unique_numbers = set(numbers)
print("Уникальные числа:", unique_numbers)

# Создать словарь, где ключи – это элементы списка, а значения – количество их повторений
lst = [1, 2, 2, 3, 3, 3, 4, 5, 5]

count_dict = {}
for item in lst:
    count_dict[item] = count_dict.get(item, 0) + 1

print(count_dict)

# Дан список слов. Создать множество из слов, длина которых больше 5 символов
words = ["яблоко", "слива", "орех", "банан", "ананас", "черешня"]
print(words)
long_words = {word for word in words if len(word) > 5}
print(long_words)

# Ввести предложение. Сохранить в словарь количество вхождений каждого слова
sentence = input("Введите предложение: ")
words = sentence.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

# Создать список чисел, преобразовать его в множество и обратно в список (убрав дубликаты)
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)

#  Дан словарь "товар – цена". Найти самый дорогой товар
products = {"яблоко": 50, "банан": 30, "виноград": 70, "персик": 70, "апельсин": 40}
max_price = max(products.values())
most_expensive = [item for item, price in products.items() if price == max_price]

print("Самые дорогие товары:", most_expensive)
print("Цена:", max_price)

# Дан список имён. Определить, какие из имён встречаются более одного раза. Какое имя встречается чаще всего
names = ["Анна", "Петр", "Анна", "Иван", "Петр", "Петр", "Мария"]

# Найти имена, которые встречаются более одного раза
duplicates = {name for name in names if names.count(name) > 1}

# Найти имя, которое встречается чаще всего
most_common = max(names, key=names.count)

print("Имена, встречающиеся более одного раза:", duplicates)
print("Чаще всего встречается имя:", most_common)

# Запросить у пользователя строку и составить словарь: символ → индекс его первого вхождения
text = input("Введите строку: ")
char_index = {}

for index, char in enumerate(text):
    if char not in char_index:
        char_index[char] = index

print(char_index)
