from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from SaleApp import app, db

class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=True)
    products = relationship('Product', backref="category", lazy=True)

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=True)
    price = Column(Float, default=0.0)
    image = Column(String(300))
    cate_id = Column(ForeignKey(Category.id), nullable=True)


if __name__=="__main__":
    with app.app_context():
        db.create_all()
