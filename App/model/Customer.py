from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .Base import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    reviews = relationship('Review', back_populates='customers')
    restaurants = relationship('Restaurant', secondary='reviews', back_populates='customers', viewonly=True)

    def __repr__(self):
        return f"<Customer(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}')>"

    def display_reviews(self):
        return self.reviews

    def display_restaurants(self):
        return self.restaurants
