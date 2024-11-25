from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from .service import create_new_order
from .schemas import OrderCreate

order_router = APIRouter()

@order_router.post("/orders", status_code=201)
async def create_order(order: OrderCreate):
    """API endpoint to create a new order in the database"""

    try:
        await create_new_order(order)

        return JSONResponse(status_code=201, content={"message": "Order created successfully"})
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(
                status_code=500,
                detail="An unexpected error occured"
            )
