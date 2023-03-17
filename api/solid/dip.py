"""
WRONG
"""


class MySqlConnection():
    def connect(self):
        pass


class PageLoader():
    def __init__(self, mysql_connection: MySqlConnection):
        self._mysql_connection = mysql_connection


"""
RIGHT
"""


class DbConnectionMeta(type):
    def __instancecheck__(self, instance):
        return self.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        return (hasattr(subclass, 'connect') and callable(subclass.connect))


class DbConnectionInterface(metaclass=DbConnectionMeta):
    pass


class MySqlConnection(DbConnectionInterface):
    def connect(self):
        pass


class PageLoader():
    def __init__(self, db_connection: DbConnectionInterface):
        self._db_connection = db_connection
