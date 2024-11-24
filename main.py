from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
import os

from customer.routes import customer_router

app = FastAPI(
        title="Savannah E-Commerce",
        docs_url="/"
    )

app.add_middleware(
        SessionMiddleware,
        secret_key=os.getenv("SECRET_KEY")
    )

app.include_router(customer_router, prefix="/api/v1", tags=["Auth routes"])
