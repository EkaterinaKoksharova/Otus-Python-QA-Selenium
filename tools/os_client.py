import os
import sys
import subprocess
from subprocess import Popen, PIPE
import argparse
import json


def get_args():
    """Arguments parser"""
    args = argparse.ArgumentParser()

    args.add_argument('--package', type=str, default='selenium',
                      help='Package name to show version')
    args.add_argument('--directory', type=str,  default='/Users/',
                      help='Directory to show files it contains')
    args.add_argument('--port', type=str, default='22',
                      help='Port number to show it\'s type')
    args.add_argument('--service', type=str, default='network',
                      help='Show service status')
    return args.parse_args()


def get_os_info():
    args = get_args()
    # Cетевые интерфейсы:
    network_interfaces_responce = subprocess.Popen("netstat -i", shell=True, stdout=PIPE).stdout
    network_interfaces = str(network_interfaces_responce.readlines())
    # Маршрут по-умолчанию:
    default_path = os.getenv('PATH')
    # Информацию о состоянии процессора:
    cpu_info_responce = subprocess.Popen("sysctl -n machdep.cpu.brand_string", shell=True, stdout=PIPE).stdout
    cpu_info = str(cpu_info_responce.readlines())
    # Информацию о процессе:
    process_id = os.getpid()
    # Список всех процессов:
    all_processes_responce = subprocess.Popen("ps aux", shell=True, stdout=PIPE).stdout
    all_processes = str(all_processes_responce.readlines())
    # Статистику работы сетевых интерфейсов:
    interfaces_stat_responce = subprocess.Popen("ifconfig", shell=True, stdout=subprocess.PIPE).stdout
    interfaces_stat = str(interfaces_stat_responce.readlines())
    # Статус работы какого либо сервиса:
    service_status_responce = subprocess.Popen(f'launchctl list | grep {args.service}', shell=True, stdout=PIPE).stdout
    service_status = str(service_status_responce.readlines())
    # Состояние сетевого порта на сервере(TCP или UDP):
    port_type_responce = subprocess.Popen(f'nmap localhost | grep {args.port}', shell=True, stdout=PIPE).stdout
    port_type = str(port_type_responce.readlines())
    # Версию пакета(имя пакета передается как аргумент):
    package_version_responce = subprocess.Popen(f'pip3 freeze | grep {args.package}', shell=True, stdout=PIPE).stdout
    package_version = str(package_version_responce.readlines())
    # Список в файлов в директории (указать директорию):
    files_list = str(os.listdir(args.directory))
    # Текущая директорию:
    current_directory = os.getcwd()
    # Версия ядра:
    python_core = sys.version.strip()
    # Версия операционной системы:
    os_information = f'{os.uname()[0]} {os.uname()[2]}'
    os_info = {
        'network_interfaces': network_interfaces,
        'default_path': default_path,
        'cpu_info': cpu_info,
        'process_id': process_id,
        'all_processes': all_processes,
        'interfaces_stat': interfaces_stat,
        'service_status': service_status,
        'port_type': port_type,
        'package_version': package_version,
        'files_list': files_list,
        'current_directory': current_directory,
        'python_core': python_core,
        'os_information': os_information,

    }

    with open('logs/os_info.json', 'w') as output:
        json.dump(os_info, output, indent=2)

    print("OS information successfully collected!")


if __name__ == '__main__':
    get_os_info()
