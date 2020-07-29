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

Запуск тестов через Selenium Grid на основной машине:
- Настройка сети виртуалки - NAT
- Убедиться, что в тестах верный url - http://localhost:8080/opencart/
- В терминале основной машины выполняем команду:
java -jar selenium selenium-server-standalone-3.141.59.jar
- В терминале PyCharm выполняем команду:
pytest --browser_name=remote --remote_browser=chrome --remote_executor=ip_основной_машины 
test_opencart.py

Запуск тестов через Selenium Grid на виртуальной машине:
- Меняем настройки сети виртуальной машины на Bridge Adapter!!!
- Сохранить > Перезагрузить виртуальную машину
- Убедиться, что в тестах верный url - http://localhost/opencart/

- В терминале основной машины выполняем команду:
java -jar selenium selenium-server-standalone-3.141.59.jar -role hub

- В терминале виртуальной машины выполняем команду:
java -jar selenium selenium-server-standalone-3.141.59.jar -role node

- В терминале PyCharm выполняем команду:
pytest --browser_name=remote --remote_browser=chrome --remote_executor=ip_основной_машины 
test_opencart.py

Запуск тестов с Selenoid:
- Настройка сети виртуалки - NAT
- Убедиться, что в тестах верный url - http://10.0.2.15/opencart/
- В терминале PyCharm выполняем команду:
pytest --browser_name=remote_selenoid --executor=localhost test_admin_page.py

Браузер меняем в конфигах conftest фикстуры browser.

**Парсинг логов:**

Запускаем скрипт server_log_parser.py
Вводим путь до файла с логами.

*Работа методов:*
```get_logfile_path``` -  обрабатывает значение, передаваемой в input терминала
```collect_request_types``` - выводит список типов запросов, которые есть в логе
```collect_ips``` - выводит список ip-адресов, с которых поступали запросы
```collect_longest_requests``` - выводит список самых долгих запросов
```collect_client_errors``` - выводит список клиентских ошибок
```collect_server_errors``` - выводит список серверных ошибок
```count``` - подсчитывает количество уникальных значений

```parse_logfile``` парсит файл с логами и выводит информацию в json файл:
- количество запросов по типу (GET - 20, POST - 10 etc);
- топ 10 IP-адресов, с которых были сделаны запросы;
- топ 10 самых долгих запросов;
- топ 10 запросов, которые завершились клиентской ошибкой;
- топ 10 запросов, которые завершились ошибкой со стороны сервера.
