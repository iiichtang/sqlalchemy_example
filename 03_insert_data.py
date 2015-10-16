from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from config import *

from sqlalchemy.orm import sessionmaker


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


if __name__ == "__main__":
    target_database = 'mysql+pymysql://%s:%s@%s:%s/%s' % (DB_USERNAME, DB_PASSWORD, DB_HOSTNAME,
                                                          DB_PORT, DB_DATABASE)

    engine = create_engine(target_database, echo=True)

    Session = sessionmaker(bind=engine)
    """
    Session = sessionmaker()
    Session.configure(bind=engine)
    """

    session = Session()
    # initiate the Session function

    user_1 = User(name="test_user_1", birthday="2015-01-02", age=54, description="just a test")
    user_2 = User(name="test_user_2", birthday="2015-01-02", age=55, description="just a test")
    user_3 = User(name="test_user_1", birthday="2015-01-03", age=56, description="just a test")
    user_4 = User(name="test_user_2", birthday="2015-01-03", age=57, description="just a test")
    user_5 = User(name="test_user_1", birthday="2015-01-04", age=58, description="just a test")
    user_6 = User(name="test_user_2", birthday="2015-01-04", age=59, description="just a test")
    user_7 = User(name="test_user_3", birthday="2015-01-03", age=57, description="just a test")
    user_8 = User(name="test_user_3", birthday="2015-01-04", age=58, description="just a test")
    user_9 = User(name="test_user_3", birthday="2015-01-04", age=59, description="just a test")
    user_10 = User(name="test_user_4", birthday="2015-01-03", age=57, description="just a test")
    user_11 = User(name="test_user_4", birthday="2015-01-04", age=58, description="just a test")
    user_12 = User(name="test_user_4", birthday="2015-01-04", age=59, description="just a test")
    session.add(user_1)
    session.add(user_2)
    session.add(user_3)
    session.add(user_4)
    session.add(user_5)
    session.add(user_6)
    session.add(user_7)
    session.add(user_8)
    session.add(user_9)
    session.add(user_10)
    session.add(user_11)
    session.add(user_12)

    session.commit()
    # data can only be written when perform QUERY, COMMIT, FLUSH

