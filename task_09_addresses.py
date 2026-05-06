# Задача 9: Очистка адресов

addresses = [
    " г.Моксва, ул.Ленина, д. 10 ",
    "г.Казань,ул.Баумана,д.15",
    "  г.Санкт-Петербург, ул. Невский, д. 10  "
]

# Вывод исходных данных
print("Исходные адреса:")
for addr in addresses:
    print(addr)

    cleaned_addresses = []

for addr in addresses:
    # Убираем пробелы по краям
    addr = addr.strip()

    # Добавляем пробелы после запятых
    addr = addr.replace(",", ", ")

    # Убираем двойные пробелы
    addr = addr.replace("  ", " ")

    cleaned_addresses.append(addr)

print("\nОчищенные адреса:")
for addr in cleaned_addresses:
    print(addr)

    normalized_addresses = []

for addr in cleaned_addresses:
    addr = addr.replace("г.", "г. ")
    addr = addr.replace("г ", "г. ")
    normalized_addresses.append(addr)

normalized_addresses = []

for addr in cleaned_addresses:
    # Нормализация "г."
    addr = addr.replace("г.", "г. ")
    addr = addr.replace("г ", "г. ")

    # Нормализация улиц и проспектов
    addr = addr.replace("ул.", "ул. ")
    addr = addr.replace("пр.", "пр. ")
    addr = addr.replace("д.", "д. ")

    # Убираем двойные пробелы (несколько раз для надежности)
    while "  " in addr:
        addr = addr.replace("  ", " ")

    normalized_addresses.append(addr)

print("\nНормализованные адреса:")
for addr in normalized_addresses:
    print(addr)
