from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from config import *

from sqlalchemy import desc
from sqlalchemy import func
from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy.orm.exc import NoResultFound


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


    # 13.1 SELECT id FROM user ORDER BY id
    for row in session.query(User.id).order_by(User.id):
        print row.id
    """
    # 13.2 You need to import desc before you order by descent.
    for row in session.query(User.id).order_by(User.id.desc()):
        print row.id

    # 14. limit
    for row in session.query(User)[1:4]:
        print row.id

    # 15. group by
    for row in session.query(User).group_by(User.name):
        print row.name

    # 16.1 count (outside the sql statements)
    print session.query(User).count()

    # 16.2 count (using sql statements, need to import func)
    print session.query(func.count(User.name), User.name).group_by(User.name).all()

    # 17. first
    print session.query(User).first()

    # 18. all
    data_list = session.query(User).all()
    print data_list

    # 19. one (check if there is exactly one result, and throw error if not)
    # need to import MultipleResultsFound, NoResultFound first
    try:
        result = session.query(User).one()
    except MultipleResultsFound, e:
        print e
    except NoResultFound, e:
        print e
    else:
        print result
    """


