from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from config import *


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

    Session = sessionmaker(bind=engine)
    session = Session()
    # initiate the Session function


    # 1. join tables by where clause
    for row in session.query(User, Address).filter(User.id == Address.user_id):
        print row
    """
    for user, user_addr in session.query(User, Address).filter(User.id==Address.user_id):
        print user
        print user_addr
        print user_addr.address

    # 2. join tables by join clause
    for row in session.query(User).join(Address).filter(Address.address == "aaaaaa"):
        print row

    # 3. specify the key (if there are multiple keys)
    for row in session.query(User).join(Address, User.id==Address.user_id).filter(Address.address == "aaaaaa"):
        print row

    # 4. outer join
    for row in session.query(User).outerjoin(Address).filter(Address.address == "aaaaaa"):
        print row
        
    #left join: http://www.w3schools.com/sql/sql_join_left.asp
    #right join: http://www.w3schools.com/sql/sql_join_right.asp
    #outer join: http://www.w3schools.com/sql/sql_join_full.asp
    #inner join: http://www.w3schools.com/sql/sql_join_inner.asp        
    """

    session.close()
