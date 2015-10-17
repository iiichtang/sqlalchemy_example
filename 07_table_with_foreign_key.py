from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from config import *

from sqlalchemy import ForeignKey


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    birthday = Column(Date)
    age = Column(Integer, nullable=False, default=1)
    description = Column(String(180, collation='utf8_unicode_ci'), index=True)

    def __init__(self, name, birthday, age, description):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.description = description

    def __repr__(self):
        return "User('%s','%s', '%s', '%s')" % \
               (self.name, self.birthday, self.age, self.description)


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(180), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self, address, user_id):
        self.address = address
        self.user_id = user_id


if __name__ == "__main__":
    target_database = 'mysql+pymysql://%s:%s@%s:%s/%s' % (DB_USERNAME, DB_PASSWORD, DB_HOSTNAME,
                                                          DB_PORT, DB_DATABASE)

    engine = create_engine(target_database, echo=True)

    Base.metadata.create_all(engine)
    # create tables based on the classes which inherit Base
    # if the table already exist, it won't re-create it

    Session = sessionmaker(bind=engine)
    session = Session()

    addr_1 = Address(address="aaaaaa", user_id=1)
    addr_2 = Address(address="aaaaaa", user_id=2)
    addr_3 = Address(address="aaaaaa", user_id=3)
    addr_4 = Address(address="bbbbbb", user_id=4)
    addr_5 = Address(address="bbbbbb", user_id=5)
    addr_6 = Address(address="bbbbbb", user_id=6)

    session.add(addr_1)
    session.add(addr_2)
    session.add(addr_3)
    session.add(addr_4)
    session.add(addr_5)
    session.add(addr_6)

    session.commit()

    """
    addr_x = Address(address="xxxxxx", user_id=99999)
    session.add(addr_x)
    session.commit()
    """

    session.close()

