from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from config import *

from sqlalchemy import and_
from sqlalchemy import or_

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
    session = Session()
    # initiate the Session function

    # other operators for filter

    # 7. not equal
    for row in session.query(User.id).filter(User.id != 2):
        print row.id
    """
    # 8. like
    for row in session.query(User.id).filter(User.name.like('%user_2%')):
        print row.id

    # 9.1 in
    for row in session.query(User.id).filter(User.name.in_(['test_user_1', 'test_user_2'])):
        print row.id

    # 9.2 in(using objects)
    for row in session.query(User.id).filter(User.name.in_(
            session.query(User.name).filter(User.name.like('%user_2%'))
    )):
        print row.id

    # 9.3 not in
    for row in session.query(User.id).filter(~User.name.in_(['test_user_1', 'test_user_2'])):
        print row.id

    # 10.1 Null
    for row in session.query(User.id).filter(User.name == None):
        print row.id

    for row in session.query(User.id).filter(User.name.is_(None)):
        print row.id

    # 10.2 not Null
    for row in session.query(User.id).filter(User.name != None):
        print row.id

    for row in session.query(User.id).filter(User.name.isnot(None)):
        print row.id

    # 11. and
    for row in session.query(User.id).filter(User.name == "test_user_1").filter(User.age >= 55):
        print row.id

    for row in session.query(User.id).filter(User.name == "test_user_1", User.age >= 55):
        print row.id

    # need to import and_
    for row in session.query(User.id).filter(and_(User.name == "test_user_1", User.age >= 55)):
        print row.id

    # 12. or
    # need to import or_
    for row in session.query(User.id).filter(or_(User.name == "test_user_1", User.name == "test_user_2")):
        print row.id
    """

    session.close()
