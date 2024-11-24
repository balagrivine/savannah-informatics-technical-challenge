from fastapi import FastAPI

from customer.routes import customer_router

app = FastAPI(
        title="Savannah E-Commerce",
        docs_url="/"
    )

app.include_router(customer_router, prefix="/api/v1", tags=["Auth routes"])
