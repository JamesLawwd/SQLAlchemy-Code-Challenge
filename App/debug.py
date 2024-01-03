from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.Restaurant import Restaurant
from model.Review import Review
from model.Customer import Customer

if __name__ == '__main__':
    engine = create_engine('sqlite:///Restaurant.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Print the name of the customers who made a review
    print("\nCustomer list:")
    for review in session.query(Review).all():
        customer = review.customers
        print(f"Review by {customer.first_name} {customer.last_name}: {review.star_rating} stars")

    # Print the name of the restaurant that has been reviewed
    print("\nRestaurant list:")
    for review in session.query(Review).all():
        restaurant = review.restaurants
        print(f"Review for {restaurant.name} - {review.star_rating} stars")

    # Retrieving a restaurant and its associated reviews from the database
    restaurant = session.query(Restaurant).first()

    # Accessing the reviews using the relationship
    all_reviews = restaurant.display_reviews()

    # Printing the restaurant and its reviews
    print("\nAll Reviews per restaurant:")
    for r in all_reviews:
        print(f"Review id: {r.id} Rating: {r.star_rating} Restaurant name: {restaurant.name}")

    # Print the name of customers who reviewed a certain restaurant
    print("\nCustomer name and restaurant:")
    all_customers = restaurant.display_customers()
    for r in all_customers:
        print(f"Review for {restaurant.name} by {r.first_name} {r.last_name}")

    # Print the list of restaurant that have been reviewed by a customer
    print("\nCustomer name, restaurant name, and restaurant star rating:")
    customer = session.query(Customer).first()
    all_customers_reviews = customer.display_reviews()
    for r in all_customers_reviews:
        print(f"Review made by {customer.first_name} {customer.last_name} for restaurant id {r.restaurant_id} and gave a rating of {r.star_rating}")

    # Print customer name and the restaurants he/she reviewed
    print("\nCustomer name, restaurant name, and restaurant price:")
    all_customers_reviewed_restaurants = customer.display_restaurants()
    for r in all_customers_reviewed_restaurants:
        print(f"Review for {r.name} by {customer.first_name} {customer.last_name} with a price of {r.price}")
