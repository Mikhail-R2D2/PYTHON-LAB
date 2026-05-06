# Задача 7: Прайс-лист материалов

# Создание словаря
materials = {
    "Бетон": 100,
    "Сталь": 500,
    "Дерево": 50,
    "Кирпич": 300,
    "Пултрузионный композит": 250
}

# Вывод
print("Исходный список материалов:")
for name, price in materials.items():
    print(name, "-", price, "руб")

    # Добавление новых материалов
materials["Минеральная вата"] = 50
materials["Керамзит"] = 20

# Изменение цены (+10%)
materials["Сталь"] = materials["Сталь"] * 1.1

print("\nПосле изменений:")
for name, price in materials.items():
    print(name, "-", price, "руб")

    # Удаление одного материала
materials.pop("Пултрузионный композит")

# Расчет средней цены
average_price = sum(materials.values()) / len(materials)

print("\nПосле удаления:")
for name, price in materials.items():
    print(name, "-", price, "руб")

print("\nСредняя цена:", average_price, "руб")

print("\nОтсортировано по цене:")
for name, price in sorted(materials.items(), key=lambda x: x[1]):
    print(name, "-", price, "руб")
