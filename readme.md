**Результати пошуку через threading:**
[WindowsPath('C:/Users/User/Documents/test_texts/1304.txt'), WindowsPath('C:/Users/User/Documents/test_texts/1404.txt'), 
WindowsPath('C:/Users/User/Documents/test_texts/1504.txt'), WindowsPath('C:/Users/User/Documents/test_texts/1804.txt'), 
WindowsPath('C:/Users/User/Documents/test_texts/19.04.txt'), WindowsPath('C:/Users/User/Documents/test_texts/2004.txt'),
WindowsPath('C:/Users/User/Documents/test_texts/204.txt'), WindowsPath('C:/Users/User/Documents/test_texts/260422.txt'),
WindowsPath('C:/Users/User/Documents/test_texts/27.04.22.txt'), 
WindowsPath('C:/Users/User/Documents/test_texts/калькулятор доставок.txt')]\
Результати для ключового слова 'товар':
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\19.04.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\2004.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\калькулятор доставок.txt\
Результати для ключового слова 'https':
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1304.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1404.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1504.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1804.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\19.04.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\2004.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\204.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\260422.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\27.04.22.txt\
Результати для ключового слова 'WindowsPath':\
Всі файли перевірені.

**Час виконання: 34.19366290001199**

**Результати пошуку** тих самих клчових слів в тій самій директорії, але **з використанням multiprocessing**:
[WindowsPath('C:/Users/User/Documents/test_texts/1304.txt'), WindowsPath('C:/Users/User/Documents/test_texts/1404.txt'),
WindowsPath('C:/Users/User/Documents/test_texts/1504.txt'), WindowsPath('C:/Users/User/Documents/test_texts/1804.txt'), 
WindowsPath('C:/Users/User/Documents/test_texts/19.04.txt'), WindowsPath('C:/Users/User/Documents/test_texts/2004.txt'),
WindowsPath('C:/Users/User/Documents/test_texts/204.txt'), WindowsPath('C:/Users/User/Documents/test_texts/260422.txt'),
WindowsPath('C:/Users/User/Documents/test_texts/27.04.22.txt'), 
WindowsPath('C:/Users/User/Documents/test_texts/калькулятор доставок.txt')]\
Результати для ключового слова 'товар':
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\19.04.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\2004.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\калькулятор доставок.txt\
Результати для ключового слова 'https':
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1304.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1404.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1804.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\1504.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\19.04.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\260422.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\204.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\2004.txt
  Знайдено у файлі 'C:\Users\User\Documents\test_texts\27.04.22.txt\
Результати для ключового слова 'WindowsPath':\
Всі файли перевірені.

**Час виконання: 11.066845400026068**

Як бачимо з часу виконання в цьому випадку на подібному пристрої (процесор AMD Ryzen 5 5500U) значно вигідніше 
використовувати multiprocessing, хоча з боку написання програм використовувати threading простіше.