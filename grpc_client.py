import grpc
import chat_gpt_pb2
import chat_gpt_pb2_grpc

def chat_with_gpt(prompt):
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = chat_gpt_pb2_grpc.ChatGPTStub(channel)
        response = stub.ChatWithGPT(chat_gpt_pb2.ChatRequest(prompt=prompt))
        return response.response

if __name__ == '__main__':
    print("Welcome to ChatGPT Bot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("ChatGPT Bot: Goodbye!")
            break
        prompt = f"You: {user_input}\nChatGPT Bot:"
        response = chat_with_gpt(prompt)
        print("ChatGPT Bot:", response)
