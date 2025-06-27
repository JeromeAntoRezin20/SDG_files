from sqlalchemy import create_engine,Column,INTEGER,String,CHAR
from sqlalchemy.orm import declarative_base,sessionmaker

engine = create_engine("sqlite:///users.db",echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id =Column(INTEGER, primary_key=True)
    name = Column(String)
    email = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def add_user(name,email):
    new_user = User(name = name, email = email)
    session.add(new_user)
    session.commit()

def view_all():
    users = session.query(User).all()
    for i in users:
        print(f"ID : {i.id}, Name : {i.name}, Email : {i.email}")


add_user('john', 'john@mail.com')
view_all()





