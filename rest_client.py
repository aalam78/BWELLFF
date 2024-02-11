import requests

def chat_with_gpt(prompt):
    url = 'http://localhost:5001/chat'
    data = {'prompt': prompt}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json().get('response')
    else:
        print(f"Error: {response.text}")
        return None

if __name__ == '__main__':
    print("Welcome to ChatGPT Bot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("ChatGPT Bot: Goodbye!")
            break
        prompt = f"You: {user_input}\nChatGPT Bot:"
        response = chat_with_gpt(prompt)
        if response:
            print("ChatGPT Bot:", response)
