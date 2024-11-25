from .repository import OrderRepository
from .schemas import OrderCreate

order_repo = OrderRepository()

async def create_new_order(order: OrderCreate):
    """Handles business logic behind creating an order in the database"""

    order_repo.create_order(
            customer_id=order.customer_id,
            order_price=order.price,
            item_id=order.item_id
        )
    return
