# pytest_ui_api_template

## Шаблон для автоматизации тестирования на Python

### Шаги:
1. Склонировать проект `git.clone https://github.com/Andrey-Andriyas/pytest_ui_api_template.git`
2. Установить все зависимости
3. Запустить тесты `pytest`
4. Сгенерировать отчет  `allure generate allure-files -o allure-report`
5. Открыть отчет `allure open allure-report`

### Стек:
- pytest
- selenium
- requests
- _sqlalchemy_
- allure
- config

### Структура:
- ./test_1 - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./db - хелперы для работы с БД



### Полезные ссылки
- [Подсказка по Markdown](https://markdownguide.org/cheat-sheet/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore/)



### Библиотеки (!)
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
