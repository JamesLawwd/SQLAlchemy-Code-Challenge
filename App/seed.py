from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from model.Restaurant import Restaurant
from model.Customer import Customer
from model.Review import Review
from model.Base import Base

def create_session():
    engine = create_engine('sqlite:///Restaurant.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    return DBSession()

def display_data(session):
    # Display Restaurants
    print("\nRestaurants:")
    for restaurant in session.query(Restaurant).all():
        print(f"ID: {restaurant.id}, Name: {restaurant.name}, Price: {restaurant.price}")

    # Display Customers
    print("\nCustomers:")
    for customer in session.query(Customer).all():
        print(f"ID: {customer.id}, Name: {customer.first_name} {customer.last_name}")

    # Display Reviews
    print("\nReviews:")
    for review in session.query(Review).all():
        print(f"ID: {review.id}, Rating: {review.star_rating}, Restaurant: {review.restaurant.name}, Customer: {review.customer.first_name} {review.customer.last_name}")

if __name__ == '__main__':
    with create_session() as session:
        # Clear existing data
        session.query(Customer).delete()
        session.query(Review).delete()
        session.query(Restaurant).delete()

        # Seed new data
        seed_data(session)

        # Display information about the generated data
        display_data(session)

    print("Finished")
