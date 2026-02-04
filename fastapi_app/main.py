# fastapi_app/main.py
from fastapi import FastAPI
import grpc
from generated import (
    user_pb2, user_pb2_grpc,
    order_pb2, order_pb2_grpc
)

app = FastAPI()

# Create channels
user_channel = grpc.aio.insecure_channel("localhost:50051")
order_channel = grpc.aio.insecure_channel("localhost:50052")

# Create stubs
user_stub = user_pb2_grpc.UserServiceStub(user_channel)
order_stub = order_pb2_grpc.OrderServiceStub(order_channel)

@app.get("/users/{user_id}/profile")
async def user_profile(user_id: int):
    user = await user_stub.GetUser(
        user_pb2.GetUserRequest(user_id=user_id)
    )

    orders = await order_stub.GetOrders(
        order_pb2.GetOrdersRequest(user_id=user_id)
    )

    return {
        "user": {
            "id": user.user_id,
            "name": user.name
        },
        "orders": [
            {"order_id": o.order_id, "item": o.item}
            for o in orders.orders
        ]
    }
