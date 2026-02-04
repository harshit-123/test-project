# grpc_services/order_server.py
import grpc
from concurrent import futures
from generated import order_pb2, order_pb2_grpc

class OrderService(order_pb2_grpc.OrderServiceServicer):
    def GetOrders(self, request, context):
        return order_pb2.GetOrdersResponse(
            orders=[
                order_pb2.Order(order_id=1, item="Laptop"),
                order_pb2.Order(order_id=2, item="Mouse"),
            ]
        )

server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
order_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)
server.add_insecure_port("localhost:50052")
server.start()
server.wait_for_termination()
