from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from config import *

from sqlalchemy import text


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

    # 1. select * from users
    for row in session.query(User):
        print row
        print row.name
        print row.birthday
        # select * does not support list usage
    """
    # 2. select name, id from users
    for row in session.query(User.name, User.id):
        print row
        print row[1]
        print row.name

    # 3. multiple arguments
    for name, id in session.query(User.name, User.id):
        print id, name

    # 4. select * from user where id = 1
    # filter_by()
    for row in session.query(User.id).filter_by(id=1):
        print row.id

    # 5. filter(map_class.column + operator)
    for row in session.query(User.id).filter(User.id == 2):
        print row.id

    # 6. filter(text.(conditions as string)). Need to import text or you'll get warning
    for row in session.query(User.id).filter(text('id=3')):
        print row.id
    """

    session.close()
