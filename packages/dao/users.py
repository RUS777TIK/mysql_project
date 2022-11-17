from packages.abstract import DAO, Connection
from sqlalchemy import Column, Integer, String, Boolean, PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base, DAO):
    __tablename__ = 'users'
    id = Column(Integer(), comment='Идентификатор', autoincrement=True)
    email = Column(String(50), nullable=False, index=True, comment='Email')
    password = Column(String(255), nullable=False, comment='Пароль')
    name = Column(String(100), nullable=False, comment='Имя пользователя')
    is_active = Column(Boolean(), default=False, comment='Активность')
    created_at = Column(Integer(), comment='Дата создания', default=DAO.get_timestamp)
    updated_at = Column(Integer(), comment='Дата изменения', default=DAO.get_timestamp, onupdate=DAO.get_timestamp)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='users_pk'),
        UniqueConstraint('email',)
    )

    @classmethod
    def one(cls, _id: int):
        return Connection.get_session().query(cls).get(_id)

    def save(self):
        session = Connection.get_session()
        session.add(self)
        session.commit()
