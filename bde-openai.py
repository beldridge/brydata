
import openai

# Set your OpenAI API key
openai.api_key = "sk-proj-uwBgDqhp1ME9vwjyqzt9T3BlbkFJCIi4AnMgqZWAaYJehoDW"

def get_openai_response(prompt, conversation_id="DPM Main 3"):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Example function to take user input and get OpenAI response
def run_app():
    user_input = input("Enter your input: ")
    prompt = f"Conversation ID: DPM Main 3\nUser: {user_input}\nAssistant:"
    response = get_openai_response(prompt)
    print(f"Response: {response}")

# Run the app
run_app()