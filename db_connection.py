from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy.exc

from data import db_options

# Database connection string
DATABASE_URL = f"mysql://{db_options.user}:{db_options.host}@{db_options.host}:3306/{db_options.database}"

# Create the engine
engine = create_engine(DATABASE_URL)

# Create a Session class to handle transactions
Session = sessionmaker(bind=engine)


# Check if the database exists, if not, create it
try:
    engine.connect()
except sqlalchemy.exc.OperationalError:
    print("Database does not exist. Creating...")
    # Datbase creation
    engine.execute(f"CREATE DATABASE {db_options.database}")

# Close the initial connection
engine.dispose()