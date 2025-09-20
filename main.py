import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
user_terminal_prompt = sys.argv[1]
toggle_verbose = sys.argv[-1]

messages = [
    types.Content(role="user", parts=[types.Part(text=user_terminal_prompt)]),
]

def generate_some_content(user_prompt):
    if not user_prompt:
        print("Error: You did not pass a prompt to the LLM :(")
        sys.exit(1)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages
    )
    if toggle_verbose == '--verbose':
        print(f'User prompt: {user_prompt}')
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    print(response.text)
    
def main():
    generate_some_content(user_terminal_prompt)
    
if __name__ == "__main__":
    main()