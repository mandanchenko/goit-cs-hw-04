import logging
import timeit
from pathlib import Path
from threading import Thread


def search_keywords_in_file(keywords_list, file_name, results):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for keyword in keywords_list:
                for line in lines:
                    if keyword in line:
                        results[keyword].append(file_name)
                        break
    except FileNotFoundError:
        logging.error(f"Файл '{file_name}' не знайдено.")
    except PermissionError as pe:
        logging.error(f"Відмовлено у доступі до файлу '{file_name}': {pe}")
    except Exception as e:
        logging.error(f"Сталася помилка під час обробки файлу '{file_name}': {e}")
    return results


def get_files(path: Path):
    input_files = []
    for item in path.iterdir():
        if item.is_file():
            input_files.append(item)
        elif item.is_dir():
            input_files.extend(get_files(item))
    return input_files


def main():
    source = Path(input("Введіть шлях до директорії: "))
    keywords_input = input("Введіть ключові слова, розділені пробілом: ")
    keywords = keywords_input.split()

    results = {keyword: [] for keyword in keywords}

    format = "%(threadName)s %(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    try:
        files = get_files(source)
    except FileNotFoundError as e:
        logging.error(f"Директорія '{source}' не знайдена: {e}")
        return

    threads = []
    for file in files:
        thread = Thread(target=search_keywords_in_file, args=(keywords, file, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Виведення результатів пошуку
    for keyword, matches in results.items():
        print(f"Результати для ключового слова '{keyword}':")
        for match in matches:
            print(f"  Знайдено у файлі '{match}")

    print("Всі файли перевірені.")


if __name__ == "__main__":
    execution_time = timeit.timeit(main, number=1)

    print("Час виконання:", execution_time)
