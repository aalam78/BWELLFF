import grpc
from concurrent import futures
import chat_gpt_pb2
import chat_gpt_pb2_grpc
import os

from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
# Set up your OpenAI API key

class ChatGPTServicer(chat_gpt_pb2_grpc.ChatGPTServicer):
    def ChatWithGPT(self, request, context):
        prompt = request.prompt
        response = self.chat_with_gpt(prompt)
        return chat_gpt_pb2.ChatResponse(response=response)

    def chat_with_gpt(self, prompt):
        response = client.completions.create(model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=50)
        return response.choices[0].text.strip()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_gpt_pb2_grpc.add_ChatGPTServicer_to_server(ChatGPTServicer(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
