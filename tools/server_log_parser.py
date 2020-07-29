""" Скрипт для обработки серверных логов"""
#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


from collections import Counter
import itertools
import json
import re
import logging
import os


ACCESS_LOG = "logs/apache_access_log.log"
PARSER_LOG_OUTPUT = "logs/parser_log_output.json"


def get_logfile_path():
    """ Метод обрабатывает значение, передаваемое в input терминала """

    path = None

    while path is None:
        path_from_input = input("Введите наименование файла или путь "
                                "(или нажмте Enter для выбора файла по умолчанию): ")

        if path_from_input == '':
            path = ACCESS_LOG
            return path

        if path_from_input.endswith('.log'):
            return path
        else:
            files_list = os.listdir(path_from_input)
            for file in files_list:
                if file.endswith('.log'):
                    path = path_from_input + "/" + file
                    return path
                else:
                    path = None


def collect_request_types(filepath):
    """ Метод выводит список типов запросов, которые есть в логе """

    with open(filepath) as log_file:
        request_list = ("GET", "POST", "OPTIONS", "HEAD", "PUT",
                        "PATCH", "DELETE", "TRACE", "CONNECT")
        log = log_file.read()
        log_request_list = list()
        for request in request_list:
            for each_log in re.findall(request, log):
                log_request_list.append(each_log)

        return log_request_list


def collect_ips(filepath, quantity=10):
    """ Метод выводит список ip-адресов, с которых поступали запросы """

    with open(filepath) as log_file:
        log = log_file.read()
        ips_list = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', log)

    return Counter(ips_list).most_common(quantity)


def collect_longest_requests(filepath, quantity=10):
    """ Метод выводит список самых долгих запросов """

    with open(filepath) as log_file:
        log_parts_list = list()
        request_duration_dict = dict()
        longest_requests_dict = dict()
        for line in log_file:
            log_parts_list.append(line.split(' '))
        for part in log_parts_list:
            request_duration_dict[part[9]] = part[0:8]
        for request_duration in itertools.islice(sorted(request_duration_dict,
                                                        reverse=True), quantity):
            longest_requests_dict[request_duration] = request_duration_dict[request_duration]

        return longest_requests_dict


def collect_client_errors(filepath):
    """ Метод выводит список клиентских ошибок """

    with open(filepath) as log_file:
        log_parts_list = list()
        client_error_list = list()
        for line in log_file:
            log_parts_list.append(line.split(' '))
        for part in log_parts_list:

            if part[8][0] == '4':
                client_error_list.append(part)

    return client_error_list


def collect_server_errors(filepath):
    """ Метод выводит список серверных ошибок """

    with open(filepath) as log_file:
        log_parts_list = list()
        server_error_list = list()
        for line in log_file:
            log_parts_list.append(line.split(' '))
        for part in log_parts_list:
            if part[8][0] == '5':
                server_error_list.append(part)

    return server_error_list


def count(item):
    """ Метод подсчитывает количество уникальных значений """

    count_list = Counter(item)
    return count_list


def parse_logfile(filepath):
    """ Метод парсит файл с логами и выводит информацию в json файл """

    try:
        req = "{}:{}".format("Requests number", count(collect_request_types(filepath)))
        ips = "{}:{}".format("Top 10 ips", collect_ips(filepath))
        dur_req = "{}:{}".format("Top 10 longest requests", collect_longest_requests(filepath))
        client_err = "{}:{}".format("Top 10client errors", collect_client_errors(filepath))
        server_err = "{}:{}".format("Top 10 server errors", collect_server_errors(filepath))
        with open(PARSER_LOG_OUTPUT, 'w') as output:
            json.dump((ips, req, dur_req, client_err, server_err), output, indent=4)
            print("File has been parsed: {}!".format(filepath))
    except(FileNotFoundError, FileExistsError):
        logging.error("Can't read file : {}!".format(filepath))


logfile = get_logfile_path()
parse_logfile(logfile)
