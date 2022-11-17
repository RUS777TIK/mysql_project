import hashlib


class Hash:
    __salt__ = 'PwH4K'.encode('utf-8')

    @staticmethod
    def get_hash(password):
        return hashlib.sha256(password.encode('utf-8') + Hash.__salt__).hexdigest()

    @staticmethod
    def check_hash(_hash, password):
        return Hash.get_hash(password) == _hash
