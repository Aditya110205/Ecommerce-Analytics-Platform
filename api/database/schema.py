from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Customer(Base):

    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True)

    name = Column(String(100))

    email = Column(String(100))

    city = Column(String(100))


class Product(Base):

    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True)

    product_name = Column(String(100))

    category = Column(String(100))

    price = Column(Float)


class Order(Base):

    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)

    customer_id = Column(
        Integer,
        ForeignKey("customers.customer_id")
    )

    product_id = Column(
        Integer,
        ForeignKey("products.product_id")
    )

    quantity = Column(Integer)

    amount = Column(Float)

    created_at = Column(DateTime)