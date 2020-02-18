# Otus-Python-QA-Selenium-Browsers
Репозиторий с ДЗ к уроку "Основы  Selenium"

Как запустить тесты в разных браузерах:

Chrome:
pytest -v --browser_name=chrome tests/test_opencart.py

FireFox:
pytest -v --browser_name=firefox tests/test_opencart.py

Safari:
pytest -v --browser_name=safari tests/test_opencart.py

Safari  не поддерживает режим запуска "headless"
