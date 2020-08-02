""" Методы для работы с SSL подключением """

import socket
import ssl


class SocketClient:
    """ Методы для работы с SSL подключением """

    host = "www.ticketland.ru"
    port = 443
    method = "GET"
    headers = "Server"

    def __init__(self):
        self.sock = self.socket_create()
        self.request = self.request_create(self.method, self.host, self.port)

    def open_ssl_connection(self):
        """ Метод создания SSL подключения """

        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.verify_mode = ssl.CERT_REQUIRED
        context.check_hostname = True
        context.load_default_certs()
        return context

    def socket_create(self):
        """ Метод создания socket """

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock = self.open_ssl_connection().wrap_socket(sock, server_hostname=self.host)

        return sock

    def socket_connect(self):
        """ Метод SSL подключения """

        self.sock.connect((self.host, self.port))

    def request_create(self, method=method, host=host, headers=headers):
        """ Метод создания запроса """

        request = f'{method} / HTTP/1.1\n\n' + f'Host: {host}\n\n' + f'{headers}'
        return request

    def socket_send(self):
        """ Метод отправления запроса """

        sock_send = self.sock.send(self.request.encode())
        return sock_send

    def socket_receive(self):
        """ Метод получения запроса """

        response = self.sock.recv(8192)
        return response

    def close_connect(self):
        """ Метод закрытия SSL подключения """

        self.sock.close()


socket_client = SocketClient()
