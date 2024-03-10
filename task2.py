import logging
import timeit
from pathlib import Path
from multiprocessing import Process, Queue


def search_keywords_in_file(keywords_list, file_name, queue):
    results = {keyword: [] for keyword in keywords_list}
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for keyword in keywords_list:
                for line in lines:
                    if keyword in line:
                        results[keyword].append(file_name)
                        break
    except FileNotFoundError:
        print(f"Файл '{file_name}' не знайдено.")
    except PermissionError as pe:
        print(f"Відмовлено у доступі до файлу '{file_name}': {pe}")
    except Exception as e:
        print(f"Сталася помилка під час обробки файлу '{file_name}': {e}")
    queue.put(results)


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

    results_queue = Queue()

    format = "%(processName)s %(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    files = get_files(source)

    processes = []
    for file in files:
        process = Process(
            target=search_keywords_in_file, args=(keywords, file, results_queue)
        )
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    # Збір результатів з черги
    results = {keyword: [] for keyword in keywords}
    while not results_queue.empty():
        partial_results = results_queue.get()
        for keyword, file_paths in partial_results.items():
            results[keyword].extend(file_paths)

    # Виведення результатів пошуку
    for keyword, matches in results.items():
        print(f"Результати для ключового слова '{keyword}':")
        for match in matches:
            print(f"  Знайдено у файлі '{match}")

    print("Всі файли перевірені.")


if __name__ == "__main__":
    execution_time = timeit.timeit(main, number=1)
    print("Час виконання:", execution_time)
