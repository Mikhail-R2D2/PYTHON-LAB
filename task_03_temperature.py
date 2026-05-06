# Задача 3: Конвертер температур

# Ввод температуры
celsius = float(input("Введите температуру в °C: "))

# Перевод в Фаренгейты
fahrenheit = celsius * 9 / 5 + 32

# Определение состояния воды
if celsius <= 0:
    state = "Лёд"
elif celsius < 100:
    state = "Жидкость"
else:
    state = "Пар"

# Вывод
print("\n=== КОНВЕРТЕР ТЕМПЕРАТУР ===")
print("Температура:", celsius, "°C")
print("В Фаренгейтах:", round(fahrenheit, 2), "°F")
print("Состояние воды:", state)
