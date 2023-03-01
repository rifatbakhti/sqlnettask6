import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    # def __str__(self):
    #     return f'{self.name}: {self.title}'

class Book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)
    publisher = relationship(Publisher, backref='book')

class Shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    # count = '' нужно понять зачем это нужно и как это сделать
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    stock_id_book = relationship(Book, backref='book')
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    stock_id_shop = relationship(Shop, backref='shop')

class Sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    prise = sq.Column(sq.Integer, primary_key=True)
    date_sale = sq.Column(sq.DateTime(), unique=True)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    sale_id_stock = relationship(Stock, backref='stock')
    # count = нужно понять зачем это нужно и как это сделать

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
