from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.Restaurant import Restaurant
from model.Review import Review
from model.Customer import Customer

if __name__ == '__main__':
    engine = create_engine('sqlite:///Restaurant.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    print("\n Customer List:")
    for review in session.query(Review).all():
        customer = review.customer
        print(f"Review by {customer.first_name} {customer.last_name}: {review.star_rating} stars")

    print("\n Restaurant List:")
    for review in session.query(Review).all():
        restaurant = review.restaurant
        print(f"Review for {restaurant.name}: {review.star_rating} stars")
