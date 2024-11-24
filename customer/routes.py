from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from .service import create_customer
from .schemas import CustomerCreate

customer_router = APIRouter()

@customer_router.post("/register", status_code=201)
async def register_customer(customer: CustomerCreate):
    """API endpoint to handle customer registration"""
    try:
        await create_customer(customer)

        return JSONResponse(status_code=201, content="Customer registered successfully")
    except Exception as e:
        raise HTTPException(
                status_code=500,
                detail="An unexpected error occured."
            )
