import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from app.config import DATABASE_URL


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine(DATABASE_URL, echo= True)