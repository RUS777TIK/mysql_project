from datetime import datetime


class DAO:
    @staticmethod
    def get_timestamp():
        return int(datetime.timestamp(datetime.now()))

    @property
    def is_exists(self):
        return hasattr(self, 'id') and getattr(self, 'id') is not None



