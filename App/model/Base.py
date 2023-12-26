from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

# Create an SQLite database engine
engine = create_engine('sqlite:///Restaurant.db')

# Define a naming convention
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

# Create a metadata object with the naming convention
metadata = MetaData(naming_convention=convention)

# Use declarative_base with the specified metadata
Base = declarative_base(metadata=metadata)
