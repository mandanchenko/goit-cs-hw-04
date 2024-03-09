import logging
from pathlib import Path
from threading import Thread


def search_keywords_in_file(keywords_list, file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line_number, line in enumerate(lines, 1):
                for keyword in keywords_list:
                    if keyword in line:
                        print(
                            f"Знайдено '{keyword}' у файлі '{file_name}' на рядку {line_number}"
                        )

    except FileNotFoundError:
        print(f"Файл '{file_name}' не знайдено.")
    except PermissionError as pe:
        print(f"Відмовлено у доступі до файлу '{file_name}': {pe}")
    except Exception as e:
        print(f"Сталася помилка під час обробки файлу '{file_name}': {e}")


def get_files(path: Path):
    input_files = []
    for item in path.iterdir():
        if item.is_file():
            input_files.append(item)
        elif item.is_dir():
            input_files.extend(get_files(item))
    return input_files


if __name__ == "__main__":
    source = Path(input("Введіть шлях до директорії: "))
    keywords_input = input("Введіть ключові слова, розділені пробілом: ")
    keywords = keywords_input.split()

    format = "%(threadName)s %(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    files = get_files(source)
    print(files)

    threads = []
    for file in files:
        thread = Thread(target=search_keywords_in_file, args=(keywords, file))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Всі файли перевірені.")
