from fastapi import HTTPException

from .repository import OrderRepository
from .schemas import OrderCreate

# Create a Data Transfer Object
order_repo = OrderRepository()

async def create_new_order(order: OrderCreate):
    """Handles business logic behind creating an order in the database"""

    try:
        order_repo.create_order(
            customer_id=order.customer_id,
            order_price=order.price,
            item_id=order.item_id
        )
        return
    except Exception as e:
        raise e

async def get_order(order_id: int):
    """Handles logic for getting an order from the database"""

    try:
        order = order_repo.get_order_by_id(order_id)

        if not order:
            raise HTTPException(
                    status_code=404,
                    detail="Order not found"
                )

        return {
            "order_id": order_id,
            "order_item_id": order["product_id"],
            "placed_at": str(order["order_date"]),
            "total": str(order["total_amount"])
        }
    except Exception as e:
        raise e

async def remove_order(order_id: int):
    """Handles logic for deleting an order record from the database"""

    try:
        if not order_repo.get_order_by_id(order_id):
            raise HTTPException(
                    status_code=204
                )

        order_repo.delete_order_by_id(order_id)

        return
    except Exception as e:
        raise e
