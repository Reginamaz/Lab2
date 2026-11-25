from PIL import Image, ImageFilter, ImageOps
from datetime import datetime
import os

INPUT_DIR = os.path.join("Lab2_Media", "data", "input")
OUTPUT_DIR = os.path.join("Lab2_Media", "data", "output")
LOG_FILE = os.path.join("Lab2_Media", "logs", "history.txt")


def write_log(filename, filter_name, status):
    try:
        with open(LOG_FILE, "a", encoding="UTF-8") as log:
            date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            log.write(
                f"[{date}] Файл: {filename} | "
                f"Фильтр: {filter_name} | Статус: {status}\n"
            )
    except OSError:
        print("Ошибка записи в журнал.")


def process_image(filename):
    filter_name = "Unsharp Masking + Автоконтраст"
    file_path = os.path.join(INPUT_DIR, filename)

    try:
        with Image.open(file_path) as img:
            img.load()
            image = img.convert("RGB")
            
        sharp_image = image.filter(
            ImageFilter.UnsharpMask(
                radius=2,
                percent=150,
                threshold=3
            )
        )

        result = ImageOps.autocontrast(sharp_image)
        
        output_path = os.path.join(OUTPUT_DIR, "result.jpg")
        result.save(output_path, "JPEG")

        print("Обработка изображения выполнена успешно!")
        print(f"Результат сохранен: {output_path}")

        write_log(filename, filter_name, "Успешно")

    except PermissionError:
        if filename == "image2.png":
            print("Ошибка: Нет прав на чтение файла image2.png. ")
            print("Обратитесь к администратору")
        else:
            print("Ошибка: Нет прав на чтение файла.")

        write_log(filename, filter_name, "Ошибка доступа")

    except FileNotFoundError:
        print("Ошибка: Файл не найден")
        write_log(filename, filter_name, "Ошибка: Файл не найден")

    except OSError as error:
        print(f"Ошибка при обработке изображения: {error}")
        write_log(filename, filter_name, "Ошибка обработки")

print("=== Лабораторная работа №2 ===")
print("Вариант 73")
print("Задание №1: Unsharp Masking")
print("Задание №2: Автоконтраст")

filename = input("Введите имя файла (image1.jpg или image2.png): ")

process_image(filename)
