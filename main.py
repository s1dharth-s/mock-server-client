from fastapi import FastAPI
import uvicorn

from utils.create_db import create_database
from app import endpoints

# Create mock database if it does not exist
create_database()

# Initialise FastAPI application
app = FastAPI(title="Mock Data App")

# Attach routers
app.include_router(endpoints.router)

if __name__ == "__main__":
    # start uvicorn server
    uvicorn.run(app, host="127.0.0.1", port=8000)