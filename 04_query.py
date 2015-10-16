from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from config import *

from sqlalchemy import text
from sqlalchemy import desc


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


    # select * from users
    for row in session.query(User):
        print row
        print row.name
        print row.birthday
        #select * does not support list usage
    """
    # select name, id from users
    for row in session.query(User.name, User.id):
        print row
        print row[1]
        print row.name

    # select * from user where id = 1
    # filter_by()
    for row in session.query(User.id).filter_by(id=1):
        print row.id

    # filter(map_class.column + operator)
    for row in session.query(User.id).filter(User.id == 2):
        print row.id

    # filter(text.(conditions as string)). This method need to import text or you'll get warning
    for row in session.query(User.id).filter(text('id=3')):
        print row.id

    # multiple filter
    for row in session.query(User.id).filter(User.name == "test_user_1").filter(User.age >= 57):
        print row.id

    # SELECT id FROM user ORDER BY id
    for row in session.query(User.id).order_by(User.id):
        print row.id

    # You need to import desc before you order by descent.
    for row in session.query(User.id).order_by(User.id.desc()):
        print row.id

    # limit
    for row in session.query(User)[1:4]:
        print row.id

    # group by
    for row in session.query(User).group_by(User.name):
        print row.name

    #count
    print session.query(User).count()

    #first
    print session.query(User).first()

    # all
    data_list = session.query(User).all()
    print data_list
    """
