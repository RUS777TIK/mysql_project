from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class Connection:
    __instance__ = {
        'engine': None,
        'connection': None
    }
    __config__ = None
    __session__ = None

    @staticmethod
    def connect(config=None):
        if Connection.__instance__.get('engine') is not None:
            return Connection.__instance__.get('engine')
        if not config:
            raise Exception('Не найдена конфигурация базы данных')
        Connection.__config__ = config
        db_host = config.get('host')
        db_port = int(config.get('port'))
        db_user = config.get('username')
        db_pass = config.get('password')
        db_table = config.get('table')
        engine = create_engine(f'mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_table}')
        Connection.__instance__['engine'] = engine
        Connection.__instance__['connection'] = engine.connect()
        return engine

    @staticmethod
    def get_instance():
        return Connection.connect(Connection.__config__)

    @staticmethod
    def close():
        connection = Connection.__instance__.get('connection')
        if connection is not None:
           connection.close()

    @staticmethod
    def get_session():
        Connection.close_session()
        Connection.__session__ = Session(bind=Connection.get_instance())
        return Connection.__session__

    @staticmethod
    def close_session():
        if Connection.__session__ is not None:
            Connection.__session__.close()


