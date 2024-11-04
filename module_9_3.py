first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка 1 (с использованием zip)
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

# Генераторная сборка 2 (без использования zip)
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Вывод результатов
print(list(first_result))
print(list(second_result))
