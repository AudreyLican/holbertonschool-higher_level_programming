"""

Not to push


"""
#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == "__main__":
    # Database connection setup
    # Construct the database URL using command-line arguments
    database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    # Create an engine to connect to the database
    engine = create_engine(database_url)

    # Create a Session class bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session object
    session = Session()
    
    query_lines = session.query(City, State).\
        filter(City.state_id == State.id).all()
    """Retrieving City-State pairs objects with matching stade_id"""

    # Print result
    for city, state in query_lines:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
