# Dialog
Инструкция по запуску автоматизированного инструмента

1) Для начала нужно установить PyCharm IDE. Интегрированная среда разработки для языка программирования Python. https://www.jetbrains.com/ru-ru/pycharm/
2) Далее скачать установочный файл для Python3 https://www.python.org/downloads/windows/ (for Windows). Версия 3.9.
3) Зайти в PyCharm IDE и импортировать проект через GitHub. PyCharm имеет встроеную интеграцию. Клонировать репозиторий через https или ssh.
4) После импорта проекта выбрать интерпретатор для текущего проекта. Python 3.9. Зайти в "PyCharm" -> "Preferences" -> "project: dialog" -> "python interpreter".
5) Установить все необходимые библиотеки и плагины (включая фреймворк PyTest и WebDriver Selenium) из файла requirements.txt. Для этого выполнить в терминале (PyCharm) команду pip3 install requirements.txt
6) Запустить тесты через терминал (указал во втором скринкасте). Как пример: pytest tests/test_elements_url.py::test_social_url - # найти тест с именем test_social_url в указанном файле, в указанной директории и выполнить 
