from packages.dao import UsersDAO
from packages.utils import Hash


class Users(UsersDAO):
    def save(self):
        original_password = self.password

        def generate_password(password):
            if not password:
                return None
            user = None
            if self.is_exists:
                user = self.one(self.id)
            if not user or (user.password != password and not Hash.check_hash(user.password, password)):
                return Hash.get_hash(password)
            return user.password

        self.password = generate_password(original_password)
        try:
            super().save()
        except Exception as e:
            self.password = original_password
            raise e
