import sqlalchemy #mb it won`t work
from datetime import datetime
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = 'postgresql://postgres:123@localhost:5432/sqlnettask6' #мб не сработает база данных. Вроде пока работает
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher1 = Publisher(name='Пушкин')
session.add(publisher1)
session.commit()

book1 = Book(title='Капитанская дочка', id_publisher=1)
session.add(book1)
book2 = Book(title='Руслан и Людмила', id_publisher=1)
session.add(book2)
book3 = Book(title='Евгений Онегин', id_publisher=1)
session.add(book3)
session.commit()
print(book3.title)

shop1 = Shop(name='Буквоед')
session.add(shop1)
shop2 = Shop(name='Лабиринт')
session.add(shop2)
shop3 = Shop(name='Книжный дом')
session.add(shop3)
session.commit()
print(shop3.name)

stock1 = Stock(id_book=1, id_shop=1)
session.add(stock1)
stock2 = Stock(id_book=2, id_shop=1)
session.add(stock2)
stock3 = Stock(id_book=1, id_shop=3)
session.add(stock3)
stock4 = Stock(id_book=3, id_shop=3)
session.add(stock4)
stock5 = Stock(id_book=1, id_shop=1)
session.add(stock5) #такое ощущение, что он не создает новые связи, а перезаписывает старые
session.commit()
# print(stock1.id_book)

sale1 = Sale(prise=600, date_sale=datetime(2022, 11, 9), id_stock=1)
session.add(sale1)
sale2 = Sale(prise=500, date_sale=datetime(2022, 11, 8), id_stock=2)
session.add(sale2)
sale3 = Sale(prise=580, date_sale=datetime(2022, 11, 5), id_stock=3)
session.add(sale3)
sale4 = Sale(prise=490, date_sale=datetime(2022, 11, 2), id_stock=4)
session.add(sale4)
sale5 = Sale(prise=600, date_sale=datetime(2022, 10, 26), id_stock=5)
session.add(sale5)

session.commit()
print(sale1.prise)
print(sale1.date_sale)

session.close()

def query_input_publisher_name_books(author_name):
    sql1 = session.query(Publisher, Book, Stock, Shop, Sale).join(Book, Publisher.id == Book.id_publisher).join(Stock, Book.id == Stock.id_book).join(Shop, Stock.id_shop == Shop.id).join(Sale, Stock.id == Sale.id_stock).filter(Publisher.name == author_name).all()
    for publisher, book, stock, shop, sale in sql1:
        print(book.title, shop.name, sale.prise, sale.date_sale)

author_name = input("Введите имя автора: ")
query_input_publisher_name_books(author_name)