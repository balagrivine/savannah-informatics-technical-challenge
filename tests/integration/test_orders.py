from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

def test_create_order_success():
    order_data = {
            "customer_id": 1,
            "price": 12.00,
            "item_id": 1
        }
    response = client.post("/api/v1/orders", json=order_data)

    assert response.status_code == 201
    assert response.json() == {"message": "Order created successfully"}
