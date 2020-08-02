""" Методы подключения к удаленному серверу с opencart """

import paramiko


HOST = '10.0.1.32'
USERNAME = 'ekaterina'
PASSWORD = 'merterbok'
PORT = 22

client = paramiko.SSHClient()


def open_ssh_connection():
    """ Метод подключения к удаленному серверу с opencart """

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=HOST,
        username=USERNAME,
        password=PASSWORD,
        port=PORT
    )
    return client


def close_ssh_connection():
    """ Метод закрытия подключения к удаленному серверу с opencart """

    client.close()
    return client
