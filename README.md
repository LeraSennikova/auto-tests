# auto-tests
Тест написан с использованием библиотеки Playwright  и фреймворка Pytest 

Рекомендуется запускать тест в PyCharm или аналогичной IDE.
Необходимые пакеты для успешного запуска теста: playwright, pytest, pytest-playwright

Для запуска в консоли набрать "pytest" со следующими параметрами
Обязательный параметр: --browser-channel=chrome
Необязательные параметры: --headed --slowmo 1000

Удобный для восприятия вариант запуска: pytest --browser-channel=chrome --headed --slowmo 1000
