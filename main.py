from fastapi import FastAPI

from utils.create_db import create_database
from app import endpoints

# Create mock database everytime on startup
create_database()

# Initialise FastAPI application
app = FastAPI()


# Attach routers
app.include_router(endpoints.router)