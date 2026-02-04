# grpc_services/user_server.py
import grpc
from concurrent import futures
from generated import user_pb2, user_pb2_grpc

class UserService(user_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        return user_pb2.GetUserResponse(
            user_id=request.user_id,
            name="Harshit"
        )

server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
server.add_insecure_port("localhost:50051")
server.start()
server.wait_for_termination()
