""" Скрипт для обработки серверных логов"""
#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


from collections import Counter
import string
import itertools
import json
import re
import logging
import argparse
import os


access_log = "logs/apache_access_log.log"
parser_log_output = "logs/parser_log_output.json"


def get_logfile_path():

    path = None

    while path is None:
        path_from_input = input("Введите наименование файла или путь (или нажмте Enter для выбора файла по умолчанию): ")

        if path_from_input == '':
            path = access_log
            return path

        if path_from_input.endswith('.log'):
            return path
        else:
            files_list = os.listdir(path_from_input)
            for file in files_list:
                if file.endswith('.log'):
                    path = path_from_input + "/" + file
                    print(path)
                    return path
                else:
                    path = None


def collect_request_types(filepath):
    with open(filepath) as log_file:
        request_list = ("GET", "POST", "OPTIONS", "HEAD", "PUT", "PATCH", "DELETE", "TRACE", "CONNECT")
        log = log_file.read()
        log_request_list = list()
        for request in request_list:
            for each_log in re.findall(request, log):
                log_request_list.append(each_log)
        print(log_request_list)
        return log_request_list


def collect_ips(filepath, quantity=10):
    with open(filepath) as log_file:
        log = log_file.read()
        ips_list = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', log)

    print(Counter(ips_list).most_common(quantity))
    return Counter(ips_list).most_common(quantity)


def collect_longest_requests(filepath, quantity=10):
    with open(filepath) as log_file:
        log_parts_list = list()
        request_duration_dict = dict()
        longest_requests_dict = dict()
        for line in log_file:
            log_parts_list.append(line.split(' '))
        for part in log_parts_list:
            request_duration_dict[part[9]] = part[0:8]
        for request_duration in itertools.islice(sorted(request_duration_dict, reverse=True), quantity):
            longest_requests_dict[request_duration] = request_duration_dict[request_duration]

        print(longest_requests_dict)
        return longest_requests_dict


def collect_client_errors(filepath):
    with open(filepath) as log_file:
        log_parts_list = list()
        client_error_list = list()
        for line in log_file:
            log_parts_list.append(line.split(' '))
        for part in log_parts_list:

            if part[8][0] == '4':
                client_error_list.append(part)

    print(client_error_list)
    return client_error_list


def collect_server_errors(filepath):
    with open(filepath) as log_file:
        log_parts_list = list()
        server_error_list = list()
        for line in log_file:
            log_parts_list.append(line.split(' '))
        for part in log_parts_list:
            if part[8][0] == '5':
                server_error_list.append(part)
                print(part[8])

    print(server_error_list)
    return server_error_list


def count(item):
    count_list = Counter(item)
    return count_list


def parse_logfile(filepath):
    try:
        req = "{}:{}".format("Requests number", count(collect_request_types(filepath)))
        ip = "{}:{}".format("Top 10 ips", collect_ips(filepath))
        dur_req = "{}:{}".format("Top 10 longest requests", collect_longest_requests(filepath))
        client_err = "{}:{}".format("Top 10client errors", collect_client_errors(filepath))
        server_err = "{}:{}".format("Top 10 server errors", collect_server_errors(filepath))
        with open(parser_log_output, 'w') as output:
            json.dump((request_number, ip, req, dur_req, client_err, server_err), output, indent=4)
    except(FileNotFoundError, FileExistsError):
        logging.error("Can't read file : {}!".format(filepath))


logfile = get_logfile_path()
parse_logfile(log)
