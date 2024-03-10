Обидві програми запускались з наступними даними:
шлях до директорії: C:\Users\User\Documents\test_texts \
ключові слова (одне з яких ніде не зустрічається): товар https WindowsPath \

**Результати пошуку через threading:**

Результати для ключового слова 'товар':
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\19.04.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\2004.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\калькулятор доставок.txt

Результати для ключового слова 'https':
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1304.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1504.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1404.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1804.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\19.04.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\2004.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\204.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\27.04.22.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\260422.txt

Результати для ключового слова 'WindowsPath':

Всі файли перевірені.

**Час виконання: 23.80633280001348**

**Результати пошуку** тих самих клчових слів в тій самій директорії, але **з використанням multiprocessing**:

Результати для ключового слова 'товар':
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\19.04.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\2004.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\калькулятор доставок.txt

Результати для ключового слова 'https':
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1304.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1504.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1404.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\19.04.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\260422.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\2004.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1804.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\204.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\27.04.22.txt

Результати для ключового слова 'WindowsPath':

Всі файли перевірені.

**Час виконання: 19.543054100009613**

Як бачимо з часу виконання в цьому випадку на подібному пристрої (процесор AMD Ryzen 5 5500U) вигідніше 
використовувати multiprocessing, хоча з боку написання програм використовувати threading простіше.
