from passlib.context import CryptContext

from .repository import CustomerRepository
from .schemas import CustomerCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
customer_repo = CustomerRepository()

async def create_customer(customer: CustomerCreate):
    """Handles business logic behind creating a customer"""

    try:
        hashed_password = pwd_context.hash(customer.password)

        customer_repo.create_customer(
                first_name=customer.first_name,
                last_name=customer.last_name,
                email=customer.email,
                password=hashed_password
            )
        return
    except Exception as e:
        raise e
