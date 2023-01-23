import sqlalchemy #mb it won`t work
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book

DSN = 'postgresql://postgres:123@localhost:5432/sqlnettask5' #мб не сработает база данных
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.close()

