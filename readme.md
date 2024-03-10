**Результати пошуку через threading:**

Введіть шлях до директорії: C:\Users\User\Documents\test_texts \
Введіть ключові слова, розділені пробілом: товар https WindowsPath \
Результати для ключового слова 'товар':
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\19.04.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\2004.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\калькулятор доставок.txt 

Результати для ключового слова 'https':
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1304.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1404.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1504.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1804.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\19.04.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\2004.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\204.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\260422.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\27.04.22.txt

Результати для ключового слова 'WindowsPath':

Всі файли перевірені.

**Час виконання: 43.26460110000335**

**Результати пошуку** тих самих клчових слів в тій самій директорії, але **з використанням multiprocessing**:

Введіть шлях до директорії: C:\Users\User\Documents\test_texts \
Введіть ключові слова, розділені пробілом: товар https WindowsPath \
Результати для ключового слова 'товар':
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\19.04.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\2004.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\калькулятор доставок.txt

Результати для ключового слова 'https':
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1304.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1504.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\19.04.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\204.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1804.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1404.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\2004.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\27.04.22.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\260422.txt

Результати для ключового слова 'WindowsPath':

Всі файли перевірені.

**Час виконання: 13.446641099988483**

Як бачимо з часу виконання в цьому випадку на подібному пристрої (процесор AMD Ryzen 5 5500U) значно вигідніше 
використовувати multiprocessing, хоча з боку написання програм використовувати threading простіше.