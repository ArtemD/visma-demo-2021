from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

Base = declarative_base()

class License(Base):
    """
    License object
    """
    __tablename__ = 'licenses'

    id = Column(Integer, primary_key=True)
    """ Primary key """
    name = Column(String(255))
    """ License holder's name """
    address = Column(String(255))
    """ Address """
    postcode = Column(String(255))
    """ Postcode """
    city = Column(String(255))
    """ City """
    license_granting_date = Column(String(255))
    """ License granting date in format dd.mm.yyyy """
    license_type = Column(String(255))
    """ License type as a string (in Finnish) """
    business_id = Column(String(255))
    """ Business id or N/A if not applicable """
    created_at  = Column(DateTime, default=datetime.utcnow)
    """ Automatically generated date and time of insertion """

    def __repr__(self):
        """ String representation of the object """
        return "<License (name='%s', created_at='%s')>" % (self.name, self.created_at)

DATABASE_URL = os.environ['DATABASE_URL']
""" Database URI string """
db = create_engine(DATABASE_URL)
""" Database connection """
Session = sessionmaker(bind=db)
""" Database session """