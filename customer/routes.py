from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from .service import create_customer, customer_login
from .schemas import CustomerCreate, CustomerLogin

customer_router = APIRouter()

@customer_router.post("/register", status_code=201)
async def register_customer(customer: CustomerCreate):
    """API endpoint to handle customer registration"""
    try:
        await create_customer(customer)

        return JSONResponse(status_code=201, content="Customer registered successfully")
    except HTTPexception as e:
        raise e
    except Exception as e:
        raise HTTPException(
                status_code=500,
                detail="An unexpected error occured while registering user"
            )

@customer_router.post("/login", status_code=200)
async def login_customer(customer: CustomerLogin):
    """API endpoint to handle user login"""
    try:
        login_data = await customer_login(customer)

        return JSONResponse(status_code=200, content=login_data)
    except HTTPException as e:
            raise e
    except Exception as e:
        raise HTTPException(
                status_code=500,
                detail="An unexpected error occured while logging in user"
            )
