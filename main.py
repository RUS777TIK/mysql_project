import sys

from dynaconf import Dynaconf
from packages.utils import Logger
from packages.abstract import Connection
from packages.services import *
from packages.services import __meta__ as service_meta


class Application:
    def __init__(self, config_file):
        config = Dynaconf(
            settings_file=[config_file],
            environments=False
        )
        Logger.config(config.get('Logger'))
        try:
            Connection.connect(config.get('MySQL', dict()))
            Logger.info('Соединение с базой данных выполнено')
            for model in service_meta:
                model.metadata.create_all(Connection.get_instance())
            Logger.info('Все модели созданы')
        except Exception as e:
            Logger.exception(e)
            raise e
    def run(self):
        Logger.info('Запуск приложения')


if __name__ == '__main__':
    try:
        app = Application('./config.json')
        app.run()
    except:
        sys.exit()
