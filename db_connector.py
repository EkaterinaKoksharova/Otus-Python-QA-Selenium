""" Методы для подключения к базе данных opencart """

import mysql.connector


class DBconnector:
    """ Класс с методами подключения к базе данных opencart """

    def db_connection(self):
        """ Метод подключения к базе данных opencart """
        self.connection = mysql.connector.connect(user='ocadmin',
                                                  password='password',
                                                  host='localhost',
                                                  port='8889',
                                                  database='opencart')

        self.cursor = self.connection.cursor()

    def count_products(self):
        """" Метод подсчета общего количества продуктов в базе данных opencart"""

        try:
            self.db_connection()
            self.cursor.execute("SELECT * FROM oc_product")
            result = self.cursor.fetchall()
            self.cursor.close()
            self.connection.close()
            print(len(result))
            return len(result)

        except mysql.connector.Error as error:
            print(format(error))

    def get_product_information(self, product_name):
        """" Метод получения информации о продукте в базе данных opencart"""

        try:
            self.db_connection()
            self.cursor.execute("SELECT * FROM oc_product_description WHERE name="
                                + "'" + product_name + "'")
            result = self.cursor.fetchall()
            self.cursor.close()
            self.connection.close()
            print(result)
            return result

        except mysql.connector.Error as error:
            print(format(error))
