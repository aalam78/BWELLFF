import grpc
from concurrent import futures
import chat_gpt_pb2
import chat_gpt_pb2_grpc
import openai

# Set up OpenAI API key
openai.api_key = "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"
# List available engines
engines = openai.Engine.list()

# Print the list of engines
print("Available Engines:")
for engine in engines.data:
    print(engine.id)

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=50,
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    print("Welcome to ChatGPT Bot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("ChatGPT Bot: Goodbye!")
            break
        prompt = f"You: {user_input}\nChatGPT Bot:"
        response = chat_with_gpt(prompt)
        print("ChatGPT Bot:", response)    
