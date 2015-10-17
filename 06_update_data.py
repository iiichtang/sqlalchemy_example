from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
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


if __name__ == "__main__":
    target_database = 'mysql+pymysql://%s:%s@%s:%s/%s' % (DB_USERNAME, DB_PASSWORD, DB_HOSTNAME,
                                                          DB_PORT, DB_DATABASE)

    engine = create_engine(target_database, echo=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    update_row = session.query(User).filter(User.name == "test_user_4").update({'name': 'newname', 'age': '999'})
    print update_row

    session.commit()

    session.close()
