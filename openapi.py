from openai import OpenAI

client = OpenAI(api_key='your_openai_api_key_here')

# Set up OpenAI API key

def chat_with_gpt(prompt):
    # Generate a response from GPT-3 model
    response = client.completions.create(engine="text-davinci-003",
    prompt=prompt,
    max_tokens=50)
    return response.choices[0].text.strip()

def main():
    print("Welcome to ChatGPT Bot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("ChatGPT Bot: Goodbye!")
            break
        prompt = f"You: {user_input}\nChatGPT Bot:"
        response = chat_with_gpt(prompt)
        print(response)

if __name__ == "__main__":
    main()
