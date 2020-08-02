""" Тесты проверки доступности сервиса и сервера """

from tools.ssh_client import PASSWORD, open_ssh_connection, close_ssh_connection, client


def test_restart_service():
    """ Проверка перезапуска и доступности сервиса"""

    open_ssh_connection()

    stdin, stdout, stderr = client.exec_command('sudo -S /etc/init.d/dbus restart')
    stdin.write(PASSWORD + '\n')
    service_restart_status = stdout.read() + stderr.read()

    close_ssh_connection()

    assert "Starting" and "dbus" in service_restart_status.decode(),\
        'Ошибка при перезагрузке сервиса'


def test_reboot_system():
    """ Проверка перезапуска и доступности сервера"""

    open_ssh_connection()

    stdin, stdout, stderr = client.exec_command('last reboot')
    last_reboot = stdout.read() + stderr.read()
    print(last_reboot.decode())

    stdin, stdout, stderr = client.exec_command('sudo -S reboot -f')
    transport = client.get_transport()
    transport.set_keepalive(5)
    stdin.write(PASSWORD + '\n')
    stdout.read()

    close_ssh_connection()

    open_ssh_connection()

    stdin, stdout, stderr = client.exec_command('last reboot')
    new_last_reboot = stdout.read() + stderr.read()
    print(new_last_reboot.decode())

    close_ssh_connection()

    assert new_last_reboot != last_reboot, 'System was NOT successfully rebooted '
