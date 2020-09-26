import mysql.connector


class MysqlConnector:
    def __init__(self, config):
        self.host = config['host']
        self.database = config['database']
        self.user = config['user']
        self.password = config['password']

    def connect(self):
        mysql.connector.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )


class MyFactory:
    available_databases = {
        'msql': MysqlConnector,
        # 'cassandra': CassandraConnector,
        # 'postgresql': PostgreSQLConnector,
        # etc.
    }

    @classmethod
    def create_connector(cls, db_name, **kwargs):
        assert db_name in cls.available_databases, 'The chosen database cannot be accessed.'
        return cls.available_databases[db_name](kwargs)


def main():
    # MyFactory.create_connector(db_name='oracle')  # Raises AssertionError
    my_connector = MyFactory.create_connector(
        db_name='msql',
        host='localhost',
        database='mysql',
        user='root',
        password='your pass'
    )
    # my_connector.connect()


if __name__ == '__main__':
    main()
