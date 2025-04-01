import grpc
from concurrent import futures
import time
from datetime import datetime
import post_pb2
import post_pb2_grpc

posts = []
id_counter = 1

def current_time():
    return datetime.utcnow().isoformat()

class PostService(post_pb2_grpc.PostServiceServicer):
    def CreatePost(self, request, context):
        global id_counter
        post = post_pb2.Post(
            id=id_counter,
            title=request.title,
            description=request.description,
            creator_id=request.creator_id,
            created_at=current_time(),
            updated_at=current_time(),
            is_private=request.is_private,
            tags=request.tags
        )
        posts.append(post)
        id_counter += 1
        return post_pb2.PostResponse(post=post)

    def DeletePost(self, request, context):
        global posts
        posts = [p for p in posts if p.id != request.id]
        return post_pb2.Empty()

    def UpdatePost(self, request, context):
        for i, post in enumerate(posts):
            if post.id == request.id:
                updated_post = post_pb2.Post(
                    id=post.id,
                    title=request.title,
                    description=request.description,
                    creator_id=post.creator_id,
                    created_at=post.created_at,
                    updated_at=current_time(),
                    is_private=request.is_private,
                    tags=request.tags
                )
                posts[i] = updated_post
                return post_pb2.PostResponse(post=updated_post)
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details("Post not found")
        return post_pb2.PostResponse()

    def GetPostById(self, request, context):
        for post in posts:
            if post.id == request.id:
                return post_pb2.PostResponse(post=post)
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details("Post not found")
        return post_pb2.PostResponse()

    def ListPosts(self, request, context):
        start = (request.page - 1) * request.page_size
        end = start + request.page_size
        return post_pb2.ListPostsResponse(posts=posts[start:end])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    post_pb2_grpc.add_PostServiceServicer_to_server(PostService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC PostService запущен на порту 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
