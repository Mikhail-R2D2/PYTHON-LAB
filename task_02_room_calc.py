# Задача 2: Параметры помещения

# Размеры комнаты (в метрах)
length = 5.25
width = 5.20
height = 3.20

# Расчёты
floor_sq = length * width  # определение площади пола
wall_sq = 2 * (length + width) * height  # определение площадь стен
volume = length * width * height  # объём

# Стоимость покраски (125 руб за м²)
paint_price_per_m2 = 125
paint_cost = wall_sq * paint_price_per_m2

# Округление
floor_area = round(floor_sq, 2)
wall_area = round(wall_sq, 2)
volume = round(volume, 2)
paint_cost = round(paint_cost, 2)

# Вывод
print("=== ПАРАМЕТРЫ ПОМЕЩЕНИЯ ===")
print("Длина:", length, "м")
print("Ширина:", width, "м")
print("Высота:", height, "м")
print()
print("Площадь пола:", floor_sq, "м²")
print("Площадь стен:", wall_sq, "м²")
print("Объём:", volume, "м³")
print("Стоимость покраски:", paint_cost, "руб")
print("Расчёт завершён")

print("*Стоимость покраски рассчитана из расчета 125 руб/м²")

