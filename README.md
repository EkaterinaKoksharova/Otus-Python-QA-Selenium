# Otus-Python-QA-Selenium-Browsers
Репозиторий с ДЗ к уроку "Основы  Selenium"

Как запустить тесты в разных браузерах:

Chrome:
pytest -v --browser_name=chrome tests

FireFox:
pytest -v --browser_name=firefox tests

Safari:
pytest -v --browser_name=safari tests

Safari  не поддерживает режим запуска "headless"

Настройка скрытого ожидания браузера:
pytest -v --implicilty_wait=10, где 10 - количество секунд

Настройка ожидания элемента:
pytest -v --wait=10, где 10 - количество секунд

Настройки логгирования:
pytest -v --log_file=logs/filename.log, где "filename" - наименование файла, куда запишутся логи
pytest -v ---log_level=INFO, где "INFO" - тип логов, которые будут собраны
