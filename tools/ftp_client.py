""" Методы FTP подключения к удаленному серверу с opencart """

from paramiko import Transport, SFTPClient


class FtpClient:
    """ Методы FTP подключения к удаленному серверу с opencart """

    HOST = '10.0.1.32'
    USERNAME = 'ekaterina'
    PASSWORD = 'merterbok'
    PORT = 22

    remote_path = '/var/log/apache2/'
    remote_file = '/var/log/apache2/access.log.1'
    local_path = 'logs/access.log'

    def __init__(self):
        self.transport = Transport(sock=(self.HOST, self.PORT))
        self.transport.connect(username=self.USERNAME, password=self.PASSWORD)
        self.ftp_connection = SFTPClient.from_transport(self.transport)

    def open_ftp_connection(self):
        """ Метод FTP подключения к удаленному серверу с opencart """

        print(self.ftp_connection.listdir(path=self.remote_path))
        return self.ftp_connection

    def close_ftp_connection(self):
        """ Метод закрытия FTP подключения к удаленному серверу с opencart """
        self.ftp_connection.close()
        return self.ftp_connection

    def download(self):
        """ Метод скачивания логов по FTP подключению к удаленному серверу с opencart """

        self.ftp_connection.get(remotepath=self.remote_file,
                                localpath=self.local_path,
                                callback=None)


if __name__ == '__main__':
    #Скрипт загрузки файлов с логами:

    ftp = FtpClient()

    ftp.open_ftp_connection()
    ftp.download()
    ftp.close_ftp_connection()
